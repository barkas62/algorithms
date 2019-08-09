from random import randint
def RabinCarp( P : 'str', T : 'str' ) -> 'List[pos_of_P_in_T]':
    n = len(T)
    m = len(P)
    if n < m or m == 0:
        return []

    q = 1<<31 - 1 # mersenne prime
    d = 256       # base for ASCI
    d = randint(2, q-1)

    h = 1
    for i in range(1,m):
        h = (h * d) % q

    hp = ord(P[0])
    ht = ord(T[0])
    for i in range(1, m):
        hp = (ord(P[i]) + h * hp) % q
        ht = (ord(T[i]) + h * ht) % q

    match_idx = []
    for i in range(0, n-m+1):
        if hp == ht and T[i:i+m] == P:
            match_idx.append(i)
        # compute ht for next match, but not if this one is last
        if i != n-m:
            ht = (ht - h*ord(T[i]))*d + ord(T[i+m])

    return match_idx

t = 'abcbc'
p = 'bc'

res = RabinCarp( p, t )

pass


