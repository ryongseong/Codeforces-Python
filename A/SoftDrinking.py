n, k, l, c, d, p, nl, np = map(int, input().split())
drink = (k * l) // nl
limes = c * d
salts = p // np
print(min([drink, limes, salts]) // n)
