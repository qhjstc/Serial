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
    plt.plot(x, y1, color="red", linewidth=1.0, linestyle='--')
    plt.plot(x, y2)

    plt.xlim((-1, 2))
    plt.ylim((-2, 3))
    plt.xlabel("I am x")
    plt.ylabel("I am y")

    # change the x index
    new_ticks = np.linspace(-1, 2, 5)
    print(new_ticks)
    plt.xticks(new_ticks)
    plt.yticks([-2, -1.8, -1, 1.22, 3],
               [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ \alpha good\ \alpha$'])
    # r regular expression, $: Beautify font, '\': Escape character
    plt.show()


if __name__ == "__main__":
    main()
