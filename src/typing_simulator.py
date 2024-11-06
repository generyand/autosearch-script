import pyautogui

class TypingSimulator:
    def type_phrase(self, phrase: str) -> None:
        """Type a phrase into the search bar."""
        pyautogui.press('/')
        pyautogui.press('backspace')
        pyautogui.typewrite(phrase)
        pyautogui.press('enter')

    def alt_tab(self) -> None:
        """
        Perform Alt + Shift + Tab to cycle backwards through windows.

        This method simulates pressing Alt + Shift + Tab, which cycles through
        open windows in reverse order. It's useful for navigating between
        multiple applications or windows during automated tasks.
        """
        pyautogui.keyDown('alt')
        pyautogui.keyDown('shift')
        pyautogui.press('tab')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('alt')
