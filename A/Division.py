for _ in range(int(input())):
    rating = int(input())
    r = 4
    if rating >= 1900:
        r = 1
    elif rating >= 1600:
        r = 2
    elif rating >= 1400:
        r = 3

    print(f"Division {r}")
