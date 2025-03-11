n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = True

for r in map(list, zip(*arr)):
    if sum(r) != 0:
        result = False

print("YES" if result else "NO")
