import numpy as np
import time
from iterativa import calcular_serie_fourier_iterativa
from recursiva import calcular_serie_fourier_recursiva
T = 2 * np.pi
t = np.linspace(0, T, 1000, endpoint=False)
f = np.sign(np.sin(t))  # Usamos la onda cuagrada aca

Ns = [5, 10, 20, 50]
tiempos_iterativo = []
tiempos_recursivo = []

# Aca  medimos los tiempos con libreria time
for N in Ns:
    inicio = time.time()
    calcular_serie_fourier_iterativa(f, t, T, N)
    tiempos_iterativo.append(time.time() - inicio)

    inicio = time.time()
    calcular_serie_fourier_recursiva(f, t, T, N)
    tiempos_recursivo.append(time.time() - inicio)

print("comparación de tiempos (S)")
print(f"{'N':<5} {'iterativo':<20} {'recursivo':<20}")
print("-" * 45)
for i in range(len(Ns)):
    print(f"{Ns[i]:<5} {tiempos_iterativo[i]:<20.6f} {tiempos_recursivo[i]:<20.6f}")
