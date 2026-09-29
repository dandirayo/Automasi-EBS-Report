@echo off
chcp 65001 >nul
title EFS Daily Health Report
color 0A

:: Hanya muncul sekilas kalau Python sedang loading
echo Memeriksa Sistem EFS Engine... 

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak terdeteksi! 
    echo Pastikan Python sudah diinstall dan kotak "Add python.exe to PATH" sudah dicentang saat instalasi.
    pause
    exit /b
)

:: Sembunyikan semua teks instalasi yang panjang
python -m pip install -q -r "%~dp0engine\requirements.txt" >nul 2>&1
python -m playwright install chromium >nul 2>&1

:: Bersihkan layar dari teks booting, agar langsung masuk ke UI Keren
cls
python "%~dp0engine\main.py" %*
echo.
pause
