"""
(3+sqrt5)^n = a_n + b_n * sqrt5
(3+sqrt5)^(n+1) = (a_n + b_n * sqrt5) * (3 + sqrt5)
                = (3a_n + 5b_n) + (a_n+3b_n)*sqrt5
                = a_(n+1) + b_(n+1)*sqrt5
즉,
a_(n+1) = 3a_n + 5b_n
b_(n+1) = a_n + 3b_n

x_0 = [1, 0]^t -> x_1 = [3, 1]^t
x_n = [a_n, b_n]^t, M = [[3, 5], [1, 3]] 일때
x_n = M * x_(n-1) = ... = M^n * x_0
=====
(3-sqrt5)^n = c_n + d_n * sqrt5
(3-sqrt5)^(n+1) = (c_n + d_n * sqrt5) * (3 - sqrt5)
                = (3c_n - 5d_n) + (-c_n+3d_n)*sqrt5
                = c_(n+1) + d_(n+1)*sqrt5
즉,
c_(n+1) = 3c_n - 5d_n
d_(n+1) = -c_n + 3d_n

y_0 = [1, 0]^t -> y_1 = [3, -1]^t
y_n = [c_n, d_n]^t, N = [[3, -5], [-1, 3]] 일때
y_n = N * y_(n-1) = ... = N^n * y_0


"""
mod = 1000
M = [[3, 5], [1, 3]]

def matrix_mult(m1, m2):
    """
    ab  ef  wx
    cd  gh  yz
    """
    [[a, b], [c, d]] = m1
    [[e, f], [g, h]] = m2
    w = a*e+b*g
    x = a*f+b*h
    y = c*e+d*g
    z = c*f+d*h
    return [[w, x], [y, z]]
print(matrix_mult(M, M))


for t in range(int(input())):
    ans = 0



    print(f"Case #{t+1}: {ans}")