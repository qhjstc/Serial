"""
Test matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-3, 3, 50)
    y1 = 2 * x + 1
    y2 = x**2
    plt.figure()                  # creat the first figure
    plt.plot(x, y1)

    plt.figure(figsize=(8, 5))                  # creat the second figure
    plt.plot(x, y2, color="red", linewidth=1.0, linestyle='--')

    plt.show()

if __name__ == "__main__":
    main()
