while True:
    a = input()
    b = input()
    if len(a) == len(b):
        break

result = ""
for i in range(len(a)):
    if a[i] == b[i]:
        result += "0"
    else:
        result += "1"

print(result)
