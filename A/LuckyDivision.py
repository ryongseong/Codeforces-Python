n = input()
if int(n) % 4 == 0 or int(n) % 7 == 0 or int(n) % 47 == 0:
    print("YES")
else:
    cnt = 0
    for i in n:
        if i == "4" or i == "7":
            cnt += 1

    if cnt == len(n):
        print("YES")
    else:
        print("NO")
