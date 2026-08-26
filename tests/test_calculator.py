import pytest

from demo_app.calculator import add, calculate_discount, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_subtract_numbers():
    assert subtract(10, 4) == 6


def test_calculate_discount():
    assert calculate_discount(200, 25) == pytest.approx(150)


def test_calculate_zero_discount():
    assert calculate_discount(80, 0) == pytest.approx(80)


def test_calculate_full_discount():
    assert calculate_discount(80, 100) == pytest.approx(0)


def test_calculate_discount_rejects_negative_price():
    with pytest.raises(ValueError, match="price"):
        calculate_discount(-1, 20)


@pytest.mark.parametrize("discount_percent", [-1, 101])
def test_calculate_discount_rejects_invalid_percentage(discount_percent):
    with pytest.raises(ValueError, match="discount_percent"):
        calculate_discount(100, discount_percent)
