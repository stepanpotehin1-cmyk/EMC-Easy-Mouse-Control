# 🖱️ EMC (Easy Mouse Control)

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/badge/Release-v1.0-orange.svg)](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control/releases)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control)

> 🎮 **Control your mouse cursor using keyboard arrow keys!** Perfect for when your mouse isn't working or you prefer keyboard navigation.

![Demo](https://img.shields.io/badge/✨%20Smooth%20Movement-9cf?style=for-the-badge)
![Demo](https://img.shields.io/badge/⚡%20Real--time%20Speed%20Control-yellow?style=for-the-badge)
![Demo](https://img.shields.io/badge/🎯%20Diagonal%20Movement-brightgreen?style=for-the-badge)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Smooth Movement** | Cursor moves smoothly while holding arrow keys |
| ↗️ **Diagonal Movement** | Move diagonally by holding two arrows simultaneously |
| ⚡ **Adjustable Speed** | Change cursor speed on the fly with `+` and `-` keys |
| 🖱️ **Mouse Clicks** | Left and right click support |
| 🌍 **Universal** | Works in all applications |
| 💻 **No Mouse Required** | Full mouse control from keyboard |

---

## 🚀 Quick Start

### Option 1: Download Ready-to-Use EXE
1. Go to [Releases](https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control/releases)
2. Download `MouseControl.exe`
3. Double-click to run!

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/stepanpotehin1-cmyk/EMC-Easy-Mouse-Control.git

# Install dependencies
pip install -r requirements.txt

# Run the program
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
| ⎋ **Esc** | Exit program |

### Speed Settings
- **Range:** 1 to 50 pixels per step
- **Default:** 10 pixels per step
- **Adjust anytime** while the program is running!

---

## 🛠️ Build Your Own EXE

```bash
pip install pyinstaller
pyinstaller --onefile --name "MouseControl" mouse_control.py
```

The executable will be created in the `dist/` folder.

---

## 📋 Requirements

- Python 3.7 or higher (for source version)
- Windows OS
- No additional requirements for EXE version!

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

# 4. Run!
python mouse_control.py
```

---

## 🎯 Use Cases

- 🖱️ **Broken mouse?** No problem! Use your keyboard instead
- ♿ **Accessibility** - Easier navigation for some users
- 🎮 **Gaming** - Alternative control method
- 💼 **Remote desktop** - Better control in limited environments
- ⚡ **Quick tasks** - Sometimes keyboard is faster!

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

---

<div align="center">

Made with ❤️ by [Stepan](https://github.com/stepanpotehin1-cmyk)

⭐ **Star this repo if you found it useful!** ⭐

</div>
