y = int(input()) + 1
s = str(y)
while True:
    a = set()
    for i in s:
        a.add(i)
    if len(a) == 4:
        print(s)
        break
    else:
        s = str(int(s) + 1)
