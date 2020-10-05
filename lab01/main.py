#
# y'(x) = f(x, y(x)),  x є [a, b] = [0, 1]
# y(x_0) = y_0
#
# h_0 = 0.5
# e_1 = 1e-6
#
# Variant 9
#
# f(x, y) = xy^3 - 1
# x_0 = 0
# y_0 = 0
#

import numpy as np
from typing import Callable, List, Tuple
import automatic as at
import manual as mn
import graphics as gr


def lagrange(xs: List[float], ys: List[float], x: float) -> float:
    return sum(np.product([(x - xs[j])/(xs[i] - xs[j]) for j in range(len(xs)) if i != j]) * ys[i] for i in range(len(xs)))


def funct(x: float, y: float) -> float:
    return x*y**3 - 1


x_0: float = 0.0
y_0: float = 0.0
a: float = 0.0
b: float = 1.0
h_0: float = 0.5


if __name__ == "__main__":

    auto_pairs : List[Tuple[float, float]] = [(x_0, y_0)]
    manual_pairs : List[Tuple[float, float]] = [(x_0, y_0)]

    xs_auto: List[float] = []
    ys_auto: List[float] = []

    auto_pairs = at.get_auto_pairs(auto_pairs, funct, a, b, h_0)
    #manual_pairs = mn.get_stable_pairs(f, len(auto_pairs), a, b)

    for x, y in auto_pairs:
        xs_auto.append(x)
        ys_auto.append(y)

    def f(x: float) -> float:
        return lagrange(xs_auto, ys_auto, x)

    gr.print_table(auto_pairs, f)
