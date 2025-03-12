n, l = map(int, input().split())
arr = sorted(map(int, input().split()))

r = max(arr[0], l - arr[n - 1]) * 2
for i in range(n - 1):
    r = max(r, arr[i + 1] - arr[i])

print(f"{r / 2:.10f}")
