n = int(input())
p = list(map(int, input().split()))
result = p[:]
for i in range(n):
    result[p[i] - 1] = i + 1

print(*result)
