from src.phrase_generator import PhraseGenerator
# from src.browser_controller import BrowserController
from src.typing_simulator import TypingSimulator
from src.config import INITIAL_DELAY, PHRASE_COUNT, DELAY_BETWEEN_WINDOWS, WINDOWS_OPEN
import time

def main():
    phrase_generator = PhraseGenerator()
    # browser_controller = BrowserController()
    typing_simulator = TypingSimulator()

    time.sleep(INITIAL_DELAY)

    for _ in range(PHRASE_COUNT):

        for _ in range(WINDOWS_OPEN):

            phrase = phrase_generator.generate_phrase()
            
            typing_simulator.type_phrase(phrase)

            typing_simulator.alt_tab()
            time.sleep(DELAY_BETWEEN_WINDOWS)

if __name__ == "__main__":
    main()