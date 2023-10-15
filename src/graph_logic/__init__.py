import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from graph_dialog import GraphDialog
from project_types import ComparedPoints, Limits


class Logic:
    __ax: Axes
    __marker_size = 5

    def __init__(self, points: ComparedPoints, limits: Limits, func: str):
        self.__outside_points, self.__inside_points = points
        self.__limits = limits
        self.__fig, self.__ax = plt.subplots()
        self.__func = func

    @property
    def container_area(self):
        (x0, x1), (y0, y1) = self.__limits

        return abs(x0 - x1) * abs(y0 - y1)

    @property
    def area(self):
        inside_length = len(self.__inside_points)
        outside_length = len(self.__outside_points)

        return self.container_area * inside_length / (
                inside_length + outside_length)

    def __setup_graphic(self, title: str):
        self.__ax.set_title(title)
        self.__ax.set_xlabel("x", loc="right")
        self.__ax.set_ylabel("y", loc="top", rotation=0)

        container_area = f"S = {round(self.container_area, 3)}"
        area = f"S = {round(self.area, 3)}"

        container_patch = patches.Patch(color="gray", label=container_area)
        area_patch = patches.Patch(color="green", label=area)

        self.__ax.legend()
        self.__fig.legend(handles=[container_patch, area_patch],
                          loc="outside upper right")

    def draw(self):
        self.__ax.plot(*list(zip(*self.__inside_points)),
                       "go",
                       label="Точки графика",
                       markersize=self.__marker_size)

        self.__ax.plot(*list(zip(*self.__outside_points)),
                       "ro",
                       label="Точки вне графика",
                       markersize=self.__marker_size)

        title = f"График функции {self.__func}"
        self.__setup_graphic(title)

        w = GraphDialog(self.__fig, title)
        w.exec()
