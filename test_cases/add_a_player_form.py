import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_player import AddPlayer
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

    def test_add_a_player_valid (self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_to_be_clickable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayer(self.driver)
        add_player.title_of_page()
        add_player.type_in_name('Adam')
        add_player.type_in_surname('Kowalski')
        add_player.type_in_age('04302012')
        add_player.type_in_main_position('attacker')
        add_player.wait_for_button_to_be_clickable()
        add_player.click_on_the_submit_button()
        add_player.click_on_the_main_page_button()
        # dashboard_page.check_last_created_player()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_add_a_player_invalid (self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_to_be_clickable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayer(self.driver)
        add_player.title_of_page()
        add_player.type_in_email('user03@getnada.com')
        add_player.wait_for_button_to_be_clickable()
        add_player.click_on_the_submit_button()
        # dashboard_page.title_of_page()
        time.sleep(5)
        add_player.click_on_the_main_page_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
        
    def test_add_a_player_leg (self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user03@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_to_be_clickable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayer(self.driver)
        add_player.title_of_page()
        add_player.select_leg("Right leg")
        time.sleep(3)
        add_player.select_leg("Left leg")
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()