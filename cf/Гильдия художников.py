m, n = map(int, input().split())
allT = []
for i in range(m):
    t = list(map(int, input().split()))
    allT.append(t)
    if i == 0:
        for j in range(1, n):
            allT[i][j] += allT[i][j - 1]
    else:
        allT[i][0] += allT[i - 1][0]
        for j in range(1, n):
            allT[i][j] += max(allT[i - 1][j], allT[i][j - 1])
for i in range(m):
    print(allT[i][n - 1], end=' ')
