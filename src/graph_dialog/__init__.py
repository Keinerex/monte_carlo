from PyQt6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT


class GraphDialog(QtWidgets.QDialog):
    def __init__(self, figure, title: str):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        self.setWindowTitle(title)

        canvas = FigureCanvasQTAgg(figure)
        toolbar = NavigationToolbar2QT(canvas, self)

        layout.addWidget(toolbar)
        layout.addWidget(canvas)

        self.setLayout(layout)
