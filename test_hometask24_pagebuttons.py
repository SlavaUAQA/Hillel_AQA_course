import pytest
from selenium_tasks.hometask24_pagebuttons import PageButtons
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("firefox")
class TestButtons:
    def test_doubleclick_button(self, firefox):
        page = PageButtons(firefox)
        page.open()
        page.maximize_window()
        action_chains = ActionChains(firefox)
        action_chains.double_click(page.doubleclick_button()).perform()
        assert page.get_button_doubleclick_message() == 'You have done a double click'

    def test_right_click_button(self, firefox):
        page = PageButtons(firefox)
        page.open()
        page.maximize_window()
        action_chains = ActionChains(firefox)
        action_chains.context_click(page.right_click_button()).perform()
        assert page.get_button_right_click_message() == 'You have done a right click'

    def test_dynamic_id_click_button(self, firefox):
        page = PageButtons(firefox)
        page.open()
        page.maximize_window()
        action_chains = ActionChains(firefox)
        action_chains.click(page.dynamic_id_click_button()).perform()
        assert page.get_button_dynamic_id_click_message() == 'You have done a dynamic click'

    def test_all_buttons_text(self, firefox):
        page = PageButtons(firefox)
        page.open()
        page.maximize_window()
        action_chains = ActionChains(firefox)
        action_chains.double_click(page.doubleclick_button()).perform()
        action_chains.context_click(page.right_click_button()).perform()
        action_chains.click(page.dynamic_id_click_button()).perform()
        assert page.get_button_doubleclick_message() == 'You have done a double click' and page.get_button_right_click_message() == 'You have done a right click' and page.get_button_dynamic_id_click_message() == 'You have done a dynamic click'
