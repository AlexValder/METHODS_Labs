from prettytable import PrettyTable
from typing import List, Tuple, Callable


# Table: x_k, y(x_k), y_k, y(x_k) - y_k,

def print_table(pairs: List[Tuple[float, float]], f: Callable[[float, float], float]) -> None:
    t = PrettyTable(["X_k", "Y(X_k)", "Y_k", "Y(X_k) - Y_k"])
    for x, y in pairs:
        t.add_row([f'{x}', f'{y}', f'{f(x)}', f'{y - f(x)}'])
    print(t)
