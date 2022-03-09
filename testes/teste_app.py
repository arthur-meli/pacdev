import pytest

from myapp.app import multiplica_por_dois, divide_por_dois


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = multiplica_por_dois(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_por_dois(numbers[1])
        assert res == numbers[0]
