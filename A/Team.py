n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for r in matrix:
    if r.count(1) >= 2:
        cnt += 1

print(cnt)
