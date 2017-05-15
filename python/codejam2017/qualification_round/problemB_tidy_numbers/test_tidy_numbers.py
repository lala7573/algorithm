import unittest

from codejam2017.qualification_round.problemB_tidy_numbers.tidy_numbers import TidyNumbers


class TestTidyNumbers(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(TidyNumbers.solve(132), 129)

    def test_2(self):
        self.assertEqual(TidyNumbers.solve(1000), 999)

    def test_3(self):
        self.assertEqual(TidyNumbers.solve(7), 7)

    def test_4(self):
        self.assertEqual(TidyNumbers.solve(111111111111111110), 99999999999999999)
