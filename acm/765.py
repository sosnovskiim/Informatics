import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
a, b = map(int, input().split())
days1 = min(a, b)
days2 = (max(a, b) - days1) // 2
print(days1, days2)
