import matplotlib.pyplot as plt


def data_point_plot(data: list):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1,)
    ax.scatter(data[0], data[1], s=10, c='k')
    plt.show()
