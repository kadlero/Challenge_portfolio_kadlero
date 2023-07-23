import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.remind_password import RemindPasswordPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemindPasswordPage(unittest.TestCase):

    driver = None
    driver_service = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remind_password (self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        # user_login.title_of_box()
        user_login.wait_for_button_to_be_clickable()
        user_login.click_on_the_remind_password_button()
        user_remind = RemindPasswordPage(self.driver)
        user_remind.title_of_page()
        user_remind.type_in_email('user03@getnada.com')
        user_remind.wait_for_button_to_be_clickable()
        user_remind.click_on_the_send_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()


