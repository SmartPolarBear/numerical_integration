import numpy as np
from scipy.stats import qmc

from typing import Callable


def van_der_corput(n_sample, base=2):
    sequence = np.zeros(n_sample)
    for i in range(n_sample):
        n_th_number, denom = 0., 1.

        k = i
        while k > 0:
            k, remainder = divmod(k, base)
            denom *= base
            n_th_number += remainder / denom
        sequence[i] = n_th_number

    return sequence


def integrate(f: Callable, a: np.float, b: np.float, n: int = 32) -> np.float:
    # samples = van_der_corput(n)
    #
    # x = (b - a) * samples + a
    x = qmc.scale(qmc.LatinHypercube(d=1).random(n), a, b)
    y = f(x)
    y_mean = np.sum(y) / n
    return (b - a) * y_mean
