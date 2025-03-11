k, n, w = map(int, input().split())
r = 0
for i in range(1, w + 1):
    r += k * i
if n > r:
    print(0)
else:
    print(r - n)
