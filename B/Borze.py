S = input()
for idx, change in enumerate(("--", "-.", ".")):
    S = S.replace(change, str(2 - idx))

print(S)
