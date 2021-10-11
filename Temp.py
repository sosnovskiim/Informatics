n = int(input())
s = input()
x = 0
s1 = [0] * n
for i in range(n):
    s1[i] = s[i]
for i in range(1, n):
    if s1[i] < s1[i - 1]:
        s1[i] = s1[i - 1]
        x += 1
print(x)
print(*s1, sep='')
