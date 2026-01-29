import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp
import asyncio
import re

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Supported sites info
SUPPORTED_SITES = """
🌐 **Supported Websites:**

**Social Media:**
• YouTube, TikTok, Instagram, Facebook, Twitter/X
• Reddit, Snapchat, LinkedIn, Pinterest

**Video Platforms:**
• Vimeo, Dailymotion, Twitch, Rumble
• Streamable, Imgur, Gfycat

**Adult Content:**
• Pornhub, xVideos, xHamster, YouPorn
• RedTube, Spankbang, and many more

**Others:**
• Google Drive (public videos)
• Dropbox (public links)
• Direct video links (.mp4, .webm, .mkv, etc.)

And 1000+ more sites supported by yt-dlp!
"""

def is_valid_url(url):
    """Check if the text is a valid URL."""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    welcome_message = f"""
👋 **Welcome to Universal Video Downloader Bot!**

📹 I can download videos from almost any website!

**How to use:**
1. Send me any video link
2. I'll download and send it to you
3. That's it!

{SUPPORTED_SITES}

**Commands:**
/start - Show this message
/help - Get help
/sites - List supported sites

⚠️ **Note:** File size limit is 50MB for regular bots
"""
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = """
🔧 **How to Use:**

1️⃣ **Copy the video link** from any supported website
2️⃣ **Send the link** to me
3️⃣ **Wait** while I download it
4️⃣ **Receive** your video!

**Tips:**
• Make sure the video is publicly accessible
• Some sites may require cookies or authentication
• Large videos may take longer to process
• Videos over 50MB cannot be sent via Telegram bot

**Examples:**
✅ https://www.youtube.com/watch?v=dQw4w9WgXcQ
✅ https://vimeo.com/123456789
✅ https://www.tiktok.com/@user/video/123
✅ https://twitter.com/user/status/123

Need more help? Contact the bot developer!
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def sites_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show list of supported sites."""
    await update.message.reply_text(SUPPORTED_SITES, parse_mode='Markdown')

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Download video from any supported website."""
    url = update.message.text.strip()
    
    # Validate URL
    if not is_valid_url(url):
        await update.message.reply_text(
            '❌ Invalid URL. Please send a valid video link.\n\n'
            'Example: https://www.youtube.com/watch?v=...'
        )
        return
    
    # Send processing message
    processing_msg = await update.message.reply_text('🔍 Analyzing video link... ⏳')
    
    try:
        # Create downloads directory if it doesn't exist
        download_dir = 'downloads'
        os.makedirs(download_dir, exist_ok=True)
        
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best[ext=mp4]/best',  # Prefer mp4 format
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            # Add cookies support for sites that need it
            'cookiefile': None,
            # Limit file size (in bytes) - 50MB
            'max_filesize': 50 * 1024 * 1024,
        }
        
        # Download video info first
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            await processing_msg.edit_text('📊 Fetching video information... ⏳')
            
            try:
                info = ydl.extract_info(url, download=False)
            except yt_dlp.utils.DownloadError as e:
                error_msg = str(e)
                if 'Unsupported URL' in error_msg:
                    await processing_msg.edit_text(
                        '❌ This website is not supported.\n\n'
                        'Try /sites to see supported websites.'
                    )
                else:
                    await processing_msg.edit_text(
                        f'❌ Error: {error_msg}\n\n'
                        'The video may be private or require login.'
                    )
                return
            
            video_title = info.get('title', 'video')
            duration = info.get('duration', 0)
            filesize = info.get('filesize') or info.get('filesize_approx', 0)
            
            # Check file size before downloading
            if filesize and filesize > 50 * 1024 * 1024:
                await processing_msg.edit_text(
                    f'❌ Video is too large ({filesize / (1024*1024):.1f}MB).\n\n'
                    f'Telegram bot limit is 50MB.\n'
                    f'Title: {video_title}'
                )
                return
            
            await processing_msg.edit_text(
                f'📥 Downloading: {video_title}\n'
                f'Duration: {duration//60}:{duration%60:02d}\n'
                f'Please wait... ⏳'
            )
            
            # Download the video
            ydl.download([url])
            
            # Find the downloaded file
            filename = ydl.prepare_filename(info)
            
            # If the exact file doesn't exist, try to find it with different extension
            if not os.path.exists(filename):
                base_name = os.path.splitext(filename)[0]
                for ext in ['.mp4', '.webm', '.mkv', '.avi', '.mov', '.flv']:
                    if os.path.exists(base_name + ext):
                        filename = base_name + ext
                        break
                else:
                    raise FileNotFoundError(f"Downloaded file not found: {filename}")
            
            file_size = os.path.getsize(filename)
            
            # Double-check file size after download
            if file_size > 50 * 1024 * 1024:
                await processing_msg.edit_text(
                    f'❌ Video is too large ({file_size / (1024*1024):.1f}MB).\n'
                    f'Telegram bot limit is 50MB.'
                )
                os.remove(filename)
                return
            
            await processing_msg.edit_text('📤 Uploading to Telegram... Please wait...')
            
            # Get thumbnail if available
            thumbnail_path = None
            if info.get('thumbnail'):
                try:
                    thumb_opts = {
                        'skip_download': True,
                        'writethumbnail': True,
                        'outtmpl': os.path.join(download_dir, '%(title)s_thumb'),
                    }
                    with yt_dlp.YoutubeDL(thumb_opts) as thumb_dl:
                        thumb_dl.download([url])
                        thumbnail_path = os.path.join(download_dir, f"{info['title']}_thumb.jpg")
                        if not os.path.exists(thumbnail_path):
                            thumbnail_path = None
                except:
                    thumbnail_path = None
            
            # Prepare caption
            caption = f"🎬 {video_title}\n"
            if duration:
                caption += f"⏱️ Duration: {duration//60}:{duration%60:02d}\n"
            caption += f"💾 Size: {file_size / (1024*1024):.1f}MB"
            
            # Send the video
            with open(filename, 'rb') as video_file:
                thumb_file = open(thumbnail_path, 'rb') if thumbnail_path else None
                
                await update.message.reply_video(
                    video=video_file,
                    caption=caption[:1024],  # Telegram caption limit
                    supports_streaming=True,
                    thumbnail=thumb_file,
                    duration=duration if duration else None,
                    width=info.get('width'),
                    height=info.get('height'),
                )
                
                if thumb_file:
                    thumb_file.close()
            
            # Delete the processing message
            await processing_msg.delete()
            
            # Clean up - delete the downloaded files
            try:
                os.remove(filename)
                if thumbnail_path and os.path.exists(thumbnail_path):
                    os.remove(thumbnail_path)
            except:
                pass
            
    except yt_dlp.utils.DownloadError as e:
        error_message = str(e)
        await processing_msg.edit_text(
            f'❌ Download Error:\n\n'
            f'{error_message}\n\n'
            'Possible reasons:\n'
            '• Video is private or deleted\n'
            '• Website requires login\n'
            '• Video format not supported\n'
            '• Geographic restrictions'
        )
        logger.error(f"Download error: {e}")
    
    except Exception as e:
        await processing_msg.edit_text(
            f'❌ An unexpected error occurred:\n\n{str(e)}\n\n'
            'Please try again or contact support.'
        )
        logger.error(f"Error: {e}", exc_info=True)

def main():
    """Start the bot."""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN environment variable not set!")
        print("ERROR: Please set BOT_TOKEN environment variable!")
        return
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("sites", sites_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    
    # Start the bot
    logger.info("Universal Video Downloader Bot started!")
    print("🤖 Bot is running... Press Ctrl+C to stop")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
