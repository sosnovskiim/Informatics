n = int(input())
a = [int(ai) for ai in input().split()]
a1 = [0 for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if a[i] == a[j]:
            a1[i] += 1
mx = 0
for k in range(n):
    mx = max(mx, a1[k])
print(mx)
