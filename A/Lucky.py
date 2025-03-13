for _ in range(int(input())):
    data = list(map(int, input()))
    print("YES" if sum(data[:3]) == sum(data[3:]) else "NO")
