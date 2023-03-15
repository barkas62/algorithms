import unittest

from src.tree_traversal import Node, \
    bfs, \
    dfs_preorder, dfs_preorder_iter, \
    dfs_postorder, dfs_postorder_iter, \
    dfs_inorder, dfs_inorder_iter

class Acc:
    def __init__(self, _s=""):
        self.s = _s

    def __call__(self, node):
        if self.s != "":
            self.s += " "
        self.s += str(node.data)

    def __str__(self):
        return self.s


class TestDfs(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Node(1)
        n2 = self.tree.add_left(2)
        n3 = self.tree.add_rite(3)
        n2.add_left(4)
        n2.add_rite(5)

    def test_bfs(self):
        acc = Acc()
        bfs(self.tree, acc)
        self.assertEqual(str(acc),  "1 2 3 4 5")

    def test_preorder(self):
        acc1 = Acc()
        acc2 = Acc()
        dfs_preorder(self.tree, acc1)
        dfs_preorder_iter(self.tree, acc2)
        self.assertEqual(str(acc2), str(acc1), "Preorder: recursive does not match iterative")

    def test_postorder(self):
        acc1 = Acc()
        acc2 = Acc()
        dfs_postorder(self.tree, acc1)
        dfs_postorder_iter(self.tree, acc2)
        self.assertEqual(str(acc2), str(acc1), "Postorder: recursive does not match iterative")

    def test_inorder(self):
        acc1 = Acc()
        acc2 = Acc()
        dfs_inorder(self.tree, acc1)
        dfs_inorder_iter(self.tree, acc2)
        self.assertEqual(str(acc2), str(acc1), "Inorder: recursive does not match iterative")

if __name__ == '__main__':
    unittest.main()