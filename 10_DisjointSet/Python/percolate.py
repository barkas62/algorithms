import random

class DisSet:
    def __init__(self, n):
        self.arr = [i for i in range(n) ]
        self.rank = [0] * n

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if self.rank[pi] < self.rank[pj]:
            self.arr[pi] = pj
        else:
            self.arr[pj] = pi
            if self.rank[pi] == self.rank[pj]:
                self.rank[pi] += 1

    def find(self, i):
        if i != self.arr[i]:
            self.arr[i] = self.find( self.arr[i] )
        return self.arr[i]


def get_neibs(i, N):
    neibs = []
    r = i // N
    c = i % N
    if r > 0:
        neibs.append(i-1)
    if r < N-1:
        neibs.append(i+1)
    if r > 0:
        neibs.append(i-N)
    if r < N-1:
        neibs.append(i+N)
    return neibs


def is_percolate(grid, N):
    N2 = N*N
    ds = DisSet( N2+2 )
    for i in range(N2):
        if grid[i]:
            if i < N:
                ds.union(i, N2)
            if i > N2 - N - 1:
                ds.union(i, N2+1)
            neibs = get_neibs(i, N)
            for n in neibs:
                if grid[n]:
                    ds.union(i, n)

    return ds.find(N2) == ds.find(N2+1)

grid = [1,0,1,0]

#grid = [[1 if random.random() < p else 0 for _ in range(N)] for _ in range(N)]
res = is_percolate(grid, 2)

pass


