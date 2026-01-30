# 🚂 Railway Deployment Guide

This guide will walk you through deploying your Universal Video Downloader bot to Railway step-by-step.

## 📋 Prerequisites

Before you begin, make sure you have:
- [ ] A Telegram account
- [ ] A GitHub account (free)
- [ ] A Railway account (free tier available)

## 🤖 Step 1: Create Your Telegram Bot

1. **Open Telegram** on your phone or computer

2. **Find BotFather:**
   - Search for `@BotFather` in Telegram
   - Start a chat with BotFather
   - This is the official bot for creating new bots

3. **Create a new bot:**
   ```
   Send: /newbot
   ```

4. **Choose a name:**
   - BotFather will ask for a name (e.g., "My Video Downloader")
   - This is the display name users will see

5. **Choose a username:**
   - Must end in `bot` (e.g., `my_video_dl_bot`)
   - Must be unique on Telegram
   - Try variations if your choice is taken

6. **Save your token:**
   - BotFather will send you a token like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`
   - **COPY THIS TOKEN** - you'll need it later
   - **Keep it secret!** Anyone with this token can control your bot

## 🐙 Step 2: Upload Code to GitHub

### Option A: Use This Repository (Easiest)

1. **Fork this repository:**
   - Click the "Fork" button at the top of this GitHub page
   - This creates a copy in your GitHub account

2. **Done!** You can skip to Step 3

### Option B: Create Your Own Repository

1. **Go to GitHub** (https://github.com)
   - Sign in to your account

2. **Create a new repository:**
   - Click the "+" button (top right)
   - Select "New repository"
   - Choose a name (e.g., "telegram-video-bot")
   - Make it Public or Private (your choice)
   - Click "Create repository"

3. **Upload files:**
   - Download all files from this project
   - In your new repository, click "Add file" > "Upload files"
   - Drag and drop all the files:
     - `bot.py`
     - `requirements.txt`
     - `Procfile`
     - `railway.json`
     - `nixpacks.toml`
     - `runtime.txt`
     - `README.md`
     - `.gitignore`
   - Click "Commit changes"

## 🚂 Step 3: Deploy to Railway

### 3.1 Create Railway Account

1. **Go to Railway:**
   - Visit https://railway.app/
   - Click "Login" or "Start a New Project"

2. **Sign up with GitHub:**
   - Click "Login with GitHub"
   - Authorize Railway to access your GitHub
   - This makes deployment easier!

### 3.2 Create New Project

1. **Start a new project:**
   - Click "New Project" on Railway dashboard
   - Select "Deploy from GitHub repo"

2. **Select your repository:**
   - Find your repository in the list
   - Click on it to select
   - Railway will start scanning your code

3. **Wait for detection:**
   - Railway will automatically detect Python
   - It will find your configuration files
   - This takes about 10-30 seconds

### 3.3 Add Your Bot Token

**This is the most important step!**

1. **Find the Variables tab:**
   - In your Railway project, look for "Variables" in the left sidebar
   - Click on it

2. **Add new variable:**
   - Click "New Variable" or "Add Variable"
   - Enter the following:
     - **Variable name:** `BOT_TOKEN`
     - **Value:** Paste your token from BotFather
   - Click "Add" or save

3. **Verify:**
   - You should see `BOT_TOKEN` listed with a hidden value (••••••)
   - The value should NOT be visible for security

### 3.4 Deploy!

1. **Start deployment:**
   - Railway should start building automatically
   - If not, click "Deploy" or "Redeploy"

2. **Monitor the build:**
   - Click on "Deployments" tab
   - Click on the latest deployment
   - You'll see the build logs

3. **Wait for success:**
   - Build usually takes 1-3 minutes
   - Look for "Bot started successfully!" in the logs
   - Status should change to "Success" or "Active"

## ✅ Step 4: Test Your Bot

1. **Find your bot on Telegram:**
   - Search for your bot's username (the one you created)
   - Start a chat

2. **Send the start command:**
   ```
   /start
   ```

3. **You should receive:**
   - A welcome message
   - Instructions on how to use the bot

4. **Test with a video:**
   - Find any YouTube video
   - Copy the URL
   - Paste it in your bot chat
   - Wait for the download!

## 🎉 Success!

If everything works, you now have a working video downloader bot!

## 🔧 Common Issues and Solutions

### Issue: "BOT_TOKEN environment variable not set!"

**Solution:**
1. Go to Railway project
2. Click "Variables"
3. Add `BOT_TOKEN` with your token
4. Wait for auto-redeploy or click "Redeploy"

### Issue: Bot doesn't respond on Telegram

**Checklist:**
- [ ] Is the Railway deployment "Active"?
- [ ] Check Railway logs for "Bot started successfully!"
- [ ] Is `BOT_TOKEN` set correctly in Variables?
- [ ] Did you copy the full token from BotFather?
- [ ] Try restarting: Go to Settings > Restart

**How to check Railway logs:**
1. Go to your Railway project
2. Click "Deployments"
3. Click on the active deployment
4. Scroll through the logs

### Issue: Build fails on Railway

**Common causes:**
1. Missing files - make sure all files are uploaded
2. Wrong Python version - should be 3.10+
3. Syntax errors in code

**Solution:**
1. Check the build logs for specific errors
2. Make sure all files from this repo are in your GitHub
3. Verify `requirements.txt` exists and has content

### Issue: "Video is too large"

**This is normal!**
- Telegram bots can only send files up to 50MB
- Try shorter videos
- The bot will tell you if a video is too large

### Issue: "This website is not supported"

**Solution:**
- Check if the site is in the supported list: `/sites` command
- Make sure you're using a video URL, not a channel or playlist
- Try a different video from the same site

## 💡 Pro Tips

1. **Check logs regularly:**
   - Railway logs show all bot activity
   - Useful for debugging issues

2. **Monitor usage:**
   - Railway shows resource usage in the Metrics tab
   - Free tier includes $5 monthly credit

3. **Update your bot:**
   - Update files in GitHub
   - Railway auto-deploys changes
   - Watch the build logs to ensure success

4. **Backup your token:**
   - Save your `BOT_TOKEN` somewhere safe
   - If you lose it, ask BotFather for a new one with `/token`

## 📊 Railway Free Tier Limits

- **$5 free credit per month**
- Resets monthly
- Enough for:
  - ~500-1000 video downloads per month
  - Continuous bot operation
  - Basic usage

## 🔐 Security Best Practices

1. **Never share your bot token:**
   - Don't post it in screenshots
   - Don't commit it to public GitHub
   - Railway Variables are secure

2. **Use environment variables:**
   - Always use Railway Variables for secrets
   - Never hardcode tokens in code

3. **Monitor usage:**
   - Check Railway logs for suspicious activity
   - Revoke token if compromised (via BotFather)

## 🆘 Still Having Issues?

1. **Check Railway status:**
   - https://railway.statuspage.io/
   - Ensure no outages

2. **Review logs carefully:**
   - Often the error message tells you exactly what's wrong

3. **Start fresh:**
   - Delete the Railway project
   - Create a new one
   - Follow steps again carefully

4. **Get help:**
   - Railway Discord: https://discord.gg/railway
   - Check Railway docs: https://docs.railway.app/

## 🎯 Next Steps

Once your bot is working:

1. **Customize the bot:**
   - Edit `bot.py` to add features
   - Commit changes to GitHub
   - Railway auto-deploys

2. **Share with friends:**
   - Give them your bot username
   - They can download videos too!

3. **Monitor performance:**
   - Check Railway metrics
   - Watch your credit usage

---

**Congratulations on deploying your bot! 🎊**

Enjoy downloading videos from anywhere on the web!
