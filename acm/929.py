import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
k = int(input())
c = 1
while c < n:
    if k != 5:
        k += 1
    else:
        k = 1
    c += 1
print(k)
