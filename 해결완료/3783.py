"""
어떤 양의 정수가 주어졌을 때, 이 수의 세제곱근을 구하는 프로그램을 작성하시오.
세제곱근을 구하고자 하는 수가 한 줄에 하나씩 입력으로 주어지며, 이 수는 150자리 이하이다. 수는 0으로 시작할 수도 있다.

해당 수를 a라고 하면
1 <= a < 10^150
1 <= cbrt(a) < 10^50

f(x) := x^3 <= a

f(0) = True, f(10^50) = False
# T, T, ..., T, F, F, ..., F

a메 대한 답을 x라고 하면, a -> a*10^30, x -> x*10^10
ex. 8에 대해 2.0000000000
    -> 8*(10^30)에 대해 20000000000(=2*10^10)

"""
def check(x, a):
    return x**3 <= a


def find(a, l, r):
    m = (l+r)//2
    if check(m, a) and not check(m+1, a):
        return m
    if check(m, a):
        return find(a, m, r)
    return find(a, l, m)


def output(ans):
    s = str(ans)


T = int(input())
for _ in range(T):
    n = int(input())
    n *= 10**30

    l = 0
    r = 10**60

    ans = str(find(n, l, r))
    ans = ans[:-10] + '.' + ans[-10:]
    print(ans)
