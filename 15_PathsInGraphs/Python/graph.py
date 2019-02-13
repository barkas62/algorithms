from collections import deque
import sys

class MinHeap:
    def parent(i):
        return (i - 1)//2

    def lchild(i):
        return 2*i + 1

    def rchild(i):
        return 2*i + 2

    def __init__(self, nodes):
        '''
        :param elems:
        '''
        self.ref = { node : i for i, node in enumerate(nodes) }
        self.heap = nodes
        self.heap[0].dist = 0

    def __len__(self):
        return len(self.heap)

    def pop_min(self):
        min_node = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.ref[self.heap[0]] = 0
        self.ref.pop(min_node)
        self.heap.pop()
        self.sift_down(0)
        return min_node

    def change_priority(self, node, new_dist):
        if node.dist == new_dist:
            return
        i = self.ref[node]
        old_dist = self.heap[i].dist
        self.heap[i].dist = new_dist
        if old_dist > new_dist:
            self.sift_up(i)
        else:
            self.sift_down(i)
        node.dist = new_dist

    def empty(self):
        return len(self.heap) == 0

    def sift_down(self, i):
        while True:
            i_dn = i
            l_id = MinHeap.lchild(i)
            if l_id < len(self) and self.heap[l_id] < self.heap[i]:
                i_dn = l_id
            r_id = MinHeap.rchild(i)
            if r_id < len(self) and self.heap[r_id] < self.heap[i_dn]:
                i_dn = r_id
            if i_dn == i:
                break
            self.ref[self.heap[i]] = i_dn
            self.ref[self.heap[i_dn]] = i
            self.heap[i_dn], self.heap[i] = self.heap[i], self.heap[i_dn]
            i = i_dn

    def sift_up(self, i):
        while i > 0:
            ip = MinHeap.parent(i)
            if self.heap[ip] > self.heap[i]:
                self.ref[self.heap[i]] = ip
                self.ref[self.heap[ip]] = i
                self.heap[ip], self.heap[i] = self.heap[i], self.heap[ip]
                i = ip
            else:
                break


class Graph:
    class Edge:
        def __init__(self, node1, node2, data=None):
            self.node1 = node1
            self.node2 = node2
            self.data = data

        def next_node(self, node):
            return self.node2 if node == self.node1 else self.node1

    class Node:
        def __init__(self, idx, data=None):
            self.edges = []  # edges to adjacent nodes
            self.idx = idx  # idx in array of nodes
            self.data = data
            self.reset()

        def reset(self):
            self.dist = sys.maxsize
            self.prev = None

        def __lt__(self, other):
            if self.dist == None and other.dist == None:
                return False
            elif self.dist == None:
                return False
            elif other.dist == None:
                return True
            return self.dist < other.dist

    def __init__(self, directed = False, n_nodes = 0):
        self.directed = directed
        self.nodes = [Graph.Node() for _ in range(n_nodes)]

    def add_node(self, data = None):
        idx = len(self.nodes)
        node = Graph.Node(idx, data)
        self.nodes.append(node)
        return node

    def add_edge(self, node1, node2, data = None):
        edge = Graph.Edge(node1, node2, data)
        node1.edges.append(edge)
        if not self.directed:
            node2.edges.append(edge)

    def reset(self):
        for node in self.nodes:
            node.reset()

    def find_shortest_paths(self, source, dest = None):
        '''
        Find shortest paths from source node to all other nodes
        :return:
        '''
        self.reset()  # clear prev results
        Q = deque([source])  # queue of discovered nodes
        source.dist = 0
        while Q:
            node = Q.popleft()
            for edge in node.edges:
                nxt_node = edge.next_node(node)
                if nxt_node.dist == sys.maxsize:
                    nxt_node.dist = node.dist + 1
                    nxt_node.prev = node
                    Q.append(nxt_node)

        if dest is not None:
            path = [dest]
            node = dest
            while node.prev is not None:
                node = node.prev
                path.insert(0, node)
            return path
        else:
            return []  # no specific destination set

    def dijkstra(self, source, dest):
        '''
        :param source:
        :param dest:
        :return:
        '''
        self.reset()
        source.dist = 0
        H = MinHeap( self.nodes )
        while not H.empty():
            min_node = H.pop_min()
            for edge in min_node.edges:
                nxt_node = edge.next_node(min_node)
                # relaxing
                if nxt_node.dist > min_node.dist + edge.data:
                    nxt_node.prev = min_node
                    H.change_priority( nxt_node, min_node.dist + edge.data)

        path = [dest]
        node = dest
        while node.prev is not None:
            node = node.prev
            path.append(node)

        return list(reversed(path))


g = Graph()

n0 = g.add_node(0)
n1 = g.add_node(1)
n2 = g.add_node(2)
n3 = g.add_node(3)

g.add_edge(n0,n1,3)
g.add_edge(n0,n2,1)
g.add_edge(n1,n2,1)
g.add_edge(n1,n3,1)

#path = g.find_shortest_paths(n0, n3)
path = g.dijkstra(n0,n3)

pass


