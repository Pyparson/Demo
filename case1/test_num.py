import pytest


class TestNum:
    def test_add(self):
        a = 3
        b = 4
        sum = a + b
        assert sum == 7, "failed"

    def test_div(self):
        a = 3
        b = 4
        sum = b - a
        assert sum == 7, "failed"
