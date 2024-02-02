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
        '',
        'perm_identity\nПерсонализированная реклама и контент, определение эффективности рекламы и контента, аналитические сведения об аудитории и разработка сервисов',
        'devices\nХранение и (или) доступ к информации на устройстве',
        '', '', '', ''
    ])
    def test_elements_response(self, chrome, expected):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_categories()
        for element, expected_value in zip(elements, expected):
            assert element == expected_value
