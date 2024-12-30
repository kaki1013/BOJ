def power(a, x, m):
    if x == 0:
        return 1
    half = power(a, x//2, m)
    if x % 2:
        return (a * half * half) % m
    return (half * half) % m

def mod_inverse(a, b):  # a: mod
    # 초기화
    r1, r2 = a, b
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
    return t1

N, E, C = map(int, input().split())
for i in range(2, int(N**0.5)+1):
    if N % i == 0:
        p, q = i, N // i
        break
phi = (p-1) * (q-1)
# D = pow(E, -1, phi)
D = mod_inverse(phi, E) % phi
M = power(C, D, N)
print(M)