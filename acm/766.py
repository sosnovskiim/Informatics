import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
n = int(input())
h = [int(i) for i in input().split()]
for i in range(n):
    ai = 0
    if i < n - 1:
        mx = max(h[i + 1:])
        if h[i] <= mx:
            ai = mx - h[i] + 1
    print(ai, end=' ')
