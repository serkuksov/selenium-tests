from selenium.webdriver.common.by import By


class IndexPageTensorLocator:
    HEADER_BLOCK_ABOUT = (By.XPATH, "//p[text()='Сила в людях']")
    BLOCK_ABOUT = (By.XPATH, f"{HEADER_BLOCK_ABOUT[1]}/parent::div")
    LINK_BLOCK_ABOUT = (By.XPATH, f"{BLOCK_ABOUT[1]}//a[text()='Подробнее']")


class AboutPageTensorLocator:
    HEADER_BLOCK_WORKING = (By.XPATH, "//h2[text()='Работаем']")
    BLOCK_WORKING = (By.XPATH, f"{HEADER_BLOCK_WORKING[1]}/parent::div/parent::div")
    IMG_BLOCK_WORKING = (By.XPATH, f"{BLOCK_WORKING[1]}//img")
