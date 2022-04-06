import numpy as np

from typing import Callable


def integrate(f: Callable, a: np.float, b: np.float, n: int = 32) -> np.float:
    x = np.random.uniform(a, b, n)
    y = f(x)
    y_mean = np.sum(y) / n
    return (b - a) * y_mean
