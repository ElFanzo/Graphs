class Dijkstra:
    """Class for implementing Dijkstra's algorithm.

    It calculates the shortest paths from the start to another nodes
    in a graph.
    """

    @staticmethod
    def get_path(arr, node: int) -> str:
        """Execute Dijkstra's algorithm for a graph.

        :param arr: an adjacency matrix
        :param node: a node to which it is necessary to find a path
        :return: the shortest path to a node
        """
        n = len(arr)
        for subarr in arr:
            if len(subarr) != n:
                return "The adjacency matrix is incorrect!"

        node = int(node)
        if node < 2 or node > n:
            return "The node is incorrect!"

        arr_v = Dijkstra.get_markers(arr, n)

        if arr_v[node - 1] == 999:
            return "There is no path from start to the node %d." % node

        path = Dijkstra.backtrace(arr, n, node, arr_v)

        return (
            "The shortest path from the start to the node %d is 1 -> %s."
            "\nThe length of the path is %d."
            % (node, " -> ".join(path[::-1]), arr_v[node - 1])
        )

    @staticmethod
    def get_markers(arr, n):
        """Get markers for each node of a graph.

        :param arr: an adjacency matrix
        :param n: the size of the adjacency matrix
        :return: a list of markers
        """
        arr_v = [999 for i in range(n)]
        arr_v[0] = 0
        arr_m = [0]

        while arr_m:
            i = arr_m.pop(0)
            arr_e = [j for j in range(n) if arr[i][j]]

            for j in arr_e:
                temp = arr_v[j]
                arr_v[j] = min(arr_v[j], arr_v[i] + arr[i][j])

                if arr_v[j] < temp:
                    arr_m.append(j)

        return arr_v

    @staticmethod
    def backtrace(arr, n, node, arr_v):
        """Reconstruct a path in a graph from the specified node to the start.

        :param arr: an adjacency matrix
        :param n: the size of the adjacency matrix
        :param node: a node to which it is necessary to find a path
        :param arr_v: a list of markers
        :return: the path
        """
        path = []
        i = node - 1

        while i:
            arr_rev_e = [j for j in range(n) if arr[j][i]]

            for j in arr_rev_e:
                if arr_v[i] - arr_v[j] == arr[j][i]:
                    path.append(str(i + 1))
                    i = j
                    break

        return path
