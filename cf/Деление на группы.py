n = int(input())
rows = []
col_sums = [0, 0, 0, 0, 0]
for i in range(n):
    rows.append(input().split())
    for j in range(5):
        col_sums[j] += int(rows[i][j])
students_in_group = n // 2
cnt = 0
for i in range(5):
    if col_sums[i] >= students_in_group:
        cnt += 1
if cnt >= 2:
    print('YES')
else:
    print('NO')
