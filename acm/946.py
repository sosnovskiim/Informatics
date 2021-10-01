import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
s = list(input())
cnt_a = s.count('a')
cnt_b = s.count('b')

cnt = 0
for i in range(1, n, 2):
    if s[i] == 'a' and s[i - 1] == 'a':
        s[i] = 'b'
        cnt += 1
    elif s[i] == 'b' and s[i - 1] == 'b':
        s[i] = 'a'
        cnt += 1

print(cnt)
print(''.join(s))
