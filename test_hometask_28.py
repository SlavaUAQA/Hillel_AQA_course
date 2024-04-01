import pytest
from selenium_tasks.hometask_28 import PageCheckbox


@pytest.mark.usefixtures("firefox")
class TestCheckboxex:
    def test_checkboxex(self, firefox):
        page = PageCheckbox(firefox)
        page.open()
        firefox.maximize_window()
        page.button_expand_all().click()
        page.commands_checkbox().click()
        page.scroll_to_general_checkbox()
        page.scroll_to_commands_checkbox()
        page.general_checkbox().click()
        assert page.commands_checkbox().is_selected and page.general_checkbox().is_selected
