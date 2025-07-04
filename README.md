# DE-CLI-Tool

A Python-based CLI tool designed for U-NEXT DE (Data Engineering) team members.

## Prerequisites

- **Python 3.10 or 3.11** (required)
  - Python 3.12 currently has compatibility issues with the `pyinstaller` package
- **Dependencies**: Install required packages with:

  ```bash
  pip install -r requirements.txt
  ```

## Development

### Building the Package

1. **Compile the application**:

   ```bash
   pyinstaller --onefile --clean --name de-cli-tool main.py
   ```

2. **Release process**:
   - Upload the compiled package from the `dist/` directory to the [GitHub releases page](https://github.com/u-next/de-cli-tool/releases)
   - Update the Homebrew formula with the new version and SHA256 hash: [de-cli-tool.rb](https://github.com/u-next/homebrew-de-tools/blob/main/de-cli-tool.rb)
   - Generate SHA256 hash with: `shasum -a 256 dist/de-cli-tool`

## Installation

### Using Homebrew (Recommended)

```bash
brew tap u-next/de-tools
brew install de-cli-tool
```

### Updating

```bash
brew upgrade de-cli-tool
```
