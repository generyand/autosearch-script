"""
Remote Desktop Configuration Utility
----------------------------------
Provides functionality to enable and configure remote desktop settings
for Linux systems using gsettings.
"""

import platform
import sys
import pyautogui

def trigger_settings_shortcut() -> bool:
    """
    Trigger remote desktop dialog by typing 'yes'
    
    Returns:
        bool: True if triggered, False otherwise
    """
    try:
        pyautogui.typewrite('yes')
        print("✅ Remote desktop dialog triggered")
        return True
    except Exception as e:
        print(f"❌ Error triggering dialog: {e}")
        return False

def enable_remote_desktop() -> bool:
    """
    Enable remote desktop by triggering the interaction dialog and guiding user
    
    Returns:
        bool: True if successful, False otherwise
    """
    print("\n📋 Remote Desktop Setup:")
    print("1. A dialog will appear when you type 'yes'")
    print("2. Enable 'Remote Desktop' in the dialog")
    print("3. Enable 'Remote Desktop Interaction' if available")
    
    while True:
        print("\nWould you like to trigger the Remote Desktop dialog? (yes/no)")
        response = input().strip().lower()
        
        if response in ['y', 'yes']:
            trigger_settings_shortcut()
            print("\n⏳ Please enable Remote Desktop in the dialog...")
            
            print("\nHave you enabled Remote Desktop? (yes/no)")
            enabled = input().strip().lower()
            
            if enabled in ['y', 'yes']:
                print("✅ Remote Desktop enabled successfully!")
                return True
            elif enabled in ['n', 'no']:
                print("❌ Remote Desktop not enabled. Please try again.")
                continue
            else:
                print("⚠️ Please answer 'yes' or 'no'")
                continue
                
        elif response in ['n', 'no']:
            print("❌ Setup cancelled. Run the script again when ready.")
            return False
        else:
            print("⚠️ Please answer 'yes' or 'no'")

def open_remote_desktop_settings() -> bool:
    """
    Open the remote desktop settings dialog
    
    Returns:
        bool: True if successful, False otherwise
    """
    return trigger_settings_shortcut()

def is_linux() -> bool:
    """Check if the current system is Linux."""
    return platform.system().lower() == 'linux'

if __name__ == "__main__":
    if not is_linux():
        print("❌ This script only works on Linux systems")
        sys.exit(1)
    
    print("\n🖥️ Remote Desktop Setup Utility")
    print("================================")
    
    if enable_remote_desktop():
        print("\n✨ Remote Desktop dialog triggered!")
    else:
        print("\n❌ Failed to trigger Remote Desktop dialog") 