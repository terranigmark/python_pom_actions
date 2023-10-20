from time import sleep
from page_objects.create_account import CreateAccount
from page_objects.home import Home
from selenium import webdriver

SIGNUP_URL = 'https://madison-island.com/account/register'
HOME_URL = 'http://demo-store.seleniumacademy.com/'


class TestSignUp:
    driver = None
    create_account = None
    home = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.create_account = CreateAccount(cls.driver)
        cls.home = Home(cls.driver)
        cls.driver.get(HOME_URL)
        cls.driver.implicitly_wait(10)

    def test_signup_valid_data(self):
        valid_data = self.create_account
        after_account_created = self.home

        valid_data.fill_input_first_name()
        valid_data.fill_input_last_name()
        valid_data.fill_input_password()
        valid_data.click_create_account()
        after_account_created.assert_home_url()

    def test_change_language(self):
        home = self.home
        home.change_language()

    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.quit()


if __name__ == '__main__':
    test_valid_data = TestSignUp()
    test_valid_data.setup_class()
    test_valid_data.test_change_language()
    test_valid_data.teardown_class()