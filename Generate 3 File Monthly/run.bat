@echo off
chcp 65001 >nul
title Automasi EFS Monthly
color 0A

:MENU
cls
echo =======================================================
echo           AUTOMASI EFS MONTHLY REPORT
echo =======================================================
echo.
echo  1. Generate 3 File Monthly (DOCX, PPTX, PDF)
echo     (Dari template ke output dengan mapping data)
echo.
echo  2. Generate PPT Kosongan (Blank Presentation)
echo     (Membuat file presentasi kosong baru)
echo.
echo  0. Keluar
echo.
echo =======================================================
set /p pilihan="Pilih menu (1/2/0): "

if "%pilihan%"=="1" goto GENERATE_ALL
if "%pilihan%"=="2" goto GENERATE_BLANK_PPT
if "%pilihan%"=="0" exit

goto MENU

:GENERATE_ALL
cls
echo =======================================================
echo   Proses Generate 3 File Monthly (DOCX, PPTX, PDF)
echo =======================================================
echo.
python engine\generate_monthly_report.py
echo.
echo =======================================================
pause
goto MENU

:GENERATE_BLANK_PPT
cls
echo =======================================================
echo          Proses Generate PPT Kosongan
echo =======================================================
echo.
python -c "from pptx import Presentation; prs = Presentation(); prs.save('Output\PPT_Kosongan.pptx'); print('[+] Berhasil membuat PPT_Kosongan.pptx di folder Output!')"
echo.
echo =======================================================
pause
goto MENU
