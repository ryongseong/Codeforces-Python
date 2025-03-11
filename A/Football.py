S = input()
cnt = 1
for i in range(len(S) - 1):
    if cnt >= 7:
        break
    if S[i] == S[i + 1]:
        cnt += 1
    else:
        cnt = 1

print("YES" if cnt >= 7 else "NO")
