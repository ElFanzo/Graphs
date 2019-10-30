class Dijkstra:
    """Class for calculating the shortest paths from the start to the other
    nodes in a graph.
    """

    @staticmethod
    def execute(arr, node: int) -> str:
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

        arrV = Dijkstra.get_markers(arr, n)

        if arrV[node - 1] == 999:
            return "There is no path from start to the node %d." % node

        path = Dijkstra.backtrace(arr, n, node, arrV)

        return (
            "The shortest path from the start to the node %d is 1 -> %s."
            "\nThe length of the path is %d."
            % (node, " -> ".join(path[::-1]), arrV[node - 1])
        )

    @staticmethod
    def get_markers(arr, n):
        """Get markers for each node of a graph.

        :param arr: an adjacency matrix
        :param n: the size of the adjacency matrix
        :return: a list of markers
        """
        arrV = [999 for i in range(n)]
        arrV[0] = 0
        arrM = [0]

        while arrM:
            i = arrM.pop(0)
            arrE = [j for j in range(n) if arr[i][j]]

            for j in arrE:
                temp = arrV[j]
                arrV[j] = min(arrV[j], arrV[i] + arr[i][j])

                if arrV[j] < temp:
                    arrM.append(j)

        return arrV

    @staticmethod
    def backtrace(arr, n, node, arrV):
        """Reconstruct a path in a graph from the specified node to the start.

        :param arr: an adjacency matrix
        :param n: the size of the adjacency matrix
        :param node: a node to which it is necessary to find a path
        :param arrV: a list of markers
        :return: the path
        """
        path = []
        i = node - 1

        while i:
            arrRevE = [j for j in range(n) if arr[j][i]]

            for j in arrRevE:
                if arrV[i] - arrV[j] == arr[j][i]:
                    path.append(str(i + 1))
                    i = j
                    break

        return path
