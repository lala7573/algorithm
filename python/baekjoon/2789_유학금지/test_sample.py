import unittest

from OversizedPancakeFlipper_set.OversizedPancakeFlipper import OversizedPancakeFlipper


class TestCountingSheepTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(OversizedPancakeFlipper.solve(), None)

    def test_2(self):
        self.assertEqual(OversizedPancakeFlipper.solve(), None)
