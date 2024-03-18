import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from interpolacja_lagrange import lagrange_interpolation_func
from interpolacja_newton import newton_interpolation_func

def data_plot(xs, ys, label='', plot_type='line'):
    plt.xlabel('x')
    plt.ylabel('y')
    if plot_type == 'scatter':
        plt.scatter(xs, ys)
    else:
        plt.plot(xs, ys)
    if label: plt.legend(loc="best")


# def func_plot(fn, a, b, n, label=''):
#     plt.xlabel('x')
#     plt.ylabel('y')
#     xs = np.linspace(a, b, num=n)
#     ys = [fn(xi) for xi in xs]
#     plt.plot(xs, ys, label=label)
#     if label: plt.legend(loc="best")
def func_plot(fn, a, b, n, label='', color='', figsize=(6, 4), subplot=None):
    if subplot is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        ax = subplot
    xs = np.linspace(a, b, num=n)
    ys = [fn(xi) for xi in xs]
    if color:
        ax.plot(xs, ys, label=label, color=color)
    else:
        ax.plot(xs, ys, label=label)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    if label:
        ax.legend(loc="best")
    # if subplot is None:
    #     plt.show()


def chebyshev_nodes(a, b, n):
    x = []
    for i in range(1, n + 1):
        x.append(0.5 * (a + b) + 0.5 * (b - a) * np.cos((2 * i - 1) / (2 * n) * np.pi))
    return x


def newton_symbol(n, k):
    m = 1
    if (n < 0):
        n = k - n - 1
        m = (-1) ** k
    result = 1
    for i in range(k):
        result *= (n - i)
    result /= math.factorial(k)
    return m * result


def max_absolute_error(f, W, xs):
    return max([abs(f(x) - W(x)) for x in xs])


def mse(f, W, xs):
    return sum([(f(x) - W(x)) ^ 2 for x in xs]) / len(xs)

def create_compare_errors_table(lagrange_errors, newton_errors):
    data = {"Interpolacja Lagrange'a":lagrange_errors, "Interpolacja Newtona":newton_errors}
    df = pd.DataFrame(data, index=["Błąd bezwzględny", "Błąd średniokwadratowy"])
    return df



def interpolation_analysis(f, a, b, n):
    points = 1000;
    xs = np.linspace(a,b, points)
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    L_W_linspace = lagrange_interpolation_func(f,a,b,n, ax=axs[0])
    L_W_chebyshev = lagrange_interpolation_func(f,a,b,n, chebyshev=True, ax=axs[1])
    N_W_linspace = newton_interpolation_func(f,a,b,n, ax=axs[0])
    N_W_chebyshev = newton_interpolation_func(f,a,b,n, chebyshev=True, ax=axs[1])

    L_W_linspace_errors = [max_absolute_error(f, L_W_linspace ,xs), mse(f,L_W_linspace ,xs)]
    N_W_linspace_errors = [max_absolute_error(f, N_W_linspace,xs), mse(f,N_W_linspace ,xs)]

    L_W_chebyshev_errors = [max_absolute_error(f,L_W_chebyshev, xs), mse(f,L_W_chebyshev, xs)]
    N_W_chebyshev_errors  = [max_absolute_error(f,N_W_chebyshev, xs), mse(f,N_W_chebyshev, xs)]

    create_compare_errors_table(L_W_linspace_errors, N_W_linspace_errors)
    create_compare_errors_table(L_W_chebyshev_errors, N_W_chebyshev_errors)
    func_plot(f, a, b, points , label='f', subplot=axs[0])
    func_plot(L_W_linspace, a, b, points , label='Lagrange', subplot=axs[0])
    func_plot(N_W_linspace, a, b, points , label='Newton', subplot=axs[0])
    func_plot(f, a, b, points, label='f', subplot=axs[1])
    func_plot(L_W_chebyshev, a, b, points , label='Lagrange',
              subplot=axs[1])
    func_plot(N_W_chebyshev, a, b, points , label='Newton', subplot=axs[1])
    plt.show()

def find_best_polynomial(f, n_max, chebyshev=False):
    a = -4 * math.pi
    b = 3 * math.pi
    points = 1000
    xs = np.linspace(a,b, points)
    lagrange_best_n = 2
    lagrange_min_mse = float('inf')
    newton_best_n = 2
    newton_min_mse = float('inf')
    for n in range(2, n_max+1):
        L_W = lagrange_interpolation_func(f, a, b, n, chebyshev=chebyshev)
        N_W = newton_interpolation_func(f, a, b, n, chebyshev=chebyshev)
        lagrange_mse = mse(f, L_W, xs)
        newton_mse = mse(f, N_W, xs)
        if lagrange_mse < lagrange_min_mse:
            lagrange_min_mse = lagrange_mse
            lagrange_best_n = n
        if newton_mse < newton_min_mse:
            newton_min_mse = newton_mse
            newton_best_n = n

    return (lagrange_best_n, newton_best_n)


