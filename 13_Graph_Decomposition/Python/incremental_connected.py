from collections import defaultdict

class DisjointSet:
    class Elem:
        def __init__(self, root_id):
            self.parent = root_id
            self.rank = 0

    def __init__(self):
        self.arr = []

    def add_root(self):
        new_root_id = len(self.arr)
        self.arr.append(DisjointSet.Elem(new_root_id))
        return new_root_id

    def find(self, i):
        if i != self.arr[i].parent:
            self.arr[i].parent = self.find(self.arr[i].parent)
        return self.arr[i].parent

    def union(self, ni, nj):
        union_id = drop_id = -1
        pi = self.find(ni)
        pj = self.find(nj)
        if pi != pj:
            if self.arr[pi].rank < self.arr[pj].rank:
                union_id, drop_id = pj, pi
                self.arr[pi].parent = pj
            else:
                union_id, drop_id = pi, pj
                self.arr[pj].parent = pi
                if self.arr[pi].rank == self.arr[pj].rank:
                    self.arr[pi].rank += 1
        return union_id, drop_id


class Graph:
    class Node:
        def __init__(self, idx):
            self.idx = idx
            self.adj = []

    def __init__(self, n_nodes = 0):
        self.nodes = []
        self.ds = DisjointSet()
        self.conn_comp = defaultdict(list)
        self.n_conncomp = 0
        if n_nodes > 0:
            for i in range(n_nodes):
                self.add_node()


    def add_node(self):
        new_idx = len(self.nodes)
        self.nodes.append(Graph.Node(new_idx))
        self.n_conncomp += 1
        comp_id = self.ds.add_root()
        self.conn_comp[comp_id] = [new_idx]

    def add_edge(self, ni, nj):
        self.nodes[ni].adj.append(nj)
        self.nodes[nj].adj.append(ni)
        comp_i = self.ds.find(ni)
        comp_j = self.ds.find(nj)
        if comp_i != comp_j:
            union_id, drop_id = self.ds.union(ni,nj)
            self.conn_comp[union_id].extend(self.conn_comp[drop_id])
            del self.conn_comp[drop_id]
            self.n_conncomp -= 1
        assert self.n_conncomp > 0, 'Bad graph: add_edge'

    def __iter__(self):
        self.iter = iter(self.conn_comp.values())
        return self

    def __next__(self):
        return next(self.iter)



if __name__ == '__main__':
    G = Graph(7)

    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(3, 4)
    G.add_edge(5, 4)
    G.add_edge(5, 6)

for cc in G:
    pass

pass