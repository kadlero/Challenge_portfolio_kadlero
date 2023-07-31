import time
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class RemindPasswordPage(BasePage):
    remind_password_url = ('https://dareit.futbolkolektyw.pl/en/remind')
    expected_title = "Remind password"
    box_title = "//*[text()='Remind password' and @class]"
    expected_text = "Remind password"
    email_field_xpath = "//*[@name='email']"
    language_listbox_xpath = "//*[@role='button' and @aria-haspopup='listbox']"
    send_button_xpath = "//*[text()='Send']"

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)
    def click_on_the_send_button(self):
        self.click_on_the_element(self.send_button_xpath)
    def title_of_page(self):
        assert self.get_page_title(self.remind_password_url) == self.expected_title
    def wait_for_button_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.send_button_xpath)
