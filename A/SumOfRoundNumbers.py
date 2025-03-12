def sol(n):
    if len(n) == 1:
        k = 1
    else:
        k = len(n) - n.count("0")
    result = []
    for i in range(len(n)):
        if n[i] != "0":
            result.append(n[i] + "0" * (len(n) - i - 1))
    print(k)
    print(*result)


for _ in range(int(input())):
    sol(input())
