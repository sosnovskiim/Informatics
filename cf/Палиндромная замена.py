t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    is_palindrome = True
    i, j = 0, -1
    for __ in range(n // 2):
        tmp = abs(ord(s[i]) - ord(s[j]))
        if tmp != 0 and tmp != 2:
            is_palindrome = False
            break
        i += 1
        j -= 1
    if is_palindrome:
        print('YES')
    else:
        print('NO')
