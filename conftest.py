import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv
from utils import attach



@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.base_url = 'https://www.saucedemo.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10.0

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASSWORD')

    if not selenoid_login or not selenoid_password:
        pytest.skip("Selenoid credentials not found in .env file")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    yield



    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)


    browser.quit()


@pytest.fixture
def authorized_user(browser_setup):
    from pages.login_page import LoginPage
    from pages.main_page import MainPage

    login_page = LoginPage()
    login_page.open().login('standard_user', 'secret_sauce')
    return MainPage()