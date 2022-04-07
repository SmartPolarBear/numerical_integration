# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import timeit

import numpy as np

# from integral.romberg import integrate as i1
# from integral.montecarlo import integrate as i2
# from integral.qmc import integrate as i3

import matplotlib.pyplot as plt
from integral.romberg import integrate2


def f(x):
    return np.cos(x)


def f2(x):
    return np.power(15 * np.power(x, 3) + 21 * np.power(x, 2) + 41 * x + 3, 1.0 / 4.0) * np.exp(-0.5 * x)


def test_cov(ff, real, a, b):
    val, iters, vals = integrate2(ff, a, b, 0.0001, 128)

    print(val)
    plt.plot(iters, vals, 'ro-', [0, len(iters)], [real, real], 'b')
    plt.xlabel('Iteration')
    plt.ylabel('Integral Value')
    plt.show()


test_cov(f, 1, 0, np.pi / 2)
test_cov(f2, 5.7674, 0, 4)

# start = timeit.default_timer()
# for i in range(1, 10):
#     i1(f, 0, np.pi / 2, 0.0001, 128)
# print(timeit.default_timer() - start)
#
# start = timeit.default_timer()
# for i in range(1, 10):
#     i2(f, 0, np.pi / 2, 8192)
# print(timeit.default_timer() - start)
#
# start = timeit.default_timer()
# for i in range(1, 10):
#     i3(f, 0, np.pi / 2, 8192)
# print(timeit.default_timer() - start)
#
# print(i1(f, 0, np.pi / 2, 0.0001, 128),
#       i2(f, 0, np.pi / 2, 16384),
#       i3(f, 0, np.pi / 2, 8192))
