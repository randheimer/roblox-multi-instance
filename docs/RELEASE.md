# Release Instructions

## Creating a New Release

### 1. Update Version

Update version numbers in:
- `setup.py` - Update the `version` field
- `CHANGELOG.md` - Add new version section with changes

### 2. Commit Changes

```bash
git add .
git commit -m "Prepare release v1.0.0"
git push origin main
```

### 3. Create and Push Tag

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### 4. Automated Build

Once you push the tag, GitHub Actions will automatically:
- Build the Windows executable using PyInstaller
- Create a GitHub Release
- Upload the .exe file to the release
- Include README and LICENSE

### 5. Verify Release

1. Go to your GitHub repository
2. Click on "Releases" in the right sidebar
3. Verify the new release appears with the .exe file attached

## Manual Build (Optional)

If you want to build locally:

```bash
# Create icon
python create_icon.py

# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name "RobloxMultiInstance" --icon=icon.ico main.py

# Executable will be in dist/ folder
```

## Version Numbering

Follow Semantic Versioning (semver.org):
- MAJOR version for incompatible API changes
- MINOR version for new functionality (backwards compatible)
- PATCH version for bug fixes (backwards compatible)

Examples:
- v1.0.0 - Initial release
- v1.1.0 - New feature added
- v1.1.1 - Bug fix
- v2.0.0 - Breaking changes

## Pre-release

For beta/alpha releases, use:
```bash
git tag -a v1.0.0-beta.1 -m "Beta release"
git push origin v1.0.0-beta.1
```

The workflow will mark it as a pre-release automatically.
