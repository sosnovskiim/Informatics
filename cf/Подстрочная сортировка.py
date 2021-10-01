n = int(input())
s = [input() for _ in range(n)]
s.sort(key=len)
isPossible = True
for i in range(n - 1):
    if not s[i] in s[i + 1]:
        isPossible = False
        break
if isPossible:
    print('YES')
    print(*s, sep='\n')
else:
    print('NO')
