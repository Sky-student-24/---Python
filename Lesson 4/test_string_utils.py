import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Exit", "Exit"),
    (" 456", "456"),
    ("   04 апреля 2023", "04 апреля 2023"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Exit", "Exit"),
    ("", ""),
    ("   ", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("Exit", "x"),
    ("12345", "4"),
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol)


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("Exit", "z"),
])
def test_contains_negative(string, symbol):
    assert not string_utils.contains(string, symbol)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Exit", "x", "Eit"),
    ("357", "3", "57"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Exit", "z", "Exit"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
