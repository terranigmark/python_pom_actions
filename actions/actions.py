from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ERROR_LOCATOR_NOT_FOUND = 'No se encontro el elemento con XPath: '

class Actions:

    def __init__(self, driver):
        self.driver = driver

    def get_element_by_xpath(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element
        except Exception as error:
            print(f'{ERROR_LOCATOR_NOT_FOUND} {xpath}')

    def fill_input(self, xpath, text):
        try:
            input_field = self.driver.find_element(By.XPATH, xpath)
            input_field.send_keys(text)
        except Exception as error:
            print(ERROR_LOCATOR_NOT_FOUND + xpath)

    def click_element(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
        except Exception as error:
            print(ERROR_LOCATOR_NOT_FOUND + xpath)

    def get_url(self):
        url = self.driver.current_url()
        return url

    def dropdown_option_by_index(self, xpath, index):
        dropdown = Select(self.driver.find_element(By.XPATH, xpath))
        dropdown.select_by_index(index)

