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


def get_stable_pairs(f: Callable[[float, float], float], x_0: float, y_0: float, a: float, b: float, h: float) -> List[Tuple[float, float]]:

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

    # x_i, i > 0
    def _recursive2(x_n: float, y_n: float, h_n: float) -> List[Tuple[float, float]]:

        if b - x_n <= eps_1:
            return res_pairs

        y_h2 = _runge(f, x_n, y_n, h_n/2)
        y_h  = _runge(f, x_n + h_n/2, y_h2, h_n/2)

        eps_h  = (y_h2 - y_h) * 2**k / (2**k - 1)
        eps_h2 = (y_h2 - y_h) / (2**k - 1)

        x_n += h_n
        y_n = y_h2 + eps_h2
        res_pairs.append((x_n, y_n))

        if abs(eps_h) <= eps:
            h_n *= 2

        print(f"[2] x_n = {x_n}, y_n = {y_n}, h_n = {h_n}")  
           
        return _recursive2(x_n, y_n, h_n)

    # x_0
    def _recursive1(x_n: float, y_n: float, h_n: float) -> List[Tuple[float, float]]:

        if b - x_n <= eps_1:
            return res_pairs

        y_h2 = _runge(f, x_n, y_n, h_n/2)
        y_h  = _runge(f, x_n + h_n/2, y_h2, h_n/2)

        eps_h  = (y_h2 - y_h) * 2**k / (2**k - 1)
        eps_h2 = (y_h2 - y_h) / (2**k - 1)

        if abs(eps_h2) > eps:
            return _recursive1(x_n, y_n, h_n / 2)
        else:
            x_n += h_n
            y_n = y_h2 + eps_h2
            res_pairs.append((x_n, y_n))

            print(f"[1] x_n = {x_n}, y_n = {y_n}, h_n = {h_n}")
                
            return _recursive2(x_n, y_n, h_n)

    return _recursive1(x_0, y_0, h_0)
