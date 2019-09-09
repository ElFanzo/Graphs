from unittest import TestCase, main
from waveAlgorithm import WaveAlgorithm


class TestAlgorithm(TestCase):

    def test_calcShortestWay(self):
        arr = [
            [0, 2, 3, 5, 0, 0, 4, 0],
            [0, 0, 0, 0, 2, 0, 1, 0],
            [0, 0, 0, 0, 3, 4, 0, 0],
            [0, 0, 0, 0, 0, 4, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 4],
            [0 for i in range(8)]
        ]
        self.assertEqual(WaveAlgorithm.calcShortestWay(arr), 'The shortest way: 1 -> 2 -> 7 -> 8'
                         '\nLength of the way = 7')

        arr = [
            [0, 4, 2, 0, 0, 0],
            [0, 0, 5, 10, 0, 0],
            [0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 11],
            [0, 0, 0, 4, 0, 0],
            [0 for i in range(6)]
        ]
        self.assertEqual(WaveAlgorithm.calcShortestWay(arr), 'The shortest way: 1 -> 3 -> 5 -> 4 -> 6'
                         '\nLength of the way = 20')

        arr = [
            [0, 1, 3, 4, 0, 9],
            [0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 2, 5],
            [0, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 0, 2],
            [0 for i in range(6)]
        ]
        self.assertEqual(WaveAlgorithm.calcShortestWay(arr), 'The shortest way: 1 -> 4 -> 6'
                         '\nLength of the way = 7')

        arr = [
            [0, 6],
            [0, 0]
        ]
        self.assertEqual(WaveAlgorithm.calcShortestWay(arr), 'The shortest way: 1 -> 2'
                         '\nLength of the way = 6')

        arr = [
            [0, 4, 2, 0, 0, 0],
            [0, 0, 5, 10, 0, 0],
            [0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 11],
            [0, 0, 0, 4, 0, 0],
        ]
        self.assertEqual(WaveAlgorithm.calcShortestWay(arr), 'The adjacency matrix is not correct!')

    
if __name__ == '__main__':
    main()
