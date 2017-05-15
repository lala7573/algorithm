import unittest

from codejam2017.qualification_round.problemC_bathroom_stalls.bathroom_stalls_2 import BathroomStalls2


class TestBathroomStalls(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_0(self):
        self.assertEqual(BathroomStalls2.solve(10, 10), (0, 0))
        # self.assertEqual(BathroomStalls.solve(5, 5), (0, 0))

    def test_1(self):
        self.assertEqual(BathroomStalls2.solve(4, 2), (1, 0))

    def test_2(self):
        self.assertEqual(BathroomStalls2.solve(5, 2), (1, 0))

    def test_3(self):
        self.assertEqual(BathroomStalls2.solve(6, 2), (1, 1))

    def test_4(self):
        self.assertEqual(BathroomStalls2.solve(1000, 1000), (0, 0))

    def test_5(self):
        self.assertEqual(BathroomStalls2.solve(1000, 1), (500, 499))

    def test_6(self):
        self.assertEqual(BathroomStalls2.solve(850651, 823923), (0, 1))

    # def test_test(self):
        # import heapq
        # heap_q = []
        # heapq.heapify(heap_q)
        # heapq.heappush(heap_q, 1)
        # heapq.heappush(heap_q, 1)
        # print(heapq.heappop(heap_q))
        # print(heapq.heappop(heap_q))
