class DisjointSet:
    class Element:
        def __init__(self, parent = -1, rank = -1):
            self.parent = parent
            self.rank   = rank

    def __init__(self, size = 0):
        assert size >= 0, 'DisjointSet.__init__ failed: wrong size param'
        self.elements = [ self.Element() for i in range(size) ]

    def add(self, i):
        if i >= len(self.elements):
            self.elements.extend([self.Element() for i in range(i - len(self.elements) + 1)])
        assert self.elements[i].parent == -1, 'DisjointSet.Add failed: element already present'
        self.elements[i] = self.Element(i,0)

    def find(self, i):
        assert i < len(self.elements), 'DisjointSet.Find failed: out of range'
        parents = []
        while i != self.elements[i].parent:
            parents.append(i)
            i = self.elements[i].parent
        # compressing
        for ip in parents:
            self.elements[ip].parent = i
        return i
        '''    
        if i != self.elements[i].parent:
            self.elements[i].parent = self.find( self.elements[i].parent )
        return self.elements[i].parent
        '''

    def union(self, i, j):
        ip = self.find(i)
        jp = self.find(j)

        if self.elements[ip].rank < self.elements[jp].rank:
            self.elements[ip].parent = jp
        elif self.elements[ip].rank > self.elements[jp].rank:
            self.elements[jp].parent = ip
        else:  # ranks are equal
            self.elements[jp].parent = ip
            self.elements[ip].rank += 1


dsu = DisjointSet(size = 10)
for i in range(10):
    dsu.add(i)

for i in range(9):
    dsu.union(i,i+1)

dsu.union(0,2)
dsu.union(2,4)
dsu.union(4,6)
dsu.union(6,8)

dsu.union(1,3)
dsu.union(3,5)
dsu.union(5,7)
dsu.union(7,9)

id7 = dsu.find(7)
id8 = dsu.find(8)

id1 = dsu.find(1)
id2 = dsu.find(2)

pass