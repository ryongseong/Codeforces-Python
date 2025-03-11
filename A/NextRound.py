n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

cnt = k

scores = arr[:k]
cnt -= scores.count(0)

if scores[-1] != 0:
    cnt += arr[k:].count(scores[-1])

print(cnt)
