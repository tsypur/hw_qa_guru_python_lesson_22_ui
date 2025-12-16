import pytest
import allure
from selene import browser, be
from pages.login_page import LoginPage
from pages.main_page import MainPage


login = LoginPage()
main = MainPage()

@allure.suite("Аутентификация")
class TestLogin:

    @allure.title("Успешный вход в систему")
    def test_successful_login(self, browser_setup):
        with allure.step("Откройте страницу входа"):
            login.open()
        with allure.step("Введите действительные учетные данные"):
            login.login('standard_user', 'secret_sauce')
        with allure.step("Убедитесь, что пользователь вошел в систему"):
            main.should_be_loaded()

    @allure.title("Неудачный вход в систему")
    def test_failed_login(self, browser_setup):
        with allure.step("Откройте страницу входа"):
            login.open()
        with allure.step("Введите неверные учетные данные"):
            login.login('invalid_user', 'invalid_password')
        with allure.step("Убедитесь, что отображается сообщение об ошибке"):
            login.should_have_error('Epic sadface: Username and password do not match any user in this service')

    @allure.title("Выход")
    def test_logout(self, authorized_user):
        with allure.step("Пользователь уже авторизован"):
            main = authorized_user
        with allure.step("Выполнить выход из системы"):
            main.logout()
        with allure.step("Убедитесь, что пользователь вышел из системы."):
            browser.element('#login-button').should(be.visible)


