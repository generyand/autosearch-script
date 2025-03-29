"""
Configuration Utility for Auto-Typer
-----------------------------------
Interactive script to create or update .env configuration
"""

import os
from pathlib import Path

def create_or_update_env():
    """
    Create or update the .env file with user-provided values
    """
    env_path = Path('.') / '.env'
    env_exists = env_path.exists()
    
    current_values = {}
    if env_exists:
        print("📝 Existing .env file found. Loading current values...")
        with open(env_path, 'r') as env_file:
            for line in env_file:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    current_values[key] = value
    
    # Configuration items with descriptions and defaults
    config_items = [
        {
            "key": "INITIAL_DELAY",
            "desc": "Initial delay in seconds before typing starts",
            "default": "4",
            "type": int
        },
        {
            "key": "PHRASE_COUNT",
            "desc": "Number of phrases to type",
            "default": "10",
            "type": int
        },
        {
            "key": "TYPING_DELAY",
            "desc": "Delay between typing characters in seconds",
            "default": "2",
            "type": int
        },
        {
            "key": "WINDOWS_OPEN",
            "desc": "Number of browser windows to use",
            "default": "10",
            "type": int
        },
        {
            "key": "MIN_DELAY_BETWEEN_WINDOWS",
            "desc": "Minimum delay between window switches",
            "default": "0.025",
            "type": float
        },
        {
            "key": "DELAY_CALCULATION_NUMERATOR",
            "desc": "Used to calculate delay between windows",
            "default": "5",
            "type": float
        }
    ]
    
    print("\n🔧 Auto-Typer Configuration")
    print("========================\n")
    print("Enter values for each setting (or press Enter to keep current/default value)")
    
    user_values = {}
    for item in config_items:
        key = item["key"]
        current = current_values.get(key, item["default"])
        
        while True:
            user_input = input(f"{key} [{current}] - {item['desc']}: ").strip()
            
            if not user_input:
                user_values[key] = current
                break
                
            try:
                # Convert to the appropriate type
                if item["type"] == int:
                    value = int(user_input)
                elif item["type"] == float:
                    value = float(user_input)
                else:
                    value = user_input
                    
                user_values[key] = str(value)
                break
            except ValueError:
                print(f"❌ Invalid input. Please enter a valid {item['type'].__name__}.")
    
    # Write the configuration to .env file
    with open(env_path, 'w') as env_file:
        env_file.write("# Auto-typer Configuration\n\n")
        
        env_file.write("# Timing settings\n")
        for key in ["INITIAL_DELAY", "PHRASE_COUNT", "TYPING_DELAY", "WINDOWS_OPEN"]:
            env_file.write(f"{key}={user_values[key]}\n")
        
        env_file.write("\n# Advanced settings\n")
        env_file.write(f"MIN_DELAY_BETWEEN_WINDOWS={user_values['MIN_DELAY_BETWEEN_WINDOWS']}\n")
        env_file.write(f"DELAY_CALCULATION_NUMERATOR={user_values['DELAY_CALCULATION_NUMERATOR']}\n")
    
    print("\n✅ Configuration saved to .env file")
    print(f"   The actual delay between windows will be: {max(float(user_values['DELAY_CALCULATION_NUMERATOR']) / int(user_values['WINDOWS_OPEN']), float(user_values['MIN_DELAY_BETWEEN_WINDOWS'])):.4f} seconds")

if __name__ == "__main__":
    create_or_update_env() 