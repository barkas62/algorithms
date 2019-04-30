def edit_dist(str1 : str, str2 : str) -> int:
    n1 = len(str1)
    n2 = len(str2)
    if n1==0 or n2==0:
        return max(n1,n2)

    dist = [[0]*(n2+1) for _ in range(n1+1)]

    for i in range(1, n1+1):
        dist[i][0] = i
    for j in range(1, n2+1):
        dist[0][j] = j

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if str1[i-1] == str2[j-1]:
                dist[i][j] = dist[i-1][j-1]  #match
            else:
                dist[i][j] = 1 + min(dist[i-1][j-1],  # replace
                                     dist[i-1][j],    # remove
                                     dist[i][j-1])    # insert

    return dist[n1][n2]


s1 = 'editing'
s2 = 'distance'

res = edit_dist(s1,s2)

pass