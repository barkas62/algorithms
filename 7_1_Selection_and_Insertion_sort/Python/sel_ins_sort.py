import random
import time

def sel_sort(a : list):
    if not a:
        return
    n = len(a)
    for i in range(n-1):
        min_j = i
        min_a = a[i]
        for j in range(i+1,n):
            if a[j] < min_a:
                min_a = a[j]
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]

def sel_sort1(a : list):
    if not a:
        return
    n = len(a)
    for i in range(n-1):
        min_a, min_i = min(zip(a[i:n], range(i,n)))
        a[i], a[min_i] = a[min_i], a[i]


def ins_sort(a : list):
    for i, ai in enumerate(a):
        j = i
        while j > 0 and a[j-1] > ai:
            a[j] = a[j-1]
            j -= 1
        a[j] = ai

def ins_sort1(a : list):
    for i, ai in enumerate(a):
        j = i
        while j > 0 and a[j-1] > ai:
            j -= 1
        del a[i]
        a.insert(j,ai)


n = 20000
a = [random.randint(0,100) for i in range(n)]

beg = time.time()
ins_sort1(a)
end = time.time()

print(f'Time elapsed: %d' % (end-beg,))

pass
