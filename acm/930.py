import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
s = input()
t = input()
result = 0
isFound = False
for i in range(n):
    if isFound:
        if s[i] != t[i - 1]:
            result = 0
            break
    else:
        if i == n - 1 or s[i] != t[i]:
            result = i + 1
            isFound = True
print(result)
