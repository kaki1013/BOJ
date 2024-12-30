# https://www.acmicpc.net/board/view/54758
# https://rkm0959.tistory.com/96
def ext_euc(a, b):
    # init
    r1 = a
    r2 = b
    q = r1 // r2
    r = r1 - q * r2

    s1 = 1
    s2 = 0
    s = s1 - q * s2

    t1 = 0
    t2 = 1
    t = t1 - q * t2

    while r != 0:
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

        q = r1 // r2
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2
        # print(q, r1, r2, r, s1, s2, s, t1, t2, t)

    return r2, s2, t2


a, b, s = map(int, input().split())
if a == s or b ==s:
    print('YES')
else:
    """
    a += b
    a,b -> a+b, b
    
    as + bt = r
    => if as0 + bt0 = r, s = s0 + (b/r)k, t = t0 - (a/r)k
    
    if r|d, as + bt = d = r(d/r)
    : s = (d/r)(s0 + (b/r)k), t = (d/r)(t0 - (a/r)k)
    
    s > 0, t > 0
    <=> (-s0*r/b) <= k <= (t0*a/r)
    
    
    """
    r, ss, tt = ext_euc(a, b)  # r = a*ss + b*tt


    print(ext_euc(a, b))

