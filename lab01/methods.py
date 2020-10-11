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


def _runge(f: Callable[[float, float], float], x_i: float, y_i: float, h: float) -> float:

    phi_0 = h * f(x_i, y_i)
    phi_1 = h * f(x_i + h/2, y_i + phi_0/2)
    phi_2 = h * f(x_i + h/2, y_i - phi_0 + 2*phi_1)

    return (phi_0 + 4*phi_1 + phi_2)/6


def get_stable_pairs(f: Callable[[float, float], float], x_0: float, y_0: float, a: float, b: float, N: int) -> List[Tuple[float, float]]:

    h = (b - a) / N
    res_pairs: List[Tuple[float, float]] = [(x_0, y_0)]

    def _recursive(x_n: float, y_n: float) -> List[Tuple[float, float]]:

        if b - x_n <= eps_1:
            return res_pairs

        y_n += _runge(f, x_n, y_n, h)
        x_n += h

        res_pairs.append((x_n, y_n))

        return _recursive(x_n, y_n)

    return _recursive(x_0, y_0)


def get_auto_pairs(f: Callable[[float, float], float], x_0: float, y_0: float, a: float, b: float, h_0: float) -> List[Tuple[float, float]]:

    res_pairs: List[Tuple[float, float]] = [(x_0, y_0)]

    x_n = x_0; y_n = y_0; h_n = h_0; h_n2 = h_0 / 2

    #i = 0

    def _recursive(x_n: float, y_n: float, h_n: float, h_n2: float):
#    while abs(b - x_n) > eps_1:

        if b - x_n < eps:
            return res_pairs
        elif abs(b - x_n) < h_n:
            h_n = abs(b - x_n)

        #i += 1
        #if i > 112:
        #    print(len(res_pairs))
        #    print(res_pairs[-1])
        #    exit()

        step_full = y_n + _runge(f, x_n, y_n, h_n)
        step_half = y_n + _runge(f, x_n + h_n2, y_n + _runge(f, x_n, y_n, h_n2), h_n2)

        eps_full = abs((step_full - step_half) * 2**k / (2**k - 1))
        eps_half = abs((step_full - step_half) / (2**k - 1))

        if eps_half > eps:
            h_n = h_n2
            h_n2 /= 2
            return _recursive(x_n, y_n, h_n, h_n2)

        x_n += h_n
        y_n = step_full

        res_pairs.append((x_n, y_n))

        if eps_full <= eps:
            h_n2 = h_n
            h_n *= 2

        return _recursive(x_n, y_n, h_n, h_n2)
        
    return _recursive(x_n, y_n, h_n, h_n2)
