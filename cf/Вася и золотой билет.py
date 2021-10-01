n = int(input())
s = list(input())
is_lucky = False

for first_s_ln in range(1, n):
    if not is_lucky:

        first_s_sm = 0
        for i in range(first_s_ln):
            first_s_sm += int(s[i])

        cnt = first_s_ln
        j = first_s_ln
        for not_first_s_ln in range(1, n - first_s_ln + 1):

            not_first_s_sm = 0
            while j < not_first_s_ln + first_s_ln and int(s[j]) + not_first_s_sm <= first_s_sm:
                not_first_s_sm += int(s[j])
                j += 1

            if not_first_s_sm == first_s_sm:

                if j == n:
                    is_lucky = True
                    break

                is_zeroes = True
                for i in range(j, n):
                    if s[i] != '0':
                        is_zeroes = False
                if is_zeroes:
                    is_lucky = True
                    break

                cnt = j

            else:
                j = cnt

    else:
        break

if is_lucky:
    print('YES')
else:
    print('NO')
