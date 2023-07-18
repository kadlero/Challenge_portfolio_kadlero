from pages.base_page import BasePage


class MatchForm(BasePage):
    expected_title = "Adding match player qaz wsx"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/players/64a59be7083fa860b1acad28/matches/add'
    main_page_field_xpath = "//*[text()='Main page']"
    my_team_field_xpath = "//*[@name='myTeam']"
    enemy_team_field_xpath = "//*[@name='enemyTeam']"
    my_team_score_field_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//*[@name='enemyTeamScore']"
    date_field_xpath = "//*[@name='date']"
    match_at_home_radio_xpath = "//*[@name='matchAtHome' and @value='true']"
    match_out_home_radio_xpath = "//*[@name='matchAtHome' and @value='false']"
    rating_field_xpath = "//*[@name='rating']"
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//*[@type='button' and contains(@class,'MuiButton-containedSecondary')]"
pass
