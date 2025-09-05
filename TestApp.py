from app import *

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_multiplicacao():
    assert multiplicacao(1, 1) == 1
    assert multiplicacao(10, 10) == 100
    assert multiplicacao(0, 15) == 0