n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
s = 0
for i in range(0, n - 1, 2):
    s += a[i + 1] - a[i]
print(s)
