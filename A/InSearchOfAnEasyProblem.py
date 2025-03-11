while True:
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) == n:
        break

print("HARD" if arr.count(1) >= 1 else "EASY")
