t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(ai) for ai in input().split()]
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        tmp = (i + 1) * a[i]
        if tmp > ans:
            ans = tmp
    print(ans)
