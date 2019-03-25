from collections import deque

class Graph:
    def __init__(self, n_vert = 0):
        self.verts = [[] for _ in range(n_vert)]

    def add_edge(self, i, j):
        assert 0<= i < len(self.verts) and 0<= j < len(self.verts) and i != j, Exception("Bad args for Graph.add_edge")
        self.verts[i].append(j)
        self.verts[j].append(i)

    def test_bipartite(self, l_part : set, r_part : set ) -> bool:
        if len(self.verts) == 0:
            return False
        l_part &= set()
        r_part &= set()
        q = deque()
        q.append(0)
        l_part.add(0)
        swt = 0
        while len(q) > 0:
            i0 = q.popleft()
            for i1 in self.verts[i0]:
                if i1 not in l_part and i1 not in r_part:
                    q.append(i1)
                    if i0 in l_part:
                        r_part.add(i1)
                    else:
                        l_part.add(i1)
                else:
                    if (i0 in l_part and i1 in l_part) or (i0 in r_part and i1 in r_part):
                        l_part &= set()
                        r_part &= set()
                        return False
        return True


g = Graph(7)
g.add_edge(0,1)
g.add_edge(2,1)
g.add_edge(2,5)
g.add_edge(4,5)
g.add_edge(6,3)
g.add_edge(2,6) #False

l_part = set()
r_part = set()
res = g.test_bipartite(l_part, r_part)

pass