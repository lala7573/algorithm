import unittest

from algospot.MEASURETIME.code import MEASURETIME, FenwickTree


class TestCountingSheepTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        MEASURETIME.solve(5, [4, 1, 2, 6, 3])
        # [7, 8, 6, 6, 1, 9, 4, 4, 3, 10]
        # self.assertEqual(MEASURETIME.solve(), None)

    def test_2(self):
        fenwick = FenwickTree(5)
        array = [4, 1, 2, 6, 3]
        for i in range(0, len(array)):
            fenwick.add(i, array[i])

        # self.assertEqual(MEASURETIME.solve(), None)

    def test_3(self):
        self.assertEqual(MEASURETIME.solve(), None)

    def test_4(self):
        self.assertEqual(MEASURETIME.solve(), None)

    def test_5(self):
        self.assertEqual(MEASURETIME.solve(), None)

