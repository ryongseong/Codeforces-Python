# https://codeforces.com/contest/2074/problem/B

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    result = sum(arr) - (n - 1)

    print(result)
