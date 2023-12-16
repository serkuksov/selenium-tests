from servises import download_file
from page_objects.sbis_pages import IndexPageSbis


class Tests:
    def test_1(self, driver):
        """Тестовый кейс № 1"""
        # открытие https://sbis.ru/
        driver.get(IndexPageSbis.url_page)
        index_page_sbis = IndexPageSbis(webdriver=driver)
        assert "СБИС" in index_page_sbis.get_title()

        # переход на страницу Контакты
        contact_page_sbis = index_page_sbis.click_link_contacts()
        assert "Контакты" in contact_page_sbis.get_title()
        assert contact_page_sbis.url_page in contact_page_sbis.get_url()

        # клик по банеру Тезор
        index_page_tensor = contact_page_sbis.click_link_tensor()
        assert "Тензор" in index_page_tensor.get_title()
        assert "Сила в людях" in index_page_tensor.get_text_header_block_about()
        assert index_page_tensor.is_block_about() is True

        # клик по ссылке подробнее в блоке Сила в людях
        about_page_tensor = index_page_tensor.click_link_block_about()
        assert "О компании" in about_page_tensor.get_title()
        assert "https://tensor.ru/about" == about_page_tensor.get_url()
        assert "Работаем" in about_page_tensor.get_text_header_block_working()
        assert about_page_tensor.is_block_working() is True

        # Проверка размера картинок
        assert about_page_tensor.is_size_photo_block_working_equal() is True

    def test_2(self, driver):
        """Тестовый кейс № 2"""
        # открытие https://sbis.ru/
        driver.get(IndexPageSbis.url_page)
        index_page_sbis = IndexPageSbis(webdriver=driver)
        assert "СБИС" in index_page_sbis.get_title()

        # переход на страницу Контакты
        contact_page_sbis = index_page_sbis.click_link_contacts()
        assert "Контакты" in contact_page_sbis.get_title()
        assert contact_page_sbis.url_page in contact_page_sbis.get_url()

        # проверка наличия выбранного региона
        name_region = contact_page_sbis.get_name_active_region()
        assert name_region is not None
        name_partners = contact_page_sbis.get_name_partners()

        # выбрать регион Камчатка
        contact_page_sbis.select_region_kamchatka()
        assert "Камчатский край" in contact_page_sbis.get_title()
        assert "41-kamchatskij-kraj" in contact_page_sbis.get_url()
        name_region_new = contact_page_sbis.get_name_active_region()
        assert name_region != name_region_new
        assert name_region_new == "Камчатский край"
        name_partners_new = contact_page_sbis.get_name_partners()
        assert name_partners != name_partners_new

    def test_3(self, driver):
        """Тестовый кейс № 3"""
        # открытие https://sbis.ru/
        driver.get(IndexPageSbis.url_page)
        index_page_sbis = IndexPageSbis(webdriver=driver)
        assert "СБИС" in index_page_sbis.get_title()

        # переход на страницу для скачивания файлов
        download_page_sbis = index_page_sbis.click_link_download_sbis()
        assert "Скачать" in download_page_sbis.get_title()

        # кликнуть по кнопке СБИС Плагин
        download_page_sbis.click_button_plugin()

        # проверить что активна кнопка Windows
        assert download_page_sbis.is_active_button_windows() is True

        # скачивание файла
        download_page_sbis.download_file()
        size_file_from_website = download_page_sbis.get_size_download_file()
        assert download_file.is_download_completed() is True
        file_path = download_file.get_latest_file()
        size_download_file = download_file.get_size_file(file_path)

        # проверка размера файла
        assert abs(size_file_from_website - size_download_file) < 0.01
