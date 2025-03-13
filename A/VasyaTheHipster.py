a, b = map(int, input().split())
d = min(a, b)
s = (max(a, b) - d) // 2

print(d, s)
