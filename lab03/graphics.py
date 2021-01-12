from prettytable import PrettyTable
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable


def draw_graph(*input_points: Tuple[List[float], List[float], List[float], str]) -> None:
    
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.grid(True)

    for graph in input_points:
        ax.plot(graph[0], graph[1], graph[2], zdir = 'z', label=graph[3])

    plt.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('T')
    ax.set_zlabel('u(x,t)')

    plt.show()


if __name__ == "__main__":
    xs = [float(x) for x in range(20)]
    ys = [float(y) for y in range(10, 30)]
    zs = [float(x * y) for x, y in zip(xs, ys)]

    print(xs)
    print(ys)
    print(zs)

    draw_graph((xs, ys, zs, ":p"))