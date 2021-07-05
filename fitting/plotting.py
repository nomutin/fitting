import matplotlib.pyplot as plt
import numpy as np


def plot(data: list, mode: list, param: dict, graph_range: int = 0, graph: bool = False):
    graph_range = len(data) if graph_range < len(data) else graph_range
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1,)
    ax.scatter([i for i, _ in enumerate(data)], data, s=10, c='k')

    t = np.linspace(0, graph_range, graph_range * 10)
    for m in mode:
        y = [param[m]['y'](x_) for x_ in t]
        plt.plot(t, y, label=m)
        print(f'{m}({param[m]["success"]}): {param[m]["equ"]}')

    if graph:
        plt.legend()
        plt.grid()
        plt.show()

