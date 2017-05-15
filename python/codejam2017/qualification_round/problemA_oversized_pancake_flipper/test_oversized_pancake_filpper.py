import unittest

from codejam2017.qualification_round.problemA_oversized_pancake_flipper.oversized_pancake_filpper import \
    OversizedPancakeFlipper


class TestOversizedPancakeFlipper(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(OversizedPancakeFlipper.solve('---+-++-', 3), 3)

    def test_2(self):
        self.assertEqual(OversizedPancakeFlipper.solve('+++++', 4), 0)

    def test_3(self):
        self.assertEqual(OversizedPancakeFlipper.solve('-+-+-', 4), 'IMPOSSIBLE')

    def test_4(self):
        self.assertEqual(OversizedPancakeFlipper.solve('-+-+-', 3), 3)

    def test_5(self):
        self.assertEqual(OversizedPancakeFlipper.solve('-++', 2), 'IMPOSSIBLE')

    def test_6(self):
        self.assertEqual(OversizedPancakeFlipper.solve('++-', 3), 'IMPOSSIBLE')
