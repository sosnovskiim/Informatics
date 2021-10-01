import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
n = int(input())
s = input().lower()
index_d = 0
index_t = 0
index_p = 0
for i in range(n):
    if s[i] == 'd':
        for j in range(i + 1, n):
            if s[j] == 't':
                for k in range(j + 1, n):
                    if s[k] == 'p':
                        index_d = i + 1
                        index_t = j + 1
                        index_p = k + 1
                        break
print(index_d, index_t, index_p)
