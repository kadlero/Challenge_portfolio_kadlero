import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    driver = None
    driver_service = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system_invalid (self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('plainadress')
        user_login.type_in_password('1234')
        user_login.wait_for_button_to_be_clickable()
        user_login.click_on_the_sign_in_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_log_in_to_the_system_valid (self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        # user_login.title_of_box()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_to_be_clickable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    # def test_language_selection (self):
    #     user_login = LoginPage(self.driver)
    #     user_login.select_language("english")
    #     time.sleep(3)
    #     user_login.select_language("polski")
    #     time.sleep(3)
    #
    # @classmethod
    # def tearDown(self):
    #     self.driver.quit()

