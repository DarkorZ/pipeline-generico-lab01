from app import sumar

def test_suma_positivos():
    assert sumar(2, 3) == 5

def test_suma_negativos():
    assert sumar(-2, -3) == -5

def test_cero():
    assert sumar(5,0)==5
