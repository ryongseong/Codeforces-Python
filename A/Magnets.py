n = int(input())
cnt = 1
data = [input() for _ in range(n)]

for i in range(n - 1):
    if data[i][1] == data[i + 1][0]:
        cnt += 1

print(cnt)
