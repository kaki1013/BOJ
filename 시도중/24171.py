"""
(b0+c0*sqrt(d0))/a0 + (b1+c1*sqrt(d1))/a1 * i

A+B =

"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def simple(a, b, c):
    g = gcd(a, b)
    g = gcd(g, c)
    if a * g < 0:
        g = -g

    a //= g
    b //= g
    c //= g
    return [a, b, c]


def add(A_real, B_real):
    a0, b0, c0, d0 = A_real
    a1, b1, c1, d1 = B_real

    a = a0 * a1
    b = a1 * b0 + a0 * b1
    c = a1 * c0 + a0 * c1
    d = d0

    return simple(a, b, c) + [d]


def mul(A_real, B_real):
    a0, b0, c0, d0 = A_real
    a1, b1, c1, d1 = B_real

    a = a0 * a1
    b = b0 * b1 + c0 * c1 * d0
    c = b0 * c1 + b1 * c0
    d = d0

    return simple(a, b, c) + [d]


def inv(A_real):
    a0, b0, c0, d0 = A_real

    a = b0 ** 2 - c0 ** 2 * d0
    b = a0 * b0
    c = -a0 * c0
    d = d0

    return simple(a, b, c) + [d]


def minus(A):
    a0, b0, c0, d0 = A
    return [a0, -b0, -c0, d0]


def mul_z(A_re, A_im, B_re, B_im):
    tmp1 = mul(A_re, B_re)
    tmp2 = mul(A_im, B_im)
    ans_re = add(tmp1, minus(tmp2))

    tmp1 = mul(A_re, B_im)
    tmp2 = mul(A_im, B_re)
    ans_im = add(tmp1, tmp2)
    return ans_re, ans_im


def inv_z(A_re, A_im):
    """
    1/(Re+Im*i) = (Re - Im * i)/(Re^2 + Im^2)
    """
    down = add(mul(A_re, A_re), mul(A_im, A_im))

    re = mul(A_re, inv(down))
    im = mul(minus(A_im), inv(down))

    return re, im


Aa0, Ab0, Ac0, Ad0, Aa1, Ab1, Ac1, Ad1 = map(int, input().split())
Ba0, Bb0, Bc0, Bd0, Ba1, Bb1, Bc1, Bd1 = map(int, input().split())

A_re, A_im = [Aa0, Ab0, Ac0, Ad0], [Aa1, Ab1, Ac1, Ad1]
B_re, B_im = [Ba0, Bb0, Bc0, Bd0], [Ba1, Bb1, Bc1, Bd1]

ans1 = add(A_re, B_re) + add(A_im, B_im)
ans2 = add(A_re, minus(B_re)) + add(A_im, minus(B_im))

# tmp1 = mul(A_re, B_re)
# tmp2 = mul(A_im, B_im)
# ans3_re = add(tmp1, minus(tmp2))
#
# tmp1 = mul(A_re, B_im)
# tmp2 = mul(A_im, B_re)
# ans3_im = add(tmp1, tmp2)
ans3_re, ans3_im = mul_z(A_re, A_im, B_re, B_im)
ans3 = ans3_re + ans3_im

B_inv_re, B_inv_im = inv_z(B_re, B_im)
ans4_re, ans4_im = mul_z(A_re, A_im, B_inv_re, B_inv_im)
ans4 = ans4_re + ans4_im

print(*ans1)
print(*ans2)
print(*ans3)
print(*ans4)
