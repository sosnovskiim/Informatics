# не доделана
import math
import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')

x, y = [0, 0, 0], [0, 0, 0]
x[0], y[0], x[1], y[1], x[2], y[2] = map(int, input().split())
s = x[0] * y[0] + x[1] * y[1] + x[2] * y[2]
c = ['A', 'B', 'C']
l = math.sqrt(s)
if l ** 2 != s:
    print(-1)
else:
    f = True
    for i in range(3):
        if x[i] > l or y[i] > l:
            print(-1)
            f = False
            break
    if f:
