from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts Panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/'
    main_page_field_xpath = "//*[text()='Main page']"
    players_field_xpath = "//*[text()='Players']"
    language_field_xpath = "/html/body/div/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_field_xpath = "//*[text()='Sign out']"
    main_page_logo_field_xpath = "//*[contains(@title, 'Logo')]"
    add_player_button_xpath = "//*[text()='Add player']"
    dev_team_contact_button_xpath = "//*[text()='Dev team contact']"
    last_created_player_xpath = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
pass
