# Roblox Multi-Instance Launcher

A Python desktop application that allows you to run multiple Roblox instances simultaneously on Windows.

## Features

- Launch multiple RobloxPlayerBeta.exe instances at the same time
- Bypass Roblox's single-instance restriction using mutex management
- System tray support for background operation
- Simple and intuitive GUI
- Toggle multi-instance mode on/off

## Requirements

- Windows OS
- Python 3.7 or higher
- Roblox installed

## Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Click **"Enable Multi-Instance"** to initialize the multi-instance system

3. Launch Roblox from your browser or desktop - you can now open multiple instances

4. Log into different accounts in each Roblox window

5. Use **"Minimize to Tray"** to run the application in the background

6. Click **"Disable Multi-Instance"** when done to clean up resources

## How It Works

The application works by:

1. **Mutex Management**: Creates Windows mutex objects (`ROBLOX_singletonMutex` and `ROBLOX_singletonEvent`) before Roblox launches, preventing the single-instance check from blocking additional instances

2. **Cookie File Locking**: Locks the Roblox cookie file in read-only mode to prevent authentication conflicts (Error 773)

3. **Process Monitoring**: Uses `psutil` to track active RobloxPlayerBeta.exe processes

## Important Notes

- **Enable BEFORE launching Roblox** - The multi-instance mode must be active before you open any Roblox instances
- **Keep the app running** - Don't close the application while using multiple Roblox instances
- **Account switching** - You'll need to manually log into different accounts in each Roblox window
- **Performance** - Running multiple instances requires more system resources (RAM, CPU)

## Troubleshooting

**"Roblox not found" error:**
- Make sure Roblox is installed
- Check that Roblox is in the default location: `%LocalAppData%\Roblox\`

**Instances won't launch:**
- Make sure you clicked "Enable Multi-Instance" first
- Try restarting the application
- Close any existing Roblox instances before starting

**Error 773 (authentication issues):**
- This should be prevented by the cookie file lock
- If it occurs, restart the application and try again

**Application crashes:**
- Check `roblox_multi.log` for detailed error traces
- Ensure all dependencies are installed correctly
- Try running as administrator if permission errors occur

## Disclaimer

This tool is for educational purposes. Use at your own risk. Review Roblox's Terms of Service before using multi-instance tools.

## License

MIT License - Feel free to modify and distribute
