import pytest
from hometask19_elementspage import ElementsPage


class TestElementsPage:
    @pytest.mark.parametrize("expected", [
        'Text Box',
        'Check Box',
        'Radio Button',
        'Web Tables',
        'Buttons',
        'Links',
        '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '', '', '', '', '', '',
    ])
    def test_elements_response(self, firefox, expected):
        page = ElementsPage(firefox)
        page.open()
        elements = page.get_elements_categories()
        if expected is not None:
            assert expected in elements
        else:
            assert expected not in elements
