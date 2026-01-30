# Universal Video Downloader Telegram Bot

A powerful Telegram bot that can download videos from **1000+ websites** and send them directly to you on Telegram!

## 🌟 Features

- 📹 Download videos from **1000+ websites**
- 🚀 Fast and reliable downloads
- 📱 Direct delivery to Telegram
- 🎯 Simple to use - just send a link
- ✅ Supports YouTube, Twitter, Instagram, TikTok, Facebook, Reddit, and many more!
- 🎬 Automatic video format conversion
- 📊 File size validation (50MB limit)

## 🌐 Supported Websites

This bot supports videos from:

### Popular Platforms
- **Video Sharing:** YouTube, Vimeo, Dailymotion, Rumble
- **Social Media:** Twitter/X, Instagram, Facebook, TikTok
- **Streaming:** Twitch, Kick, YouTube Live
- **Forums:** Reddit, 9GAG
- **Adult Content:** xHamster, Pornhub, xVideos, and others
- **And 1000+ more sites!**

Full list: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

## 🚂 Deploy to Railway

### Prerequisites

1. A [Railway](https://railway.app/) account (free tier available)
2. A Telegram Bot Token from [@BotFather](https://t.me/botfather)
3. A GitHub account

### Step-by-Step Deployment

#### 1. Create Your Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow the instructions to choose a name and username
4. **Save the bot token** you receive (looks like `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

#### 2. Deploy to Railway

##### Option A: Deploy from GitHub (Recommended)

1. **Fork or create a repository** with these files on GitHub

2. **Go to [Railway](https://railway.app/)**
   - Sign up or log in with GitHub

3. **Create a New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect the configuration

4. **Add Environment Variables**
   - In your Railway project, go to "Variables" tab
   - Add a new variable:
     - **Name:** `BOT_TOKEN`
     - **Value:** Your bot token from BotFather (paste the full token)
   - Click "Add"

5. **Deploy**
   - Railway will automatically build and deploy your bot
   - Wait for the deployment to complete (usually 1-2 minutes)
   - Check the logs to ensure it's running

##### Option B: Deploy with Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Add environment variable
railway variables set BOT_TOKEN=your_bot_token_here

# Deploy
railway up
```

#### 3. Verify Deployment

1. Check the Railway logs for "Bot started successfully!"
2. Open Telegram and search for your bot
3. Send `/start` to your bot
4. If you get a response, your bot is working! 🎉

### 📝 Railway Configuration Files Explained

- **`Procfile`** - Tells Railway how to start the bot
- **`railway.json`** - Railway-specific configuration
- **`nixpacks.toml`** - Specifies system dependencies (Python, FFmpeg)
- **`runtime.txt`** - Python version specification
- **`requirements.txt`** - Python package dependencies

## 🎮 How to Use

1. Start a chat with your bot on Telegram
2. Send `/start` to see the welcome message
3. Send any video link from supported websites
4. Wait for the bot to download and process
5. Receive your video directly in the chat!

### Commands

- `/start` - Welcome message and bot info
- `/help` - Usage instructions
- `/sites` - List of popular supported sites

### Example Usage

```
You: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Bot: 🔍 Analyzing video... ⏳
Bot: 📥 Downloading: Never Gonna Give You Up
     👤 Uploader: Rick Astley
     ⏱ Duration: 3m 32s
Bot: 📤 Uploading to Telegram... (8.5MB)
Bot: [Sends video]
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Your Telegram bot token from BotFather | ✅ Yes |
| `PORT` | Port for the application (default: 8080) | ❌ No |

### File Size Limits

- **Maximum file size:** 50MB (Telegram bot API limitation)
- Videos larger than 50MB will be rejected with an error message
- For larger videos, consider using Telegram Premium features

## 🔧 Troubleshooting

### Bot is not responding

**Check Railway logs:**
1. Go to your Railway project
2. Click on "Deployments"
3. Check the logs for errors

**Common issues:**
- ❌ `BOT_TOKEN environment variable not set!`
  - Solution: Add BOT_TOKEN in Railway Variables
  
- ❌ Bot token is invalid
  - Solution: Get a new token from @BotFather and update the variable

### Download errors

- **"This website is not supported"**
  - The site may not be in yt-dlp's supported list
  - Use `/sites` to check supported platforms

- **"Video is too large"**
  - File exceeds 50MB Telegram limit
  - Try a shorter video or lower quality

- **"Cannot access this video"**
  - Video might be private or geo-restricted
  - Check if the URL is correct
  - Try accessing the video in your browser first

### Railway-specific issues

- **Build fails:**
  - Check that all configuration files are present
  - Verify `requirements.txt` has correct dependencies
  - Check Railway logs for specific error messages

- **Bot keeps restarting:**
  - Check for errors in Railway logs
  - Ensure BOT_TOKEN is set correctly
  - Verify your Railway account has sufficient credits

## 💰 Cost

- **Railway Free Tier:** 
  - $5 free credit per month
  - Enough for moderate bot usage
  - No credit card required initially

- **Railway Pro:**
  - Pay-as-you-go after free credits
  - ~$5-10/month for typical bot usage

## 🔐 Security

- Never share your BOT_TOKEN publicly
- Don't commit `.env` files to Git
- Use Railway's environment variables for sensitive data
- Consider adding user restrictions in production

## 📚 Technical Details

- **Language:** Python 3.10
- **Bot Framework:** python-telegram-bot 20.7
- **Download Engine:** yt-dlp (supports 1000+ sites)
- **Video Processing:** FFmpeg
- **Hosting:** Railway.app

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

MIT License - feel free to use and modify as needed.

## ⚠️ Disclaimer

This bot is for educational purposes. Respect copyright laws and terms of service of the websites you download from. Users are responsible for their own usage.

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review Railway deployment logs
3. Verify your bot token is correct
4. Ensure the video URL is valid and accessible

## 🎯 Roadmap

Potential future features:
- [ ] Audio-only downloads
- [ ] Playlist support
- [ ] Custom quality selection
- [ ] Download progress tracking
- [ ] Multiple simultaneous downloads

---

**Made with ❤️ for the Telegram community**

Deploy now and start downloading videos! 🚀
