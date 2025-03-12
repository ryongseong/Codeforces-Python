s = input()
for i in range(len(s), 0, -1):
    s = s.replace("WUB" * i, " ")
print(s.strip())
