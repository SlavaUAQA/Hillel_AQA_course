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
        '',
        '',
        '',
        '',
        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        ''
    ])
    def test_elements_response(self, chrome, expected):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_categories()
        for element in elements:
            assert element in expected
