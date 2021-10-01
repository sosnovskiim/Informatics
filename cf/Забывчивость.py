da, db = map(int, input().split())
if da == db:
    print(da * 10, db * 10 + 1)
elif db == da + 1:
    print(da, db)
elif da == 9 and db == 1:
    print(da, db * 10)
else:
    print(-1)
