t = int(input())
for _ in range(t):
    is_ok, mn, n = True, 10 ** 9, int(input())
    a, b = [], []

    for tmp in input().split():
        ai = int(tmp)
        a.append(ai)
        b.append(ai)
        mn = min(mn, ai)

    b.sort()

    for i in range(n):
        if a[i] != b[i] and a[i] % mn > 0:
            is_ok = False

    if is_ok:
        print('YES')
    else:
        print('NO')
