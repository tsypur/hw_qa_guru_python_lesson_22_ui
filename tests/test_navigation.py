import allure
import pytest
from selene import browser, have
from pages.main_page import MainPage

@allure.suite("Навигация")
class TestNavigation:

    @allure.title("Меню")
    def test_navigation(self, authorized_user):
        with allure.step("Выполните вход в систему"):
            main = authorized_user
        with allure.step("Открыть страницу «О нас» через меню"):
            main.open_about_page()
        with allure.step("Подтвердите, что страница «О нас» открыта"):
            browser.should(have.url_containing('saucelabs.com'))

    @allure.title("Фильтрация товаров")
    def test_product_filtering(self, authorized_user):
        with allure.step("Выполните вход в систему"):
            main = authorized_user
        with allure.step("Примените ценовой фильтр от низкой к высокой"):
            browser.element('.product_sort_container').element('option[value="lohi"]').click()
        with allure.step("Убедитесь, что фильтр применен."):
            browser.element('.active_option').should(have.text('Price (low to high)'))
