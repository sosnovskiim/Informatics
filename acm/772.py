import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
p = int(input())
cnt = 0
while p > 0:
    if p >= 100:
        p -= 100
    elif p >= 10:
        p -= 10
    else:
        p -= 1
    cnt += 1
print(cnt)
