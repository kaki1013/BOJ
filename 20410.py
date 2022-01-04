m, seed, x1, x2 = map(int, input().split())
found = False
for a in range(m):
    if found:
        break
    for c in range(m):
        x_1 = (a * seed + c) % m
        if x_1 == x1:
            x_2 = (a * x_1 + c) % m
            if x_2 == x2:
                print(a, c)
                found = True
                break