for _ in range(int(input())):
    a, b = map(int, input().split())
    print(b - a % b if a % b != 0 else 0)
