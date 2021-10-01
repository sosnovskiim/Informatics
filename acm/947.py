# не доделана
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n =
a = [int(i) for i in input().split()]
x = 0
s = 0
b = []
while x != n:
    mx = 0
    mxi = 0
    for i in range(n):
        if a[i] > mx and i + 1 not in b:
            mx = a[i]
            mxi = i
    s += mx * x + 1
    b.append(mxi + 1)
    x += 1
print(s)
print(*b)
