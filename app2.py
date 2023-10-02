import matplotlib.pyplot as plt
import numpy as np

def calcular_fuerza(m, vi, vf, t):
    a = (vf - vi) / t
    F = m * a
    return F

if __name__ == "__main__":
    m = float(input("Ingrese masa en kg: "))
    vi = float(input("Ingrese la velocidad inicial en m/s: "))
    vf = float(input("Ingrese la velocidad final en m/s: "))
    t = float(input("Ingrese el tiempo en s: "))

    fuerza = calcular_fuerza(m, vi, vf, t)

    tiempo_grafica = np.linspace(0, t, 100)

    # Calcular la velocidad en función del tiempo para el grafico
    v = vi + (fuerza / m) * tiempo_grafica

    # Grafico
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo_grafica, v, label='Velocidad')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.legend()
    plt.title('Cambio de Velocidad del Móvil')
    plt.grid(True)
    plt.show()

    print("La fuerza experimentada por el móvil durante el cambio de velocidad es: {:.2f} N".format(fuerza))