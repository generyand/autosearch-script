import webbrowser
from src.config import EDGE_PATH, BING_URL

class BrowserController:
    def open_edge(self) -> None:
        """Open Microsoft Edge browser."""
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(EDGE_PATH))
        webbrowser.get('edge').open(BING_URL)