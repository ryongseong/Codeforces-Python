n = int(input())
cnt = 0
s = 0
for i in range(n):
    a, b = map(int, input().split())
    s += b - a
    cnt = max(cnt, s)

print(cnt)
