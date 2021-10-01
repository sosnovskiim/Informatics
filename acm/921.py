import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a = int(input())
b = int(input())
if b % 2 != 0 and a < 0:
    print(-1)
elif a == 0:
    print(0)
else:
    print(1)
