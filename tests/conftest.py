from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from config import settings


def get_options_chrome_webdriver() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    if settings.IS_HEADLESS_BROWSER:
        options.add_argument("--headless")
    prefs = {"download.default_directory": settings.DOWNLOAD_DIRECTORY}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"--window-size={settings.WINDOW_SIZE}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--user-agent={settings.USER_AGENT}")
    options.enable_downloads = True
    return options


def get_service_chrome_webdriver() -> webdriver.ChromeService:
    return webdriver.ChromeService(ChromeDriverManager().install())


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    driver = webdriver.Chrome(
        options=get_options_chrome_webdriver(),
        service=get_service_chrome_webdriver(),
    )
    try:
        yield driver
    finally:
        driver.close()
        driver.quit()
