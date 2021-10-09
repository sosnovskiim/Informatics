n, w = map(int, input().split())
a = [int(ai) for ai in input().split()]
mx, mn = 0, 0
cnt = 0
for i in range(n):
    cnt += a[i]
    mx = max(mx, cnt)
    mn = min(mn, cnt)
print(max(0, w - mx + mn + 1))
