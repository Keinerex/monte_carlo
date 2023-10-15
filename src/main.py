import sys

from PyQt6 import QtWidgets

from graph_logic import Logic
from model import MonteCarlo
from ui import InputWindow


def handle_submit(func, limits, n):
    model = MonteCarlo(func, limits, n)

    logic = Logic(model.compared_points, limits, func)

    logic.draw()


def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = InputWindow(widget, handle_submit)
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
