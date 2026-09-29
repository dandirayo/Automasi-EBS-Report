@echo off
chcp 65001 >nul
title Setup Auto-Nyala & Auto-Sync EFS Report
color 0B

:MENU
cls
echo =======================================================
echo   PENGATURAN AUTO-NYALA & AUTO-SYNC SAAT KOMPUTER NYALA
echo =======================================================
echo.
echo Setiap kali komputer/laptop Anda dinyalakan dan login ke Windows:
echo  1. Menu CMD EFS otomatis terbuka siap pakai (Auto-Nyala).
echo  2. Folder OneDrive / Teams otomatis disinkronkan ke versi terbaru (Auto-Sync).
echo  (Tidak ada auto-generate H-1 otomatis, report menunggu pilihan Anda di menu)
echo.
echo Pilih opsi:
echo.
echo  [1] 🚀 Aktifkan Auto-Nyala + Auto-Sync saat Windows Boot
echo  [2] ❌ Nonaktifkan Auto-Run (Matikan)
echo  [3] 🔙 Keluar
echo.
echo =======================================================
set /p "opt=Pilihan Anda [1-3]: "

if "%opt%"=="1" (
    python "%~dp0engine\setup_autorun.py" menu
    echo.
    echo [SUKSES] Fitur Auto-Nyala & Auto-Sync berhasil DIAKTIFKAN!
    echo.
    pause
    goto MENU
)

if "%opt%"=="2" (
    python "%~dp0engine\setup_autorun.py" disable
    echo.
    echo [SUKSES] Fitur Auto-Nyala & Auto-Sync berhasil DIMATIKAN.
    echo.
    pause
    goto MENU
)

if "%opt%"=="3" (
    exit /b
)

goto MENU
