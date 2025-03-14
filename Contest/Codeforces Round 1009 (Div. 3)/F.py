# https://codeforces.com/contest/2074/problem/F


def dyadic_cover_exponents(L, R):
    exponents = []
    x = L
    while x < R:
        s = 1
        while (x % (2 * s) == 0) and (x + 2 * s <= R):
            s *= 2
        exponents.append(s.bit_length() - 1)
        x += s
    return exponents


for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())

    x_exps = dyadic_cover_exponents(l1, r1)
    y_exps = dyadic_cover_exponents(l2, r2)

    freq_x = [0] * 32
    freq_y = [0] * 32
    for exp in x_exps:
        freq_x[exp] += 1
    for exp in y_exps:
        freq_y[exp] += 1

    total = 0
    for exp_x in range(1 << 5):
        if freq_x[exp_x]:
            for exp_y in range(1 << 5):
                if freq_y[exp_y]:
                    total += freq_x[exp_x] * freq_y[exp_y] * (1 << abs(exp_x - exp_y))
    print(total)
