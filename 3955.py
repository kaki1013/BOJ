def e_gcd(a, b):
    # 초기화
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        # r
        r = r1 - q * r2
        r1 = r2
        r2 = r
        # s
        s = s1 - q * s2
        s1 = s2
        s2 = s
        # t
        t = t1 - q * t2
        t1 = t2
        t2 = t
    return r1, s1, t1


# 1 <= y < 10^9
T = int(input())
for _ in range(T):
    K, C = map(int, input().split())
    r, s, t = e_gcd(K, C)
    # Ks + Ct = 1
#    print(r, s, t)
    if r != 1:
        print('IMPOSSIBLE')
    else:
        if s < 0 and t > 0:
            print(t % K)
        else:
            low = int(max(0, s / C, -t / K))
            high = int((10 ** 9 - t) / K)
            # low < x <= high
            if high - low >= 1:
                print(t + K * (low + 1))
            else:
                print('IMPOSSIBLE')
"""
    else:  # K(-x) + Cy = 1, r = -x, t = y  => r < 0, t > 0
        if C == 1:
            print('IMPOSSIBLE' if K+1>10**9 else K+1)
        elif K == 1:
            print(C-1)
        else:
            print(t % K)
"""