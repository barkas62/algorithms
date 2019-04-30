import random

def partition(x, b, e):
    m = random.randint(b,e-1) #pivot
    pivot = x[m]
    x[b],x[m] = x[m],x[b]
    m = b   # position of a pivot: all to the left <= pivot; all to the right > pivot
    for i in range(b+1,e):
        xi = x[i]
        if xi < pivot:
            m += 1
            x[m], x[i] = x[i], x[m]   # m points to rightmost elem which is < pivot
    x[b], x[m] = x[m], x[b]
    return m

def fat_partition(x, b, e):
    m = random.randint(b, e-1)
    pivot = x[m]
    x[b],x[m] = x[m],x[b]
    m1 = b # start of '=' range
    m2 = b # start of '>' range
    for i in range(b+1,e):
        xi = x[i]
        if xi < pivot:
            m2 += 1
            x[m2], x[i ] = x[i ], x[m2]
            m1 += 1
            x[m2], x[m1] = x[m1], x[m2]
        elif x[i] == pivot:
            m2 += 1
            x[m2], x[i] = x[i], x[m2]

    x[b], x[m1] = x[m1], x[b]
    return m1,m2


def quicksort(x, b = 0, e = -1):
    if e == -1:
        e = len(x)
    if b>=e:
        return
    m = partition(x, b, e )
    quicksort(x, b, m)
    quicksort(x, m+1, e)

def quicksort2(x, b = 0, e = -1):
    if e == -1:
        e = len(x)
    if b>=e:
        return
    m1,m2 = fat_partition(x, b, e )
    quicksort2(x, b, m1)
    quicksort2(x, m2+1, e)

random.seed(0)
x = [3,1,7,2,8,5,4,2,2,2,2,1,2,1,1,7]
quicksort2(x)

pass