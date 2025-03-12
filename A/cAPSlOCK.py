S = input()
up_cnt, low_cnt = 0, 0
for a in S:
    if a.isupper():
        up_cnt += 1
    else:
        low_cnt += 1

if S[0].islower() and up_cnt == len(S) - 1:
    S = S.lower()
    print(S.title())
elif up_cnt == len(S):
    print(S.lower())
else:
    print(S)
