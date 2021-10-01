import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
n, m = map(int, input().split())
ls = list(map(int, input().split()))
sls = set(ls)
counts = [ls.count(i) for i in sls]
res = 0
for c in counts:
    res += c * (n - c)
print(res // 2)
