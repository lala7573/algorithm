import unittest

from codejam2017.round1c.problemA_ample_syrup.amplesyrup import AmpleSyrup, Pancake


class TestCountingSheepTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(AmpleSyrup.solve(2, 1, [Pancake(100, 20), Pancake(200, 10)]), 138230.076757951)

    def test_2(self):
        self.assertEqual(AmpleSyrup.solve(2, 2, [Pancake(100, 20), Pancake(200, 10)]), 150796.447372310)

    def test_3(self):
        self.assertEqual(AmpleSyrup.solve(), None)

    def test_4(self):
        self.assertEqual(AmpleSyrup.solve(), None)

    def test_5(self):
        self.assertEqual(AmpleSyrup.solve(), None)

