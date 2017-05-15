import unittest

from codejam2016.problemB_revenge_of_the_pancakes.revenge_of_the_pancakes import revenge_of_the_pancakes


class TestRevengeOfThePancakes(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(1, revenge_of_the_pancakes('-'))

    def test_2(self):
        self.assertEqual(1, revenge_of_the_pancakes('-+'))

    def test_3(self):
        self.assertEqual(2, revenge_of_the_pancakes('+-'))

    def test_4(self):
        self.assertEqual(0, revenge_of_the_pancakes('+++'))

    def test_0(self):
        self.assertEqual(3, revenge_of_the_pancakes('--+-'))

