t, s, n = input(), input(), int(input())
sn = s * n
sn_ln = len(sn)
t_ln = len(t)
cnt = 0
for i in range(sn_ln - t_ln + 1):
    if i + t_ln - 1 < sn_ln:
        sl = sn[i:i + t_ln]
        if t == sl:
            cnt += 1
    else:
        break
print(cnt)
