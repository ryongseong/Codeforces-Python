input()
arr = list(map(int, input().split()))
h, u = 0, 0
for a in arr:
    if a > 0:
        h += a
        continue
    if h > 0 and a < 0:
        h -= 1
        continue
    if a < 0:
        u += 1

print(u)
