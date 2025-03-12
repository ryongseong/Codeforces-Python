for _ in range(int(input())):
    arr = sorted(map(int, input().split()))
    print("YES" if arr[0] + arr[1] == arr[2] else "NO")
