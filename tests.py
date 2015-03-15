import pytest

import billboards


def test_fit_string():
    width, height = 100, 2
    text = "First test string"
    font_size = 2
    assert billboards.text_fits(width, height, text, font_size)

def test_fit_string_too_tall():
    width, height = 100, 2
    text = "First test string"
    font_size = 3
    assert not billboards.text_fits(width, height, text, font_size)

def test_fit_string_too_wide():
    width, height = 10, 2
    text = "First test string"
    font_size = 2
    assert not billboards.text_fits(width, height, text, font_size)

def test_fit_string_two_line_wrap():
    width, height = 6, 2
    text = "Test string"
    font_size = 1
    assert billboards.text_fits(width, height, text, font_size)

def test_five_words():
    width, height = 9, 2
    text = "Test test test test test"
    font_size = 1
    assert not billboards.text_fits(width, height, text, font_size)

def test_strip_words():
    width = 9
    words = ["Test", "test", "test", "test", "test"]
    assert billboards.strip_words(width, words) == ['test', 'test', 'test']

def test_search_font_size():
    width, height = 10,2
    text = "First test string"
    assert billboards.search_font_size(width, height, text) == 1

def test_search_font_size_high():
    width, height = 18, 9
    text = "First test string"
    assert billboards.search_font_size(width, height, text) == 3


if __name__ == '__main__':
    pytest([__file__])