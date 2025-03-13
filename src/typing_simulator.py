"""
Typing Simulator Module
---------------------
Provides automation for typing and window management.
Handles keyboard interactions for searching and navigating between windows.
"""

import pyautogui
import time

class TypingSimulator:
    """
    Automates keyboard interactions for typing and window management.
    
    This class provides methods to:
    - Type phrases into search bars
    - Navigate between pages
    - Switch between windows
    - Handle text selection and submission
    
    All methods include small delays to ensure reliable operation
    across different system speeds.
    """
    
    # Delay constants for timing control
    NAVIGATION_DELAY = 0.1
    TYPING_DELAY = 0.1
    SUBMISSION_DELAY = 0.2
    
    def type_phrase(self, phrase: str, is_first_iteration: bool = False) -> None:
        """
        Type a phrase into the search bar with proper setup and cleanup.
        
        Args:
            phrase: The text to type into the search bar
            is_first_iteration: Whether this is the first time typing in this window
        
        Flow:
        1. Go back to previous page (if not first iteration)
        2. Focus search bar
        3. Select and clear existing text
        4. Type new phrase
        5. Submit search
        """
        if not is_first_iteration:
            self._go_back_to_previous_page()
        
        self._focus_search_bar()
        self._select_all_text()
        self._type_text(phrase)
        self._submit_search()
    
    def switch_to_next_window(self) -> None:
        """
        Switch to the next window in the sequence using Alt + Shift + ~.
        Includes a small delay to ensure the window switch is complete.
        """
        pyautogui.keyDown('alt')
        pyautogui.keyDown('shift')
        pyautogui.press('`')  # The tilde key
        pyautogui.keyUp('shift')
        pyautogui.keyUp('alt')
        time.sleep(self.NAVIGATION_DELAY)

    def _go_back_to_previous_page(self) -> None:
        """
        Navigate to the previous page using Alt + Left Arrow.
        Used to clear the previous search before typing a new phrase.
        """
        pyautogui.keyDown('alt')
        pyautogui.press('left')
        pyautogui.keyUp('alt')
        time.sleep(self.NAVIGATION_DELAY)

    def _focus_search_bar(self) -> None:
        """
        Focus the search bar by pressing '/'.
        This is a common shortcut in many browsers to focus the search field.
        """
        pyautogui.press('/')
        time.sleep(self.NAVIGATION_DELAY)

    def _select_all_text(self) -> None:
        """
        Select all text in the current field using Ctrl+A.
        This ensures any existing text is replaced when typing begins.
        """
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')
        time.sleep(self.TYPING_DELAY)

    def _type_text(self, text: str) -> None:
        """
        Type the specified text into the currently focused field.
        
        Args:
            text: The text to type
        """
        pyautogui.typewrite(text)
        time.sleep(self.TYPING_DELAY)

    def _submit_search(self) -> None:
        """
        Submit the search by pressing Enter.
        Uses a slightly longer delay to allow the search to begin processing.
        """
        pyautogui.press('enter')
        time.sleep(self.SUBMISSION_DELAY)
