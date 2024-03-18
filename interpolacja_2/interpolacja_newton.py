import matplotlib.pyplot as plt
import numpy as np
import math
from interpolacja_2.utils import func_plot, chebyshev_nodes, newton_symbol


def newton_interpolation(x, y):
    n = len(x)
    quoteint_difference_tab = [[y[j] if i == 0 else 0 for i in range(n)] for j in range(n)]
    for j in range(1, n):
        for i in range(j, n):
            quoteint_difference_tab[i][j] = (quoteint_difference_tab[i][j - 1] - quoteint_difference_tab[i - 1][
                j - 1]) / (x[i] - x[i - j])
    factor_tab = [quoteint_difference_tab[i][i] for i in range(n)]

    def f(x_arg):
        result = factor_tab[n - 1]
        for i in range(n - 2, -1, -1):
            result = result * (x_arg - x[i]) + factor_tab[i]
        return result

    return f


def newton_interpolation_eq(x, y):
    n = len(x)
    h = x[1] - x[0]
    diff_tab = [y[i] for i in range(n)]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff_tab[i] = diff_tab[i] - diff_tab[i - 1]

    def f(x_arg):
        s = (x_arg - x[0]) / h
        result = 0
        for i in range(0, n):
            result += newton_symbol(s, i) * diff_tab[i]
        return result

    return f


def newton_interpolation_func(f, a, b, n, chebyshev=False, ax=None):
    if chebyshev:
        x = chebyshev_nodes(a, b, n)
        y = [f(xi) for xi in x]
        if ax is not None:
            ax.plot(x, y, 'o', c="r")
        return newton_interpolation(x, y)
    else:
        x = np.linspace(a, b, n)
        y = [f(xi) for xi in x]
        if ax is not None:
            ax.plot(x, y, 'o', c="r")
        return newton_interpolation_eq(x, y)


my_func = lambda x, k=4, m=1: math.exp(-k * math.sin(m * x)) + k * math.sin(m * x) - 1

func = newton_interpolation_func(my_func, -4 * math.pi, 3 * math.pi, 50, True)

func_plot(func, -4 * math.pi, 3 * math.pi, 1000)
func_plot(my_func, -4 * math.pi, 3 * math.pi, 1000)
plt.show()

# def find_max_error(my_func, func):
#     maxx = 0
#     x = np.linspace(-4*math.pi, 3*math.pi, 1000)
#     for i in range(len(x)):
#         if(maxx< math.abs())


# policz bład na przedziale [a,b]: maxIwartosc funkcji - wartosc wielomianu wedlug newtona/lagrangeaI
# lub 1/N suma((wartosc funkcji - wartosc wielomianu...)^2)
