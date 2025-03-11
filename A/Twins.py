while True:
    n = int(input())
    arr = sorted(map(int, input().split()))
    if n == len(arr):
        break
sum_v, cnt = 0, 0

while sum_v <= sum(arr):
    sum_v += arr.pop()
    cnt += 1

print(cnt)
