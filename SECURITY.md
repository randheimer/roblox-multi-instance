# Security Policy

## Supported Versions

Currently supported versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do NOT** open a public issue
2. Email the maintainer directly with details
3. Include steps to reproduce the vulnerability
4. Allow reasonable time for a fix before public disclosure

## Security Considerations

This application:
- Manipulates Windows system mutexes
- Accesses local file system (Roblox installation directory)
- Manages process execution
- Locks cookie files

### Best Practices for Users

- Only download from official repository
- Review source code before running
- Run with standard user privileges (avoid administrator unless necessary)
- Keep Python and dependencies updated
- Be aware this tool modifies Roblox's normal behavior

### Known Limitations

- Cookie file locking may fail if Roblox is already running
- Mutex management requires Windows-specific APIs
- No encryption for inter-process communication
- Relies on Roblox's default installation paths

## Disclaimer

This tool is provided as-is for educational purposes. Users are responsible for compliance with Roblox's Terms of Service and any applicable laws.
