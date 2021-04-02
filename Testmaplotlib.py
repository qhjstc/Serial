"""
Test matplotlib
come from mofan python
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib import animation


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

    #############################################################################
    # plot annotation #
    # method 1 #
    plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points')

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(12)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

    #####################################################################
    # plot scatter
    # plt.figure()
    # n = 1024
    # x = np.random.normal(0, 1, n)
    # y = np.random.normal(0, 1, n)
    # t = np.arctan2(y, x)        # for color value
    # plt.scatter(x, y, s=75, c=t, alpha=0.5)
    # plt.xlim((-1.5, 1.5))
    # plt.ylim((-1.5, 1.5))
    # plt.xticks(())
    # plt.yticks(())
    #
    # plt.figure()
    # plt.scatter(np.arange(5), np.arange(5))

    #############################################################################
    # plot bar
    # plt.figure()
    # n = 12
    # x = np.arange(n)
    # y1 = (1 - x/float(n)) * np.random.uniform(0.5, 1.0, n)
    # y2 = (1 - x/float(n)) * np.random.uniform(0.5, 1.0, n)
    #
    # plt.bar(x, +y1, facecolor='#9999ff', edgecolor='white')
    # plt.bar(x, -y2, facecolor='#ff9999', edgecolor='white')
    #
    # for i, j in zip(x, y1):
    #     # ha: horizontal alignment
    #     plt.text(i, j + 0.05, '%.2f' % j, ha='center', va='bottom')
    #
    # for i, j in zip(x, y2):
    #     # ha: horizontal alignment
    #     plt.text(i, -j - 0.05, '-%.2f' % j, ha='center', va='top')
    #
    # plt.xlim(-.5, n)
    # plt.xticks(())
    # plt.ylim(-1.25, 1.25)
    # plt.yticks(())

    ################################################################
    # subplot example
    # plt.figure()
    # plt.subplot(2, 1, 1)
    # plt.plot([0, 1], [0, 1])
    #
    # plt.subplot(2, 3, 4)
    # plt.plot([0, 1], [0, 2])
    #
    # plt.subplot(2, 3, 5)
    # plt.plot([0, 1], [0, 3])
    #
    # plt.subplot(236)
    # plt.plot([0, 1], [0, 4])

    # other subplot methods. it is very useful!
    # method 1
    # plt.figure()
    # ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)  # regulate grid
    # ax1.plot([1, 2])
    # ax1.set_title('ax1 title')
    #
    # ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    #
    # ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    #
    # ax4 = plt.subplot2grid((3, 3), (2, 0))
    #
    # ax5 = plt.subplot2grid((3, 3), (2, 1))

    # method 2: gridspec
    # plt.figure()
    # gs = gridspec.GridSpec(3, 3)
    # ax1 = plt.subplot(gs[0, :])
    # ax2 = plt.subplot(gs[1, :2])
    # ax3 = plt.subplot(gs[1:, 2])
    # ax4 = plt.subplot(gs[-1, 0])
    # ax5 = plt.subplot(gs[-1, -2])

    # method 3
    # f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
    # ax11.scatter([1, 2], [2, 1])

    ##########################################################
    # plot second z
    # x = np.arange(0, 10, 0.1)
    # y1 = 0.05*x**2
    # y2 = -1 * y1
    #
    # fig, ax1 = plt.subplots()
    # ax2 = ax1.twinx()
    # ax1.plot(x, y1, 'g-')
    # ax2.plot(x, y2, 'b--')
    # ax1.set_xlabel('X data')
    # ax1.set_ylabel('Y data')
    # ax2.set_ylabel('Y data')

    ############################
    # animation
    # fig, ax = plt.subplots()
    #
    # x = np.arange(0, 2*np.pi, 0.01)
    # line, = ax.plot(x, np.sin(x))
    #
    # def animation_function(i):
    #     line.set_ydata(np.sin(x+i/10))
    #     return line,
    #
    # def init():
    #     line.set_ydata(np.sin(x))
    #     return line,
    #
    # ani = animation.FuncAnimation(fig=fig, func=animation_function, frames=100, init_func=init, interval=20, blit=True)  # blit = True 只更新变化的点

    plt.show()


if __name__ == "__main__":
    main()
