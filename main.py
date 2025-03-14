"""
Auto Typer Script
----------------
This script automates typing phrases into multiple browser windows.
It handles both initial setup and continuous typing operations.
"""

from src.phrase_generator import PhraseGenerator
from src.typing_simulator import TypingSimulator
from src.config import INITIAL_DELAY, PHRASE_COUNT, DELAY_BETWEEN_WINDOWS, WINDOWS_OPEN
import time
import pyautogui
from src.utils.remote_desktop import enable_remote_desktop, is_linux

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

def setup_remote_desktop() -> bool:
    """
    Ensure remote desktop is properly configured
    
    Returns:
        bool: True if remote desktop is enabled, False otherwise
    """
    if not is_linux():
        print("ℹ️ Not running on Linux, skipping remote desktop setup")
        return True
        
    print("\n⚙️ Checking Remote Desktop configuration...")
    if not enable_remote_desktop():
        print("\n❌ Remote Desktop setup required. Please run 'python -m src.utils.remote_desktop' and try again.")
        return False
    return True

def main():
    """
    Main execution function that coordinates the typing automation.
    Flow:
    1. Setup remote desktop
    2. Setup components
    3. Initial delay
    4. First iteration (setup windows)
    5. Subsequent iterations (continuous operation)
    """
    print("\n🤖 Auto Typer Script")
    print("===================")
    
    # Setup remote desktop first
    if not setup_remote_desktop():
        return
    
    # Initialize components
    phrase_generator, typing_simulator = setup_automation()
    
    # Wait for initial setup
    print(f"\nStarting in {INITIAL_DELAY} seconds...")
    time.sleep(INITIAL_DELAY)
    
    # Execute automation
    print("Running first iteration...")
    handle_first_iteration(typing_simulator, phrase_generator)
    
    print("Running subsequent iterations...")
    handle_subsequent_iterations(typing_simulator, phrase_generator)
    
    print("\n✨ Automation completed!")

if __name__ == "__main__":
    main()
    