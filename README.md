# 🖱️ EMC (Easy Mouse Control)

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/badge/Release-v1.1.0-orange.svg)](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control/releases)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control)

> 🎮 **Control your mouse cursor using keyboard arrow keys!** Perfect for when your mouse isn't working or you prefer keyboard navigation.

![Demo](https://img.shields.io/badge/✨%20Beautiful%20GUI-9cf?style=for-the-badge)
![Demo](https://img.shields.io/badge/⚡%20Real--time%20Speed%20Control-yellow?style=for-the-badge)
![Demo](https://img.shields.io/badge/🎯%20Smooth%20Movement-brightgreen?style=for-the-badge)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **Beautiful GUI** | Modern dark-themed interface with customtkinter |
| 🎯 **Smooth Movement** | Cursor moves smoothly while holding arrow keys |
| ↗️ **Diagonal Movement** | Move diagonally by holding two arrows simultaneously |
| ⚡ **Adjustable Speed** | Real-time speed control with slider and buttons (1-50 px) |
| 🖱️ **Mouse Clicks** | Left and right click support (Ctrl+Enter for right) |
| 🌍 **Universal** | Works in all applications and games |
| 💻 **No Mouse Required** | Full mouse control from keyboard |
| 🎮 **Easy Toggle** | Start/Stop with a single click |

---

## 🖼️ Screenshots

```
┌─────────────────────────────────────┐
│  🖱️ Easy Mouse Control              │
│                                     │
│  ┌─ Status ──────────────────────┐  │
│  │  ▶️ ACTIVE                    │  │
│  │  Use arrow keys to control    │  │
│  └────────────────────────────────┘  │
│                                     │
│  ┌─ Speed Control ───────────────┐  │
│  │  Speed: 10 px                 │  │
│  │  [========●==========]        │  │
│  │  [➖ Slower]  [➕ Faster]     │  │
│  └────────────────────────────────┘  │
│                                     │
│  ┌─ Keyboard Controls ───────────┐  │
│  │  ⬆️⬇️⬅️➡️ Arrows → Move     │  │
│  │  ⏎ Enter → Left Click        │  │
│  │  ⌨️ Ctrl+Enter → Right Click │  │
│  └────────────────────────────────┘  │
│                                     │
│     [     ⏹️  STOP     ]            │
│                                     │
└─────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Option 1: Download Ready-to-Use EXE (Recommended)
1. Go to [Releases](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control/releases)
2. Download `EMC_GUI.exe` (GUI version) or `EMC_CLI.exe` (Command line)
3. Double-click to run - no installation needed!

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control.git
cd EMC-Easy-Mouse-Control

# Install dependencies
pip install -r requirements.txt

# Run GUI version (recommended)
python mouse_control_gui.py

# Or run CLI version
python mouse_control.py
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| ⬆️ ⬇️ ⬅️ ➡️ **Arrow Keys** | Move cursor |
| ⏎ **Enter** | Left mouse click |
| ⌨️ **Ctrl + Enter** | Right mouse click |
| ➕ **+** or **=** | Increase speed (+2) |
| ➖ **-** | Decrease speed (-2) |
| ⎋ **Esc** | Stop program |

### Speed Settings
- **Range:** 1 to 50 pixels per step
- **Default:** 10 pixels per step
- **Adjust anytime** via GUI slider or keyboard!

---

## 🛠️ Build Your Own EXE

```bash
# Install pyinstaller
pip install pyinstaller

# Build GUI version (recommended)
pyinstaller --onefile --name "EMC_GUI" --windowed mouse_control_gui.py

# Build CLI version
pyinstaller --onefile --name "EMC_CLI" mouse_control.py
```

The executable will be created in the `dist/` folder.

---

## 📋 Requirements

- Python 3.7+ (for source version)
- Windows OS
- Dependencies (auto-installed):
  - `customtkinter` - Modern GUI framework
  - `pynput` - Keyboard/mouse control
  - `Pillow` - Image processing

---

## 📦 Installation from Source

```bash
# 1. Clone repository
git clone https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control.git
cd EMC-Easy-Mouse-Control

# 2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run GUI version
python mouse_control_gui.py
```

---

## 🎯 Use Cases

- 🖱️ **Broken mouse?** No problem! Use your keyboard instead
- ♿ **Accessibility** - Easier navigation for users with motor difficulties
- 🎮 **Gaming** - Alternative control method for games
- 💼 **Remote desktop** - Better control in limited environments
- ⚡ **Quick tasks** - Sometimes keyboard is faster than mouse!
- 🔧 **Technicians** - Control PC when mouse drivers aren't working

---

## 📝 Changelog

### v1.1.0 - GUI Update 🎨
- ✨ Added beautiful modern GUI with customtkinter
- 🎨 Dark theme with accent colors
- 🎚️ Real-time speed slider
- 📊 Visual status indicators
- 🖱️ One-click Start/Stop
- 🌍 Full English localization

### v1.0.0 - Initial Release 🚀
- 🎯 Basic mouse control with arrow keys
- ⚡ Adjustable speed
- 🖱️ Left & Right click support
- 💻 Command line interface

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs via [Issues](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control/issues)
- 💡 Suggest features
- 🔧 Submit pull requests

---

<div align="center">

**Made with ❤️ by [Stepan](https://github.com/stepanpotehin1-cmyk)**

⭐ **Star this repo if you found it useful!** ⭐

</div>
