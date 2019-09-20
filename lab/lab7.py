import numpy as np
import matplotlib.pyplot as plt


def smooth_spline(x1, y1, x2, y2, x3, y3, X0, Y0, XN, YN):
    matrix = np.matrix([
        [3, 2, 1, 0, 0, 0, -1, 0],
        [6, 2, 0, 0, 0, -2, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 2, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],

    ])

    X0 = 0.1
    XN = 1
    x1 = 0
    x2 = 2
    x3 = 3

    Y0 = 1
    YN = 1
    y1 = 0
    y2 = -1
    y3 = -1.5

    bx = np.array([
        0,
        0,
        X0,
        XN,
        x1,
        x2,
        x2,
        x3
    ])

    by = np.array([
        0,
        0,
        Y0,
        YN,
        y1,
        y2,
        y2,
        y3
    ])

    coeffx = np.linalg.solve(matrix, bx)
    fx1 = lambda t: coeffx[0] * (t**3) + coeffx[1] * \
        (t**2) + coeffx[2] * t + coeffx[3]
    fx2 = lambda t: coeffx[4] * (t**3) + coeffx[5] * \
        (t**2) + coeffx[6] * t + coeffx[7]

    coeffy = np.linalg.solve(matrix, by)
    fy1 = lambda t: coeffy[0] * (t**3) + coeffy[1] * \
        (t**2) + coeffy[2] * t + coeffy[3]
    fy2 = lambda t: coeffy[4] * (t**3) + coeffy[5] * \
        (t**2) + coeffy[6] * t + coeffy[7]

    t = np.linspace(0, 1, 101)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid(True)

    # два сплайна
    ax.plot(fx1(t), fy1(t))
    ax.plot(fx2(t), fy2(t))

    # касательные
    ax.plot([x1, X0 + x1], [y1, Y0 + y1], 'r-')
    ax.plot([x3, XN + x3], [y3, YN + y3], 'r-')

    # точки
    ax.plot(x1, y1, 'k.')
    ax.plot(x2, y2, 'k.')
    ax.plot(x3, y3, 'k.')

    plt.show()
smooth_spline(0,0,0,0,0,0,0,0,0,0)