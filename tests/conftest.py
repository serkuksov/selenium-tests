import os
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from config import settings


def get_options_chrome_webdriver() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    if settings.IS_HEADLESS_BROWSER:
        options.add_argument("--headless")
    prefs = {"download.default_directory": settings.DOWNLOAD_DIRECTORY}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f"--window-size={settings.WINDOW_SIZE}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--user-agent={settings.USER_AGENT}")
    options.enable_downloads = True
    return options


def get_service_chrome_webdriver() -> webdriver.ChromeService:
    from webdriver_manager.chrome import ChromeDriverManager

    return webdriver.ChromeService(ChromeDriverManager().install())


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    is_start_docker = os.environ.get("IS_START_DOCKER", False)
    if is_start_docker:
        driver = webdriver.Chrome(options=get_options_chrome_webdriver())
    else:
        driver = webdriver.Chrome(
            options=get_options_chrome_webdriver(),
            service=get_service_chrome_webdriver(),
        )
    try:
        yield driver
    finally:
        driver.close()
        driver.quit()
