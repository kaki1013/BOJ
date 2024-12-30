a, b = map(int, input().split())
square_nono = [True for _ in range(a, b+1)]  # a, a+1, ..., b

for check in range(2, int(b**0.5)+1):
    square = check ** 2
    start = (a // square) * square
    for nono in range(start, b+1, square):
        if a <= nono <= b:
            if nono % square == 0:
                square_nono[nono-a] = False

ans = sum([int(square_nono[i]) for i in range(b-a+1)])
print(ans)
