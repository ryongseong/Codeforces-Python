s = input()
u_cnt = 0
l_cnt = 0
for w in s:
    if w == w.upper():
        u_cnt += 1
    elif w == w.lower():
        l_cnt += 1

if u_cnt > l_cnt:
    print(s.upper())
else:
    print(s.lower())
