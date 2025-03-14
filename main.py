"""
Auto Typer Script
----------------
This script automates typing phrases into multiple browser windows.
It handles both initial setup and continuous typing operations.
"""

from src.phrase_generator import PhraseGenerator
# from src.browser_controller import BrowserController
from src.typing_simulator import TypingSimulator
from src.config import INITIAL_DELAY, PHRASE_COUNT, DELAY_BETWEEN_WINDOWS, WINDOWS_OPEN
import time
import pyautogui
from src.utils.typing_simulator import TypeSimulator
from src.utils.remote_desktop import check_remote_desktop_status, prompt_user_confirmation

def setup_automation() -> tuple[PhraseGenerator, TypingSimulator]:
    """
    Initialize and return the required automation components.
    
    Returns:
        tuple: (PhraseGenerator, TypingSimulator) instances
    """
    return PhraseGenerator(), TypingSimulator()

def handle_first_iteration(typing_simulator: TypingSimulator, 
                         phrase_generator: PhraseGenerator) -> None:
    """
    Handle the first iteration of typing across all windows.
    This sets up the initial state for each window.
    
    Args:
        typing_simulator: Instance of TypingSimulator for typing automation
        phrase_generator: Instance of PhraseGenerator for creating search phrases
    """
    for window_index in range(WINDOWS_OPEN):
        phrase = phrase_generator.generate_phrase()
        typing_simulator.type_phrase(phrase, is_first_iteration=True)
        
        # Don't switch window on the last iteration
        if window_index < WINDOWS_OPEN - 1:
            typing_simulator.switch_to_next_window()
            time.sleep(DELAY_BETWEEN_WINDOWS)

def handle_subsequent_iterations(typing_simulator: TypingSimulator,
                              phrase_generator: PhraseGenerator) -> None:
    """
    Handle all subsequent typing iterations after the first one.
    This maintains the continuous search operation across all windows.
    
    Args:
        typing_simulator: Instance of TypingSimulator for typing automation
        phrase_generator: Instance of PhraseGenerator for creating search phrases
    """
    for _ in range(PHRASE_COUNT - 1):  # -1 because we already did first iteration
        for window_index in range(WINDOWS_OPEN):
            phrase = phrase_generator.generate_phrase()
            typing_simulator.type_phrase(phrase)
            
            # Don't switch window on the last window of each iteration
            if window_index < WINDOWS_OPEN - 1:
                typing_simulator.switch_to_next_window()
                time.sleep(DELAY_BETWEEN_WINDOWS)
        
        # Add a small delay between iterations
        time.sleep(DELAY_BETWEEN_WINDOWS)

def check_remote_desktop():
    """Check if remote desktop is properly configured"""
    if not check_remote_desktop_status():
        print("\n⚠️ Remote Desktop is not properly configured!")
        print("This is required for the auto-typer to work correctly.")
        print("\nWould you like to configure Remote Desktop now? (y/n)")
        response = input().strip().lower()
        if response in ['y', 'yes']:
            if not prompt_user_confirmation():
                print("\n❌ Remote Desktop setup not completed. Please run the script again when ready.")
                return False
        else:
            print("\n❌ Remote Desktop is required. Please run 'python -m src.utils.remote_desktop' first.")
            return False
    return True

def main():
    """
    Main execution function that coordinates the typing automation.
    Flow:
    1. Setup components
    2. Initial delay
    3. First iteration (setup windows)
    4. Subsequent iterations (continuous operation)
    """
    print("\n🤖 Auto Typer Script")
    print("===================")
    
    # Check remote desktop configuration first
    if not check_remote_desktop():
        return
    
    # Initialize components
    phrase_generator, typing_simulator = setup_automation()
    
    # Wait for initial setup
    print(f"Starting in {INITIAL_DELAY} seconds...")
    time.sleep(INITIAL_DELAY)
    
    # Execute automation
    print("Running first iteration...")
    handle_first_iteration(typing_simulator, phrase_generator)
    
    print("Running subsequent iterations...")
    handle_subsequent_iterations(typing_simulator, phrase_generator)
    
    print("Automation completed!")

if __name__ == "__main__":
    main()
    