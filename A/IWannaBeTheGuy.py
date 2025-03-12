n = int(input())

_, *x = map(int, input().split())
_, *y = map(int, input().split())
arr = set(x + y)
if arr == set(range(1, n + 1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
