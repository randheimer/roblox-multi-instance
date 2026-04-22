## Frequently Asked Questions

### General Questions

**Q: Is this safe to use?**
A: The application only manipulates Windows mutexes and doesn't modify Roblox files. However, use at your own risk and review Roblox's Terms of Service.

**Q: Will I get banned for using this?**
A: This tool doesn't inject code or modify Roblox. However, we cannot guarantee anything. Use responsibly.

**Q: Does this work on Mac or Linux?**
A: No, this is Windows-only as it uses Windows-specific APIs (win32 mutexes).

**Q: How many instances can I run?**
A: Limited only by your system resources (RAM, CPU). Most systems can handle 2-4 instances comfortably.

### Technical Questions

**Q: What is a mutex?**
A: A mutex (mutual exclusion object) is a Windows synchronization primitive. Roblox uses mutexes to prevent multiple instances from running.

**Q: Why do I need to enable it before launching Roblox?**
A: The mutexes must be created before Roblox checks for them. If Roblox starts first, it will create its own mutexes.

**Q: What is Error 773?**
A: Error 773 is a Roblox authentication error that can occur when multiple instances try to access the same cookie file. This tool locks the file to prevent this.

**Q: Can I use this with Roblox Studio?**
A: This tool is designed for RobloxPlayerBeta.exe. It may not work with Roblox Studio.

### Troubleshooting

**Q: The application crashes on startup**
A: Check that all dependencies are installed correctly. Run `pip install -r requirements.txt` again.

**Q: I enabled multi-instance but can't launch multiple Roblox windows**
A: Make sure you're launching Roblox AFTER enabling multi-instance mode. Try closing all Roblox windows and starting fresh.

**Q: The system tray icon doesn't appear**
A: This is usually a Windows notification area setting. Check your system tray settings or restart the application.

**Q: Can I run this on startup?**
A: Yes, you can add it to your Windows startup folder or create a scheduled task.

### Development Questions

**Q: Can I contribute to this project?**
A: Yes! Check out CONTRIBUTING.md for guidelines.

**Q: How do I report a bug?**
A: Open an issue on GitHub with details about the problem, your system, and steps to reproduce.

**Q: Can I modify the code?**
A: Yes, this project is MIT licensed. Feel free to fork and modify.
