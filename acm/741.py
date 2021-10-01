import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
n = int(input())
a = list(map(int, input().split()))
ans, ans_l, ans_r, ln, minus_pos = 0, 0, 0, 0, 0
if n != 1:
    for r in range(1, n):
        if a[r] > a[r - 1]:
            ln += 1

            if ln >= ans:
                ans = ln
                ans_l = minus_pos
                ans_r = r

        else:
            ln = 0
            minus_pos = r

if ans_l != ans_r:
    print(ans_l + 1, ans_r + 1)
else:
    print(n, n)
