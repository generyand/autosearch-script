"""
Remote Desktop Configuration Utility
----------------------------------
Simple utility to trigger remote desktop dialog and confirm setup.
"""

import platform
import sys
import pyautogui

def prompt_user(prompt: str) -> bool:
    """
    Get yes/no response from user
    
    Returns:
        bool: True if user answers yes, False if no
    """
    while True:
        response = input(f"\n{prompt} (yes/no) ").strip().lower()
        if response in ['y', 'yes']:
            return True
        if response in ['n', 'no']:
            return False
        print("⚠️ Please answer 'yes' or 'no'")

def trigger_dialog() -> bool:
    """
    Trigger remote desktop dialog
    """
    try:
        pyautogui.typewrite('yes')
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def enable_remote_desktop() -> bool:
    """
    Guide user through enabling remote desktop
    """
    print("\n📋 Remote Desktop Setup:")
    print("1. Dialog will appear when you type 'yes'")
    print("2. Enable 'Allow Desktop Interaction'")
    print("3. Click 'Share'")
    
    if not prompt_user("Ready to trigger the Remote Desktop dialog?"):
        print("❌ Setup cancelled")
        return False
        
    if not trigger_dialog():
        return False
        
    print("\n⏳ Please enable Remote Desktop in the dialog...")
    while not prompt_user("Have you enabled Remote Desktop?"):
        if not prompt_user("Would you like to try again?"):
            print("❌ Setup cancelled")
            return False
        trigger_dialog()
        print("\n⏳ Please enable Remote Desktop in the dialog...")
    
    print("✅ Remote Desktop enabled!")
    return True

def is_linux() -> bool:
    """Check if system is Linux"""
    return platform.system().lower() == 'linux'

if __name__ == "__main__":
    if not is_linux():
        print("❌ This script only works on Linux")
        sys.exit(1)
    
    print("\n🖥️ Remote Desktop Setup")
    print("=====================")
    
    if enable_remote_desktop():
        print("\n✨ Setup complete!")
    else:
        print("\n❌ Setup failed") 