from selene import browser, have


class MainPage:
    def should_be_loaded(self):
        browser.element('.title').should(have.text('Products'))
        return self

    def add_item_to_cart(self, item_id):
        browser.element(f'#{item_id}').click()
        return self

    def remove_item_from_cart(self, item_id):
        browser.element(f'#{item_id}').click()
        return self

    def open_about_page(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#about_sidebar_link').click()
        return self

    def logout(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#logout_sidebar_link').click()
        return self
