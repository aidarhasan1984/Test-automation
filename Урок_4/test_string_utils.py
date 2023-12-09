import pytest
from string_utils import StringUtils

class TestStringUtils:

    @pytest.fixture
    def string_utils(self):
        return StringUtils()
        
    # Позитивные тесты
    def test_capitalize_first_letter(self, string_utils):
        assert string_utils.capitilize("skypro") == "Skypro"
        
    def test_trim_leading_whitespace(self, string_utils):
        assert string_utils.trim("   skypro") == "skypro"

    # Негативные тесты
    def test_to_list_empty_string(self, string_utils):
        assert string_utils.to_list("") == []

    def test_contains_empty_symbol(self, string_utils):
        assert not string_utils.contains("SkyPro", "")