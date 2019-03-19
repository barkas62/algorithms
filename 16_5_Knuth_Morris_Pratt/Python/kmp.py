def KMP(pattern : str, target : str) -> 'List[int]':
    np = len(pattern)
    joined = pattern + '$' + target
    pf = prefix_function(joined)
    return [i - 2*np for i in range(np+1, len(joined)) if pf[i] == np]


def prefix_function(string : str) -> 'List[int]':
    n = len(string)
    pf = [0]*n
    bord = 0
    for i in range(1, n):
        while bord > 0 and string[i] != string[bord]:
            bord = pf[bord-1]
        if string[i] == string[bord]:
            bord += 1
        else:
            bord = 0
        pf[i] = bord
    return pf


s = "abababcaab"

p = "abra"
t = "abracadabra"

pf = prefix_function(s)

res = KMP(p, t)

pass
