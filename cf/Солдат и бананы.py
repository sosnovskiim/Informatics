k, n, w = map(int, input().split())
s = 0
i = 1
while i <= w:
    s += i * k
    i += 1
if n >= s:
    print('0')
else:
    print(s - n)
