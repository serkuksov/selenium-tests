import time

from page_objects.sbis_pages import IndexPageSbis


class Tests:
    def test_1(self, driver):
        """Тестовый кейс в соответствии с первым пунктом ТЗ"""
        driver.get(IndexPageSbis.url_page)
        index_page_sbis = IndexPageSbis(webdriver=driver)
        assert index_page_sbis.get_url() == index_page_sbis.url_page
        contact_page_sbis = index_page_sbis.click_link_contacts()
        assert "Контакты" in contact_page_sbis.get_title()
        assert contact_page_sbis.url_page in contact_page_sbis.get_url()
        index_page_tensor = contact_page_sbis.click_link_tensor()
        assert "Тензор" in index_page_tensor.get_title()
        assert "Сила в людях" in index_page_tensor.get_text_header_block_about()
        assert index_page_tensor.is_block_about() is True
        about_page_tensor = index_page_tensor.click_link_block_about()
        assert "О компании" in about_page_tensor.get_title()
        assert "https://tensor.ru/about" == about_page_tensor.get_url()
        assert "Работаем" in about_page_tensor.get_text_header_block_working()
        assert about_page_tensor.is_block_working() is True
        assert about_page_tensor.is_size_photo_block_working_equal() is True
