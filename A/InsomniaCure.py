k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input())
answer = 0
if k == 1 or l == 1 or m == 1 or n == 1:
    print(d)
else:
    for i in range(1, d + 1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0 or i % n == 0:
            answer += 1
    print(answer)
