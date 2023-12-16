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
        """Кликнуть по банеру Тезор"""
        block_contacts_tensor = self._get_block_contacts_clients()
        self.click_to_elm(self.locators.LINK_TENSOR, element=block_contacts_tensor)
        self.switch_to_new_tabs()
        return IndexPageTensor(self._webdriver)

    def get_name_active_region(self) -> str | None:
        """Получить имя выбранного региона"""
        elm = self.find_element(self.locators.ACTIVE_REGION)
        if elm:
            return elm.text

    def get_name_partners(self) -> list[str]:
        """Получить список партнеров"""
        elements = self.find_elements(self.locators.PARTNERS)
        return [elm.text for elm in elements]

    def _select_region(self, locator: tuple[str, str]) -> None:
        """Выбрать регион"""
        self.click_to_elm(self.locators.ACTIVE_REGION)
        self.click_to_elm(locator)
        if self._check_url(url_page="41-kamchatskij-kraj") is False:
            raise ValueError("Не удалось выбрать регион")

    def select_region_kamchatka(self) -> None:
        """Выбрать регион Камчатка"""
        self._select_region(self.locators.REGION_NAME_KAMCHATKA)


class IndexPageSbis(BasePage):
    """Класс главной страницы sbis.ru"""

    url_page = "https://sbis.ru/"
    locators = IndexPageSbisLocator()

    def _get_block_header(self) -> WebElement:
        return self.find_element(self.locators.HEADER)

    def click_link_contacts(self):
        """Кликнуть по ссылке Контакты в header"""
        block_header = self._get_block_header()
        self.click_to_elm(self.locators.LINK_CONTACTS, element=block_header)
        return ContactsPageSkis(self._webdriver)
