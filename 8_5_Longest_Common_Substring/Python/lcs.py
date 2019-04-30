def lcs(str1 : str, str2 : str) ->str:
    if not str1 or not str2:
        return ''

    n1 = len(str1)
    n2 = len(str2)

    dp = [[(0,0,0)]*(n2+1) for _ in range(n1+1)] # (length, di, dj)

    for i in range(1,n1+1):
        for j in range(1, n2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = (dp[i-1][j-1][0]+1, 1, 1)
            else:
                if dp[i][j-1][0] > dp[i-1][j][0]:
                    dp[i][j] = (dp[i][j-1][0], 0, 1)
                else:
                    dp[i][j] = (dp[i-1][j][0], 1, 0)

    n12 = dp[n1][n2][0]
    s12 = [''] * n12
    i,j = n1, n2 # positions in str1, str2 (plus 1)
    while i > 0 and j > 0:
        i12, di, dj = dp[i][j]
        if di == dj:
            s12[i12-1] = str1[i-1]
        i -= di
        j -= dj

    return ''.join(s12)


s1 = 'editing'
s2 = 'distance'

res = lcs(s1, s2)

pass