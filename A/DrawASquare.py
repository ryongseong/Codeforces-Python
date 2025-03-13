def sol(l, r, d, u):
    return l == r == d == u


for _ in range(int(input())):
    l, r, d, u = map(int, input().split())
    print("YES" if sol(l, r, d, u) else "NO")
