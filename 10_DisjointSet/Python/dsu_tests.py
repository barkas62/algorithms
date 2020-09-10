import unittest
from dsu import DisjointSet

class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        # Disjoint set of size 5
        self.size = 5
        self.dsu = DisjointSet(self.size)


    def test_1_Exceptions_Test(self):
        # find method should raise IndexError if out-of-range id is passed
        with self.assertRaises(IndexError):
            self.dsu.find(self.size + 1)


    def test_2_Functionality_Test(self):
        # testing union and find methods
        self.dsu.union(0, 2)
        self.dsu.union(2, 4)
        self.dsu.union(2, 4)

        self.dsu.union(1, 3)

        self.assertEqual(self.dsu.find(0), self.dsu.find(4),
                         "elements 0 and 4 must be in the same set")
        self.assertEqual(self.dsu.find(1), self.dsu.find(3),
                         "elements 1 and 3 must be in the same set")

        id0 = self.dsu.find(0)
        id1 = self.dsu.find(1)
        self.assertNotEqual(self.dsu.find(0), self.dsu.find(1),
                            "elements 0 and 1 must NOT be in the same set")

