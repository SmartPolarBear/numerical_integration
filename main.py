# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import timeit

import numpy as np

from integral.romberg import integrate as i1
from integral.montecarlo import integrate as i2
from integral.qmc import integrate as i3


def f(x):
    return np.cos(x)


start = timeit.default_timer()
for i in range(1, 10):
    i1(f, 0, np.pi / 2, 0.0001, 128)
print(timeit.default_timer() - start)

start = timeit.default_timer()
for i in range(1, 10):
    i2(f, 0, np.pi / 2, 8192)
print(timeit.default_timer() - start)

start = timeit.default_timer()
for i in range(1, 10):
    i3(f, 0, np.pi / 2, 8192)
print(timeit.default_timer() - start)

print(i1(f, 0, np.pi / 2, 0.0001, 128),
      i2(f, 0, np.pi / 2, 16384),
      i3(f, 0, np.pi / 2, 8192))
