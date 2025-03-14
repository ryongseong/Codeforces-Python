# https://codeforces.com/contest/2074/problem/C


def is_non_degenerate(a, b, c):
    return a + b > c and a + c > b and b + c > a


t = int(input())
for _ in range(t):
    n = int(input())
    L = n.bit_length()

    s = None
    for bit in range(L):
        if (n >> bit) & 1:
            s = 1 << bit
            break

    r = None
    for bit in range(L):
        if not ((n >> bit) & 1):
            r = 1 << bit
            break

    if s is None or r is None:
        print(-1)
    else:
        candidate = s + r
        if candidate < n:
            print(candidate)
        else:
            print(-1)
