from app import add, is_prime, fibonacci


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(1) is False
    assert is_prime(10) is False


def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(1) == [0]
