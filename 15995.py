a, m = map(int, input().split())
for i in range(1, m):
    if (a * i) % m == 1:
        print(i)
        break