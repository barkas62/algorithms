class BST:
    '''
    Binary Search Tree: node definition and main concepts
    '''
    class BST_Node:
        def __init__(self, value, parent = None, left = None, right = None):
            self.value  = value
            self.parent = parent
            self.left   = left
            self.right  = right

    def __init__(self):
        self.root = None
        self.size = 0
        self.iter = None

    def find(self, value):
        '''
        Checks whether value is present in BST
        :return: Boolean
        '''
        if self.root is None:
            return None
        node = self._find(value, self.root)
        return node.value == value

    def __contains__(self, value):
        if self.root is None:
            return False
        node = self._find(value, self.root)
        return node.value == value

    def __len__(self):
        return self.size

    def __iter__(self):
        self.iter = None
        return self

    def __next__(self):
        if self.iter is None:
            if self.root is None:
                raise StopIteration
            self.iter = self._findMin(self.root)
        else:
            self.iter = self._findNext(self.iter)
        if self.iter is not None:
            return self.iter.value
        else:
            raise StopIteration

    def _find(self, value, node):
        '''
        Finds and returns the node containing value, starts in node
        If value is not in the BST, returns the node containing the nearest value.
        '''
        assert node is not None, '_find tries to access None node'
        if node.value == value:
            return node
        if value < node.value:
            return self._find(value, node.left) if node.left is not None else node
        else:
            return self._find(value, node.right) if node.right is not None else node

    def _findMin(self, root):
        '''
        Returns a node with a min value in a subtree rooted in root
        '''
        assert root is not None, '_findMin tries to access None node'
        node = root
        while node.left is not None:
            node = node.left
        return node

    def _findMax(self, root):
        '''
        Returns a node with a max value in a subtree rooted in root
        '''
        assert root is not None, '_findMax tries to access None node'
        node = root
        while node.right is not None:
            node = node.right
        return node

    def _findNext(self, node):
        '''
        Returns a node with a value next to node.value
        '''
        assert node is not None, '_findNext tries to access None node'
        if node.right is not None:
            return self._findMin(node.right)
        else:
            while node.parent is not None:
                if node.parent.value > node.value:
                    return node.parent
                node = node.parent
        return None


    def add(self, value):
        '''
        Adds value to BST. Returns True on success, False if there is already such value
        '''
        if self.root is None:
            self.root = self.BST_Node(value)
            self.size = 1
            return True

        nearest_node = self._find(value, self.root)
        if nearest_node.value == value:
            return False

        node = self.BST_Node(value, parent = nearest_node)
        if value < nearest_node.value:
            nearest_node.left = node
        else:
            nearest_node.right = node

        self.size += 1
        return True

    def add_list(self, vals):
        '''
        Adds all elements from the list
        '''
        for v in vals:
            self.add(v)

    def nxt(self, value):
        if self.root is None:
            return None

        node = self._find(value, self.root)
        if node.value > value:
            return node.value

        if node.right is not None:
            node_min = self._findMin(node.right)
            return node_min.value
        else:
            while node.parent is not None:
                if node.parent.value > value:
                    return node.parent.value
                node = node.parent
        return None

    def prv(self, value):
        if self.root is None:
            return None

        node = self._find(value, self.root)
        if node.value < value:
            return node.value

        if node.left is not None:
            max_node = self._findMax(node.left)
            return max_node.value
        else:
            while node.parent is not None:
                if node.parent.value < value:
                    return node.parent.value
                node = node.parent
        return None


T = BST()
T.add_list( [5,2,6,1,3,7,4] )

for v in T:
    print(str(v))

res = T.nxt(7)
res = T.prv(6)

pass


