q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    a = [int(ai) for ai in input().split()]
    mn = min(a)
    mx = max(a)
    if mx - mn > 2 * k:
        print(-1)
    else:
        print(mn + k)
