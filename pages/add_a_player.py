from pages.base_page import BasePage
import time


class AddPlayer(BasePage):
    expected_title = "Add player"
    add_player_url = ('https://dareit.futbolkolektyw.pl/en/players/add')
    add_player_email_field_xpath = "//*[@name='email']"
    add_player_name_field_xpath = "//*[@name='name']"
    add_player_surname_field_xpath = "//*[@name='surname']"
    add_player_age_field_xpath = "//*[@name='age']"
    add_player_leg_xpath = "//*[@id='leg']"
    add_player_right_leg_xpath = "//*[@data-value='right']"
    add_player_left_leg_xpath = "//*[@data-value='left']"
    add_player_main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[text()='Submit']"
    clear_button_xpath = "//*[text()='Clear']"
    main_page_button_xpath = "// *[text() = 'Main page']"

    def type_in_name(self, name):
        self.field_send_keys(self.add_player_name_field_xpath, name)
    def type_in_surname(self, surname):
        self.field_send_keys(self.add_player_surname_field_xpath, surname)
    def type_in_age(self, age):
        self.field_send_keys(self.add_player_age_field_xpath, age)
    def type_in_email(self, email):
        self.field_send_keys(self.add_player_email_field_xpath, email)
    def type_in_main_position(self, main_position):
        self.field_send_keys(self.add_player_main_position_field_xpath, main_position)
    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
    def click_on_the_main_page_button(self):
        self.click_on_the_element(self.main_page_button_xpath)
    def wait_for_button_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_player_url) == self.expected_title
    def select_leg(self, leg):
        self.wait_for_element_to_be_clickable(self.add_player_leg_xpath)
        self.click_on_the_element(self.add_player_leg_xpath)
        if leg == "Right leg":
            self.click_on_the_element(self.add_player_right_leg_xpath)
        else:
            self.click_on_the_element(self.add_player_left_leg_xpath)

