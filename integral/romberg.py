import numpy as np

from typing import Callable


def integrate(f: Callable[[np.float], np.float], a: np.float, b: np.float, epsilon: np.float = 0.001,
              n: int = 32) -> np.float:
    r: np.ndarray = np.zeros((n + 1, n + 1), dtype=float)
    h: np.float = b - a
    r[0, 0] = 0.5 * h * (f(a) + f(b))

    p2: int = 1
    for k in range(1, n + 1):
        h *= 0.5
        p2 *= 2

        r[k, 0] = 0.0
        for i in range(1, p2, 2):
            r[k, 0] += f(a + i * h)
        r[k, 0] *= h
        r[k, 0] += 0.5 * r[k - 1, 0]

        p4 = 1
        for m in range(1, k + 1):
            p4 *= 4
            r[k, m] = r[k, (m - 1)] + (r[k, (m - 1)] - r[k - 1, (m - 1)]) / (p4 - 1)

        if k != 1 and np.abs(r[k, 0] - r[(k - 1), 0]) < epsilon:
            return r[k, 0]

    return r[n, 0]
