# PyWinOptiPC

A Python-based Windows service and process optimizer that helps manage system services and background processes. PyWinOptiPC automatically stops specified Windows services and terminates configured processes for improved system performance and resource management.

## 🎯 Features

- ⚙️ **Automatically stops specified Windows services** - Configure which services to disable
- 🛑 **Terminates configured background processes** - Remove unnecessary processes running in the background
- 📊 **Continuous monitoring and management** - Keep your system optimized with periodic checks
- 🔐 **Administrator privileges handling** - Safely manages elevated permissions
- ✅ **Graceful error handling** - Reliable error handling and service state verification
- 🎨 **Colored terminal output** - Easy-to-read console feedback

## 📋 Prerequisites

- **Python 3.7+**
- **Windows Operating System** (Windows 7, 8, 10, 11, Server editions)
- **Administrator privileges** (required to stop services and terminate processes)

## 🚀 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/acrdiaz/PyWinOptiPC.git
cd PyWinOptiPC
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the application:
```bash
python main.py
```

## ⚙️ Configuration

### Setting Up Commands

Create or edit the `config/commands.txt` file to specify which services and processes to manage:

**Example `config/commands.txt`:**
```
# Windows Services to stop (one per line)
# Service names should be the service's internal name, not display name
servicename1
servicename2
OneDrive
DiagTrack

# Processes to terminate
process1.exe
process2.exe
```

### Finding Service Names

To find the correct service names for your configuration:

```bash
# List all services and their states
Get-Service | Format-Table Name, DisplayName, Status

# Or in Command Prompt:
sc query
```

## 📖 Usage

### Basic Usage

Simply run the application with administrator privileges:

```bash
python main.py
```

The application will:
1. Read the commands from `config/commands.txt`
2. Start monitoring and executing commands
3. Check every 3 seconds for services/processes to manage
4. Display status messages with colored output
5. Exit gracefully when you press `Ctrl+C`

### Running with Administrator Privileges

**Option 1: Command Prompt as Administrator**
```bash
# Open Command Prompt as Administrator, then:
cd path\to\PyWinOptiPC
python main.py
```

**Option 2: Create a Batch File**
Create `run.bat` in the project root:
```batch
@echo off
python main.py
pause
```
Then right-click → "Run as administrator"

### Example Output
```
Service monitor started. Press Ctrl+C to exit.

Checking and stopping services...
✓ Service 'OneDrive' stopped successfully
✓ Process 'bloatware.exe' terminated

Waiting 3 seconds before next check...

[Next iteration...]

Program terminated by user.
```

## 🔧 Dependencies

- **psutil** (≥5.9.0) - System and process management
- **pywin32** (≥306) - Advanced Windows service management
- **colorama** (≥0.4.6) - Cross-platform colored terminal output

## ⚠️ Important Notes

- **Administrator Privileges Required**: This application must run with elevated privileges to stop services and terminate processes
- **Be Careful with Configuration**: Stopping critical system services may cause system instability
- **Test Before Production**: Always test your configuration on a non-critical system first
- **Backup Configuration**: Keep a backup of your working `config/commands.txt`

### Recommended Services to Disable (at your own risk)

Common bloatware/telemetry services:
- `DiagTrack` - Diagnostic Tracking Service
- `dmwappushservice` - DmwAppPushService
- `OneDrive` - OneDrive (if not needed)
- `WSearch` - Windows Search (if using alternative search)

## 🐛 Troubleshooting

### "Access Denied" Error
- **Solution**: Run the application as Administrator

### Service/Process Not Stopping
- **Solution**: Verify the exact service name or process name in `config/commands.txt`
- Some services may require reboot or have dependencies

### Application Crashes on Startup
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For issues, questions, or suggestions, please open an [issue](https://github.com/acrdiaz/PyWinOptiPC/issues) on GitHub.

## ⚖️ Disclaimer

This application interacts with Windows system services and processes. Use it responsibly and at your own risk. The author is not responsible for any system damage or data loss caused by improper use of this tool.

---

**Last Updated**: 2026-03-13 01:26:32
**Version**: 1.0.0
**Author**: acrdiaz