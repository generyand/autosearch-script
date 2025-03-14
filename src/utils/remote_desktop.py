"""
Remote Desktop Configuration Utility
----------------------------------
Provides functionality to enable and configure remote desktop settings
for Linux systems using gsettings.
"""

import subprocess
import platform
import sys

def enable_remote_desktop() -> bool:
    """
    Enable remote desktop access and configure necessary settings.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Enable RDP
        subprocess.run(['gsettings', 'set', 'org.gnome.desktop.remote-desktop.rdp', 'enable', 'true'],
                      check=True)
        
        # Enable required remote desktop settings
        settings = [
            # Enable screen sharing
            ['org.gnome.desktop.sharing', 'enabled', 'true'],
            # Allow remote control
            ['org.gnome.desktop.remote-desktop.rdp', 'enable-remote-control', 'true'],
            # Enable encryption
            ['org.gnome.desktop.remote-desktop.rdp', 'tls-cert', 'true'],
            # Enable view-only access
            ['org.gnome.desktop.remote-desktop.rdp', 'view-only', 'false']
        ]
        
        for schema, key, value in settings:
            subprocess.run(['gsettings', 'set', schema, key, value], check=True)
            
        print("✅ Remote desktop has been enabled successfully")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error enabling remote desktop: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_remote_desktop_status() -> bool:
    """
    Check if remote desktop is currently enabled.
    
    Returns:
        bool: True if enabled, False otherwise
    """
    try:
        result = subprocess.run(
            ['gsettings', 'get', 'org.gnome.desktop.remote-desktop.rdp', 'enable'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip() == 'true'
    except subprocess.CalledProcessError:
        return False

def is_linux() -> bool:
    """Check if the current system is Linux."""
    return platform.system().lower() == 'linux'

if __name__ == "__main__":
    if not is_linux():
        print("❌ This script only works on Linux systems")
        sys.exit(1)
        
    if check_remote_desktop_status():
        print("✅ Remote desktop is already enabled")
    else:
        print("⚙️ Enabling remote desktop...")
        enable_remote_desktop() 