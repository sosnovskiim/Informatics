n = int(input())
s = 3
for i in range(n):
    w = int(input())
    if w == s:
        print('NO')
        break
    else:
        s = 6 - w - s
if w != s:
    print('YES')
