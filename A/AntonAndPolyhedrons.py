dic = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

n = int(input())
arr = [input() for _ in range(n)]
result = 0
for i in arr:
    result += dic[i]

print(result)
