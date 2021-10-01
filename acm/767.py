import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=False)
prev = 0
for i in range(n):
    print(a[i] - prev, end=' ')
    prev = a[i]
