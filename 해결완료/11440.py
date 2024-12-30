"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, ...
# 관찰 : 제곱 합
0, 1, 2, 6, 15, 25, 40, 104, ... (자신 * 뒤)
# 증명 : 귀납법

# without induction
f(n) = f(n-1) + f(n-2) -> f(n) = f(n+1) + f(n-1)
f(n)^2 = f(n) * (f(n+1) - f(n-1)) = f(n) * f(n+1) - f(n) * f(n-1)
: by telescoping

# fibonacci : O(logN)
[f_(n) , f_(n+1)] = [[0, 1], [1, 1]] * [f_(n-1), f_(n)]
let M := [[0, 1], [1, 1]]. Then,
[f_(n) , f_(n+1)] = M * [f_(n-1), f_(n)] = M^2 * [f_(n-2), f_(n-1)] = ... =  M^n * [f_(0), f_(1)]

"""
mod = 10 ** 9 + 7
M = [[0, 1], [1, 1]]


def matrix_mult(m1, m2):
    [[a, b], [c, d]] = m1
    [[e, f], [g, h]] = m2
    return [[(a*e+b*g)%mod, (a*f+b*h)%mod], [(c*e+d*g)%mod, (c*f+d*h)%mod]]


def matrix_power(n):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n == 1:
        return M
    half = matrix_power(n//2)
    half2 = matrix_mult(half, half)
    if n % 2 == 0:
        return half2
    return matrix_mult(half2, M)


def fibo(n):
    # f_(n), f_(n+1)
    if n == 1:
        return 1, 1
    if n == 2:
        return 1, 2
    [[a, b], [c, d]] = matrix_power(n)
    return b, d


def solve(n):
    a, b = fibo(n)
    return (a*b) % mod


n = int(input())
print(solve(n))