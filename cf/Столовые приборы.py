import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
g = a[:]
t = list(set(g))
g = []
for x in t:
    g.append(a.count(x))
p = max(g)
print((math.ceil(p / k) * len(t) * k) - n)
