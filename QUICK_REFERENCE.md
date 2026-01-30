# ⚡ QUICK COMMAND REFERENCE

## 🚀 Render Deployment (5 Minutes)

### Step 1: Create Bot (2 mins)
```
1. Telegram → Search @BotFather
2. Send: /newbot
3. Name: My Premium Video Bot
4. Username: mypremium_video_bot
5. Save token: 1234567890:ABCdef...
```

### Step 2: Upload to GitHub (1 min)
```
1. GitHub → New Repository
2. Name: premium-video-bot
3. Upload 4 files:
   - bot.py
   - requirements.txt
   - render.yaml
   - .gitignore
```

### Step 3: Deploy on Render (2 mins)
```
1. Render.com → Sign up with GitHub
2. New Web Service → Connect repo
3. Environment Variables:
   - BOT_TOKEN = your_token
   - ADMIN_IDS = your_telegram_id
4. Click Deploy!
```

---

## 🎯 Bot Commands

### User Commands
```
/start   → Welcome & Features
/help    → Usage Guide
/stats   → Your Statistics
/quality → Set Default Quality
/sites   → Supported Platforms
/about   → Bot Information
```

### Admin Commands
```
/admin   → Admin Dashboard
         (Requires ADMIN_IDS set)
```

---

## 📥 Download Process

### Method 1: Direct Link
```
1. Copy video URL
2. Paste in bot
3. Choose quality
4. Receive video
```

### Quality Options
```
🎬 Best Quality  → Highest available
📺 720p HD       → Standard HD
📱 480p SD       → Mobile friendly
📉 360p          → Low bandwidth
🎵 Audio Only    → MP3 format
📋 Video Info    → Preview details
```

---

## 🔧 Environment Variables

### Required
```bash
BOT_TOKEN=1234567890:ABCdefGHIjklMNO
```

### Optional
```bash
ADMIN_IDS=123456789,987654321
```

### Get Your Telegram ID
```
Telegram → Search @userinfobot
Send: /start
Copy your ID
```

---

## 🌐 Supported Sites (Examples)

### Video Platforms
```
✅ youtube.com
✅ vimeo.com
✅ dailymotion.com
✅ rumble.com
```

### Social Media
```
✅ instagram.com
✅ facebook.com
✅ tiktok.com
✅ twitter.com/x.com
✅ reddit.com
```

### Streaming
```
✅ twitch.tv
✅ kick.com
✅ youtube.com/live
```

### Adult Content
```
✅ xhamster.com
✅ pornhub.com
✅ xvideos.com
✅ redtube.com
```

**Total: 1000+ sites!**

---

## 🐛 Quick Troubleshooting

### Bot Not Responding
```
✓ Check Render logs
✓ Verify BOT_TOKEN
✓ Check service status (must be "Live")
✓ Restart service if needed
```

### Download Failed
```
✓ Try lower quality
✓ Check video is public
✓ Verify site is supported
✓ Check file size (<50MB)
```

### Build Failed
```
✓ Check requirements.txt exists
✓ Verify Python 3.9+ specified
✓ Check all files uploaded
✓ Review build logs
```

---

## 💰 Render Free Tier

### Included Free
```
✅ 750 hours/month
✅ 512 MB RAM
✅ Auto-deploy from GitHub
✅ SSL certificate
```

### Limitations
```
⚠️ Sleeps after 15 min inactivity
⚠️ 30 sec wake time
⚠️ 50MB file size limit (Telegram)
```

### Keep Active (Free)
```
1. UptimeRobot.com (free account)
2. Add HTTP monitor
3. URL: Your Render service URL
4. Interval: 5 minutes
5. Bot stays awake! ✅
```

---

## 📊 File Structure

### Required Files
```
premium-video-bot/
├── bot.py              # Main bot code
├── requirements.txt    # Python dependencies
├── render.yaml         # Render config
└── .gitignore         # Git ignore rules
```

### Optional Files
```
├── README.md          # Project documentation
├── SETUP_GUIDE.md     # Detailed setup guide
└── LICENSE            # License file
```

---

## 🎨 Customization Quick Tips

### Change Welcome Message
```python
# bot.py, line ~35
welcome_text = (
    f"🎬 <b>Your Custom Title</b>\n\n"
    # Edit this...
)
```

### Add Custom Command
```python
async def mycommand(update, context):
    await update.message.reply_text("Custom!")

# In main():
app.add_handler(CommandHandler("mycommand", mycommand))
```

### Change Quality Presets
```python
# bot.py, line ~150
format_options = {
    'best': 'best[filesize<50M]',
    'custom': 'best[height<=1080]',  # Add this
}
```

---

## 🔐 Security Checklist

### DO:
```
✅ Use environment variables
✅ Keep token secret
✅ Use private repo (optional)
✅ Set ADMIN_IDS for admin features
✅ Regular updates
```

### DON'T:
```
❌ Share BOT_TOKEN
❌ Commit .env to GitHub
❌ Hardcode sensitive data
❌ Use same token for testing
❌ Ignore security updates
```

---

## 📞 Quick Links

### Deployment
- **Render**: https://render.com
- **Railway**: https://railway.app (alternative)
- **Replit**: https://replit.com (for testing)

### Documentation
- **Setup Guide**: SETUP_GUIDE.md
- **yt-dlp Sites**: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md
- **Telegram Bot API**: https://core.telegram.org/bots/api

### Tools
- **BotFather**: @BotFather (Telegram)
- **Get User ID**: @userinfobot (Telegram)
- **UptimeRobot**: https://uptimerobot.com

---

## 🎯 Success Checklist

### Deployment
- [ ] Bot token obtained
- [ ] GitHub repo created
- [ ] Files uploaded
- [ ] Render service created
- [ ] Environment variables set
- [ ] Build successful
- [ ] Bot responding

### Testing
- [ ] /start works
- [ ] Quality buttons appear
- [ ] Video downloads
- [ ] Audio extraction works
- [ ] Statistics tracking
- [ ] All commands functional

---

## 💡 Pro Tips

### Best Practices
```
✓ Test locally first
✓ Start with simple videos
✓ Monitor Render logs
✓ Keep dependencies updated
✓ Backup configuration
```

### Performance
```
✓ Use lower quality for faster downloads
✓ Audio only is quickest
✓ Monitor usage stats
✓ Consider upgrade if heavy use
```

### User Experience
```
✓ Set clear bot description
✓ Add profile picture
✓ Respond to errors gracefully
✓ Provide helpful messages
```

---

## 🆘 Emergency Commands

### If Bot Crashes
```bash
# Render Dashboard
1. Go to service
2. Manual Deploy → Redeploy
3. Check logs for errors
```

### If Token Leaked
```
1. Telegram → @BotFather
2. Send: /mybots
3. Select bot
4. /revoke
5. Get new token
6. Update Render env variable
```

### Fresh Start
```
1. Delete Render service
2. Create new service
3. Re-add environment variables
4. Deploy again
```

---

## 📈 Monitoring

### Check Bot Health
```
Render Dashboard:
- Metrics tab → CPU/RAM usage
- Logs tab → Real-time activity
- Events tab → Deployment history
```

### User Activity
```
Bot Statistics:
- /admin command (owner)
- Check total users
- Monitor downloads
```

---

**Keep this reference handy! 📋**

**For detailed guide, see SETUP_GUIDE.md**
