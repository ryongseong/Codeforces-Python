def sol(s):
    return len(set(s)) == 26


int(input())
print("YES" if sol(input().lower()) else "NO")
