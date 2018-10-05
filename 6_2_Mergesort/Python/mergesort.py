
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
    i = 0
    while x1 and x2:
        if x1[0] < x2[0]:
            x[i] = x1.pop(0)
        else:
            x[i] = x2.pop(0)
        i += 1
    if x1:
        x[i:] = x1
    elif x2:
        x[i:] = x2

    return x

x = [3,2,5,1,8,5,2,1]
x = mergesort(x)

# s = 'fhaknciwnc'
# s = mergesort(s) Not working because s in unmutable => 'x[] =' does not work

pass


