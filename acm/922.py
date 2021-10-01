import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
m = int(input())
a = []

for i in range(n):
    a.append(int(input()))
mx = max(a) + m
mn = mx
i = 0
while m > 0:
    if i == n:
        i = 0
    if a[i] == min(a):
        a[i] += 1
        m -= 1
    i += 1
print(max(a), mx)
