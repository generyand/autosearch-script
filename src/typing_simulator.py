import pyautogui

class TypingSimulator:
    def type_phrase(self, phrase: str, is_first_iteration: bool = False) -> None:
        """Type a phrase into the search bar."""
        if not is_first_iteration:
            # Press Alt + Left Arrow to go back
            pyautogui.keyDown('alt')
            pyautogui.press('left')
            pyautogui.keyUp('alt')
            
        pyautogui.press('/')
        pyautogui.press('backspace')
        pyautogui.typewrite(phrase)
        pyautogui.press('enter')

    def alt_shift_tilde(self) -> None:
        """
        Perform Alt + Shift + ~ to cycle through windows.
        """
        pyautogui.keyDown('alt')
        pyautogui.keyDown('shift')
        pyautogui.press('`')  # The tilde key
        pyautogui.keyUp('shift')
        pyautogui.keyUp('alt')
