class DisjointSet:
    class Element:
        def __init__(self, parent, rank = 0):
            self.parent = parent
            self.rank   = rank

    def __init__(self, size):
        assert size > 0, 'DisjointSet.__init__ failed: wrong size param'
        self.elements = [ self.Element(i) for i in range(size) ]


    def find(self, i):
        '''
        Find set id that contains element i
        :param i: element id
        :return: set id
        '''
        if i >= len(self.elements):
            raise  IndexError('DisjointSet.find failed: out of range')
        '''
        # Iterative variant
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

    def union(self, i, j):
        '''
        Union of sets containing elements i and j
        :param i: element id
        :param j: element id
        :return: None
        '''
        ip = self.find(i)
        jp = self.find(j)
        if ip != jp:
            if self.elements[ip].rank < self.elements[jp].rank:
                self.elements[ip].parent = jp
            elif self.elements[ip].rank > self.elements[jp].rank:
                self.elements[jp].parent = ip
            else:  # ranks are equal
                self.elements[jp].parent = ip
                self.elements[ip].rank += 1


