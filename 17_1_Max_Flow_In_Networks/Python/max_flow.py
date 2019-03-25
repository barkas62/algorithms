from collections import deque

class Edge:
    def __init__(self, vert_from, vert_to, Capacity):
        self.vert_from = vert_from
        self.vert_to = vert_to
        self.C = Capacity
        self.f = 0

    def get_next(self, vert_id):
        if vert_id == self.vert_from:
            return self.vert_to
        elif vert_id == self.vert_to:
            return self.vert_from
        else:
            raise Exception('Bad struct')

    def get_residual(self, vert_id):
        return self.C - self.f if vert_id == self.vert_from else self.f

    def update_flow(self, vert_id, df):
        if vert_id == self.vert_from:
            self.f += df
        else:
            self.f -= df

class Network:
    def __init__(self, n_vert):
        self.verts = [{} for _ in range(n_vert)]
        self.parent_id = [-1]*n_vert

    def add_edge(self, i, j, Capacity):
        e = Edge(i, j, Capacity)
        self.verts[i][j] = e
        self.verts[j][i] = e

    def get_max_flow(self, src_id, snk_id):
        '''
        Fulkerson-Ford algorithm
        '''
        max_flow = 0
        while self.find_path(src_id, snk_id):  # DFS: max_flow*E in worst case;
            df = self.augment(snk_id)
            if df == 0:
                break
            max_flow += df
        return max_flow

    def find_path(self, src_id, snk_id):
        # BFS: Edmonds - Karp
        self.parent_id = [-1] * len(self.verts)
        q = deque()
        q.append(src_id)
        self.parent_id[src_id] = src_id
        while len(q):
            vert_id = q.popleft()
            for e in self.get_edges(vert_id):
                next_id = e.get_next(vert_id)
                if self.parent_id[next_id] == -1:
                    self.parent_id[next_id] = vert_id
                    q.append(next_id)
        return  self.parent_id[snk_id] != -1

    def augment(self, snk_id):
        # follow path and find bottleneck
        vert_id = snk_id
        bottleneck = -1
        while self.parent_id[vert_id] != vert_id:
            from_id = self.parent_id[vert_id]
            e = self.verts[from_id][vert_id]
            res = e.get_residual(from_id )
            if bottleneck == -1:
                bottleneck = res
            else:
                bottleneck = min(bottleneck, res)
            vert_id = from_id

        vert_id = snk_id
        while self.parent_id[vert_id] != vert_id:
            from_id = self.parent_id[vert_id]
            e = self.verts[from_id][vert_id]
            e.update_flow( from_id, bottleneck )
            vert_id = from_id

        return bottleneck

    def get_edges(self, vert_id):
        for e in self.verts[vert_id].values():
            Capacity = e.get_residual(vert_id)
            if Capacity > 0:
                yield e


net = Network(4)
net.add_edge(0,1,3)
net.add_edge(1,2,2)
net.add_edge(0,3,2)
net.add_edge(3,2,1)
net.add_edge(1,3,2)

res = net.get_max_flow(0,3)

pass

