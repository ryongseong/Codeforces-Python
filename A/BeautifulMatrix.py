matrix = [list(map(int, input().split())) for _ in range(5)]
x, y = 0, 0

for idx, r in enumerate(matrix, start=1):
    if sum(r) != 0:
        x, y = idx, r.index(1) + 1

r, c = 3, 3
print(abs(x - r) + abs(y - c))
