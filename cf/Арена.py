t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(ai) for ai in input().split()]
    print(n - a.count(min(a)))
