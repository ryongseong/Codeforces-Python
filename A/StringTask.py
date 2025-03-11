s = input().lower()
r = []
for w in s:
    if w not in ("a", "o", "y", "e", "u", "i"):
        r.append(w)

print("." + ".".join(r))
