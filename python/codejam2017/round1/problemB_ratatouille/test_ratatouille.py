import unittest

from codejam2017.round1.problemB_ratatouille.ratatouille import Ratatouille


class TestRatatouille(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(Ratatouille.solve(
            2, 1, [500, 300], [[900], [660]]
        ), None)

    def test_2(self):
        self.assertEqual(Ratatouille.solve(
            2, 1, [500, 300], [[1500], [809]]
        ), None)

    def test_3(self):
        self.assertEqual(Ratatouille.solve(
            2, 2, [50, 100], [[450, 449], [1100, 1101]]
        ), None)

    def test_4(self):
        self.assertEqual(Ratatouille.solve(), None)

    def test_5(self):
        self.assertEqual(Ratatouille.solve(), None)

