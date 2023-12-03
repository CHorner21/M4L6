import matplotlib.pyplot as plt
import numpy as np

def plot_cubes(n):
    x = np.arange(1, n + 1)
    y = x ** 3

    plt.scatter(x, y, c=y, cmap='viridis', edgecolors='k')
    plt.title(f'Plot of the First {n} Cubic Numbers')
    plt.xlabel('Number')
    plt.ylabel('Cube')
    plt.colorbar(label='Cube Value')
    plt.grid(True)
    plt.show()

plot_cubes(5)

plot_cubes(5000)
