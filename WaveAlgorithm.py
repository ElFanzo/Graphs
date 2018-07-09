class WaveAlgorithm:
    """
    Class for calculating the shortest way in an oriented graph.
    """

    @staticmethod
    def calcShortestWay(arr, n):
        """
        :param arr: Adjacency matrix
        :param n: Length of adjacency matrix
        :return: Shortest way if it exists
        """
        arrV = [999 for i in range(n)]
        arrM = []
        arrMin = [[0 for i in range(n)] for j in range(n)]

        arrV[0] = 0
        arrM.append(0)
        while len(arrM) > 0:
            i = arrM.pop(0)
            arrE = [j for j in range(n) if not arr[i][j] == 0]
            for j in arrE:
                temp = arrV[j]
                arrV[j] = min(arrV[j], arrV[i] + arr[i][j])
                if arrV[j] < temp:
                    arrM.append(j)

        if arrV[n - 1] == 999:
            return 'There is no way'

        i = n - 1
        while not i == 0:
            arrRevE = [j for j in range(n) if not arr[j][i] == 0]
            for j in arrRevE:
                if arrV[i] - arrV[j] == arr[j][i]:
                    arrMin[j][i] = arr[j][i]
                    i = j
                    break

        s = 'Shortest way: 1'
        i = 0
        while not i == n - 1:
            j = 0
            while arrMin[i][j] == 0 and j < n:
                j += 1
            if not arrMin[i][j] == 0:
                s += ' -> ' + str(j + 1)
                i = j
        return "%s\nLength of the way = %d" % (s, arrV[n - 1])


if __name__ == '__main__':
    a = [
            [0, 2, 3, 5, 0, 0, 4, 0],
            [0, 0, 0, 0, 2, 0, 1, 0],
            [0, 0, 0, 0, 3, 4, 0, 0],
            [0, 0, 0, 0, 0, 4, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 4],
            [0 for i in range(8)]
        ]
    print(WaveAlgorithm.calcShortestWay(a, 8))