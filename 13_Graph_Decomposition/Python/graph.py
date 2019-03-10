class Vert:
    ''' Graph Vertex '''
    def __init__(self, id):
        '''
        :param id: vert id, for debug
        '''
        self.id = id
        self.edges = []  # edges
        self.data  = {}  # attached data: { data_type : data }

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_data(self, typeData):
        self.data[typeData] = typeData()

    def get_data(self, typeData):
        return self.data[typeData] if typeData in self.data else None


class Edge:
    ''' Graph Edge '''
    def __init__(self, v1, v2):
        '''
        Edge connecting vertexes v1 and v2
        '''
        self.v1 = v1
        self.v2 = v2

    def other(self, v):
        '''
        Returns vertex connected to v.
        None if nether v1 or v2 is v
        '''
        if v == self.v1:
            return self.v2
        elif v == self.v2:
            return self.v1
        else:
            return None


        # dfs_data: to be kept on vertexes
class dfs_data:
    def __init__(self):
        self.visited  = False
        self.cc_id    = -1
        self.beg_time = -1
        self.end_time = -1

class Graph:
    '''
    Graph: directed or not
    '''
    def __init__(self, nV, directed = False):
        self.directed = directed # is it a directed graph
        self.nV = nV  # number of verts in graph
        self.verts = [Vert(i) for i in range(nV)] # init verts in graph

    def add_edge(self, iv1, iv2):
        '''
        Connect vertexes with indexes iv1 and iv2
        '''
        assert (iv1 >= 0 or iv1 < self.nV or
                iv2 >= 0 or iv2 < self.nV), 'Out or range!'
        assert iv1 != iv2, 'Ring edges are not allowed!'

        e = Edge(self.verts[iv1], self.verts[iv2])
        self.verts[iv1].add_edge(e)
        if not self.directed:
            self.verts[iv2].add_edge(e)

    def add_vert_data(self, typeData):
        '''
        Add instance of typeData to all vertexes
        '''
        for v in self.verts:
            v.add_data(typeData)

    def dfs(self):
        '''
        Deep first search
        :return: number of connected components
        '''
        self.add_vert_data(dfs_data)

        def is_visited(v):
            '''
            check if vertex v is visited
            '''
            d = v.get_data(dfs_data)
            assert d, 'Missing vertex dfs_data'
            return d.visited

        def explore(v, cc_id, time):
            '''
            Exploring vertex v.
            :param v     : vertex to explore
            :param cc_id : id of current connected component
            :param time  : current time
            :return      : current time
            '''
            d = v.get_data(dfs_data)
            d.cc_id = cc_id
            d.visited = True
            d.beg_time = time
            time += 1
            for e in v.edges:
                w = e.other(v)
                assert w, 'Bad graph structure!'
                if not is_visited(w):
                    time = explore(w, cc_id, time)
            d.end_time = time
            time += 1
            return time
        # running dfs
        cc_id = 0
        time = 0
        for v in self.verts:
            if not is_visited(v):
                time = explore(v, cc_id, time)
                cc_id += 1
        return cc_id
    # end of dfs

    def isDAG(self):
        '''
        checks if it is a DAG
        '''
        assert self.directed, 'Graph is not directed!'
        self.dfs()

        def is_back_edge(e):
            d1 = e.v1.get_data(dfs_data)
            d2 = e.v2.get_data(dfs_data)
            assert d1 and d2, 'Dfs data unavailable!'
            # check if v1 is ancestor of v2
            return d2.beg_time < d1.beg_time and d1.end_time < d2.end_time

        for v in self.verts:
            for e in v.edges:
                if is_back_edge(e):
                    return False
        return True

    def topological_sort(self):
        if not self.isDAG():
            return []

        def get_postorder_time( v ):
            d = v.get_data(dfs_data)
            assert d, 'Dfs data unavailable!'
            return d.end_time

        self.verts.sort(key=get_postorder_time, reverse=True)
        return [v.id for v in self.verts]

if __name__ == '__main__':
    G = Graph(7)

    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(0, 2)
    G.add_edge(3, 4)
    G.add_edge(5, 6)

    nConnComp = G.dfs()

    G = Graph(3, True)
    G.add_edge(0, 1)
    G.add_edge(2, 1)
    G.add_edge(0, 2)

    order = G.topological_sort()

    pass








