import random

from project_types import Limits, Point, ComparedPoints, Points


class MonteCarlo:
    def __init__(self, function: str, limits: Limits, n: int):
        self.__n = n
        self.__limits = limits
        self.__func = function

    def __check(self, point: Point) -> bool:
        x, y = point
        result = eval(self.__func)
        assert type(result) == bool, "Функция не возвращает булево значение"
        return result

    def __generate_point(self) -> Point:
        x = random.uniform(*self.__limits.x)
        y = random.uniform(*self.__limits.y)

        return Point(x, y)

    @property
    def compared_points(self) -> ComparedPoints:
        arr: ComparedPoints = [[], []]
        for _ in range(self.__n):
            point = self.__generate_point()
            arr[self.__check(point)].append(point)

        return arr

    @property
    def points(self) -> Points:
        a, b = self.compared_points
        return a + b
