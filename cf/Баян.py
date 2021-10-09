def main(s):
    l_bracket = s.find('[')
    if l_bracket == -1:
        return -1
    s = s[l_bracket + 1:]

    l_colon = s.find(':')
    if l_colon == -1:
        return -1
    s = s[l_colon + 1:]

    s = s[::-1]

    r_bracket = s.find(']')
    if r_bracket == -1:
        return -1
    s = s[r_bracket + 1:]

    r_colon = s.find(':')
    if r_colon == -1:
        return -1
    s = s[r_colon + 1]

    return s.count('|') + 4


print(main(s=input()))
