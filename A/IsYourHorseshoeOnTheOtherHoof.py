s = sorted(list(map(int, input().split())))
cnt = 0
for i in range(3):
    if s[i] == s[i + 1]:
        cnt += 1

print(cnt)
