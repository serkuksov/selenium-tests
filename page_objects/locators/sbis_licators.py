from selenium.webdriver.common.by import By


class IndexPageSbisLocator:
    HEADER = (By.CLASS_NAME, "sbisru-Header")
    LINK_CONTACTS = (By.LINK_TEXT, "Контакты")
    LINK_DOWNLOAD_SBIS = (By.XPATH, "//a[text()='Скачать СБИС']")


class ContactsPageSbisLocator:
    CONTACTS_CLIENTS = (By.ID, "contacts_clients")
    LINK_TENSOR = (By.CSS_SELECTOR, "[title*='tensor.ru']")
    ACTIVE_REGION = (
        By.XPATH,
        "//div[@class='sbisru-Contacts']//span[contains(@class, 'sbis_ru-Region-Chooser__text')]",
    )
    PARTNERS = (By.XPATH, "//div[contains(@class, 'sbisru-Contacts-List__name')]")
    REGION_NAME_KAMCHATKA = (By.XPATH, "//span[@title='Камчатский край']")
