t = int(input())
for _ in range(t):
    s = input()
    l1 = s.find('1')
    r1 = s.rfind('1')
    cnt = 0
    for d in s[l1:r1]:
        if d == '0':
            cnt += 1
    print(cnt)
