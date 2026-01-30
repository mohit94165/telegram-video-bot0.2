import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp
from urllib.parse import urlparse

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')
PORT = int(os.getenv('PORT', '8080'))

def is_valid_url(url):
    """Check if the provided string is a valid URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        '🎥 *Universal Video Downloader Bot*\n\n'
        'Send me a video link from any website and I will download it for you!\n\n'
        '*Supported Sites:*\n'
        '✅ YouTube, Vimeo, Twitter/X\n'
        '✅ Facebook, Instagram, TikTok\n'
        '✅ Reddit, Dailymotion, Twitch\n'
        '✅ And 1000+ more sites!\n\n'
        'Just paste the video URL and I\'ll handle the rest! 🚀',
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        '*How to use:*\n'
        '1. Copy a video link from any website\n'
        '2. Send it to me\n'
        '3. Wait for the download\n'
        '4. Receive your video!\n\n'
        '*Note:* File size limit is 50MB.\n\n'
        'For a list of supported sites, use /sites',
        parse_mode='Markdown'
    )

async def sites_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show some popular supported sites."""
    await update.message.reply_text(
        '*Popular Supported Sites:*\n\n'
        '🎬 YouTube, Vimeo, Dailymotion\n'
        '📱 TikTok, Instagram, Facebook\n'
        '🐦 Twitter/X, Reddit\n'
        '🎮 Twitch, Kick\n'
        '📺 Rumble, Bitchute\n'
        '🌐 And 1000+ more!\n\n'
        'Full list: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md',
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Download video from any supported website."""
    url = update.message.text.strip()
    
    # Check if it's a valid URL
    if not is_valid_url(url):
        await update.message.reply_text(
            '❌ Please send a valid video URL.\n\n'
            'Example: https://www.youtube.com/watch?v=...'
        )
        return
    
    # Send processing message
    processing_msg = await update.message.reply_text('🔍 Analyzing video... ⏳')
    
    try:
        # Create downloads directory if it doesn't exist
        download_dir = 'downloads'
        os.makedirs(download_dir, exist_ok=True)
        
        # Configure yt-dlp options for universal downloading
        ydl_opts = {
            'format': 'best[ext=mp4][filesize<50M]/best[filesize<50M]/best',
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }
        
        # Download video info first
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
            except yt_dlp.utils.DownloadError as e:
                error_msg = str(e)
                if 'Unsupported URL' in error_msg:
                    await processing_msg.edit_text(
                        '❌ This website is not supported.\n\n'
                        'Use /sites to see supported platforms.'
                    )
                else:
                    await processing_msg.edit_text(
                        f'❌ Cannot access this video.\n\n'
                        f'Possible reasons:\n'
                        f'• Video is private or restricted\n'
                        f'• Invalid URL\n'
                        f'• Geographic restrictions'
                    )
                return
            
            video_title = info.get('title', 'video')
            duration = info.get('duration', 0)
            uploader = info.get('uploader', 'Unknown')
            
            # Check if it's a playlist
            if info.get('_type') == 'playlist':
                await processing_msg.edit_text(
                    '❌ Playlists are not supported.\n'
                    'Please send a direct video link.'
                )
                return
            
            # Check estimated file size
            filesize = info.get('filesize') or info.get('filesize_approx', 0)
            if filesize > 50 * 1024 * 1024:
                await processing_msg.edit_text(
                    f'❌ Video is too large (~{filesize/(1024*1024):.1f}MB).\n\n'
                    f'Maximum size: 50MB'
                )
                return
            
            await processing_msg.edit_text(
                f'📥 *Downloading:*\n{video_title[:100]}\n\n'
                f'👤 Uploader: {uploader}\n'
                f'⏱ Duration: {duration//60}m {duration%60}s',
                parse_mode='Markdown'
            )
            
            # Download the video
            ydl.download([url])
            
            # Find the downloaded file
            filename = ydl.prepare_filename(info)
            
            # Sometimes the extension changes after download
            if not os.path.exists(filename):
                base_name = os.path.splitext(filename)[0]
                possible_files = [
                    f for f in os.listdir(download_dir) 
                    if f.startswith(os.path.basename(base_name))
                ]
                if possible_files:
                    filename = os.path.join(download_dir, possible_files[0])
                else:
                    raise FileNotFoundError(f"Downloaded file not found")
            
            file_size = os.path.getsize(filename)
            file_size_mb = file_size / (1024 * 1024)
            
            # Double check file size
            if file_size > 50 * 1024 * 1024:
                await processing_msg.edit_text(
                    f'❌ Video is too large ({file_size_mb:.1f}MB).\n\n'
                    f'Telegram bot limit is 50MB.'
                )
                os.remove(filename)
                return
            
            await processing_msg.edit_text(
                f'📤 Uploading to Telegram... ({file_size_mb:.1f}MB)'
            )
            
            # Send the video
            with open(filename, 'rb') as video_file:
                caption = f"🎬 {video_title[:200]}\n👤 {uploader}"
                
                await update.message.reply_video(
                    video=video_file,
                    caption=caption,
                    supports_streaming=True,
                    width=info.get('width'),
                    height=info.get('height'),
                    duration=int(duration) if duration else None
                )
            
            # Delete the processing message
            await processing_msg.delete()
            
            # Clean up
            os.remove(filename)
            
    except yt_dlp.utils.DownloadError as e:
        error_message = str(e)
        await processing_msg.edit_text(
            f'❌ Download failed.\n\n'
            f'Please check:\n'
            f'• Video is publicly accessible\n'
            f'• URL is correct\n'
            f'• Video is not geo-restricted'
        )
        logger.error(f"Download error: {e}")
    
    except Exception as e:
        await processing_msg.edit_text(
            f'❌ An unexpected error occurred.\n\n'
            f'Please try again or use /help'
        )
        logger.error(f"Error: {e}", exc_info=True)
    
    finally:
        # Clean up any remaining files
        try:
            for file in os.listdir(download_dir):
                file_path = os.path.join(download_dir, file)
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                    except:
                        pass
        except:
            pass

def main():
    """Start the bot."""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN environment variable not set!")
        print("Error: BOT_TOKEN environment variable not set!")
        return
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("sites", sites_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    
    # Start the bot
    logger.info("Bot started successfully!")
    print("Bot is running on Railway...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
