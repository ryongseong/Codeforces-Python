n = int(input())
arr = list(map(int, input().split()))
print(sum(1 for i in range(1, n) if max(arr[:i]) < arr[i] or min(arr[:i]) > arr[i]))
