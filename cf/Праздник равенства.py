n = int(input())
a = [int(i) for i in input().split()]
mx = max(a)
s = 0
for i in range(n):
    s += mx - a[i]
print(s)
