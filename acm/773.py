import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
m, t = int(input()), int(input())
cnt = 0
while t < m:
    t *= 2
    cnt += 1
print(cnt)
