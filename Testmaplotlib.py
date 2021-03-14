"""
Test matplotlib
come from mofan python
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
    l1, = plt.plot(x, y1, color="red", linewidth=1.0, linestyle='--', label='down')
    l2, = plt.plot(x, y2, label='up')

    plt.xlim((-1, 2))
    plt.ylim((-2, 5))
    plt.xlabel("I am x")
    plt.ylabel("I am y")

    # change the x index
    new_ticks = np.linspace(-1, 2, 5)
    print(new_ticks)
    plt.xticks(new_ticks)
    plt.yticks([-2, -1.8, -1, 1.22, 3],
               [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ \alpha good\ \alpha$'])
    # r regular expression, $: Beautify font, '\': Escape character
    # gca: get current axis
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best')

    x0 = 1
    y0 = 2*x0 + 1
    plt.scatter(x0, y0, color='b')             # plot some point
    plt.plot([x0, x0], [y0, 0], 'k--')

    # plot annotation #
    # method 1 #
    plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points')

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(12)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

    plt.show()


if __name__ == "__main__":
    main()
