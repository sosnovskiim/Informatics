import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
x1, x2, x, y = map(int, input().split())
ty = y
tx = 0
if x < x1:
    tx = int((x1 - x) / 0.25)
elif x2 < x:
    tx = int((x - x2) / 0.25)
t = ty + tx
print(t)
