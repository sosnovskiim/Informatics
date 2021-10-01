n = int(input())
text = [word for word in input().split()]
mx = 0
for word in text:
    cnt = 0
    for i in range(len(word)):
        if 'A' <= word[i] <= 'Z':
            cnt += 1
    if cnt > mx:
        mx = cnt
print(mx)
