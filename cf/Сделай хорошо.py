t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(ai) for ai in input().split()]
    p = n - 1
    while p > 0 and a[p - 1] >= a[p]:
        p -= 1
    while p > 0 and a[p - 1] <= a[p]:
        p -= 1
    print(p)
