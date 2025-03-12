n, k = map(int, input().split())
k = 240 - k
a, b, c, d = 1, 5, 0, 5

while True:
    if d <= k:
        a += 1
        d += a * b
        c += 1
    else:
        break

print(c if c < n else n)
