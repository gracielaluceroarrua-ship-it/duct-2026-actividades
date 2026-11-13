from analizador import contar_frecuencias

def test_contar_frecuencias_basico():
    """Verifica que cuente correctamente las palabras en un texto sencillo."""
    texto = "hola mundo hola"
    resultado = contar_frecuencias(texto)
    esperado = {"hola": 2, "mundo": 1}
    assert resultado == esperado

def test_contar_frecuencias_vacio():
    """Verifica que un texto vacío devuelva un diccionario vacío sin errores."""
    texto = ""
    resultado = contar_frecuencias(texto)
    esperado = {}
    assert resultado == esperado

def test_contar_frecuencias_mayusculas():
    """Verifica que las mayúsculas y minúsculas se traten como la misma palabra."""
    texto = "Sol sol SOL"
    resultado = contar_frecuencias(texto)
    esperado = {"sol": 3}
    assert resultado == esperado