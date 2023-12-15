from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from .locators.sbis_licators import IndexPageSbisLocator, ContactsPageSbisLocator
from .tensor_page import IndexPageTensor


class ContactsPageSkis(BasePage):
    """Класс страницы Контакты - sbis.ru"""

    url_page = "https://sbis.ru/contacts/"
    locators = ContactsPageSbisLocator()

    def _get_block_contacts_clients(self) -> WebElement:
        return self.find_element(self.locators.CONTACTS_CLIENTS)

    def click_link_tensor(self) -> IndexPageTensor:
        block_contacts_tensor = self._get_block_contacts_clients()
        self.click_to_elm(self.locators.LINK_TENSOR, element=block_contacts_tensor)
        self.switch_to_new_tabs()
        return IndexPageTensor(self._webdriver)


class IndexPageSbis(BasePage):
    """Класс главной страницы sbis.ru"""

    url_page = "https://sbis.ru/"
    locators = IndexPageSbisLocator()

    def _get_block_header(self) -> WebElement:
        return self.find_element(self.locators.HEADER)

    def click_link_contacts(self):
        block_header = self._get_block_header()
        self.click_to_elm(self.locators.LINK_CONTACTS, element=block_header)
        return ContactsPageSkis(self._webdriver)
