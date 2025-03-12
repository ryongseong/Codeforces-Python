input()
arr = list(map(int, input().split()))

cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0

for a in arr:
    if a == 1:
        cnt1 += 1
    elif a == 2:
        cnt2 += 1
    elif a == 3:
        cnt3 += 1
    else:
        cnt4 += 1

result = cnt4

result += cnt2 // 2
cnt2 = cnt2 % 2

if cnt1 <= cnt3:
    result += cnt1
    result += cnt2
    result += cnt3 - cnt1
else:
    result += cnt3
    cnt1 -= cnt3
    result += cnt1 // 4
    cnt1 %= 4

    a = cnt1 + cnt2 * 2
    if a > 0:
        result += 1 if a <= 4 else 2

print(result)
