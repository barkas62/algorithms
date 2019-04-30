class Vert:
    def __init__(self):
        self.edges = []

    def get_out_edges(self):
        for e in self.edges:
            if e.v1 == self:
                yield e


class Edge:
    def __init__(self, v1, v2, capacity):
        self.v1 = v1
        self.v2 = v2
        self.f = 0
        self.c = capacity

    def get_other_vert(self, v):
        return self.v2 if v == self.v1 else self.v1

    def get_residual_capacity(self, from_v):
        return self.c - self.f if from_v == self.v1 else self.f


class Network:
    def __init__(self, n_vert):
        self.verts = [Vert() for _ in range(n_vert)]

    def add_edge(self, i1, i2):
        v1 = self.verts[i1]
        v2 = self.verts[i2]
        e12 = Edge(v1, v2)
        v1.edges.append(e12)
        v2.edges.append(e12)

    def push_relabel(self, src, snk):
        self.vsrc = self.verts[src]
        self.vsnk = self.verts[snk]

        self.init_preflow()
        done = False
        while not done:
            done = True
            for u in self.verts:
                if u.e <= 0:
                    continue # this vert is not overflowing
                if self.push_flow(u) or self.relabel(u):
                    done = False
        return self.get_flow()

    def init_preflow(self):
        for v in self.verts:
            v.h = 0 # height
            v.e = 0 # excess flow

        self.vsrc.h = len(self.verts)
        for edge in self.vsrc.get_out_edges():
            edge.f = edge.c
            edge.v2.e   += edge.f
            self.vsrc.e -= edge.f

    def push_flow(self, u):
        for edge in u.edges:
            v = edge.get_other_vert(u)
            if v.h < u.h:
                cf = edge.get_residual_capacity(u)
                df = min(u.e, cf)
                edge.f += df
                u.e -= df
                v.e += df
                return True
        return False

    def relabel(self, u):
        if u.e <= 0:
            return False
        min_h = (2<<31) - 1
        for edge in u.edges.values():
            v = edge.get_other_vert(u)
            if v.h < u.h:
                return False
            min_h = min(min_h, v.h)
        u.h = 1 + min_h
        return True