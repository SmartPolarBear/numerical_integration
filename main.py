# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import timeit

import numpy as np

from integral.romberg import integrate as i1
from integral.montecarlo import integrate as i2
from integral.qmc import integrate as i3

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


def test_speed():
    rm = []
    mc = []
    qmc = []

    start = timeit.default_timer()
    for i in range(1, 1000):
        i1(f, 0, np.pi / 2, 0.0001, 128)
    rm.append((timeit.default_timer() - start) / 1000)

    start = timeit.default_timer()
    for i in range(1, 1000):
        i1(f2, 0, 4, 0.0001, 128)
    rm.append((timeit.default_timer() - start) / 1000)

    start = timeit.default_timer()
    for i in range(1, 1000):
        i2(f, 0, np.pi / 2, 8192)
    mc.append((timeit.default_timer() - start) / 1000)

    start = timeit.default_timer()
    for i in range(1, 1000):
        i2(f2, 0, 4, 8192)
    mc.append((timeit.default_timer() - start) / 1000)

    start = timeit.default_timer()
    for i in range(1, 1000):
        i3(f, 0, np.pi / 2, 8192)
    qmc.append((timeit.default_timer() - start) / 1000)

    start = timeit.default_timer()
    for i in range(1, 1000):
        i3(f2, 0, 4, 8192)
    qmc.append((timeit.default_timer() - start) / 1000)

    x = np.arange(2)
    total_width, n = 0.8, 3
    width = total_width / n
    x = x - (total_width - width) / 2

    tick_labels = ["f(x)", "g(x)"]
    plt.bar(x, rm, width=width, label='Romberg')
    plt.bar(x + width, mc, width=width, label='Monte Carlo')
    plt.bar(x + 2 * width, qmc, width=width, label='Quasi-Monte Carlo')
    plt.legend()
    plt.xticks(x + width / 2, tick_labels)
    plt.show()


def test_variance():
    iters = []
    vals1 = []
    vals2 = []
    for i in range(1, 500):
        iters.append(i)
        vals1.append(i2(f2, 0, 4, 8192))
        vals2.append(i3(f2, 0, 4, 8192))

    print(np.mean(np.array(vals1, dtype=float)))
    print(np.var(np.array(vals1, dtype=float)))
    print(np.mean(np.array(vals2, dtype=float)))
    print(np.var(np.array(vals2, dtype=float)))

    real = 5.767433490695931
    plt.plot(iters, vals1, 'ro', iters, vals2, 'go', [0, len(iters)], [real, real], 'b')
    plt.xlabel('Iteration')
    plt.ylabel('Integral Value')
    plt.show()

    plt.plot(iters, vals1, 'ro', [0, len(iters)], [real, real], 'b')
    plt.xlabel('Iteration')
    plt.ylabel('Integral Value')
    plt.show()

    plt.plot(iters, vals2, 'go', [0, len(iters)], [real, real], 'b')
    plt.xlabel('Iteration')
    plt.ylabel('Integral Value')
    plt.show()

test_variance()

start = timeit.default_timer()
for i in range(1, 1000):
    i1(f2, 0, 4, 0.0001, 128)
print(timeit.default_timer() - start)

start = timeit.default_timer()
for i in range(1, 10):
    i2(f, 0, np.pi / 2, 8192)
print(timeit.default_timer() - start)

start = timeit.default_timer()
for i in range(1, 1000):
    i3(f2, 0, 4, 8192)
print(timeit.default_timer() - start)

print(i1(f, 0, np.pi / 2, 0.0001, 128),
      i2(f, 0, np.pi / 2, 16384),
      i3(f, 0, np.pi / 2, 8192))
