from operator import attrgetter

class DisjointSet:
    def __init__(self, n_items):
        self.data = list(range(n_items))
        self.rank = [0]*n_items

    def find(self, i):
        if i != self.data[i]:
            i = self.find(self.data[i])
        return i

    def union(self, i, j):
        id_i = self.find(i)
        id_j = self.find(j)
        if id_i == id_j:
            return
        if self.rank[id_i] < self.rank[id_j]:
            self.data[id_i] = id_j
        else:
            self.data[id_j] = id_i
            if self.rank[id_i] == self.rank[id_j]:
                self.rank[id_i] += 1
        return

class Edge:
    def __init__(self, ni, nj, w):
        self.ni = ni
        self.nj = nj
        self.w  = w

class Node:
    def __init__(self):
        self.edges = []  # list of edges: (ni, nj, w)


class Graph:
    def __init__(self, n_nodes):
        # list of adjacency list of (node_idx, edge_weight)
        self.nodes = [Node() for _ in range(n_nodes)]
        self.edges = []

    def add_edge(self, ni, nj, w):
        edge = Edge(ni, nj, w)
        self.nodes[ni].edges.append(edge)
        self.nodes[nj].edges.append(edge)
        self.edges.append(edge)

    def Kruskal(self):
        gr = Graph(len(self.nodes))
        self.edges.sort(key=attrgetter('w'))
        ds = DisjointSet(len(self.nodes))
        for e in self.edges:
            if ds.find(e.ni) != ds.find(e.nj):
                ds.union(e.ni, e.nj)
                gr.add_edge(e.ni, e.nj, e.w)
        return gr



gr = Graph(4)
gr.add_edge(0,1,1)
gr.add_edge(1,2,2)
gr.add_edge(2,3,3)
gr.add_edge(0,3,5)
gr.add_edge(3,1,4)

min_tree = gr.Kruskal()

pass





