
class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent  = None
        self.child   = None
        self.sibling = None

def mergeBinTrees(root1 : Node, root2 : Node)->Node:
    assert root1.degree == root2.degree, Exception('mergeBinTrees should be called for trees with same degree')
    if root1.key > root2.key:
        root1, root2 = root2, root1
    root2.parent = root1
    root2.sibling = root1.child
    root1.child = root2
    root1.degree += 1
    return root1

def chop_root(root):
    assert root.parent is None, Exception('tree2heap should be called for tree root')
    new_roots = []
    new_root = root.child
    while new_root:
        new_roots.append(new_root)
        new_root = new_root.sibling
    return new_roots[::-1]

def parse_tree(root, keys):
    while root:
        keys.append(root.key)
        parse_tree(root.child, keys)
        root = root.sibling

class BinaryHeap:
    def __init__(self):
        self.roots = []

    def _adjust(self):
        n = len(self.roots)
        if n <= 1:
            return  # nothing to do
        if n == 2:
            if self.roots[0].degree == self.roots[1].degree:
                # otherwise everything OK
                self.roots = [ mergeBinTrees(self.roots[0], self.roots[1]) ]
            return
        # Note: max 3 trees of the same degree may exist simultaneously: 2 from mergeBinTrees + 1 from prev merge
        # in case 3 consecutive: move 1 step ahead, this leaves one untouched, then merge last pair
        i = 0
        while i < len(self.roots) - 1:
            if i >= len(self.roots) - 2:
                root1, root2 = self.roots[i], self.roots[i+1]
                if root1.degree == root2.degree:
                    keys1 = []
                    parse_tree(self.roots[i], keys1)
                    keys2 = []
                    parse_tree(self.roots[i+1], keys2)
                    self.roots[i] = mergeBinTrees(self.roots[i], self.roots[i+1])
                    self.roots.pop() # last one
                    keys = self.parse()
                    pass
            else:
                root1, root2, root3 = self.roots[i], self.roots[i+1], self.roots[i+2]
                if root1.degree < root2.degree or root1.degree == root2.degree == root3.degree:
                    i += 1
                elif root1.degree == root2.degree:
                    keys1 = []
                    parse_tree(self.roots[i], keys1)
                    keys2 = []
                    parse_tree(self.roots[i+1], keys2)
                    self.roots[i] = mergeBinTrees(self.roots[i], self.roots[i+1])
                    self.roots.pop(i+1)
                    keys = self.parse()
                    pass



    def merge(self, heap):
        if not self.roots:
            self.roots = heap.roots
            return
        if not heap.roots:
            return
        merged = []
        i1, i2 = 0, 0
        n1, n2 = len(self.roots), len(heap.roots)
        while i1 < n1 and i2 < n2:
            root1 = self.roots[i1]
            root2 = heap.roots[i2]
            if root1.degree <= root2.degree:
                merged.append(root1)
                i1 += 1
            else:
                merged.append(root2)
                i2 += 1

        while i1 < n1:
            merged.append(self.roots[i1])
            i1 += 1
        while i2 < n2:
            merged.append(heap.roots[i2])
            i2 += 1

        self.roots = merged
        self._adjust()

    def insert(self, key):
        tmp = BinaryHeap()
        tmp.roots = [Node(key)]
        self.merge(tmp)

    def _get_min(self):
        assert len(self.roots) > 0, Exception('Empty heap')
        min_key = self.roots[0].key
        min_id = 0
        for i in range(1,len(self.roots)):
            if min_key > self.roots[i].key:
                min_key = self.roots[i].key
                min_id = i
        return min_key, min_id

    def get_min(self):
        min_key, _ = self._get_min()
        return min_key

    def pop_min(self):
        min_key, min_id = self._get_min()
        new_heap = BinaryHeap()
        root2chop = self.roots.pop(min_id)
        new_heap.roots = chop_root(root2chop)
        self.merge(new_heap)
        return min_key

    def parse(self):
        all_keys = []
        for root in self.roots:
            parse_tree(root, all_keys)
        return all_keys



bh = BinaryHeap()
bh.insert(50)
bh.insert(10)
bh.insert(30)
bh.insert(40)
bh.insert(20)

keys0 = bh.parse()
min_key = bh.pop_min()
keys1 = bh.parse()

bh1 = BinaryHeap()
bh1.insert(51)
bh1.insert(11)
bh1.insert(31)
bh1.insert(41)
bh1.insert(21)

bh.merge(bh1)
keys2 = bh.parse()
min_key = bh.pop_min()
keys3 = bh.parse()

pass










