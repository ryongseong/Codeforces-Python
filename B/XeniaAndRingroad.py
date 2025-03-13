n, m = map(int, input().split())
arr = list(map(int, input().split()))
current = 1

cnt = 0
for a in arr:
    if current != a:
        if a - current < 0:
            cnt += n
        cnt += a - current
        current = a

print(cnt)
