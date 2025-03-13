## Auto Typer

An automated typing tool with both command-line and GUI interfaces.

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
# On Linux, make sure to set the DISPLAY variable
DISPLAY=:0 python main.py

# On Windows
python main.py
```

### GUI Version

Run the GUI script:
```bash
# On Linux, make sure to set the DISPLAY variable
DISPLAY=:0 python gui.py

# On Windows
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
1. Make sure X11 permissions are set: `xhost +SI:localuser:$USER`
2. Set the DISPLAY environment variable: `export DISPLAY=:0`
3. Ensure Remote Desktop is enabled: `gsettings set org.gnome.desktop.remote-desktop.rdp enable true`
4. Run the script with the display variable: `DISPLAY=:0 python gui.py`

The `DISPLAY=:0` variable tells the application which display to use:
- `:0` refers to the first (usually main) display on your local machine
- This is required for GUI applications to know where to appear
- If you have multiple monitors, you might need to use `:0.0`, `:0.1`, etc.
- Without this setting, GUI applications won't know which display to use

### Common Issues
- If PyAutoGUI is not found, try reinstalling it: `pip install --force-reinstall pyautogui`
- Make sure all system dependencies are installed before running the scripts

## Deactivating Virtual Environment

When you're done, you can deactivate the virtual environment:
```bash
deactivate
```

## Note

Make sure to have the necessary windows/applications open before starting the auto-typer, as it will automatically switch between windows using Alt+Tab.

Made by Exploiter ni Sah