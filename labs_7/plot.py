import matplotlib.pyplot as plt

def create_plot(x, y1, y2, title):
    plt.title(title)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.grid(True)
    plt.show()

