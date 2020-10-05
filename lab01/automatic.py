from typing import Callable, List, Tuple

# Automatic step
# h_0 = 0.5
#
# Variant 3 (Runge) // third
#
# e = 1e-3
#
# y_{i+1} = y_i + 1/6*(phi_0 + 4*phi_1 + phi_2)
# phi_0 = h * f(x_i, y_i)
# phi_1 = h * f(x_i + h/2, y_i + phi_0/2)
# phi_2 = h * f(x_i + h, y_i - phi_0 + 2*phi_1)
#

k: int = 3
eps_1: float = 1e-6
eps: float = 1e-3

def runge_kutte(x_i: float, y_i: float, f: Callable[[float, float], float], h: float) -> float:

    phi_0 = h * f(x_i, y_i)
    phi_1 = h * f(x_i + h/2, y_i + phi_0/2)
    phi_2 = h * f(x_i + h/2, y_i - phi_0 + 2*phi_1)

    return y_i + (phi_0 + 4*phi_1 + phi_2)/6


def get_auto_pairs(res_pairs: List[Tuple[float, float]], f: Callable[[float, float], float], a: float, b: float, h_0: float) -> List[Tuple[float, float]]:
    return main_flow(res_pairs, f, a, b, h_0)


def main_flow(res_pairs: List[Tuple[float, float]], f: Callable[[float, float], float], a: float, b: float, h_0: float) -> List[Tuple[float, float]]:

    (x_0, y_0) = res_pairs[-1]

    y_h2 = runge_kutte(x_0, y_0, f, h_0/2)
    y_h = runge_kutte(x_0 + h_0/2, y_h2, f, h_0/2)

    eps_h = (y_h2 - y_h) * 2**k/(2**k - 1)
    eps_h2 = (y_h2 - y_h)/(2**k - 1)

    if abs(eps_h2) > eps:
        h_0 /= 2
        main_flow(res_pairs, f, x_0, y_0, h_0)

    x_0 += h_0
    y_0 = y_h2 + eps_h2
    res_pairs.append((x_0, y_0))
    if b - x_0 <= eps_1:
        return res_pairs
    else:
        return main_flow(res_pairs, f, a, b, h_0)
