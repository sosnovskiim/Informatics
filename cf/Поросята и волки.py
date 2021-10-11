n, m = map(int, input().split())
a = [[i for i in input()] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'P':
            if i != 0 and a[i - 1][j] == 'W':
                a[i][j] = '0'
                a[i - 1][j] = '0'
                cnt += 1
            elif j != 0 and a[i][j - 1] == 'W':
                a[i][j] = '0'
                a[i][j - 1] = '0'
                cnt += 1
            elif j != m - 1 and a[i][j + 1] == 'W':
                a[i][j] = '0'
                a[i][j + 1] = '0'
                cnt += 1
            elif i != n - 1 and a[i + 1][j] == 'W':
                a[i][j] = '0'
                a[i + 1][j] = '0'
                cnt += 1
print(cnt)
