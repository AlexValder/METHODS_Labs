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
import methods as mth, graphics as gr, more_precise as mp


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
    xs_stable: List[float] = []
    ys_stable: List[float] = []

    auto_pairs = mth.get_auto_pairs(funct, x_0, y_0, a, b, h_0)
    stable_pairs = mth.get_stable_pairs(funct, x_0, y_0, a, b, .1)

    print(f"Кол-во пар при автоматическом: {len(auto_pairs)}")

    for x, y in auto_pairs:
        xs_auto.append(x)
        ys_auto.append(y)

    for x, y in stable_pairs:
        xs_stable.append(x)
        ys_stable.append(y)

    def f(x: float) -> float:
        return mp.more_precise_value(funct, x_0, y_0, x, (b - a)/len(auto_pairs))

    gr.print_table(auto_pairs, f)
    gr.draw_graph((xs_auto, ys_auto, "С авто шагом"), (xs_stable, ys_stable, "Со стаб. шагом"), (xs_auto, [f(x) for x in xs_auto], "Точное решение"))
