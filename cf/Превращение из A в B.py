a, b = map(int, input().split())
k = 1
j = [b]
while b > a:
    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b // 2
    else:
        break
    k += 1
    j.append(b)
if b == a:
    print('YES')
    print(k)
    print(*j[::-1])
else:
    print('NO')
