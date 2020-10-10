from prettytable import PrettyTable
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable

# Table: x_k, y(x_k), y_k, y(x_k) - y_k,

def print_table(pairs: List[Tuple[float, float]], f: Callable[[float, float], float]) -> None:
    t = PrettyTable(["X_k", "Y(X_k) (точное)", "Y_k (численное)", "Y(X_k) - Y_k (погрешность)"])
    for x, y in pairs:
        t.add_row([f'{x}', f'{f(x)}', f'{y}', f'{f(x) - y}'])
    print(t)


def draw_graph(*input_points: Tuple[List[float], List[float], str]) -> None:
    plt.figure(figsize=(12, 7))
    plt.grid(True)

    plt.plot(input_points[0][0], input_points[0][1], '-', label=input_points[0][2])
    for xy in input_points[1::]:
        plt.plot(xy[0], xy[1], 'o-', label=xy[2])
    plt.legend()
    plt.title("Сравнение решений")

    plt.show()
