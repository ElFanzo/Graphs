class Algorithm:
    """
    Class for calculating the shortest path from the start to the end.
    """

    @staticmethod
    def route(arr, start: tuple, end: tuple):
        """
        :param arr: a grid representation
        :param start: a dot from which it is necessary to find a path
        :param end: a dot to which it is necessary to find a path
        :return:
        """
        height = len(arr)
        width = len(arr[0])
        
        Algorithm.wave_expansion(arr, start, end, height, width)
        Algorithm.backtrace(arr, start, end, height, width)

    @staticmethod
    def wave_expansion(arr, start: tuple, end: tuple, height, width):
        currents = []
        nexts = [start]

        while not arr[end[0]][end[1]] and nexts:
            currents = nexts
            nexts = []
            for current in currents:
                left = (current[0], current[1] - 1)
                right = (current[0], current[1] + 1)
                up = (current[0] - 1, current[1])
                down = (current[0] + 1, current[1])
                neighbours = [left, right, up, down]
                for x, y in neighbours:
                    if 0 <= x and x < height and 0 <= y and y < width \
                       and not arr[x][y] and arr[x][y] != "#" and (x, y) != start:
                        arr[x][y] = arr[current[0]][current[1]] + 1
                        nexts.append((x, y))

    @staticmethod
    def backtrace(arr, start: tuple, end: tuple, height, width):
        current = end
        while current != start:
            left = (current[0], current[1] - 1)
            right = (current[0], current[1] + 1)
            up = (current[0] - 1, current[1])
            down = (current[0] + 1, current[1])
            neighbours = [left, right, up, down]
            for x, y in neighbours:
                if 0 <= x and x < height and 0 <= y and y < width \
                   and arr[x][y] != "#" and arr[x][y] == arr[current[0]][current[1]] - 1:
                    arr[current[0]][current[1]] = "x"
                    current = (x, y)


if __name__ == "__main__":
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

    Algorithm.route(field, (2, 5), (7, 6))

    for j in field:
        print(" ".join(str(i) for i in j))
