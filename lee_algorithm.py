"""Implementation of Lee algorithm."""

from typing import List


def find_path(arr, start: tuple, end: tuple):
    """Find the shortest path in a grid from one point to another.

    :param arr: a grid representation
    :param start: a point, from which it is necessary to find a path
    :param end: a point, to which it is necessary to find a path

    Example of grid representation:
        # This is a barrier sign
        x = "#"
        field = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, x, x, x, x, x, x, 0],
            [0, x, 0, 0, 0, 0, x, 0],
            [0, x, 0, x, x, x, x, 0],
            [0, x, 0, 0, 0, 0, 0, 0],
            [0, x, x, x, x, x, x, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    """
    if not (is_fit(*start, arr) and is_fit(*end, arr)):
        raise IndexError("Check the start and end points coordinates.")

    wave_expansion(arr, start, end)

    backtrace(arr, start, end)


def wave_expansion(arr, start: tuple, end: tuple):
    """Expand wave in a grid from the start point to the end.

    :param arr: a grid representation
    :param start: a point, from which it is necessary to find a path
    :param end: a point, to which it is necessary to find a path
    """
    nexts = [start]

    while not arr[end[0]][end[1]] and nexts:
        currents = nexts
        nexts = []

        for current in currents:
            for x, y in get_neighbours(current):
                if (
                    is_fit(x, y, arr)
                    and not arr[x][y]
                    and arr[x][y] != "#"
                    and (x, y) != start
                ):
                    arr[x][y] = arr[current[0]][current[1]] + 1
                    nexts.append((x, y))

        if not nexts:
            raise Warning(
                "There is no path from the start to the end point!"
            )


def backtrace(arr, start: tuple, end: tuple):
    """Reconstruct the path in a grid from the end point to the start.

    :param arr: a grid representation
    :param start: a point, from which it is necessary to find a path
    :param end: a point, to which it is necessary to find a path
    """
    current = end
    while current != start:
        for x, y in get_neighbours(current):
            if (
                is_fit(x, y, arr)
                and arr[x][y] != "#"
                and arr[x][y] == arr[current[0]][current[1]] - 1
            ):
                arr[current[0]][current[1]] = "^"
                current = (x, y)

    for row in arr:
        for j in range(len(row)):
            if row[j] not in ["^", "#", 0]:
                row[j] = 0
    arr[start[0]][start[1]] = "A"
    arr[end[0]][end[1]] = "B"


def get_neighbours(cell: tuple) -> List[tuple]:
    """Search for cell's neighbours."""
    left = (cell[0], cell[1] - 1)
    right = (cell[0], cell[1] + 1)
    up = (cell[0] - 1, cell[1])
    down = (cell[0] + 1, cell[1])

    return [left, right, up, down]


def is_fit(x: int, y: int, arr) -> bool:
    """Determine if cell with x and y coordinates fits an array."""
    return 0 <= x < len(arr) and 0 <= y < len(arr[0])
