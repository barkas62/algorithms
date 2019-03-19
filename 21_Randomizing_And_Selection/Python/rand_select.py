import random

# Knuth shuffle (Fisher-Yates)
def shuffle(a: 'List') -> None:
    n = len(a)
    if n <= 1:
        return
    for i in range(n-1):
        j = random.randint(i, n-1)
        a[i], a[j] = a[j], a[i]
    return

arr = ['one', 'two', 'three', 4, 5, 'six', 'seven']

shuffle(arr)

pass

def select_k(a: 'List', k : int)-> 'List[0..k-1]':
    n = len(a)
    if n < k:
        return []
    reservoir = a[:k]
    for i in range(k,n):
        j = random.randint(0,i)
        if j < k:
            reservoir[j] = a[i]
    return reservoir


a = [i for i in range(100)]
k = 5
samples = select_k(a, 5)

pass





