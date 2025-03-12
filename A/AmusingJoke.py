s = input().upper() + input().upper()
c = input().upper()

if len(s) != len(c):
    print("NO")
else:
    for a in s:
        if s.count(a) != c.count(a):
            print("NO")
            break
    else:
        print("YES")
