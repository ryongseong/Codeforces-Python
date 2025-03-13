for _ in range(int(input())):
    a, *arr = list(map(int, input().split()))
    print(sum(1 if a < i else 0 for i in arr))
