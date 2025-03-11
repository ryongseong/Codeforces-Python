n, h = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    if i > h:
        cnt += 2
    else:
        cnt += 1

print(cnt)
