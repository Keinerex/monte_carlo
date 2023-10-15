import typing

Point = typing.NamedTuple("Point", [("x", float), ("y", float)])

Points = typing.List[Point]

ComparedPoints = typing.List[Points]

MinMax = typing.NamedTuple("MinMax", [("min", float), ("max", float)])

Limits = typing.NamedTuple("Limits", [("x", MinMax), ("y", MinMax)])

SubmitCallback = typing.Callable[[str, Limits, int], None]
