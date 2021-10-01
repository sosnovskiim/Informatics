# не доделана
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n =
p = [int(i) for i in input().split()]
c = 0
d = 1
i = 0
while p[i] != d:
    i += 1
d += 1
while d <= n:
    while p[i] != d:
        if i != n - 1:
            i += 1
        else:
            i = 0
        c += 1
    d += 1
print(c)
