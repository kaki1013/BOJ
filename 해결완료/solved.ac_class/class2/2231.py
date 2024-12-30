N = int(input())  # 1~1,000,000
esc = True

for a in range(0, min(9, N // 100001) + 1):
    for b in range(0, min(9, N // 10001) + 1):
        for c in range(0, min(9, N // 1001) + 1):
            for d in range(0, min(9, N // 101) + 1):
                for e in range(0, min(9, N // 11) + 1):
                    for f in range(10):  # 한자리수 고려
                        if N == 100001 * a + 10001 * b + 1001 * c + 101 * d + 11 * e + 2 * f:
                            print(100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f)
                            esc = False
                            break
                    if not esc:
                        break
                if not esc:
                    break
            if not esc:
                break
        if not esc:
            break
    if not esc:
        break

if esc:
    print(0)
