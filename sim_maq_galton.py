import numpy as np
import matplotlib.pyplot as plt

def simular_galton(n_canicas=3000, n_niveles=12):
    """
    Simula una máquina de Galton con n_canicas y n_niveles filas de obstáculos.
    Cada canica se desplaza aleatoriamente derecha/izquierda por nivel.
    Retorna una lista con la posición final (número de veces que cayó en el lado izquierdo) de cada canica.
    """
    resultados = np.random.binomial(n_niveles, 0.5, size=n_canicas)
    return resultados.tolist()

def graficar_histograma(resultados, n_niveles):
    """
    Graficar el histograma de los resultados (variable entre 0 y n_niveles).
    Colocar título y nombres de ejes.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(resultados, bins=range(n_niveles), align='left',
             rwidth=1, color='skyblue', edgecolor='black')
    plt.title('"Distribución de Canicas en la Máquina de Galton"')
    plt.xlabel('Contenedor (número de desviaciones a la Izquierda)')
    plt.ylabel('Cantidad de Canicas')
    plt.xticks(range(n_niveles))
    plt.grid(axis='y', linestyle='--', alpha=0)
    plt.show()

if __name__ == '__main__':
    n_bolas = 3000
    n_niveles = 12
    resultados = simular_galton(n_bolas, n_niveles)
    graficar_histograma(resultados, n_niveles)