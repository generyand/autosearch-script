# Auto Typer

An automated typing tool that simulates user input across multiple browser windows. Perfect for parallel search operations and automated form filling. Features both command-line and GUI interfaces with configurable delays and intelligent window management.

Key Features:
- 🔄 Multi-window support with smart window cycling
- ⚡ Optimized window switching patterns
- ⌨️ Automated text input with configurable delays
- 🎯 Intelligent search bar focusing and text selection
- 🖥️ GUI interface with real-time delay recommendations
- 🐧 Cross-platform support (Linux/Windows)

## Prerequisites

### Linux (Fedora/RHEL)
```bash
# Install Tkinter and other required system dependencies
sudo dnf install python3-tkinter scrot python3-devel

# Set up X11 permissions (required for GUI automation)
xhost +SI:localuser:$USER

# Enable Remote Desktop (if not already enabled)
gsettings set org.gnome.desktop.remote-desktop.rdp enable true
```

### Linux (Ubuntu/Debian)
```bash
# Install Tkinter and other required system dependencies
sudo apt-get install python3-tk scrot python3-dev

# Set up X11 permissions (required for GUI automation)
xhost +SI:localuser:$USER

# Enable Remote Desktop (if not already enabled)
gsettings set org.gnome.desktop.remote-desktop.rdp enable true
```

### Windows
Tkinter comes pre-installed with Python.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/generyand/autosearch-script.git
   cd autosearch-script
   ```

2. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate virtual environment
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows:
   .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the setup script (Linux only):
   ```bash
   # This will automatically:
   # - Check for required dependencies
   # - Set up X11 permissions
   # - Enable and configure Remote Desktop
   python -m src.utils.setup
   
   # If you only need to configure Remote Desktop:
   python -m src.utils.remote_desktop
   ```

## Configuration

Before running the script, configure the following settings in `config.py`:

```python
# Number of windows to cycle through
WINDOWS_OPEN = 3  # Adjust this to match your open window count

# Number of phrases to type in each window
PHRASE_COUNT = 5  # Adjust based on your needs
```

Make sure these values match your setup:
1. `WINDOWS_OPEN`: Set this to the exact number of windows you have open
2. `PHRASE_COUNT`: Set this to the number of phrases you want to type in each window

**Important**: Incorrect window count can cause the script to malfunction, so ensure this matches your actual open windows.

## Usage

### Command Line Version

Run the script:
```bash
# On Linux:
# IMPORTANT: Do not use sudo with the script. Instead, use the setup utility:
python -m src.utils.setup  # Run this first to set up permissions
DISPLAY=:0 python main.py

# On Windows:
python main.py
```

### GUI Version

Run the GUI script:
```bash
# On Linux:
# IMPORTANT: Do not use sudo with the script. Instead, use the setup utility:
python -m src.utils.setup  # Run this first to set up permissions
DISPLAY=:0 python gui.py

# On Windows:
python gui.py
```

The GUI provides an easy-to-use interface with the following features:
- Configurable initial delay
- Adjustable phrase count
- Multiple window support
- Customizable delay between windows
- Real-time recommended delay calculations

## Troubleshooting

### Linux
If you encounter X11/display-related errors:
1. Run the setup utility: `python -m src.utils.setup`
2. If issues persist, manually check:
   - X11 permissions: `xhost +SI:localuser:$USER`
   - Display variable: `export DISPLAY=:0`
   - Remote Desktop: `python -m src.utils.remote_desktop`
3. Run the script with display variable: `DISPLAY=:0 python gui.py`

**Important Note**: Do not run the script with sudo. If you get permission errors:
1. Use the setup utility: `python -m src.utils.setup`
2. Ensure your virtual environment is activated and packages are installed there
3. If you absolutely must use sudo (not recommended), install packages system-wide: `sudo pip install -r requirements.txt`

The setup utility (`src.utils.setup`) will:
- Check for required system dependencies
- Configure X11 permissions automatically
- Enable and configure Remote Desktop
- Provide clear error messages if anything fails

The `DISPLAY=:0` variable tells the application which display to use:
- `:0` refers to the first (usually main) display on your local machine
- This is required for GUI applications to know where to appear
- If you have multiple monitors, you might need to use `:0.0`, `:0.1`, etc.
- Without this setting, GUI applications won't know which display to use

### Common Issues
- If PyAutoGUI is not found, try reinstalling it: `pip install --force-reinstall pyautogui`
- Make sure all system dependencies are installed before running the scripts
- If setup fails, run `python -m src.utils.setup` to see detailed error messages

## Deactivating Virtual Environment

When you're done, you can deactivate the virtual environment:
```bash
deactivate
```

## Note

Make sure to have the necessary windows/applications open before starting the auto-typer, as it will automatically switch between windows using Alt+Tab.

Made by Exploiter ni Sah