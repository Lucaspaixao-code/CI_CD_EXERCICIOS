from app import soma

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_multiplicacao():
    assert soma(1, 1) == 1
    assert soma(10, 10) == 100
    assert soma(0, 15) == 0