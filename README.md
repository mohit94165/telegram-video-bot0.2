# 🎬 Premium Telegram Video Downloader Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**The most powerful Telegram bot for downloading videos from 1000+ websites!**

[Features](#-features) • [Demo](#-demo) • [Installation](#-quick-start) • [Commands](#-commands) • [Support](#-support)

</div>

---

## 🌟 Features

### 🎯 Core Features
- 📹 **Download from 1000+ sites** - YouTube, Instagram, TikTok, Twitter, Facebook, Reddit, and more
- 🎬 **Multiple Quality Options** - Best, 720p, 480p, 360p
- 🎵 **Audio Extraction** - Download as MP3 with metadata
- 📊 **User Statistics** - Track your download history
- 🖼️ **Thumbnail Support** - Preview videos before downloading
- 📋 **Video Information** - View details before download
- ⚙️ **Quality Settings** - Set your preferred default quality

### 💎 Premium Features
- ⚡ **Fast Processing** - Optimized download engine
- 🎨 **Beautiful UI** - Inline keyboard buttons
- 📈 **Statistics Dashboard** - Personal download metrics
- 👑 **Admin Panel** - For bot owners
- 🔄 **Auto-Updates** - Always uses latest yt-dlp
- 🌐 **Multi-Platform** - Works on all Telegram clients

---

## 🎮 Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message with bot info |
| `/help` | Detailed usage instructions |
| `/stats` | Your personal statistics |
| `/quality` | Set default quality preference |
| `/sites` | List of supported websites |
| `/about` | Bot version and features |
| `/admin` | Admin panel (owner only) |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Telegram Bot Token
- Render/Railway/Heroku account (for hosting)

### Installation

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/premium-video-bot.git
cd premium-video-bot
```

#### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3️⃣ Set Environment Variables
```bash
export BOT_TOKEN="your_bot_token_here"
export ADMIN_IDS="your_telegram_id"  # Optional
```

#### 4️⃣ Run Bot
```bash
python bot.py
```

---

## 🌐 Deploy to Render (Recommended)

### Why Render?
- ✅ **Free Forever** - No credit card required
- ✅ **Auto-Deploy** - Connects to GitHub
- ✅ **SSL Included** - Secure by default
- ✅ **Easy Setup** - 5 minutes deployment

### Deployment Steps

1. **Fork this repository** to your GitHub

2. **Sign up on Render**: https://render.com

3. **Create New Web Service**:
   - Connect your GitHub repository
   - Select the forked repository
   - Use these settings:
     ```
     Build Command: pip install -r requirements.txt
     Start Command: python bot.py
     ```

4. **Add Environment Variables**:
   - `BOT_TOKEN`: Your bot token from @BotFather
   - `ADMIN_IDS`: Your Telegram user ID (optional)

5. **Deploy!** 🚀

**📖 Detailed Guide**: See [SETUP_GUIDE.md](SETUP_GUIDE.md) for step-by-step instructions

---

## 🎯 Usage Examples

### Download Video
1. Send any video link to the bot
2. Choose your preferred quality
3. Wait for download and upload
4. Enjoy your video! 🎉

### Example Links
```
YouTube: https://youtube.com/watch?v=...
Instagram: https://instagram.com/p/...
TikTok: https://tiktok.com/@user/video/...
Twitter: https://twitter.com/user/status/...
```

### Quality Options
- 🎬 **Best Quality** - Highest available quality
- 📺 **720p HD** - Standard HD quality
- 📱 **480p SD** - Mobile-friendly quality
- 📉 **360p** - Low bandwidth option
- 🎵 **Audio Only** - MP3 extraction

---

## 🌐 Supported Sites (1000+)

### Popular Platforms
- **Video**: YouTube, Vimeo, Dailymotion, Rumble
- **Social**: Instagram, Facebook, TikTok, Twitter/X
- **Streaming**: Twitch, Kick, YouTube Live
- **Reddit**: All video posts
- **Adult**: xHamster, Pornhub, xVideos, etc.
- **And 1000+ more!**

**Full List**: [yt-dlp Supported Sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

---

## 📊 Statistics Features

Track your usage with built-in statistics:
- Total downloads count
- Download history
- User information
- Admin dashboard (for owners)

---

## 🔐 Admin Features

Set `ADMIN_IDS` environment variable to enable:
- View total users
- View total downloads
- System statistics
- User management (coming soon)

---

## 🛠️ Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `BOT_TOKEN` | ✅ Yes | Your Telegram bot token |
| `ADMIN_IDS` | ❌ No | Comma-separated admin user IDs |

### Custom Settings

Edit `bot.py` to customize:
- Welcome messages
- Quality presets
- File size limits
- Download paths

---

## 📱 Screenshots

### Bot Interface
```
🎬 Premium Video Downloader Bot

👋 Welcome User!

✨ Features:
📹 Download videos from 1000+ sites
🎵 Extract audio (MP3)
🎯 Multiple quality options
📊 Download statistics
...
```

### Quality Selection
```
🎯 Choose Quality

Select your preferred download option:
[🎬 Best Quality] [📺 720p]
[📱 480p] [📉 360p]
[🎵 Audio Only (MP3)]
[📋 Video Info]
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 To-Do List

- [ ] Playlist support
- [ ] Batch downloads
- [ ] Custom thumbnail extraction
- [ ] Video editing features
- [ ] Multiple language support
- [ ] Download queue system
- [ ] Progress bar during download
- [ ] Scheduled downloads

---

## 🐛 Known Issues

- File size limited to 50MB (Telegram API limit)
- Some sites may require authentication
- Regional restrictions may apply
- Free tier may sleep after inactivity (Render)

**Solutions**: Check [SETUP_GUIDE.md](SETUP_GUIDE.md) troubleshooting section

---

## 💡 Tips & Tricks

### Keep Bot Active (Free Tier)
Use [UptimeRobot](https://uptimerobot.com) to ping your Render URL every 5 minutes

### Faster Downloads
Ensure good server location (select region closest to you)

### Better Quality
Use "Best Quality" option for optimal results

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot API wrapper
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video download engine
- [FFmpeg](https://ffmpeg.org/) - Media processing

---

## 📞 Support

### Need Help?
- 📖 Read [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions
- 🐛 Report issues on [GitHub Issues](https://github.com/yourusername/premium-video-bot/issues)
- 💬 Join our community (coming soon)

### Contact
- Telegram: [@YourUsername](https://t.me/yourusername)
- Email: your.email@example.com

---

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

---

## 📈 Statistics

![GitHub stars](https://img.shields.io/github/stars/yourusername/premium-video-bot?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/premium-video-bot?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/premium-video-bot?style=social)

---

<div align="center">

**Made with ❤️ for the Telegram community**

**Enjoy downloading! 🎬**

[⬆ Back to Top](#-premium-telegram-video-downloader-bot)

</div>
