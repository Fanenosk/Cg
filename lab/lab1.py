import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QHBoxLayout, QVBoxLayout, QSizePolicy, QMessageBox, \
    QWidget, QPushButton, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np



class App(QMainWindow):

    def __init__(self):
        super().__init__()
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
        label = QtWidgets.QLabel("a:")
        text_field = QtWidgets.QLineEdit(self)
        text_field.setFixedWidth(120)
        text_field.textChanged.connect(self.update)
        input_param.addWidget(label)
        input_param.addWidget(text_field)
        main_layout.addLayout(input_param)

    def update(self, text):
        try:
            # check input value
            value = float(text)
        except ValueError:
            value = 1
        if value <= 0:
            value = 1
        self.sc.update_plot(value)
        self.sc.draw()


class PlotCanvas(FigureCanvas):
    # class for plot canvas
    def __init__(self, parent=None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)  # , projection='polar')
        self.plot(1)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.updateGeometry(self)

    def update_plot(self, a):
        self.axes.cla()  # clear all data
        self.plot(a)

    def plot(self, a):
        phi = np.arange(0, 2 * np.pi, 0.001, )
        x = a * (np.cos(phi) ** 3)
        y = a * (np.sin(phi) ** 3)
        self.axes.set_aspect('equal')  # preserve aspect
        self.axes.set_title(r'$x=a*cos^3(\varphi), y=a*sin^3(\varphi)$')
        self.axes.grid(True)
        self.axes.plot(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
