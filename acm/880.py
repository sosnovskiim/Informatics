# import sys
#
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

a = int(input())
d = a % 10
if d == 0:
    print(a)
elif d < 5:
    print(a - d)
else:
    print(a + (10 - d))
