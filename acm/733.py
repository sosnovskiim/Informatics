import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
n, d = map(int, input().split())
t = list(map(int, input().split()))
cnt = 1
tmp = t[0]
for i in range(1, n):
    if tmp + d <= t[i]:
        cnt += 1
        tmp = t[i]
print(cnt)
