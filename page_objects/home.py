from actions.actions import Actions

HOME_URL = 'https://madison-island.com/'
LANGUAGE_DROPDOWN = '//*[@id="select-language"]'

class Home:
    actions = Actions

    def __init__(self, driver):
        self.actions = Actions(driver)

    def assert_home_url(self):
        assert self.actions.get_url() == HOME_URL

    def change_language(self):
        self.actions.dropdown_option_by_index(LANGUAGE_DROPDOWN, 2)
