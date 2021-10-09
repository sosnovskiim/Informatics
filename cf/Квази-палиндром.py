x = input()
x = x[::-1]
z = 0
for i in range(len(x)):
    if x[i] != '0':
        z = i
        break
x = x[z:]
if x == x[::-1]:
    print('YES')
else:
    print('NO')
