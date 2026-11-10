# test_analizador.py
from analizador import contar_frecuencias

def test_frecuencias_basico():
    resultado = contar_frecuencias("sol luna sol")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1

def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}

def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("Sol sol SOL")
    # TODO resuelto: verifica que las tres variantes se cuentan como la misma palabra
    assert resultado["sol"] == 3
def test_frecuencias_espacios_extras():
    texto = "   sol    luna   sol   "
    resultado = contar_frecuencias(texto)
    assert resultado == {"sol": 2, "luna": 1}
def test_frecuencias_con_puntuacion_sin_limpieza():
    texto = "¡Sol, luna! sol."
    resultado = contar_frecuencias(texto)
    # Verificamos qué pasa exactamente con la puntuación en el código actual
    assert resultado == {"¡sol,": 1, "luna!": 1, "sol.": 1}