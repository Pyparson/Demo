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

    def test_sum(self):
        a = 3
        b = 4
        sum = a + b
        assert sum == 7, "failed"

    def test_sub(self):
        a = 3
        b = 4
        sum = b - a
        assert sum == 7, "failed"
        
    def test_sum1(self):
        a = 4
        b = 4
        sum = a + b
        assert sum == 8, "failed"



# if __name__ == '__main__':
#
#
#     True
#     pytest.main("-q test_work.py")
