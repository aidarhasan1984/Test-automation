import pytest
from string_utils import StringUtils

# Позитивные тесты
def test_capitalize():
    utils = StringUtils()
    assert utils.capitalize("skypro") == "Skypro"

def test_trim():
    utils = StringUtils()
    assert utils.trim("   skypro") == "skypro"

def test_to_list():
    utils = StringUtils()
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]

def test_contains():
    utils = StringUtils()
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("SkyPro", "U") == False

def test_delete_symbol():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_starts_with():
    utils = StringUtils()
    assert utils.starts_with("SkyPro", "S") == True
    assert utils.starts_with("SkyPro", "P") == False

def test_end_with():
    utils = StringUtils()
    assert utils.end_with("SkyPro", "o") == True
    assert utils.end_with("SkyPro", "P") == False

# Негативные тесты
def test_capitalize_empty_string():
    utils = StringUtils()
    assert utils.capitalize("") == ""

def test_trim_with_space():
    utils = StringUtils()
    assert utils.trim(" ") == ""

def test_to_list_empty_string():
    utils = StringUtils()
    assert utils.to_list("") == []

def test_contains_none_symbol():
    utils = StringUtils()
    assert not utils.contains("SkyPro", None)

def test_delete_symbol_none_symbol():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", None) == "SkyPro"

def test_starts_with_empty_string():
    utils = StringUtils()
    assert not utils.starts_with("", "S")

def test_end_with_empty_string():
    utils = StringUtils()
    assert not utils.end_with("", "o")