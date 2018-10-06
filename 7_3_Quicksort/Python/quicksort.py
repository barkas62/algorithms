import random

def partition(x, b, e):
    m = random.randint(b,e-1) #pivot
    pivot = x[m]
    x[b],x[m] = x[m],x[b]
    m = b
    for i in range(b+1,e):
        if x[i] < pivot:
            m += 1
            x[m], x[i] = x[i], x[m]
    x[b], x[m] = x[m], x[b]
    return m

def quicksort(x, b = 0, e = -1):
    if e == -1:
        e = len(x)
    if b>=e:
        return
    m = partition(x, b, e )
    quicksort(x, b, m)
    quicksort(x, m+1, e)

x = [3,1,7,2,8,4,1,2,1,1]
quicksort(x)

pass