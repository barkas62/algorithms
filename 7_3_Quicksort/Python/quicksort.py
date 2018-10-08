import random

def partition(x, b, e):
    m = random.randint(b,e-1) #pivot
    pivot = x[m]
    x[b],x[m] = x[m],x[b]
    m = b   # position of a pivot: all to the left < pivot; all to the right >= pivot
    for i in range(b+1,e):
        if x[i] < pivot:
            m += 1
            x[m], x[i] = x[i], x[m]   # m points to rightmost elem which is < pivot
    x[b], x[m] = x[m], x[b]
    return m

def fat_partition(x, b, e):
    m = (b+e)//2 # random.randint(b, e - 1)
    pivot = x[m]
    x[b],x[m] = x[m],x[b]
    m1 = b+1 # start of '=' range
    m2 = b+1 # start of '>' range
    for i in range(b+1,e):
        if x[i] < pivot:
            x[m2], x[i ] = x[i ], x[m2]
            x[m2], x[m1] = x[m1], x[m2]
            m1 += 1
            m2 += 1
        elif x[i] == pivot:
            x[m1], x[i] = x[i], x[m1]
            m2 += 1
    m1 -= 1
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
    quicksort(x, b, m1)
    quicksort(x, m2+1, e)

x = [3,1,7,2,8,4,1,2,1,1]
quicksort2(x)

pass