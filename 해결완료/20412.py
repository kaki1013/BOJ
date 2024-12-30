# x1 = a*s+c, x2 = a*x1+c
# => a * (s - x1) = x1 - x2
# => a = (s - x1)^(-1) * (x1 - x2)
# => c = x1 - a * s
# 단, a = x1일 때: a = 0, c = s 선택
def mod_inverse(a, m):
    # 초기화
    r1, r2 = a, m
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        # r
        temp = r1 - q * r2
        r1 = r2
        r2 = temp
        # s
        temp = s1 - q * s2
        s1 = s2
        s2 = temp
        # t
        temp = t1 - q * t2
        t1 = t2
        t2 = temp
    return s1 % m

m, seed, x1, x2 = map(int, input().split())
if seed != x1:
#    a = pow(seed-x1, -1, m) * (x1-x2) % m
    a = mod_inverse(seed-x1, m) * (x1-x2) % m
    c = (x1-a*seed) % m
else:
    a = 0
    c = seed
print(a, c)