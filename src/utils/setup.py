"""
Setup Script
-----------
Handles initial setup requirements for the auto-typer,
including remote desktop configuration and permissions.
"""

import subprocess
import sys
import os
from .remote_desktop import enable_remote_desktop, is_linux, check_remote_desktop_status

def setup_x11_permissions() -> bool:
    """
    Set up X11 permissions for the current user.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Get actual username instead of $USER
        username = os.environ.get('USER', os.environ.get('USERNAME'))
        if not username:
            print("❌ Could not determine username")
            return False

        # Try the more specific command first
        try:
            subprocess.run(['xhost', f'+SI:localuser:{username}'], 
                         check=True, 
                         capture_output=True,
                         text=True)
            print(f"✅ X11 permissions set successfully for user: {username}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Specific user permission failed, trying alternative method...")
            
            # Fallback to less restrictive permission
            subprocess.run(['xhost', '+'], 
                         check=True, 
                         capture_output=True,
                         text=True)
            print("✅ X11 permissions set using alternative method")
            print("⚠️ Note: This is less secure. Consider running 'xhost -' when done")
            return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Error setting X11 permissions: {e}")
        print("Try running: export DISPLAY=:0 before setup")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("Troubleshooting steps:")
        print("1. Make sure X server is running")
        print("2. Try: export DISPLAY=:0")
        print("3. Check if xhost is installed")
        return False

def check_dependencies() -> bool:
    """
    Check if all required system dependencies are installed.
    
    Returns:
        bool: True if all dependencies are present, False otherwise
    """
    try:
        # Check for required commands
        required_commands = ['python3', 'pip', 'xhost']
        missing_commands = []
        
        for cmd in required_commands:
            try:
                subprocess.run(['which', cmd], 
                             check=True, 
                             capture_output=True,
                             text=True)
            except subprocess.CalledProcessError:
                missing_commands.append(cmd)
        
        if missing_commands:
            print("❌ Missing dependencies:")
            for cmd in missing_commands:
                print(f"  - {cmd}")
            print("\nInstall missing dependencies with:")
            print("sudo dnf install python3 python3-pip xorg-x11-server-utils  # Fedora/RHEL")
            print("sudo apt-get install python3 python3-pip x11-xserver-utils  # Ubuntu/Debian")
            return False
            
        print("✅ All required dependencies are installed")
        return True
        
    except Exception as e:
        print(f"❌ Error checking dependencies: {e}")
        return False

def check_display_variable() -> bool:
    """
    Check if DISPLAY environment variable is set correctly.
    
    Returns:
        bool: True if set, False otherwise
    """
    display = os.environ.get('DISPLAY')
    if not display:
        print("❌ DISPLAY environment variable not set")
        print("Run: export DISPLAY=:0")
        return False
    print(f"✅ DISPLAY variable set to: {display}")
    return True

def setup_environment() -> bool:
    """
    Set up the complete environment for auto-typer.
    
    Returns:
        bool: True if setup is successful, False otherwise
    """
    if not is_linux():
        print("ℹ️ Running on non-Linux system, skipping Linux-specific setup")
        return True

    success = True
    
    # Check DISPLAY variable first
    if not check_display_variable():
        success = False
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Please install missing dependencies")
        success = False

    # Set up X11 permissions
    if not setup_x11_permissions():
        print("❌ Failed to set up X11 permissions")
        success = False

    # Configure remote desktop if not already enabled
    if not check_remote_desktop_status():
        if not enable_remote_desktop():
            print("❌ Failed to enable remote desktop")
            success = False

    if success:
        print("\n✅ Environment setup completed successfully")
        print("\nYou can now run the auto-typer with:")
        print("DISPLAY=:0 python main.py  # For CLI version")
        print("DISPLAY=:0 python gui.py   # For GUI version")
    else:
        print("\n⚠️ Some setup steps failed, please check the errors above")
        print("For help, visit: https://github.com/generyand/autosearch-script/issues")

    return success

if __name__ == "__main__":
    if not setup_environment():
        sys.exit(1) 