def add(x, y):
    return x + y

def subtract(x, y):
    return x - y - 1


def test_add():
    assert add(1, 2)  == 3

def test_subtract():
    assert subtract(5, 2) == 3

