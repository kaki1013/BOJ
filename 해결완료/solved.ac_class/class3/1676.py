def two_five(n):
    n_two, n_five = n, n
    two, five = 0, 0
    while True:
        if n_two % 2 == 0:
            n_two //= 2
            two += 1
            continue
        break
    while True:
        if n_five % 5 == 0:
            n_five //= 5
            five += 1
            continue
        break
    return two, five


N = int(input())
ans_2, ans_5 = 0, 0
for i in range(1, N+1):
    ans_2 += two_five(i)[0]
    ans_5 += two_five(i)[1]
print(min(ans_2, ans_5))