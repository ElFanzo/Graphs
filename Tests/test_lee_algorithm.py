from unittest import main, TestCase

from lee_algorithm import Algorithm


class TestAlgorithm(TestCase):
    def test_execute(self):
        x = "#"
        A = "A"
        B = "B"
        t = "^"

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

        Algorithm.execute(field, (2, 5), (7, 6))

        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, x, x, x, x, x, x, 0],
            [0, x, t, t, t, A, x, 0],
            [0, x, t, x, x, x, x, 0],
            [0, x, t, t, t, t, t, t],
            [0, x, x, x, x, x, x, t],
            [0, 0, 0, 0, 0, 0, 0, t],
            [0, 0, 0, 0, 0, 0, B, t],
        ]

        self.assertListEqual(field, expected)

        field = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, x, 0, 0, 0],
            [0, 0, 0, x, 0, 0, 0],
            [0, 0, 0, x, 0, 0, 0],
            [0, 0, 0, x, 0, 0, 0],
            [0, 0, 0, x, 0, 0, 0],
        ]

        Algorithm.execute(field, (6, 1), (6, 5))

        expected = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, t, t, t, t, 0, 0],
            [0, t, 0, x, t, 0, 0],
            [0, t, 0, x, t, 0, 0],
            [0, t, 0, x, t, 0, 0],
            [0, t, 0, x, t, 0, 0],
            [0, A, 0, x, t, B, 0],
        ]

        self.assertListEqual(field, expected)

        field = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        Algorithm.execute(field, (0, 0), (5, 5))

        expected = [
            [A, 0, 0, 0, 0, 0],
            [t, 0, 0, 0, 0, 0],
            [t, 0, 0, 0, 0, 0],
            [t, 0, 0, 0, 0, 0],
            [t, 0, 0, 0, 0, 0],
            [t, t, t, t, t, B],
        ]

        self.assertListEqual(field, expected)

        field = [
            [0, 0, 0, 0, 0],
            [x, x, 0, 0, 0],
            [0, x, x, 0, 0],
            [0, 0, x, x, 0],
            [x, 0, 0, x, 0],
            [x, x, 0, 0, 0],
            [0, x, x, 0, 0],
        ]

        Algorithm.execute(field, (2, 0), (0, 0))

        expected = [
            [B, t, t, t, t],
            [x, x, 0, 0, t],
            [A, x, x, 0, t],
            [t, t, x, x, t],
            [x, t, t, x, t],
            [x, x, t, t, t],
            [0, x, x, 0, 0],
        ]

        self.assertListEqual(field, expected)

        field = [[0, 0, 0, 0, 0, 0, 0]]

        Algorithm.execute(field, (0, 0), (0, 6))

        expected = [[A, t, t, t, t, t, B]]

        self.assertListEqual(field, expected)

        field = [
            [0, x, 0, 0],
            [x, x, 0, 0],
        ]

        with self.assertRaises(IndexError):
            Algorithm.execute(field, (2, 0), (0, 0))
        with self.assertRaises(IndexError):
            Algorithm.execute(field, (1, 0), (0, 6))
        with self.assertRaises(IndexError):
            Algorithm.execute(field, (4, 0), (5, 0))

        with self.assertRaises(Warning):
            Algorithm.execute(field, (0, 0), (1, 2))

    @staticmethod
    def run_test():
        main()
