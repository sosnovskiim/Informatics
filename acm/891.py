import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')

n = int(input())
a = input().split()
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 0
for i in range(n):
    if a[i] == '29':
        a[i] = '28'
        cnt += 1
if cnt <= 1 and ' '.join(a) in ' '.join(map(str, m * 3)):
    print('Yes')
else:
    print('No')
