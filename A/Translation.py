s = input().lower()
t = input().lower()
print("YES" if s == t[::-1] else "NO")
