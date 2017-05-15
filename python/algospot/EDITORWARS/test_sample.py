import unittest

from algospot.EDITORWARS.sample import EditorWars


class TestCountingSheepTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(EditorWars.solve(
            4,
            4,
            [
                (True, 0, 1),
                (True, 1, 2),
                (False, 1, 3),
                (True, 2, 0),
            ]
        ), (True, 3))

    def test_2(self):
        self.assertEqual(EditorWars.solve(
            100, 4, [(True, 0, 1), (True, 1, 2), (True, 2, 3), (True, 3, 4)]
        ), (True, 100))

    def test_3(self):
        self.assertEqual(EditorWars.solve(
            3, 3, [(True, 0, 1), (True, 1, 2), (False, 2, 0)]
        ), (False, 3))

    def test_4(self):
        self.assertEqual(EditorWars.solve(
            8, 6, [
                (False, 0, 1),
                (True, 1, 2),
                (True, 1, 4),
                (False, 4, 3),
                (False, 5, 6),
                (True, 5, 7)]
        ), (True, 5))
