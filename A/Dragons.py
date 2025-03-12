s, n = map(int, input().split())

arr = sorted([list(map(int, input().split())) for _ in range(n)])
for a, b in arr:
    if s > a:
        s += b
    else:
        print("NO")
        break
else:
    print("YES")
