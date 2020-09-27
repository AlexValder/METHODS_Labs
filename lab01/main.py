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
# Variant 3
#
# e = 1e-3
#
# y_{i+1} = y_i + 1/6*(phi_0 + 4*phi_1 + phi_2)
# phi_0 = h * f(x_i, y_i)
# phi_1 = h * f(x_i + h/2, y_i + phi_0/2)
# phi_2 = h * f(x_i + h, y_i - phi_0 + 2*phi_1)
#

import numpy as np
from typing import Callable


def get_next(x_i: float, y_i: float, f: Callable[[float, float], float] , step: float = 0.5) -> float:
	def phi_0() -> float:
		return step * f(x_i, y_i)

	def phi_1() -> float:
		return step * f(x_i + step/3, y_i + phi_0()/3)

	def phi_2() -> float:
		return step * f(x_i + 2*step/3, y_i + 2*phi_1()/3)
		
	return y_i + 0.25 * (phi_0() + 3 * phi_2())


def funct(x: float, y: float) -> float:
	return x*y**3 - 1


x_0: float = 0.0
y_0: float = 0.0


if __name__ == "__main__":
	print("Heyy!")

	step = 0.05

	for i in np.arange(0.0, 1.0, step):
		print(f"f({x_0}, {y_0}) = {get_next(x_0, y_0, funct, step)}")
		x_0 += step
		y_0 += step
