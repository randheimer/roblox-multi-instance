## Quick Start Guide

### Prerequisites
- Windows 10 or 11
- Python 3.7+
- Roblox installed

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/roblox-multi-instance.git
cd roblox-multi-instance
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python main.py
```

### First Time Setup

1. Launch the application
2. Click "Enable Multi-Instance"
3. Open Roblox from your browser or desktop
4. You can now launch multiple Roblox windows
5. Log into different accounts in each window

### Tips

- Enable multi-instance mode BEFORE launching Roblox
- Keep the application running while using multiple instances
- Use "Minimize to Tray" to run in the background
- Click "Disable Multi-Instance" when done to clean up resources

### Common Issues

**Application won't start:**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.7+)

**"Roblox not found" error:**
- Verify Roblox is installed in the default location
- Try reinstalling Roblox

**Multiple instances won't launch:**
- Make sure you enabled multi-instance mode first
- Close all existing Roblox windows and try again
- Restart the application

### Building Executable (Optional)

To create a standalone .exe file:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

The executable will be in the `dist/` folder.
