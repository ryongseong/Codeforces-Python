while True:
    n = int(input())
    arr = list(map(int, input().split()))
    if n == len(arr):
        break

if sum(1 if a % 2 == 0 else 0 for a in arr) > sum(1 if a % 2 == 1 else 0 for a in arr):
    for idx, i in enumerate(arr):
        if i % 2 == 1:
            print(idx + 1)
            break
else:
    for idx, i in enumerate(arr):
        if i % 2 == 0:
            print(idx + 1)
            break
