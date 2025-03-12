## Auto Typer

An automated typing tool with both command-line and GUI interfaces.

## Prerequisites

### Linux (Fedora/RHEL)
```bash
sudo dnf install python3-tkinter
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get install python3-tk
```

### Windows
Tkinter comes pre-installed with Python.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
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

## Usage

### Command Line Version

Run the script:
```bash
python main.py
```

### GUI Version

Run the GUI script:
```bash
python gui.py
```

The GUI provides an easy-to-use interface with the following features:
- Configurable initial delay
- Adjustable phrase count
- Multiple window support
- Customizable delay between windows
- Real-time recommended delay calculations

## Deactivating Virtual Environment

When you're done, you can deactivate the virtual environment:
```bash
deactivate
```

## Note

Make sure to have the necessary windows/applications open before starting the auto-typer, as it will automatically switch between windows using Alt+Tab.

Made by Exploiter ni Sah