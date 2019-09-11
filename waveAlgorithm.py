class WaveAlgorithm:
    """
    Class for calculating the shortest way in an oriented planar graph.
    """

    @staticmethod
    def calcShortestWay(arr):
        """
        :param arr: Adjacency matrix
        :return: The shortest way, if it exists
        """
        n = len(arr)
        for subarr in arr:
            if len(subarr) != n:
                return 'The adjacency matrix is not correct!'
        
        arrV = [999 for i in range(n)]
        arrM = []
        arrMin = [[0 for i in range(n)] for j in range(n)]

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

        if arrV[n - 1] == 999:
            return 'There is no way'

        i = n - 1
        while i:
            arrRevE = [j for j in range(n) if arr[j][i]]
            for j in arrRevE:
                if arrV[i] - arrV[j] == arr[j][i]:
                    arrMin[j][i] = arr[j][i]
                    i = j
                    break

        s = 'The shortest way: 1'
        i = 0
        while i != n - 1:
            j = 0
            while not arrMin[i][j] and j < n:
                j += 1
            if arrMin[i][j]:
                s += ' -> ' + str(j + 1)
                i = j
        return "%s\nLength of the way = %d" % (s, arrV[n - 1])
