import time
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_box_title = "//*[text()='Scouts Panel']"
    expected_text = "Scouts Panel"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en/login')
    expected_title = "Scouts panel - sign innnn"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
    # def title_of_box(self, driver, login_box_title, expected_text, xpath=login_box_title):
    #     element = driver.find_element(by=By.XPATH, value=xpath)
    #     element_text = element.text
    #     assert expected_text == element_text


