import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, a, b = int(input()), int(input()), int(input())

if a + b + a <= n:
    print(1)
elif a + a > n and a + b > n:
    print(3)
else:
    print(2)
