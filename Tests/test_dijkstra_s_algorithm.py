from unittest import TestCase, main
from dijkstra_s_algorithm import Dijkstra


class TestDijkstra(TestCase):
    def test_execute(self):
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
        self.assertEqual(
            Dijkstra.execute(arr, 8),
            "The shortest path from the start to the node 8 is "
            "1 -> 2 -> 7 -> 8.\nThe length of the path is 7.",
        )
        self.assertEqual(
            Dijkstra.execute(arr, 7),
            "The shortest path from the start to the node 7 is 1 -> 2 -> 7."
            "\nThe length of the path is 3.",
        )
        self.assertEqual(Dijkstra.execute(arr, 0), "The node is incorrect!")
        self.assertEqual(Dijkstra.execute(arr, 9), "The node is incorrect!")

        arr = [
            [0, 4, 2, 0, 0, 0],
            [0, 0, 5, 10, 0, 0],
            [0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 11],
            [0, 0, 0, 4, 0, 0],
            [0 for i in range(6)]
        ]
        self.assertEqual(
            Dijkstra.execute(arr, 6),
            "The shortest path from the start to the node 6 is "
            "1 -> 3 -> 5 -> 4 -> 6.\nThe length of the path is 20.",
        )

        arr = [
            [0, 1, 3, 4, 0, 9],
            [0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 2, 5],
            [0, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 0, 2],
            [0 for i in range(6)]
        ]
        self.assertEqual(
            Dijkstra.execute(arr, 6),
            "The shortest path from the start to the node 6 is 1 -> 4 -> 6."
            "\nThe length of the path is 7.",
        )

        arr = [
            [0, 6],
            [0, 0]
        ]
        self.assertEqual(
            Dijkstra.execute(arr, 2),
            "The shortest path from the start to the node 2 is 1 -> 2."
            "\nThe length of the path is 6.",
        )

        arr = [
            [0, 4, 2, 0, 0, 0],
            [0, 0, 5, 10, 0, 0],
            [0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 11],
            [0, 0, 0, 4, 0, 0]
        ]
        self.assertEqual(
            Dijkstra.execute(arr, 5), "The adjacency matrix is incorrect!"
        )

        arr = [
            [0, 6, 0],
            [6, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(
            Dijkstra.execute(arr, 3),
            "There is no path from start to the node 3."
        )

    @staticmethod
    def run_test():
        main()
