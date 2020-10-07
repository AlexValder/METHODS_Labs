from typing import Callable, Tuple, List, Dict


def more_precise_list(f: Callable[[float, float], float], x_0: float, y_0: float, x_end: float, h: float) -> List[Tuple[float, float]]:

    for_return : List[Tuple[float, float]] = [(x_0, y_0)]
  
    def _recursive(x_n: float, y_n: float) -> List[Tuple[float, float]]:

        k1 = h * f(x_n, y_n)
        k2 = h * f(x_n + h/2, y_n + k1/2)
        k3 = h * f(x_n + h/2, y_n + k2/2)
        k4 = h * f(x_n + h, y_n + k3)

        x_n += h
        y_n += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

        for_return.append((x_n, y_n))

        if x_n + h >= x_end:
            return for_return
        else:
            return _recursive(x_n, y_n)

    return _recursive(x_0, y_0)


def more_precise_value(f: Callable[[float, float], float], x_0: float, y_0: float, x: float, h: float) -> float:
    
    def _recursive(x_n: float, y_n: float) -> float:

        if x_n + h >= x:
            return y_n

        k1 = h * f(x_n, y_n)
        k2 = h * f(x_n + h/2, y_n + k1/2)
        k3 = h * f(x_n + h/2, y_n + k2/2)
        k4 = h * f(x_n + h, y_n + k3)

        x_n += h
        y_n += (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

        return _recursive(x_n, y_n)
            
    return _recursive(x_0, y_0)


if __name__ == "__main__":

    def fun(x: float, y: float) -> float:
        return x*y


    print(more_precise_value(fun, 0.0, 1.0, 1.0, 0.1))
