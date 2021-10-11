def main(s):
    tmp = s.find('[')
    if tmp == -1:
        return -1
    s = s[tmp + 1:]

    tmp = s.find(':')
    if tmp == -1:
        return -1
    s = s[tmp + 1:]

    s = s[::-1]

    tmp = s.find(']')
    if tmp == -1:
        return -1
    s = s[tmp + 1:]

    tmp = s.find(':')
    if tmp == -1:
        return -1
    s = s[tmp + 1:]

    return 4 + s.count('|')


print(main(s=input()))
