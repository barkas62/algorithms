
class Node:
    def __init__(self, val, parent = None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
        self.h = 1

    def is_leaf(self):
        return (self.left is None) and (self.right is None)

    def detach(self, child):
        if self.left == child:
            self.left = None
        elif self.right == child:
            self.right = None
        else:
            raise Exception('No child to detach')

    def replace_child(self, child, new_child):
        if self.left == child:
            self.left = new_child
        elif self.right == child:
            self.right = new_child
        else:
            raise Exception('No child to replace')

    def get_lh(self):
        return self.left.h if self.left else 0

    def get_rh(self):
        return self.right.h if self.right else 0

    def adjust_height(self):
        self.h = 1 + max(self.get_rh(), self.get_lh())

    def rotate_right(self):
        P = self.parent
        C = self.left
        if not C:
            return
        T2 = C.right
        if P:
            P.replace_child(self, C)
        self.left = T2
        self.parent = C
        C.parent = P
        C.right = self
        if T2:
            T2.parent = self

    def rotate_left(self):
        P = self.parent
        C = self.right
        if not C:
            return
        T2 = C.left
        if P:
            P.replace_child(self, C)
        self.parent = C
        self.right = T2
        C.parent = P
        C.left = self
        if T2:
            T2.parent = self


class AVL_Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def find_(self, val, node):
        if node is None:
            raise Exception('Tree is Empty')
        if node.val == val:
            return node
        elif val < node.val:
            if node.left is not None:
                return self.find_(val, node.left)
            else:
                return node
        else:  # val > node.val
            if node.right is not None:
                return self.find_(val, node.right)

    def find_min_(self, node):
        while node.left:
            node = node.left
        return node

    def remove_leaf(self, leaf):
        assert leaf and leaf.is_leaf(), Exception('Not a leaf')
        if leaf.parent is not None:
            leaf.parent.detach(leaf)
        else:
            assert leaf == self.root, Exception('Bad Structure')
            self.root = None

    def splice(self, node):
        assert node.parent, Exception('Bad Structure')
        assert node.left or node.right, Exception('Bad Structure')
        assert not (node.left or node.right), Exception('Bad Structure')
        child = node.left if node.left else node.right
        parent = node.parent
        if node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child
        child.parent = parent

    def find(self, val):
        if self.root is None:
            raise Exception('Empty Tree')

        node = self.find_(val, self.root)
        return node.val == val

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        node = self.find_(val, self.root)
        if val == node.val:
            return
        new_node = Node(val, node)
        if val < node.val:
            node.left = new_node
        else:
            node.right = new_node
        new_node.parent = node
        node.adjust_height()
        self.rebalance(node)

    def rebalance_right(self, P):
        N = P.left
        if N.get_lh() < N.get_rh():
            N.rotate_left()
        P.rotate_right()
        P.adjust_height()
        N.adjust_height()

    def rebalance_left(self, P):
        N = P.right
        if N.get_rh() < N.get_lh():
            N.rotate_right()
        P.rotate_left()
        P.adjust_height()
        N.adjust_height()

    def rebalance(self, P):
        great_parent = P.parent
        if P.get_lh() > P.get_rh() + 1:
            self.rebalance_right(P)
        elif P.get_rh() > P.get_lh() + 1:
            self.rebalance_left(P)
        #else:
        #    return # no need to balance
        P.adjust_height()
        if great_parent:
            self.rebalance(great_parent)

    def remove(self, val):
        node2del = self.find_(val, self.root)
        if node2del.val != val:
            raise Exception('Key Missing')
        parent = node2del.parent
        if node2del.is_leaf():
            if parent is not None:
                node2del.parent.detach(node2del)
            else:
                assert node2del == self.root, 'Bad Structure'
                self.root = None
        elif node2del.left is None or node2del.right is None:
            next_node = node2del.left if node2del.left is not None else node2del.right
            if parent is not None:
                parent.replace_child(node2del, next_node)
                next_node.parent = parent
            else:
                assert node2del == self.root, 'Bad Structure'
                self.root = next_node
                next_node.parent = 0
        else:
            next_node = self.find_min_(node2del.right)
            assert next_node.left is None, Exception('find_min_ error')
            next_node.val, node2del.val = node2del.val, next_node.val
            if next_node.is_leaf():
                self.remove_leaf(next_node)
            else:
                self.splice(next_node)
        self.rebalance(parent)


tree = AVL_Tree()
tree.insert(5)
tree.insert(4)
tree.insert(3)

pass

