import re
import time

from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from .locators import sbis_licators
from .tensor_page import IndexPageTensor


class ContactsPageSkis(BasePage):
    """Класс страницы Контакты - sbis.ru"""

    url_page = "https://sbis.ru/contacts/"
    locators = sbis_licators.ContactsPageSbisLocator()

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


class DownloadPageSbis(BasePage):
    """Класс главной страницы sbis.ru"""

    url_page = "https://sbis.ru/download"
    locators = sbis_licators.DownloadPageSbisLocator()

    def click_button_plugin(self):
        """Кликнуть по кнопке СБИС Плагин"""
        self.click_to_elm(self.locators.BUTTON_PLUGIN)
        time.sleep(1)
        self.click_to_elm(self.locators.BUTTON_PLUGIN)

    def is_active_button_windows(self) -> bool:
        """Активна ли кнопка windows"""
        elm = self.find_element(self.locators.BUTTON_WINDOWS)
        atr_class = elm.get_attribute("class")
        active_class = "controls-Checked__checked"
        return True if active_class in atr_class else False

    def download_file(self):
        """Скачать файл"""
        self.click_to_elm(self.locators.DOWNLOAD_FILE)

    def get_size_download_file(self) -> float:
        """Получить размер скачиваемого файла указанный на странице"""
        elm = self.find_element(self.locators.DOWNLOAD_FILE)
        size_file = self._get_size_file_of_str(elm.text)
        return size_file

    @staticmethod
    def _get_size_file_of_str(string: str) -> float:
        """Получение числа из строки"""
        match = re.search(r"\d+(\.\d+)?\s+МБ", string)
        if match:
            return float(match.group()[:-2])
        else:
            raise ValueError("Строка не содержит число")


class IndexPageSbis(BasePage):
    """Класс главной страницы sbis.ru"""

    url_page = "https://sbis.ru/"
    locators = sbis_licators.IndexPageSbisLocator()

    def _get_block_header(self) -> WebElement:
        return self.find_element(self.locators.HEADER)

    def click_link_contacts(self):
        """Кликнуть по ссылке Контакты в header"""
        block_header = self._get_block_header()
        self.click_to_elm(self.locators.LINK_CONTACTS, element=block_header)
        return ContactsPageSkis(self._webdriver)

    def click_link_download_sbis(self) -> DownloadPageSbis:
        """Кликнуть по ссылке Скачать СБИС"""
        elm = self.find_element(self.locators.FOOTER_CONTAINER)
        self.scroll_to_element(elm)
        self.click_to_elm(self.locators.LINK_DOWNLOAD_SBIS)
        return DownloadPageSbis(self._webdriver)
