t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    x = min(n // k, m)
    print(x - min(n // k, (m - x + k - 2) // (k - 1)))
