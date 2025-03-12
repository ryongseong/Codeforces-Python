n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i][0] == arr[j][1]:
            cnt += 1
        if arr[i][1] == arr[j][0]:
            cnt += 1
print(cnt)
