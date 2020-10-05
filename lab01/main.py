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
import graphics as gr


def funct(x: float, y: float) -> float:
	return x*y**3 - 1


x_0: float = 0.0
y_0: float = 0.0
a: float = 0.0
b: float = 1.0
h_0: float = 0.5

if __name__ == "__main__":

	auto_pairs : List[Tuple[float, float]] = [(x_0, y_0)]

	auto_pairs = at.get_pairs(auto_pairs, funct, a, b, h_0)

	gr.print_table(auto_pairs, funct)
