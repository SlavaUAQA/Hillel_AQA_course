# -*- coding: utf-8 -*-
import pytest
from selenium_tasks.hometask_18_textbox import TextBoxPage

class TestTextBoxPage:
    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()

    def test_curr_addr_fill_and_check(self, chrome):
        pass

    def test_perm_addr_fill_and_check(self, chrome):
        pass
