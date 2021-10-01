n, m = map(int, input().split())
min_street_prices = []
for _ in range(n):
    street_prices = [int(i) for i in input().split()]
    min_street_prices.append(min(street_prices))
print(max(min_street_prices))
