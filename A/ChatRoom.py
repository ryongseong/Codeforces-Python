s = input().lower()
h_flag = False
e_flag = False
l_flag_1 = False
l_flag_2 = False
o_flag = False

for i in s:
    if i == "h" and not h_flag:
        h_flag = True
    elif i == "e" and h_flag and not e_flag:
        e_flag = True
    elif i == "l" and h_flag and e_flag and not l_flag_1:
        l_flag_1 = True
    elif i == "l" and h_flag and e_flag and l_flag_1 and not l_flag_2:
        l_flag_2 = True
    elif i == "o" and h_flag and e_flag and l_flag_1 and l_flag_2:
        o_flag = True

if h_flag and e_flag and l_flag_1 and l_flag_2 and o_flag:
    print("YES")
else:
    print("NO")
