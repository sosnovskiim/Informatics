import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())
t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2
res_in_sec = t2 - t1
res_h = res_in_sec // 3600
res_m = (res_in_sec % 3600) // 60
res_s = (res_in_sec % 3600) % 60
print(res_h, res_m, res_s)
