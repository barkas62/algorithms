from sortedcontainers import SortedDict
import random
import time

def count_sort( x ):

    max_x = max(x)
    min_x = min(x)

    m = max_x - min_x + 1
    cnt = [0]*m
    pos = [0]*m

    for a in x:
        cnt[a-min_x] += 1

    for i in range(1,m):
        pos[i] = pos[i-1] + cnt[i-1]

    x_sorted = [0]*len(x)
    for a in x:
        x_sorted[ pos[a-min_x] ] = a
        pos[a-min_x] += 1

    return x_sorted

def count_sort2( x ):
    d = SortedDict( {a : [0,0] for a in x} )
    for a in x:
        d[a][0] += 1

    pos = 0
    for v in d.values():
        v[1] = pos         # position
        pos += v[0]        # update position using count

    x_sorted = [0]*len(x)
    for a in x:
        v = d[a]
        x_sorted[ v[1] ] = a
        v[1] += 1
    return x_sorted


x = [3,1,2,2,3,3,1,1,1]

nx = 4000000
x = [random.randint(0,nx) for _ in range(nx)]
beg = time.time()
x = count_sort(x)
end = time.time()

print('elapsed time: '+str(end-beg))

pass