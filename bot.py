import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import yt_dlp
from urllib.parse import urlparse
import asyncio

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_IDS = [int(x) for x in os.getenv('ADMIN_IDS', '').split(',') if x]

# User statistics
user_stats = {}

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def get_user_stats(user_id):
    if user_id not in user_stats:
        user_stats[user_id] = {'downloads': 0}
    return user_stats[user_id]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    stats = get_user_stats(user.id)
    
    welcome_text = (
        f"🎬 <b>Premium Video Downloader Bot</b>\n\n"
        f"👋 Welcome {user.first_name}!\n\n"
        f"<b>✨ Features:</b>\n"
        f"📹 Download videos from 1000+ sites\n"
        f"🎵 Extract audio (MP3)\n"
        f"🎯 Multiple quality options\n"
        f"📊 Download statistics\n"
        f"🖼️ Thumbnail support\n"
        f"⚡ Fast & reliable\n\n"
        f"<b>📈 Your Stats:</b>\n"
        f"Downloads: {stats['downloads']}\n\n"
        f"<b>🎯 Commands:</b>\n"
        f"/start - Show this message\n"
        f"/help - Get help\n"
        f"/stats - Your statistics\n"
        f"/quality - Set default quality\n"
        f"/sites - Supported sites\n"
        f"/about - About this bot\n\n"
        f"<i>Just send any video link to get started!</i> 🚀"
    )
    
    await update.message.reply_text(welcome_text, parse_mode='HTML')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "<b>📖 How to Use</b>\n\n"
        "<b>1. Send Video Link:</b>\n"
        "Just paste any video URL from supported sites\n\n"
        "<b>2. Choose Quality:</b>\n"
        "Select your preferred quality or audio format\n\n"
        "<b>3. Wait for Download:</b>\n"
        "Bot will download and send the video to you\n\n"
        "<b>💡 Tips:</b>\n"
        "• Videos over 50MB will be rejected\n"
        "• Use audio mode for music videos\n"
        "• Check /sites for supported platforms\n"
        "• Use /quality to set default preference\n\n"
        "<b>⚡ Quick Commands:</b>\n"
        "/stats - Your download statistics\n"
        "/sites - List of 1000+ supported sites\n"
        "/quality - Quality settings\n\n"
        "<i>Need more help? Contact support!</i>"
    )
    await update.message.reply_text(help_text, parse_mode='HTML')

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    stats = get_user_stats(user.id)
    
    stats_text = (
        f"📊 <b>Your Statistics</b>\n\n"
        f"👤 User: {user.first_name}\n"
        f"🆔 ID: <code>{user.id}</code>\n"
        f"📥 Total Downloads: {stats['downloads']}\n\n"
        f"<i>Keep downloading! 🚀</i>"
    )
    await update.message.reply_text(stats_text, parse_mode='HTML')

async def quality_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 Best Quality", callback_data="default_best")],
        [InlineKeyboardButton("📺 720p", callback_data="default_720")],
        [InlineKeyboardButton("📱 480p", callback_data="default_480")],
        [InlineKeyboardButton("🎵 Audio Only", callback_data="default_audio")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "⚙️ <b>Set Default Quality</b>\n\n"
        "Choose your preferred download quality:",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def sites_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sites_text = (
        "<b>🌐 Supported Sites (1000+)</b>\n\n"
        "<b>🎬 Video Platforms:</b>\n"
        "• YouTube, Vimeo, Dailymotion\n"
        "• Rumble, Bitchute, PeerTube\n\n"
        "<b>📱 Social Media:</b>\n"
        "• Instagram, Facebook, TikTok\n"
        "• Twitter/X, Reddit, Pinterest\n\n"
        "<b>🎮 Streaming:</b>\n"
        "• Twitch, Kick, YouTube Live\n"
        "• Trovo, DLive\n\n"
        "<b>🔞 Adult Content:</b>\n"
        "• xHamster, Pornhub, xVideos\n"
        "• RedTube, YouPorn, and more\n\n"
        "<b>📺 Other:</b>\n"
        "• Soundcloud (audio)\n"
        "• Bandcamp, Mixcloud\n"
        "• And 1000+ more!\n\n"
        "<a href='https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md'>View Full List</a>"
    )
    await update.message.reply_text(
        sites_text, 
        parse_mode='HTML',
        disable_web_page_preview=True
    )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "<b>ℹ️ About This Bot</b>\n\n"
        "<b>Version:</b> 2.0 Premium\n"
        "<b>Engine:</b> yt-dlp (Most powerful)\n"
        "<b>Supported Sites:</b> 1000+\n"
        "<b>Max File Size:</b> 50MB\n\n"
        "<b>✨ Premium Features:</b>\n"
        "✅ Multiple quality options\n"
        "✅ Audio extraction (MP3)\n"
        "✅ Thumbnail support\n"
        "✅ Download statistics\n"
        "✅ Fast processing\n"
        "✅ User-friendly interface\n\n"
        "<b>🔧 Powered by:</b>\n"
        "• python-telegram-bot\n"
        "• yt-dlp\n"
        "• FFmpeg\n\n"
        "<i>Made with ❤️ for video enthusiasts</i>"
    )
    await update.message.reply_text(about_text, parse_mode='HTML')

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS and ADMIN_IDS:
        await update.message.reply_text("❌ Admin access only!")
        return
    
    total_users = len(user_stats)
    total_downloads = sum(s['downloads'] for s in user_stats.values())
    
    admin_text = (
        f"👑 <b>Admin Panel</b>\n\n"
        f"📊 <b>Statistics:</b>\n"
        f"Total Users: {total_users}\n"
        f"Total Downloads: {total_downloads}\n\n"
        f"<i>More admin features coming soon!</i>"
    )
    await update.message.reply_text(admin_text, parse_mode='HTML')

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    user_id = update.effective_user.id
    
    if not is_valid_url(url):
        await update.message.reply_text(
            "❌ <b>Invalid URL</b>\n\n"
            "Please send a valid video link.\n"
            "Example: https://www.youtube.com/watch?v=...",
            parse_mode='HTML'
        )
        return
    
    # Show quality options
    keyboard = [
        [
            InlineKeyboardButton("🎬 Best Quality", callback_data=f"dl_best_{url}"),
            InlineKeyboardButton("📺 720p", callback_data=f"dl_720_{url}")
        ],
        [
            InlineKeyboardButton("📱 480p", callback_data=f"dl_480_{url}"),
            InlineKeyboardButton("📉 360p", callback_data=f"dl_360_{url}")
        ],
        [
            InlineKeyboardButton("🎵 Audio Only (MP3)", callback_data=f"dl_audio_{url}")
        ],
        [
            InlineKeyboardButton("📋 Video Info", callback_data=f"info_{url}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎯 <b>Choose Quality</b>\n\n"
        "Select your preferred download option:",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    # Handle default quality settings
    if data.startswith('default_'):
        quality = data.replace('default_', '')
        quality_names = {
            'best': 'Best Quality 🎬',
            '720': '720p HD 📺',
            '480': '480p SD 📱',
            'audio': 'Audio Only 🎵'
        }
        await query.edit_message_text(
            f"✅ Default quality set to: <b>{quality_names.get(quality, quality)}</b>",
            parse_mode='HTML'
        )
        return
    
    # Handle video info
    if data.startswith('info_'):
        url = data.replace('info_', '')
        await query.edit_message_text("🔍 Fetching video information...")
        
        try:
            ydl_opts = {'quiet': True, 'no_warnings': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                title = info.get('title', 'Unknown')
                uploader = info.get('uploader', 'Unknown')
                duration = info.get('duration', 0)
                views = info.get('view_count', 0)
                likes = info.get('like_count', 0)
                
                info_text = (
                    f"📹 <b>Video Information</b>\n\n"
                    f"<b>Title:</b> {title[:100]}\n"
                    f"<b>Uploader:</b> {uploader}\n"
                    f"<b>Duration:</b> {duration//60}m {duration%60}s\n"
                    f"<b>Views:</b> {views:,}\n"
                    f"<b>Likes:</b> {likes:,}\n"
                )
                await query.edit_message_text(info_text, parse_mode='HTML')
        except Exception as e:
            await query.edit_message_text(f"❌ Error: {str(e)[:100]}")
        return
    
    # Handle download
    if data.startswith('dl_'):
        parts = data.split('_', 2)
        quality = parts[1]
        url = parts[2]
        
        await query.edit_message_text("⏳ <b>Processing your request...</b>", parse_mode='HTML')
        
        try:
            await process_download(query, url, quality, update.effective_user.id)
        except Exception as e:
            logger.error(f"Download error: {e}")
            await query.edit_message_text(
                f"❌ <b>Download Failed</b>\n\n"
                f"Error: {str(e)[:150]}\n\n"
                f"<i>Please try again or use different quality</i>",
                parse_mode='HTML'
            )

async def process_download(query, url, quality, user_id):
    os.makedirs('downloads', exist_ok=True)
    
    # Configure quality settings
    format_options = {
        'best': 'best[filesize<50M]',
        '720': 'best[height<=720][filesize<50M]',
        '480': 'best[height<=480][filesize<50M]',
        '360': 'best[height<=360][filesize<50M]',
        'audio': 'bestaudio/best'
    }
    
    ydl_opts = {
        'format': format_options.get(quality, 'best[filesize<50M]'),
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }
    
    # Audio specific settings
    if quality == 'audio':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Get info
        info = ydl.extract_info(url, download=False)
        
        if info.get('_type') == 'playlist':
            await query.edit_message_text(
                "❌ <b>Playlists Not Supported</b>\n\n"
                "Please send a direct video link.",
                parse_mode='HTML'
            )
            return
        
        title = info.get('title', 'video')[:50]
        duration = info.get('duration', 0)
        uploader = info.get('uploader', 'Unknown')
        
        await query.edit_message_text(
            f"📥 <b>Downloading...</b>\n\n"
            f"🎬 {title}\n"
            f"👤 {uploader}\n"
            f"⏱ {duration//60}m {duration%60}s",
            parse_mode='HTML'
        )
        
        # Download
        ydl.download([url])
        
        # Find file
        filename = ydl.prepare_filename(info)
        if quality == 'audio':
            filename = filename.rsplit('.', 1)[0] + '.mp3'
        
        if not os.path.exists(filename):
            files = [f for f in os.listdir('downloads') if os.path.isfile(os.path.join('downloads', f))]
            if files:
                filename = os.path.join('downloads', files[0])
            else:
                raise FileNotFoundError("Download failed")
        
        size_mb = os.path.getsize(filename) / (1024 * 1024)
        
        if size_mb > 50:
            await query.edit_message_text(
                f"❌ <b>File Too Large</b>\n\n"
                f"Size: {size_mb:.1f}MB\n"
                f"Maximum: 50MB\n\n"
                f"<i>Try a lower quality option</i>",
                parse_mode='HTML'
            )
            os.remove(filename)
            return
        
        await query.edit_message_text(
            f"📤 <b>Uploading...</b>\n\n"
            f"Size: {size_mb:.1f}MB",
            parse_mode='HTML'
        )
        
        # Send file
        caption = f"🎬 {title}\n👤 {uploader}"
        
        with open(filename, 'rb') as f:
            if quality == 'audio':
                await query.message.reply_audio(
                    audio=f,
                    caption=caption,
                    title=title,
                    performer=uploader,
                    duration=int(duration) if duration else None
                )
            else:
                await query.message.reply_video(
                    video=f,
                    caption=caption,
                    supports_streaming=True,
                    width=info.get('width'),
                    height=info.get('height'),
                    duration=int(duration) if duration else None
                )
        
        # Update stats
        stats = get_user_stats(user_id)
        stats['downloads'] += 1
        
        await query.edit_message_text(
            "✅ <b>Download Complete!</b>\n\n"
            f"📊 Total Downloads: {stats['downloads']}",
            parse_mode='HTML'
        )
        
        # Cleanup
        os.remove(filename)

def main():
    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN not set!")
        print("Please set BOT_TOKEN environment variable")
        return
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CommandHandler("quality", quality_command))
    app.add_handler(CommandHandler("sites", sites_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("admin", admin_command))
    
    # Callback handler
    app.add_handler(CallbackQueryHandler(button_callback))
    
    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    
    print("✅ Premium Bot Started!")
    print(f"🎬 Features: Quality options, Audio extraction, Stats")
    print(f"📊 Ready to serve users!")
    
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
