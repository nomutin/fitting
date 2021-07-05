import matplotlib.pyplot as plt


class Plot:
    def __init__(self, data: list, mode: list, graph_range: int = 0):
        self.modes = mode
        self.graph_range = len(data) if graph_range < len(data) else graph_range

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1,)
        self.ax.scatter([i for i, _ in enumerate(data)], data, s=10, c='k')

        plt.show()

