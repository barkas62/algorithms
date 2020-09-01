import random

class DisSet:
    def __init__(self, n):
        self.arr = [i for i in range(n) ]
        self.weight = [1] * n

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if self.weight[pi] < self.weight[pj]:
            self.arr[pi] = pj
            self.weight[pj] += self.weight[pi]
        else:
            self.arr[pj] = pi
            self.weight[pi] += self.weight[pj]

    def find(self, i):
        if i != self.arr[i]:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]


def get_neibs(i, N):
    neibs = []
    r = i // N
    c = i % N
    if c > 0:
        neibs.append(i-1)
    if c < N-1:
        neibs.append(i+1)
    if r > 0:
        neibs.append(i-N)
    if r < N-1:
        neibs.append(i+N)
    return neibs


def can_percolate(grid, n):
    # n sites + source + sink
    source_id = n*n
    sink_id = n*n + 1
    ds = DisSet(n*n+2)
    # Connect first row to source (has index n*n)
    for c in range(n):
        if grid[c]:
            ds.union(c, source_id)
    # Connect left-to-right and to below
    for r in range(n-1):
        for c in range(n-1):
            i = r*n + c
            if grid[i]:
                if grid[i+1]:  # right
                    ds.union(i, i+1)
                if grid[i+n]:  # below
                    ds.union(i, i+n)
    # Connect last row to sink (has index n*n+1)
    for c in range(n*(n-1), n*n):
        if grid[c]:
            ds.union(c, sink_id)

    return ds.find(source_id) == ds.find(sink_id)

grid = [1,0,0,1]

N = 100
p = 0.58
grid = [1 if random.random() < p else 0 for _ in range(N*N)]

res = can_percolate(grid, N)

pass


