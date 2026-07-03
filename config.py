import os
from dotenv import load_dotenv

load_dotenv()
class Config:

    # Application
    BASE_URL = os.getenv("BASE_URL")

    # Credentials
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    # Browser settings
    BROWSER = "chromium"
    HEADLESS = False
    SLOW_MO = 0

    # Timeouts
    DEFAULT_TIMEOUT = 30000

    # Retry
    RETRY_COUNT = 3
    TEST_DIR = "C:\OrangeHRM"

    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    REPORT_PATH = os.path.join(BASE_DIR, "reports")
    SCREENSHOT_PATH = os.path.join(BASE_DIR, "screenshots")

    