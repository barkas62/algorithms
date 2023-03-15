class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.rite = None

    def add_left(self, data):
        self.left = Node(data)
        return self.left

    def add_rite(self, data):
        self.rite = Node(data)
        return self.rite

    def __radd__(self, data):
        return data + self.data

from collections import deque

def bfs(root, func):
    if root is None or func is None:
        return
    de = deque([root])
    while de:
        node = de.popleft()
        func(node)
        if node.left:
            de.append(node.left)
        if node.rite:
            de.append(node.rite)


def dfs_preorder(node, func):
    if node is None or func is None:
        return
    if func:
        func(node)
    dfs_preorder(node.left, func)
    dfs_preorder(node.rite, func)


def dfs_preorder_iter(root, func):
    if root is None or func is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        func(node)
        if node.rite:
            stack.append(node.rite)
        if node.left:
            stack.append(node.left)


def dfs_inorder(node, func=None):
    if node is None or func is None:
        return
    dfs_inorder(node.left, func)
    func(node)
    dfs_inorder(node.rite, func)


def dfs_inorder_iter(root, func):
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if stack:
                curr = stack.pop()
                func(curr)
                curr = curr.rite
            else:
                break

def dfs_postorder(node, func):
    if node is None or func is None:
        return
    dfs_postorder(node.left, func)
    dfs_postorder(node.rite, func)
    func(node)


def dfs_postorder_iter(root, func):
    if root is None or func is None:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.rite:
            stack1.append(node.rite)
    while stack2:
        node = stack2.pop()
        func(node)

if __name__ == "__main__":
    root = Node(1)
    n2 = root.add_left(2)
    n3 = root.add_rite(3)
    n2.add_left(4)
    n2.add_rite(5)

    fprn = lambda node: print(str(node.data))

    class Sum:
        def __init__(self):
            self.s = 0
        def __call__(self, node):
            self.s += node.data
        def __str__(self):
            return str(self.s)

    # bfs(root, fprn)

    dfs_postorder_iter(root, func=fprn)
    print("---------------")

    summ = Sum()
    dfs_inorder_iter(root, func=summ)
    print("Sum: "+str(summ))










