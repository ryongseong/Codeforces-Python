for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    diff = b - a
    print((diff + 9) // 10)
