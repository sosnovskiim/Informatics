n, a, b = map(int, input().split())
na, nb = 1, 2
mn = n
while n >= a + nb * b:
    for na in range(1, nb):
        tmp = a * na + b * nb
        if tmp <= n:
            tmp1 = n - tmp
            if tmp1 < mn:
                mn = tmp1
        else:
            break
    nb += 1
print(mn)
