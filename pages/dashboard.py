from pages.base_page import BasePage
import time


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = ('https://scouts-test.futbolkolektyw.pl/en/')
    main_page_field_xpath = "//*[text()='Main page']"
    players_field_xpath = "//*[text()='Players']"
    language_field_xpath = "/html/body/div/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_field_xpath = "//*[text()='Sign out']"
    main_page_logo_field_xpath = "//*[contains(@title, 'Logo')]"
    add_player_button_xpath = "//*[text()='Add player']"
    dev_team_contact_button_xpath = "//*[text()='Dev team contact']"
    last_created_player_xpath = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)
    def wait_for_button_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.dev_team_contact_button_xpath)
    def click_on_the_dev_team_contact_button(self):
        self.click_on_the_element(self.dev_team_contact_button_xpath)
