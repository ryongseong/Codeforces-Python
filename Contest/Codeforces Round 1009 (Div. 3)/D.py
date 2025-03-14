# https://codeforces.com/contest/2074/problem/D

import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    centers = list(map(int, input().split()))
    radii = list(map(int, input().split()))

    updates = []
    for i in range(n):
        x_center = centers[i]
        r = radii[i]
        r2 = r * r
        updates.append((x_center, r))
        for dx in range(1, r + 1):
            h = math.isqrt(r2 - dx * dx)
            updates.append((x_center + dx, h))
            updates.append((x_center - dx, h))
    updates.sort(key=lambda p: p[0])

    result = 0
    i = 0
    N = len(updates)
    while i < N:
        x_val = updates[i][0]
        max_h = updates[i][1]
        i += 1
        while i < N and updates[i][0] == x_val:
            if updates[i][1] > max_h:
                max_h = updates[i][1]
            i += 1
        result += 2 * max_h + 1

    print(result)
