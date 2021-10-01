t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    lnb = len(str(b + 1))
    print(a * (lnb - 1))
