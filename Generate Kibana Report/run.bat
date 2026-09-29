@echo off
chcp 65001 >nul
title Kibana Report Engine
color 0B

echo Memeriksa Sistem Kibana Engine... 

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak terdeteksi! 
    pause
    exit /b
)

:: Install requirement diam-diam
python -m pip install -q -r "%~dp0engine\requirements.txt" >nul 2>&1
python -m playwright install chromium >nul 2>&1

cls
python "%~dp0engine\main.py" %*
echo.
pause
