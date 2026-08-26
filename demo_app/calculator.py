def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def calculate_discount(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("price must be greater than or equal to zero")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    return price * (1 - discount_percent / 100)
