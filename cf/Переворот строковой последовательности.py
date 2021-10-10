n = int(input())
ans = [0] * n
for i in range(n):
    a = input()
    ans[n - i - 1] = a
for i in ans:
    print(i)
