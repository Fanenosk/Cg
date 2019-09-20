import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QHBoxLayout, QVBoxLayout, QSizePolicy, QMessageBox, \
    QWidget, QPushButton, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

# Лукашкин К.В.


def smooth_spline(axes, x1, y1, x2, y2, x3, y3, X0, Y0, XN, YN):
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

    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    ax = axes
    ax.grid(True)

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

   # plt.show()


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.x1 = 0
        self.x2 = 2
        self.x3 = 3

        self.y1 = 0
        self.y2 = -1
        self.y3 = -1.5

        self.X0 = 0.1
        self.XN = 1
        self.Y0 = 1
        self.YN = 1


        self.setMinimumWidth(600)
        self.setMinimumHeight(600)

        # set layout
        main_widget = QWidget(self)
        main_layout = QHBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        # plot
        self.sc = PlotCanvas(main_widget)
        main_layout.addWidget(self.sc)
        # field for parameter
        input_param = QVBoxLayout()
        input_param.setAlignment(Qt.AlignTop)

 
        label = QtWidgets.QLabel("x1:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)
        text_field.setText(str(self.x1))
        text_field.textChanged.connect(self.change_x1)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        label = QtWidgets.QLabel("y1:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)
        text_field.setText(str(self.y1))
        text_field.textChanged.connect(self.change_y1)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        label = QtWidgets.QLabel("x2:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)
        text_field.setText(str(self.x2))
        text_field.textChanged.connect(self.change_x2)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        label = QtWidgets.QLabel("y2:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)
        text_field.setText(str(self.y2))
        text_field.textChanged.connect(self.change_y2)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        label = QtWidgets.QLabel("x3:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)        
        text_field.setText(str(self.x3))
        text_field.textChanged.connect(self.change_x3)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        label = QtWidgets.QLabel("y3:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)
        text_field.setText(str(self.y3))
        text_field.textChanged.connect(self.change_y3)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        label = QtWidgets.QLabel("X0:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)
        text_field.setText(str(self.X0))
        text_field.textChanged.connect(self.change_X0)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        label = QtWidgets.QLabel("Y0:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)        
        text_field.setText(str(self.Y0))
        text_field.textChanged.connect(self.change_Y0)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        label = QtWidgets.QLabel("XN:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)        
        text_field.setText(str(self.XN))
        text_field.textChanged.connect(self.change_XN)
        input_param.addWidget(label)
        input_param.addWidget(text_field)        
        label = QtWidgets.QLabel("YN:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)    
        text_field.setText(str(self.YN))
        text_field.textChanged.connect(self.change_YN)
        input_param.addWidget(label)
        input_param.addWidget(text_field)


        main_layout.addLayout(input_param)

    def change_x1(self, text):
        try:
            self.x1 = float(text)
        except ValueError:
            pass
        self.update()
    def change_y1(self, text):
        try:
            self.y1 = float(text)
        except ValueError:
            pass
        self.update()
    def change_x2(self, text):
        try:
            self.x2 = float(text)
        except ValueError:
            pass
        self.update()
    def change_y2(self, text):
        try:
            self.y2 = float(text)
        except ValueError:
            pass
        self.update()
    def change_x3(self, text):
        try:
            self.x3 = float(text)
        except ValueError:
            pass
        self.update()
    def change_y3(self, text):
        try:
            self.y3 = float(text)
        except ValueError:
            pass
        self.update()
    def change_X0(self, text):
        try:
            self.X0 = float(text)
        except ValueError:
            pass
        self.update()
    def change_Y0(self, text):
        try:
            self.Y0 = float(text)
        except ValueError:
            pass
        self.update()

    def change_XN(self, text):
        try:
            self.XN = float(text)
        except ValueError:
            pass
        self.update()
    def change_YN(self, text):
        try:
            self.YN = float(text)
        except ValueError:
            pass
        self.update()

    def update(self):
        self.sc.update_plot(self.x1, self.y1, self.x2, self.y2,
                            self.x3, self.y3, self.X0, self.Y0, self.XN, self.YN)
        self.sc.draw()


class PlotCanvas(FigureCanvas):
    # class for plot canvas

    def __init__(self, parent=None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.plot(0, 0, 2, -1, 3, -1.5, 0.1, 1, 1, 1)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.updateGeometry(self)

    def update_plot(self, x1, y1, x2, y2, x3, y3, X0, Y0, XN, YN):
        self.axes.cla()  # clear all data
        self.plot(x1, y1, x2, y2, x3, y3, X0, Y0, XN, YN)

    def plot(self,  x1, y1, x2, y2, x3, y3, X0, Y0, XN, YN):
        smooth_spline(self.axes, x1, y1, x2, y2, x3, y3, X0, Y0, XN, YN)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
