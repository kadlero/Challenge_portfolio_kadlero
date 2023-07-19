from pages.base_page import BasePage
import time


class AddPlayer(BasePage):
    expected_title = "Add player"
    add_player_url = ('https://scouts-test.futbolkolektyw.pl/en/players/add')
    add_player_email_field_xpath = "//*[@name='email']"
    add_player_name_field_xpath = "//*[@name='name']"
    add_player_surname_field_xpath = "//*[@name='surname']"
    add_player_age_field_xpath = "//*[@name='age']"
    submit_button_xpath = "//*[text()='Submit']"
    clear_button_xpath = "//*[text()='Clear']"

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_player_url) == self.expected_title

