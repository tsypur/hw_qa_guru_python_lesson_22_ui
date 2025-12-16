import allure
import pytest
from selene import browser, have
from pages.main_page import MainPage
from pages.cart_page import CartPage



main = MainPage()
cart = CartPage()

@allure.suite("Корзина")
class TestCart:

    @allure.title("Добавление товара в корзину")
    def test_add_item_to_cart(self, authorized_user):
        with allure.step("Выполните вход в систему"):
            main = authorized_user
        with allure.step("Добавить товар в корзину"):
            main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
        with allure.step("Проверить корзину"):
            cart.open_cart()
            browser.element('.title').should(have.text('Your Cart'))
            cart.should_contain_item('Sauce Labs Backpack')
        with allure.step("Проверьте количество товара в корзине"):
            cart.should_have_items_count(1)

    @allure.title("Удаление товара из корзины")
    def test_remove_item_from_cart(self, authorized_user):
        with allure.step("Выполните вход в систему"):
            main = authorized_user
        with allure.step("Добавить товар в корзину"):
            main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
        with allure.step("Удалить товар из корзины"):
            main.remove_item_from_cart('remove-sauce-labs-backpack')
        with allure.step("Убедитесь, что корзина пуста."):
            cart.open_cart()
            cart.should_have_items_count(0)










