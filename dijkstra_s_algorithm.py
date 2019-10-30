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

        arrV = [999 for i in range(n)]
        arrM = []

        arrV[0] = 0
        arrM.append(0)
        while arrM:
            i = arrM.pop(0)
            arrE = [j for j in range(n) if arr[i][j]]
            for j in arrE:
                temp = arrV[j]
                arrV[j] = min(arrV[j], arrV[i] + arr[i][j])
                if arrV[j] < temp:
                    arrM.append(j)

        if arrV[node - 1] == 999:
            return "There is no path from start to the node %d." % node

        path = []
        i = node - 1
        while i:
            arrRevE = [j for j in range(n) if arr[j][i]]
            for j in arrRevE:
                if arrV[i] - arrV[j] == arr[j][i]:
                    path.append(str(i + 1))
                    i = j
                    break

        return (
            "The shortest path from the start to the node %d is 1 -> %s."
            "\nThe length of the path is %d."
            % (node, " -> ".join(path[::-1]), arrV[node - 1])
        )
