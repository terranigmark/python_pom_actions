from actions.actions import Actions
from fixtures.signup_data import users


FIRST_NAME_LOCATOR = '//*[@id="FirstName"]'
LAST_NAME_LOCATOR = '//*[@id="LastName"]'
EMAIL_LOCATOR = '//*[@id="Email"]'
PASSWORD_LOCATOR = '//*[@id="CreatePassword"]'
CREATE_ACCOUNT_BUTTON = '//*[@value="Create"]'


class CreateAccount:
    actions = Actions

    def __init__(self, driver):
        self.actions = Actions(driver)

    def assert_presence_first_name(self):
        print(self.actions.get_element_by_xpath(FIRST_NAME_LOCATOR))

    def fill_input_first_name(self):
        self.actions.fill_input(FIRST_NAME_LOCATOR, users['valid_data']['first_name'])

    def fill_input_last_name(self):
        self.actions.fill_input(LAST_NAME_LOCATOR, users['valid_data']['last_name'])

    def fill_input_email(self):
        self.actions.fill_input(EMAIL_LOCATOR, users['valid_data']['email'])

    def fill_input_password(self):
        self.actions.fill_input(PASSWORD_LOCATOR, users['valid_data']['password'])

    def click_create_account(self):
        self.actions.click_element(CREATE_ACCOUNT_BUTTON)