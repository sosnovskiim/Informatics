n, k = map(int, input().split())
sieve = [0] * 2 + [1] * n
primes = []
for i in range(n + 1):
    if sieve[i]:
        for j in range(i ** 2, n + 1, i):
            sieve[j] = 0
        primes.append(i)

cnt = 0
j = 0
for p in primes:
    while j + 1 < len(primes) and p > primes[j] + primes[j + 1] + 1:
        j += 1
    if j + 1 < len(primes) and p == primes[j] + primes[j + 1] + 1:
        cnt += 1
if cnt >= k:
    print('YES')
else:
    print('NO')
