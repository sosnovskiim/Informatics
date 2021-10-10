mx = 2 * 10 ** 9
mn = -mx
n = int(input())
for _ in range(n):
    s, x, ans = input().split()
    x = int(x)

    if ans == 'N':
        if s == '<=':
            s = '>'
        elif s == '<':
            s = '>='
        elif s == '>=':
            s = '<'
        else:
            s = '<='

    if s == '>=':
        mn = max(mn, x)
    elif s == '>':
        mn = max(mn, x + 1)
    elif s == '<=':
        mx = min(mx, x)
    else:
        mx = min(mx, x - 1)

if mn <= mx:
    print(mn)
else:
    print('Impossible')
