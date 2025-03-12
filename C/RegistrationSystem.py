data = dict()

for _ in range(int(input())):
    name = input()
    if data.get(name) is None:
        print("OK")
        data[name] = 1
    else:
        print(name + str(data[name]))
        data[name] += 1
