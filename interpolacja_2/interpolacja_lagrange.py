import numpy as np
from interpolacja_2.utils import func_plot, chebyshev_nodes
import matplotlib.pyplot as plt
import math


def lagrange_interpolation(x, y):
    n = len(x) - 1
    m = []
    for i in range(n + 1):
        m_val = 1
        for j in range(n + 1):
            if j == i: continue
            m_val *= (x[i] - x[j])
        m.append(m_val)

    def f(x_arg):
        y_val = 0
        for k in range(n + 1):
            p = 1
            for j in range(n + 1):
                if j == k: continue
                p *= (x_arg - x[j])
            y_val += p * y[k] / m[k]
        return y_val

    return f


def lagrange_interpolation_func(f, a, b, n, chebyshev=False, ax=None):
    if chebyshev:
        x = chebyshev_nodes(a, b, n)
    else:
        x = np.linspace(a, b, n)
    y = [f(xi) for xi in x]
    if ax is not None:
        ax.plot(x, y, 'o', c="r")
    return lagrange_interpolation(x, y)


my_func = lambda x, k=4, m=1: math.exp(-k * math.sin(m * x)) + k * math.sin(m * x) - 1

func = lagrange_interpolation_func(my_func, -4 * math.pi, 3 * math.pi, 50, True)

func_plot(func, -4 * math.pi, 3 * math.pi, 1000)
func_plot(my_func, -4 * math.pi, 3 * math.pi, 1000)
plt.show()

# tabelki z bledami, porównać newtona i lagrange'a, jak te same wyniki to tylko jedna tabelka
# osobno sytuacja w której sie rozjechało
# wezly musza byc zaznaczone na wykresie

# hermit - ograniczamy sie do pierwszej pochodnej
# hermita mozna oprzec na newtona albo lagrangea, wystarczy jeden z nich, ale trzeba miec siwadomosc który
