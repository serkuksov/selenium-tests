from page_objects.base_page import BasePage
from page_objects.locators.tensor_licators import (
    IndexPageTensorLocator,
    AboutPageTensorLocator,
)


class AboutPageTensor(BasePage):
    """Класс Главной страницы - tensor.ru"""

    url_page = "https://tensor.ru/about"
    locators = AboutPageTensorLocator()

    def is_block_working(self) -> bool:
        """Проверить наличие блока working"""
        return self.element_visibility(self.locators.BLOCK_WORKING)

    def get_text_header_block_working(self) -> str:
        """Получить заголовок блока working"""
        elm = self.find_element(self.locators.HEADER_BLOCK_WORKING)
        return elm.text

    def is_size_photo_block_working_equal(self) -> bool:
        """Проверить одинаковость размера картинок в блоке working"""
        elements = self.find_elements(self.locators.IMG_BLOCK_WORKING)
        size = self.get_elm_size(elements[0])
        for element in elements[1:]:
            if self.get_elm_size(element) != size:
                return False
        return True


class IndexPageTensor(BasePage):
    """Класс Главной страницы - tensor.ru"""

    url_page = "https://tensor.ru"
    locators = IndexPageTensorLocator()

    def is_block_about(self) -> bool:
        """Проверить наличие блока about"""
        return self.element_visibility(self.locators.BLOCK_ABOUT)

    def get_text_header_block_about(self) -> str:
        """Получить заголовок блока about"""
        self.element_visibility(self.locators.HEADER_BLOCK_ABOUT)
        elm = self.find_element(self.locators.HEADER_BLOCK_ABOUT)
        return elm.text

    def click_link_block_about(self) -> AboutPageTensor:
        """Кликнуть по ссылке в блоке about"""
        elm = self.find_element(self.locators.LINK_BLOCK_ABOUT)
        self.scroll_to_element(elm, y=100)
        self.click_to_elm(self.locators.LINK_BLOCK_ABOUT)
        return AboutPageTensor(self._webdriver)
