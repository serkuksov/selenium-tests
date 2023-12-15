import os


class Settings:
    IS_HEADLESS_BROWSER = False
    BASE_PATH = os.path.dirname(__file__)
    DOWNLOAD_DIRECTORY = os.path.join(BASE_PATH, "downloads")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64)"
    WINDOW_SIZE = "1920x1080"


settings = Settings()
