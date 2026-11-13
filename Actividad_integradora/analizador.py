import matplotlib.pyplot as plt

def contar_frecuencias(texto):
    """
    Recibe un texto en formato string, lo pasa a minúsculas, 
    lo separa en palabras y devuelve un diccionario con las frecuencias.
    """
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def main():
    ruta = "texto_integradora.txt"
    
    # 1. Lectura del archivo manejando la excepción si no existe
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta}'. Asegúrate de que esté en la misma carpeta.")
        return
    
    # 2. Conteo de frecuencias
    frecuencias = contar_frecuencias(texto)
    
    # Mostrar estadísticas generales en consola (opcional pero útil)
    print(f"Cantidad total de palabras: {sum(frecuencias.values())}")
    print(f"Cantidad de palabras distintas: {len(frecuencias)}")
    
    # Obtener el top 10 de palabras más frecuentes
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
    
    print("\nLas 10 palabras más frecuentes:")
    for palabra, frecuencia in top10:
        print(f"  {palabra}: {frecuencia}")
        
    # 3. Generar y guardar el gráfico de barras con matplotlib
    palabras_grafico = [item[0] for item in top10]
    valores_grafico = [item[1] for item in top10]
    
    plt.figure(figsize=(10, 6))
    # Usamos barh invertido para que la palabra más frecuente quede arriba
    plt.barh(palabras_grafico[::-1], valores_grafico[::-1], color="steelblue")
    plt.title("Top 10 palabras más frecuentes (Actividad Integradora)")
    plt.xlabel("Frecuencia")
    plt.ylabel("Palabra")
    plt.tight_layout()
    
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()