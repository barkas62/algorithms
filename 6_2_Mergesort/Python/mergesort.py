
def mergesort( x ):
    '''
    Mergesort of a MUTABLE sequence.
    Elements of a sequence must support __lt__
    O(n) additional memory
    :param x: input sequence
    :return:  in-place sorted sequence
    '''
    if len(x) <= 1:
        return x
    # split into 2 halves
    split_idx = len(x)//2

    # recurse to sort both halves
    x1 = mergesort(x[:split_idx])
    x2 = mergesort(x[split_idx:])

    # merge x1 and x2
    i = i1 = i2 = 0

    while i1 < len(x1) and i2 < len(x2):
        if x1[i1] < x2[i2]:
            x[i] = x1[i1]
            i1 += 1
        else:
            x[i] = x2[i2]
            i2 += 1
        i += 1

    if i1 < len(x1):
        x[i:] = x1[i1:]
    elif i2 < len(x2):
        x[i:] = x2[i2:]

    return x


import random

x = [3,2,5,1,8,5,2,1]
x = mergesort(x)

n_test = 10

a = [random.randrange(0, n_test) for _ in range(2*n_test)]
a_stable = [(val, i) for i, val in enumerate(a)]

a_sorted = mergesort(a_stable)

for i in range(len(a_sorted)-1):
    if a_sorted[i][0] > a_sorted[i+1][0]:
        print("Sort test failed!")
    if a_sorted[i][0] == a_sorted[i+1][0]:
        if a_sorted[i][1] > a_sorted[i+1][1]:
            print('Stability test failed!')
            break
else:
    print('Sort and Stability test OK')

s = 'fhaknciwnc'
s = mergesort(s) #Not working because s in unmutable => 'x[] =' does not work

pass


