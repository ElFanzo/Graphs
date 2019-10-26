from unittest import TestCase, main
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

    @staticmethod
    def run_test():
        main()
