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


def dfs_preorder(node, func=None):
    if node is None:
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
    if node is None:
        return
    dfs_inorder(node.left, func)
    if func is not None:
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
    if node is None:
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


n4 = Node(4)
n2 = n4.add_left(2)
n2.add_left(1)
n2.add_rite(3)

n5 = n4.add_rite(5)
n5.add_rite(6)

fprn = lambda node : print(str(node.data))

class Sum:
    def __init__(self):
        self.s = 0
    def __call__(self, node):
        self.s += node.data

summator = Sum()
'''
n1 = Node(1)
n2 = n1.add_left(2)
n3 = n1.add_rite(3)
n4 = n2.add_left(4)
n5 = n2.add_rite(5)
n6 = n3.add_left(6)
n7 = n3.add_rite(7)
'''

dfs_inorder(n4, func=fprn)
print("---------------")
dfs_inorder_iter(n4, func=fprn)

pass







