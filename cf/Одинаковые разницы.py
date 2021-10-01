t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    for i in range(n):
        if a[i] - i in d:
            d[a[i] - i] += 1
        else:
            d[a[i] - i] = 1
    sm = 0
    for x in d.keys():
        sm += d[x] * (d[x] - 1) // 2
    print(sm)
