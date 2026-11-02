import matplotlib.pyplot as plt

def analizar_y_graficar(ruta, top_n=10):
    """
    Lee un archivo de texto, cuenta la frecuencia de cada palabra
    y genera un grafico de barras horizontales con las top_n
    palabras mas frecuentes.
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
        
    palabras_texto = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras_texto:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    # Líneas a completar:
    palabras = [item[0] for item in top10]
    valores = [item[1] for item in top10]
    
    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()

def main():
    analizar_y_graficar("texto.txt")

if __name__ == "__main__":
    main()