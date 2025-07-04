import numpy as np
def calcular_serie_fourier_iterativa(f, t, T, N):
    a0 = (2 / T) * np.trapz(f * np.ones_like(t), t)
    an = []
    bn = []
    for n in range(1, N + 1):
        cos_term = np.cos(2 * np.pi * n * t / T)
        sin_term = np.sin(2 * np.pi * n * t / T)
        an_n = (2 / T) * np.trapz(f * cos_term, t)
        bn_n = (2 / T) * np.trapz(f * sin_term, t)
        an.append(an_n)
        bn.append(bn_n)
    return a0, an, bn
