
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
    x1 = x[:split_idx]
    x2 = x[split_idx:]

    # recurse to sort both halves
    x1 = mergesort(x1)
    x2 = mergesort(x2)

    # merge x1 and x2
    i = 0; i1 = 0; i2 = 0
    while i1<len(x1) and i2 < len(x2):
        if x1[i1] < x2[i2]:
            x[i] = x1[i1]; i1 += 1
        else:
            x[i] = x2[i2]; i2 += 1
        i += 1
    if i1<len(x1):
        x[i:] = x1[i1:]
    elif i2<len(x2):
        x[i:] = x2[i2:]

    return x


x = [3,2,5,1,8,5,2,1]
x = mergesort(x)

# s = 'fhaknciwnc'
# s = mergesort(s) Not working because s in unmutable => 'x[] =' does not work

pass


