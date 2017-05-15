import unittest

from codejam2017.round1.problemA_alphabet_cake.alphabet_cake import AlphabetCake


class TestAlphabetCake(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(AlphabetCake.solve(
            3, 3, [
                ['G', '?', '?'],
                ['?', 'C', '?'],
                ['?', '?', 'J']
            ]), 'GGG\nCCC\nJJJ')

    def test_2(self):
        self.assertEqual(AlphabetCake.solve(
            3, 3, [
                ['G', '?', '?'],
                ['?', 'G', '?'],
                ['?', '?', 'J']
            ]), 'GGG\nGGG\nJJJ')

    def test_3(self):
        self.assertEqual(AlphabetCake.solve(
            4, 4, [
                ['G', '?', '?', '?'],
                ['?', 'G', '?', '?'],
                ['?', '?', '?', '?'],
                ['?', '?', '?', 'J']
            ]), 'GGGG\nGGGG\nGGGG\nJJJJ')

    def test_4(self):
        # 3 4
        # CGED
        # ?AFB
        # ????
        self.assertEqual(AlphabetCake.solve(
            3, 4, [
                ['C', 'G', 'E', 'D'],
                ['?', 'A', 'F', 'B'],
                ['?', '?', '?', '?']
            ]), 'CGED\nAAFB\nAAFB')

    def test_5(self):
        self.assertEqual(AlphabetCake.solve(
            3, 4, [
                ['?', '?', '?', '?'],
                ['?', 'C', 'J', '?'],
                ['?', '?', '?', '?']
            ]
        ), 'CCJJ\nCCJJ\nCCJJ')

    def test_6(self):
        self.assertEqual(AlphabetCake.solve(
            3, 4, [
                ['?', '?', '?', '?'],
                ['?', 'C', 'A', '?'],
                ['D', '?', 'B', 'E']
            ]
        ), 'CCAA\nCCAA\nDDBE')

    def test_7(self):
        self.assertEqual(AlphabetCake.solve(
            4, 3, [
                ['?', '?', '?'],
                ['E', '?', '?'],
                ['A', 'B', 'F'],
                ['?', 'D', 'C'],
            ]
        ), 'EEE\nEEE\nABF\nDDC')