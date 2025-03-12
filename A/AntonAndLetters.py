s = list(input().lstrip("{").rstrip("}").split(", "))
if s[0] == "":
    print(0)
else:
    print(len(set(s)))
