n, k = int(input()), int(input())
cnt = 1
cnt_row = 1
is_odd = True
while cnt < k:
    r = n
    if not is_odd:
        r += 1
    for i in range(r):
        if cnt != k:
            cnt += 1
        else:
            print(cnt_row, i + 1)
            break
    cnt_row += 1
    if is_odd:
        is_odd = False
    else:
        is_odd = True
