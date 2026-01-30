#!/bin/bash

echo "Starting Universal Video Downloader Bot..."
echo "Python version:"
python --version

echo "Installing dependencies..."
pip install --no-cache-dir -r requirements.txt

echo "Starting bot..."
python bot.py
