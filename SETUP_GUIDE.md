# 🚀 PREMIUM VIDEO DOWNLOADER BOT - COMPLETE SETUP GUIDE

## 🎯 Bot Features

### ✨ Premium Features:
- 🎬 **Multiple Quality Options** (Best, 720p, 480p, 360p)
- 🎵 **Audio Extraction** (MP3 format)
- 📊 **User Statistics** (Track your downloads)
- 🖼️ **Thumbnail Support**
- 📋 **Video Info** (Before downloading)
- ⚙️ **Quality Settings** (Set default preference)
- 👑 **Admin Panel** (For bot owners)
- 🌐 **1000+ Supported Sites**

### 🎮 Commands:
- `/start` - Welcome message
- `/help` - How to use guide
- `/stats` - Your download statistics
- `/quality` - Set default quality
- `/sites` - List of supported sites
- `/about` - Bot information
- `/admin` - Admin panel (owner only)

---

## 📋 STEP-BY-STEP DEPLOYMENT ON RENDER

### 🔰 Prerequisites:
- [ ] GitHub account
- [ ] Telegram account
- [ ] 10 minutes of your time

---

## STEP 1: Create Your Telegram Bot

### 1.1 Open Telegram
- On your phone or computer, open Telegram

### 1.2 Find BotFather
```
Search: @BotFather
Start chat
```

### 1.3 Create New Bot
```
Send: /newbot

BotFather will ask:
1. Choose a name for your bot (Example: "My Premium Video Bot")
2. Choose a username (Must end with 'bot', Example: "mypremium_video_bot")
```

### 1.4 Save Your Token
```
BotFather will give you a token like:
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

⚠️ SAVE THIS TOKEN - You'll need it!
```

### 1.5 Optional: Set Bot Profile
```
/setdescription - Add bot description
/setabouttext - Add about text
/setuserpic - Upload bot profile picture
```

---

## STEP 2: Upload Code to GitHub

### Option A: Create New Repository (Recommended)

#### 2.1 Go to GitHub
- Visit: https://github.com
- Login to your account

#### 2.2 Create New Repository
```
1. Click the "+" icon (top right)
2. Select "New repository"
3. Repository name: "premium-video-bot"
4. Description: "Premium Telegram Video Downloader Bot"
5. Select: ✅ Public (or Private)
6. ✅ Add README file
7. Click "Create repository"
```

#### 2.3 Upload Files
```
1. Click "Add file" → "Upload files"
2. Drag and drop these 4 files:
   ✅ bot.py
   ✅ requirements.txt
   ✅ render.yaml
   ✅ .gitignore

3. Commit message: "Initial commit - Premium bot"
4. Click "Commit changes"
```

### Option B: Use Git Command Line
```bash
# On your computer
git clone https://github.com/YOUR_USERNAME/premium-video-bot.git
cd premium-video-bot

# Copy all files here, then:
git add .
git commit -m "Premium bot initial commit"
git push origin main
```

---

## STEP 3: Deploy on Render

### 3.1 Create Render Account
```
1. Go to: https://render.com
2. Click "Get Started" or "Sign Up"
3. Choose: "Sign up with GitHub"
4. Authorize Render to access GitHub
```

### 3.2 Create New Web Service
```
1. On Render Dashboard, click "New +"
2. Select "Web Service"
3. Click "Connect Account" (if needed)
4. Find your repository: "premium-video-bot"
5. Click "Connect"
```

### 3.3 Configure Service
```
Name: premium-video-bot
Region: Oregon (US West) [or closest to you]
Branch: main
Root Directory: (leave blank)

Build Command: pip install --no-cache-dir -r requirements.txt
Start Command: python bot.py

Instance Type: Free
```

### 3.4 Add Environment Variables
```
Scroll down to "Environment Variables"

Click "Add Environment Variable"

Variable 1:
Key: BOT_TOKEN
Value: [Paste your token from BotFather]

Variable 2 (Optional - for admin features):
Key: ADMIN_IDS
Value: [Your Telegram User ID - get from @userinfobot]

Click "Add" for each
```

### 3.5 Deploy!
```
1. Click "Create Web Service"
2. Wait for build to complete (2-3 minutes)
3. Check logs for "✅ Premium Bot Started!"
```

---

## STEP 4: Test Your Bot

### 4.1 Find Your Bot
```
1. Open Telegram
2. Search for your bot username
3. Click "Start" or send /start
```

### 4.2 Test Commands
```
/start   - See welcome message
/help    - View help guide
/sites   - Check supported sites
/stats   - See your statistics
```

### 4.3 Download a Video
```
1. Copy any video link (YouTube, Instagram, etc.)
2. Paste it in bot chat
3. Choose quality option
4. Wait for download
5. Receive video! 🎉
```

---

## 🎯 DETAILED COMMAND GUIDE

### For Users:

#### `/start` Command
Shows welcome message with features and statistics

#### `/help` Command  
Detailed usage instructions and tips

#### `/stats` Command
```
View your personal statistics:
- Total downloads
- User ID
- Username
```

#### `/quality` Command
```
Set default quality preference:
- 🎬 Best Quality
- 📺 720p HD
- 📱 480p SD
- 🎵 Audio Only
```

#### `/sites` Command
Lists all 1000+ supported platforms with categories

#### `/about` Command
Bot version, features, and technical details

#### Downloading Videos
```
1. Send video link
2. Bot shows quality options:
   - 🎬 Best Quality
   - 📺 720p
   - 📱 480p
   - 📉 360p
   - 🎵 Audio Only (MP3)
   - 📋 Video Info

3. Click your choice
4. Wait for download
5. Receive file!
```

### For Admins:

#### `/admin` Command (Owner Only)
```
Shows admin panel with:
- Total users
- Total downloads
- System statistics
```

To enable admin features:
```
Add your Telegram User ID to ADMIN_IDS in Render

Get your ID from: @userinfobot
Example: ADMIN_IDS=123456789,987654321
```

---

## 🔧 TROUBLESHOOTING

### Bot Not Responding?

#### Check 1: Render Logs
```
1. Go to Render Dashboard
2. Click your service
3. Check "Logs" tab
4. Look for errors
```

#### Check 2: Environment Variables
```
1. Render Dashboard → Your Service
2. "Environment" tab
3. Verify BOT_TOKEN is set correctly
4. No extra spaces!
```

#### Check 3: Service Status
```
Render Dashboard → Your Service
Status should show: "Live" (green)
```

### Download Errors?

#### "File Too Large"
```
Solution: Try lower quality option
- 480p instead of 720p
- 360p for longer videos
- Audio only for music
```

#### "Unsupported URL"
```
Solution: Check if site is supported
- Use /sites command
- Try different video from same site
- Ensure link is direct video URL
```

#### "Download Failed"
```
Possible causes:
- Video is private/restricted
- Geographic restrictions
- Video deleted/unavailable

Solution:
- Check video is accessible in browser
- Try different video
- Wait and retry
```

---

## 🎨 CUSTOMIZATION

### Change Bot Messages

Edit `bot.py` file, find these sections:

#### Welcome Message
```python
# Line ~35
welcome_text = (
    f"🎬 <b>Premium Video Downloader Bot</b>\n\n"
    # Edit this text
)
```

#### Bot Name/Description
```python
# Change all instances of "Premium Video Downloader Bot"
# To your custom name
```

### Add More Features

#### Add New Command
```python
async def mycommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("My custom message!")

# In main():
app.add_handler(CommandHandler("mycommand", mycommand))
```

#### Change Quality Options
```python
# Line ~150
format_options = {
    'best': 'best[filesize<50M]',
    'custom': 'best[height<=1080]',  # Add this
}
```

---

## 📊 MONITORING

### Check Bot Usage
```
1. Render Dashboard
2. Your service → Metrics tab
3. View:
   - CPU usage
   - Memory usage
   - Request count
```

### View Logs
```
Render Dashboard → Logs tab
Shows all bot activity:
- User commands
- Downloads
- Errors
```

---

## 💰 RENDER FREE TIER

### What You Get:
- ✅ Free forever
- ✅ 750 hours/month
- ✅ Auto-deploys from GitHub
- ✅ SSL certificate
- ✅ Continuous deployment

### Limitations:
- ⚠️ Spins down after 15 mins inactivity
- ⚠️ Takes 30 seconds to wake up
- ⚠️ 512MB RAM

### Keep Bot Always Active:
Use UptimeRobot (free):
```
1. Go to: https://uptimerobot.com
2. Sign up (free)
3. Add new monitor:
   - Type: HTTP(s)
   - URL: Your Render service URL
   - Interval: 5 minutes
4. This keeps bot awake!
```

---

## 🔐 SECURITY

### Protect Your Token
- ❌ Never share your BOT_TOKEN
- ❌ Don't commit .env files to GitHub
- ✅ Always use environment variables
- ✅ Use private repos for sensitive bots

### Admin Access
```
Set ADMIN_IDS for admin commands:
ADMIN_IDS=123456789,987654321

Get your ID: @userinfobot
```

---

## 🚀 ADVANCED TIPS

### Faster Downloads
```python
# In ydl_opts, add:
'concurrent_fragment_downloads': 5,
```

### Better Quality Selection
```python
# Custom format:
'format': 'bestvideo[height<=1080]+bestaudio/best',
```

### Add Download Progress
```python
# In ydl_opts:
'progress_hooks': [progress_hook],

def progress_hook(d):
    if d['status'] == 'downloading':
        # Update message with progress
```

---

## 📞 SUPPORT & UPDATES

### Get Help:
- Check Render logs first
- Review troubleshooting section
- Test locally: `python bot.py`

### Update Bot:
```
1. Edit files on GitHub
2. Commit changes
3. Render auto-deploys!
```

### Monitor Updates:
- yt-dlp updates monthly
- python-telegram-bot stable
- Check GitHub for security updates

---

## ✅ QUICK CHECKLIST

### Before Deploy:
- [ ] Bot token from @BotFather
- [ ] GitHub repository created
- [ ] All 4 files uploaded
- [ ] Render account ready

### During Deploy:
- [ ] Web service created
- [ ] GitHub repo connected
- [ ] BOT_TOKEN added to environment
- [ ] Build completed successfully

### After Deploy:
- [ ] Bot responds to /start
- [ ] All commands working
- [ ] Test video download
- [ ] Check quality options

---

## 🎉 SUCCESS!

If everything works:
- ✅ Bot responds in Telegram
- ✅ Quality options appear
- ✅ Videos download successfully
- ✅ Statistics tracking works

**Congratulations! Your premium bot is live! 🚀**

---

## 📚 RESOURCES

- **Render Docs**: https://render.com/docs
- **yt-dlp GitHub**: https://github.com/yt-dlp/yt-dlp
- **python-telegram-bot**: https://python-telegram-bot.org
- **Supported Sites**: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

**Made with ❤️ for the Telegram community**

**Enjoy your premium video downloader bot! 🎬**
