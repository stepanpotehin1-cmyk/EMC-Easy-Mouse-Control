# EMC - Easy Mouse Control

[![Version](https://img.shields.io/badge/Version-1.2.0-blue.svg)](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control/releases)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Control your mouse cursor using keyboard arrow keys! Perfect for when your mouse isn't working.

![GUI Preview](https://img.shields.io/badge/Modern-Dark%20GUI-purple?style=for-the-badge)

---

## Download & Install

### Option 1: Installer (Recommended)
1. Download **`EMC-Installer.zip`** from [Releases](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control/releases)
2. Extract and run `install.bat`
3. Shortcuts will be created on Desktop and Start Menu

### Option 2: Portable (Just Run)
1. Download **`EMC.exe`** from [Releases](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control/releases)
2. Double-click to run - no installation needed!

---

## Controls

| Key | Action |
|-----|--------|
| Arrow Keys | Move cursor |
| Enter | Left click |
| Ctrl + Enter | Right click |
| + or = | Increase speed |
| - | Decrease speed |
| Esc | Stop / Exit |

---

## Features

- **Modern Dark GUI** - Beautiful interface with real-time controls
- **Speed Slider** - Adjust cursor speed from 1-50 pixels
- **Visual Status** - Clear ACTIVE / STOPPED indicators
- **Big START Button** - Easy to find and click!
- **No Installation Required** - Portable version available
- **System Tray** - Minimize to tray (coming soon)

---

## Screenshot

```
┌─────────────────────────────┐
│           EMC               │
│    Easy Mouse Control       │
│                             │
│  ┌─ STATUS ─────────────┐   │
│  │      STOPPED         │   │
│  └──────────────────────┘   │
│                             │
│  ┌─ SPEED CONTROL ──────┐   │
│  │  Speed: 10 px        │   │
│  │  [────────●────]     │   │
│  │  [- Slower] [+ Faster]  │
│  └──────────────────────┘   │
│                             │
│  ┌─ CONTROLS ───────────┐   │
│  │  Arrow Keys - Move   │   │
│  │  Enter - Left click  │   │
│  │  Ctrl+Enter - Right  │   │
│  │  +/- - Speed         │   │
│  │  Esc - Stop          │   │
│  └──────────────────────┘   │
│                             │
│   [        START        ]   │
│                             │
│      Made by Stepan         │
└─────────────────────────────┘
```

---

## Build from Source

```bash
# Install dependencies
pip install customtkinter pynput

# Run
python EMC.py

# Build EXE
pyinstaller --onefile --windowed EMC.py
```

---

Made with ❤️ by [Stepan](https://github.com/stepanpotehin1-cmyk)
