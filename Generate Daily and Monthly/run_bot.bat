@echo off
chcp 65001 >nul
title EFS Telegram Bot Listener
color 0B

echo Menyalakan Telegram Bot Listener...
python -m pip install -q pyTelegramBotAPI >nul 2>&1

cls
python "%~dp0engine\telegram_bot.py"
pause
