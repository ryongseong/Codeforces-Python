a = int(input())
arr = [100, 20, 10, 5, 1]
cnt = 0
idx = 0
while a:
    if a // arr[idx] >= 1:
        cnt += a // arr[idx]
        a %= arr[idx]
    idx += 1

print(cnt)
