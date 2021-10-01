x = list(input())
for i in range(len(x)):
    d = int(x[i])
    if d > 4 and not (i == 0 and d == 9):
        x[i] = str(9 - d)
print(*x, sep='')
