from collections import deque

class Network:
    class Vert:
        def __init__(self):
            self.edges = {} # next_vert_id : data
            self.pred  = None  # predecessor vert

    class Edge:
        def __init__(self, capacity):
            self.c = capacity
            self.f = 0

    class REdge:
        def __init__(self, edge, forward=True):
            self.edge = edge
            self.forward = forward
            self.update_capacity()

        def update_capacity(self):
            self.c = self.edge.c - self.edge.f if self.forward else self.edge.f


    def __init__(self, n_vert):
        self.verts = [Network.Vert() for _ in range(n_vert)]

    def add_edge(self, i, j, capacity):
        v_from = self.verts[i]
        v_to   = self.verts[j]
        v_from.edges[v_to] = Network.Edge(capacity)


    def get_max_flow(self, src_id, snk_id):
        max_flow = 0
        self.set_residual_graph()
        while self.find_augmenting_path(src_id, snk_id):
            df = self.augment_flow(snk_id)
            max_flow += df
            self.update_residual_graph()
        self.del_residual_graph()
        return max_flow


    def set_residual_graph(self):
        for v in self.verts:
            v.r_edges = {}
        for vi in self.verts:
            for vj, e in vi.edges.items():
                vi.r_edges[vj] = Network.REdge(e, forward=True)
                vj.r_edges[vi] = Network.REdge(e, forward=False)


    def find_augmenting_path(self, src_id, snk_id):
        for v in self.verts:
            v.pred = None
        q = deque()
        src = self.verts[src_id]
        snk = self.verts[snk_id]
        q.append(src)
        src.pred = src
        while len(q) and snk.pred is None:
            cur = q.popleft()
            for nxt, e in cur.r_edges.items():
                if e.c > 0 and nxt.pred is None:
                    nxt.pred = cur
                    if nxt == snk:
                        break
                    q.append(nxt)
        return snk.pred is not None

    def augment_flow(self, snk_id):
        bn = -1 # bottleneck
        cur = self.verts[snk_id]
        while cur.pred != cur:
            prv = cur.pred
            redge = prv.r_edges[cur]
            if bn == -1:
                bn = redge.c
            else:
                bn = min(bn, redge.c)
            cur = prv

        cur = self.verts[snk_id]
        while cur.pred != cur:
            prv = cur.pred
            redge = prv.r_edges[cur]
            if redge.forward:
                redge.edge.f += bn
            else:
                redge.edge.f -= bn
            cur = prv
        return bn

    def update_residual_graph(self):
        for v in self.verts:
            for redge in v.r_edges.values():
                redge.c = redge.edge.c - redge.edge.f if redge.forward else redge.edge.f

    def del_residual_graph(self):
        for v in self.verts:
            del v.r_edges


net = Network(4)
net.add_edge(0,1,3)
net.add_edge(1,2,2)
net.add_edge(0,3,1)
net.add_edge(3,2,2)
net.add_edge(1,3,2)

res = net.get_max_flow(0,2)

pass