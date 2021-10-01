n, m, x, y = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]
result = []

i = 0
j = 0
while i < n and j < m:

    if a[i] - x <= b[j] <= a[i] + y:
        result.append([i + 1, j + 1])
        i += 1
        j += 1
        continue

    if a[i] + y < b[j]:
        i += 1
        continue

    if a[i] - x > b[j]:
        j += 1
        continue

print(len(result))
for raw in result:
    print(*raw)
