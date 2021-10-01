t = int(input())
for _ in range(t):
    s = input()
    cnt0 = 0
    cnt1 = 0
    for i in range(len(s)):
        if s[i] == '0':
            cnt0 += 1
            continue
        if s[i] == '1':
            cnt1 += 1
            continue
    if min(cnt0, cnt1) % 2 != 0:
        print('DA')
    else:
        print('NET')
