import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
k, s, n = map(int, input().split())
d = list(map(int, input().split()))
while k > 0 or not (s % 7 != 0 and s % 7 != 6 and s not in d):
    if s % 7 != 0 and s % 7 != 6 and s not in d:
        k -= 1
    s += 1
print(s)
