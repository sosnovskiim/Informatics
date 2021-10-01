import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, a, b = int(input()), int(input()), int(input())
r = [0, 0]
while True:
    r[0] = (n - (b * r[1]))
    if r[0] >= 0:
        if r[0] % a == 0:
            print('YES')
            print(r[0] // a, r[1])
            break
    else:
        print('NO')
        break
    r[1] += 1
