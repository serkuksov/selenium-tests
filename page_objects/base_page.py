from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    url_page: str

    def __init__(self, webdriver: WebDriver, timeout: int = 10):
        self._webdriver = webdriver
        self.timeout = timeout
        if self._check_url(self.url_page) is False:
            raise ValueError(
                f"Страница {self.get_url()} не соответствует классу: {self.__class__.__name__}"
            )

    def _check_url(self, url_page: str, timeout=None) -> bool:
        """Проверка наличия в URL текущей страницы текста url_page"""
        if timeout is None:
            timeout = self.timeout
        try:
            WebDriverWait(self._webdriver, timeout).until(EC.url_contains(url_page))
            return True
        except TimeoutException:
            return False

    def get_title(self) -> str:
        """Получить Title страницы"""
        return self._webdriver.title

    def get_url(self) -> str:
        """Получить URL страницы"""
        return self._webdriver.current_url

    def find_element(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> WebElement:
        """Получить элемент страницы"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._webdriver
        return WebDriverWait(element, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> list[WebElement]:
        """Получить список элементов страницы"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._webdriver
        return WebDriverWait(element, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def get_clickable_element(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> WebElement:
        """Получить кликабельный элемент"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._webdriver
        return WebDriverWait(element, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click_to_elm(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> None:
        """Кликнуть по элементу"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._webdriver
        elm = self.get_clickable_element(locator, element=element, timeout=timeout)
        elm.click()

    def element_visibility(
        self, locator: tuple[str, str], element: WebElement = None, timeout=None
    ) -> bool:
        """Проверить видимость элемента на странице"""
        if timeout is None:
            timeout = self.timeout
        if element is None:
            element = self._webdriver
        try:
            WebDriverWait(element, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True

    def switch_to_new_tabs(self):
        """Переключится на новую вкладку браузера"""
        tabs = self._webdriver.window_handles
        self._webdriver.switch_to.window(tabs[-1])

    def scroll_to_element(self, element: WebElement, x: int = 0, y: int = 0) -> None:
        """Прокрутить страницу до элемента и на смещение x, y"""
        actions = ActionChains(self._webdriver)
        actions.scroll_to_element(element).scroll_by_amount(x, y).perform()

    @staticmethod
    def get_elm_size(element: WebElement) -> tuple[str, str]:
        """Получить размеры элемента"""
        width = element.size["width"]
        height = element.size["height"]
        return width, height
