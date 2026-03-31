@echo off
chcp 65001 >nul
echo Installing EMC (Easy Mouse Control)...

set INSTALL_DIR=%LOCALAPPDATA%\EMC
set EXE_NAME=EMC.exe

if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

copy /Y "%EXE_NAME%" "%INSTALL_DIR%\%EXE_NAME%" >nul

echo Creating shortcuts...

set DESKTOP=%USERPROFILE%\Desktop
set STARTMENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs

powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%DESKTOP%\EMC.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\%EXE_NAME%'; $Shortcut.WorkingDirectory = '%INSTALL_DIR%'; $Shortcut.IconLocation = '%INSTALL_DIR%\%EXE_NAME%'; $Shortcut.Save()"

powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%STARTMENU%\EMC.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\%EXE_NAME%'; $Shortcut.WorkingDirectory = '%INSTALL_DIR%'; $Shortcut.IconLocation = '%INSTALL_DIR%\%EXE_NAME%'; $Shortcut.Save()"

echo.
echo ===================================
echo  EMC installed successfully!
echo.
echo  Location: %INSTALL_DIR%
echo  Shortcuts created on Desktop and Start Menu
echo ===================================
echo.
pause
