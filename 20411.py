# c = (x1 - a * seed) % m
# c = (x2 - a * x1) % m
m, seed, x1, x2 = map(int, input().split())
for a in range(m):
    c1 = (x1 - a * seed) % m
    c2 = (x2 - a * x1) % m
    if c1 == c2:
        print(a, c1)
        break