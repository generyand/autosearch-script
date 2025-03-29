"""
Configuration module for the Auto-typer script
Loads settings from .env file with fallbacks to default values
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Configuration constants
# EDGE_PATH = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
# BING_URL = "https://www.bing.com"

# Timing settings with fallbacks to default values
INITIAL_DELAY = int(os.getenv('INITIAL_DELAY', 4))
PHRASE_COUNT = int(os.getenv('PHRASE_COUNT', 10))
TYPING_DELAY = int(os.getenv('TYPING_DELAY', 2))
WINDOWS_OPEN = int(os.getenv('WINDOWS_OPEN', 10))
MIN_DELAY_BETWEEN_WINDOWS = float(os.getenv('MIN_DELAY_BETWEEN_WINDOWS', 0.025))

# Calculate delay between windows (MAX(DELAY_CALCULATION_NUMERATOR/WINDOWS_OPEN, MIN_DELAY))
DELAY_CALCULATION_NUMERATOR = float(os.getenv('DELAY_CALCULATION_NUMERATOR', 5))
DELAY_BETWEEN_WINDOWS = DELAY_CALCULATION_NUMERATOR / WINDOWS_OPEN

# Ensure minimum delay is respected
if DELAY_BETWEEN_WINDOWS < MIN_DELAY_BETWEEN_WINDOWS:
    DELAY_BETWEEN_WINDOWS = MIN_DELAY_BETWEEN_WINDOWS

