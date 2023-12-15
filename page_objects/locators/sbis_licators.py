from selenium.webdriver.common.by import By


class IndexPageSbisLocator:
    HEADER = (By.CLASS_NAME, "sbisru-Header")
    LINK_CONTACTS = (By.LINK_TEXT, "Контакты")


class ContactsPageSbisLocator:
    CONTACTS_CLIENTS = (By.ID, "contacts_clients")
    LINK_TENSOR = (By.CSS_SELECTOR, "[title*='tensor.ru']")
