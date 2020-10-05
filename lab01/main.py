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


def funct(x: float, y: float) -> float:
	return x*y**3 - 1


a: float = 0.0
b: float = 1.0
h_0: float = 0.5

if __name__ == "__main__":

	auto_pairs : List[Tuple[float, float]] = [(0.0, 0.0)]

	auto_pairs = at.get_pairs(auto_pairs, funct, a, b, h_0)

	print("VALUES:")
	for x, y in auto_pairs:
		print(f'x = {x}\t\ty = {y}')
