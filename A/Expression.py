a = int(input())
b = int(input())
c = int(input())

if a == 1:
    if c != 1:
        print((a + b) * c)
    else:
        print(a + b + c)
elif b == 1:
    if a > c:
        print(a * (b + c))
    else:
        print((a + b) * c)
elif c == 1:
    print(a * (b + c))
else:
    print(a * b * c)
