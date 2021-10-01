def is_prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num


n = int(input())
for i in range(n, 2 * n + 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)
