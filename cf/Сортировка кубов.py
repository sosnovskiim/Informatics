t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(ai) for ai in input().split()]
    is_sort_possible = False
    for i in range(1, n):
        if a[i - 1] <= a[i]:
            is_sort_possible = True
            break
    if is_sort_possible:
        print('YES')
    else:
        print('NO')
