k, r = map(int, input().split())

n = 0
result = 0

while True:
    if n != 0 and (10 * n) % k == 0:
        result = (10 * n) // k
        break
    if (10 * n + r) % k == 0:
        result = (10 * n + r) // k
        break
    n += 1

print(result)
