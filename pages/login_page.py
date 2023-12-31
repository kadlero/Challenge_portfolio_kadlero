import time
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class LoginPage(BasePage):
    login_box_title = "//*[text()='Scouts Panel']"
    expected_text = "Scouts Panel"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    remind_password_button_xpath = "//*[text()='Remind password']"
    language_listbox_xpath = "//*[@class='MuiSelect-nativeInput']"
    language_listbox_en_xpath = "//*[@data-value='en']"
    language_listbox_pl_xpath = "//*[@data-value='pl']"
    login_url = ('https://dareit.futbolkolektyw.pl/en/login')
    expected_title = "Scouts panel - sign in"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def click_on_the_remind_password_button(self):
        self.click_on_the_element(self.remind_password_button_xpath)
    def select_language(self, language):
        self.click_on_the_element(self.language_listbox_xpath)
        time.sleep(1)
        if language == "english":
            self.click_on_the_element(self.language_listbox_en_xpath)
        else:
            self.click_on_the_element(self.language_listbox_pl_xpath)
    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
    # def title_of_box(self, driver, login_box_title, expected_text, xpath=login_box_title):
    #     element = driver.find_element(by=By.XPATH, value=xpath)
    #     element_text = element.text
    #     assert expected_text == element_text
    def wait_for_button_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)





