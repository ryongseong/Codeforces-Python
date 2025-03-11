while True:
    n = int(input())
    arr = list(map(int, input().split()))
    if n == len(arr):
        break

result = sum(arr) / n
print(f"{result:.12f}")
