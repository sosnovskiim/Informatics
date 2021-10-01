def is_magic(n):
    for d in n:
        if d != '1' and d != '4':
            return False
    if n[0] == '4':
        return False
    if '444' in n:
        return False
    return True


number = input()
if is_magic(number):
    print('YES')
else:
    print('NO')
