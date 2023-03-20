import unittest
from src.greedy_examples import *

class TestExamples(unittest.TestCase):
    def test1_children_groups(self):
        ages = [5, 5.5, 7, 7, 3, 3.3, 4]
        n_groups = children_groups(ages)
        self.assertEqual(n_groups, 3, "children_groups: wrong result")

    def test2_car_stops(self):
        L = 20
        X = [1, 2, 7, 11, 20, 20]
        n_stops = car_stops(L, X)
        self.assertEqual(n_stops, 3, "car_stops: wrong result")
        X = [1, 2, 7, 11, 21, 20]
        n_stops = car_stops(L, X)
        self.assertEqual(n_stops, -1, "car_stops (unreacheable case): wrong result")

    def test3_max_activities(self):
        Activities = [(0,6), (1,4), (3,5), (5,7), (3,8), (5,9), (6,10), (8,11), (8,12), (2,13), (12,14)]
        max_act = max_activities(Activities)
        self.assertEqual(max_act, [0, 3, 7, 10], "max_activities: wrong result")

    def test4_used_halls(self):
        Activities = [(1,4), (2,5), (6,7), (4,8)]
        n_used = used_halls(Activities)
        self.assertEqual(n_used, 2, "used_halls: wrong answer")


if __name__ == '__main__':
    unittest.main()

