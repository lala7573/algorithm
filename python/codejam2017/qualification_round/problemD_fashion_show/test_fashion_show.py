import unittest

from OversizedPancakeFlipper_set.OversizedPancakeFlipper import OversizedPancakeFlipper

from codejam2017.qualification_round.problemD_fashion_show.fashion_show import FashionShow


class TestFashionShow(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(FashionShow.solve(
            2, 0, []), None)

    def test_2(self):
        self.assertEqual(FashionShow.solve(
            1, 1, [('o', 1, 1)]), None)

    def test_3(self):
        self.assertEqual(FashionShow.solve(
            3, 4, [
                ('+', 2, 3),
                ('+', 2, 1),
                ('x', 3, 1),
                ('+', 2, 2),
            ]), None)

    def test_4(self):
        pass
        # self.assertEqual(FashionShow.solve(), None)

    def test_5(self):
        pass
        # self.assertEqual(FashionShow.solve(), None)

