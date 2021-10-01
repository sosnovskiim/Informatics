import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
if n < 13:
    print(750 * n)
if n == 13:
    print((750 * 13) - 350)
if n > 13:
    x = 750 * n
    y = (n // 13) * 350
    print(x - y)
