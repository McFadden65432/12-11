import numpy as np


def f(x, s, y):
    return 1 - np.exp(x - s) * y


def solve(f, a, b, n, y0):
    x = np.linspace(a, b, n + 1)
    h = x[1] - x[0]
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(1, n + 1):
        s = np.linspace(a, x[i], i + 1)
        w = np.ones(i + 1)
        w[0] = 0.5
        w[-1] = 0.5
        y[i] = y[i - 1] + h * np.dot(w, f(x[i], s, y[:i+1]))
    return x, y


a = 0
b = 2
y0 = 0

# Различные значения числа частичных (частных?) отрезков
n_values = [10, 20, 40, 80]

for n in n_values:
    x, y = solve(f, a, b, n, y0)
    print("Число отрезков: ", n)
    print("Решение: ", y)