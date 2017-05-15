import unittest

from codejam2017.round1c.problemB_Parenting_partnering.sample import ParentingPartner


class TestCountingSheepTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(ParentingPartner.solve(
            1, 1, [(540, 600)], [(840, 900)]
        ), 2)

    def test_2(self):
        self.assertEqual(ParentingPartner.solve(
            2, 0, [(900, 1260), (180, 540)], []
        ), 4)

    def test_3(self):
        self.assertEqual(ParentingPartner.solve(), None)

    def test_4(self):
        self.assertEqual(ParentingPartner.solve(), None)

    def test_5(self):
        self.assertEqual(ParentingPartner.solve(), None)

