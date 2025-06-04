import numpy as np
def calcular_serie_fourier_recursiva(f, t, T, N):
    a0 = (2 / T) * np.trapz(f * np.ones_like(t), t)
        
        def calcular_n(n):
        if n == 0:
            return [], []
        an_rest, bn_rest = calcular_n(n - 1)
        cos_term = np.cos(2 * np.pi * n * t / T)
        sin_term = np.sin(2 * np.pi * n * t / T)
        an_n = (2 / T) * np.trapz(f * cos_term, t)
        bn_n = (2 / T) * np.trapz(f * sin_term, t)
        return an_rest + [an_n], bn_rest + [bn_n]

    an, bn = calcular_n(N)
    return a0, an, bn
