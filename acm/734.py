import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')
s = list(input())
cnt2, cnt3, cnt4, cnt5 = 0, 0, 0, 0

i = 0
while s:

    if s[i] == '0':
        cnt2 += 1
        del s[0]
        continue

    if s[i + 1] == '1':
        cnt5 += 1
        del s[0:2]
        continue

    if s[i + 2] == '0':
        cnt3 += 1
        del s[0:3]
        continue

    if s[i + 2] == '1':
        cnt4 += 1
        del s[0:3]
        continue

mx = max(cnt2, cnt3, cnt4, cnt5)
for _ in range(1):

    if mx == cnt2:
        print('2')
        break

    if mx == cnt3:
        print('3')
        break

    if mx == cnt4:
        print('4')
        break

    if mx == cnt5:
        print('5')
        break
