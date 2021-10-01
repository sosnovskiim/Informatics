import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, a, b = int(input()), int(input()), int(input())
s = input()
p = [int(s[i]) for i in range(n)]
ar = []
br = []
ac = 0
bc = 0

if a > 0:
    i = 0
    while i < n - 1 and ac < a:
        if p[i] == 0 and p[i + 1] == 0:
            p[i] = 1
            p[i + 1] = 1
            ar.append(str(i + 1) + ' ' + str(i + 2))
            ac += 1
        i += 1
    i = 0
    while i < n and bc < b:
        if p[i] == 0:
            p[i] = 1
            br.append(str(i + 1))
            bc += 1
        i += 1
    if ac < a or bc < b:
        print('NO')
    else:
        print('YES')
        print(*ar, sep='\n')
        print(*br, sep='\n')
else:
    i = 0
    while i < n and bc < b:
        if p[i] == 0:
            p[i] = 1
            br.append(str(i + 1))
            bc += 1
        i += 1
    if bc < b:
        print('NO')
    else:
        print('YES')
        print(*br, sep='\n')
