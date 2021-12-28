# 이 문제 테스트 데이터: http://acm.student.cs.uwaterloo.ca/~acm00/020928/data/A.1.dat
# waterloo 테스트 데이터: https://uwaterloo.ca/international-collegiate-programming-contest/past-local-contest-results
import sys
from math import gcd


def coefficient(term, variable):
    term_clear = term.strip()
    coeff = term_clear.split(variable)[0]
    if len(coeff) == 0:  # x
        return 1
    elif coeff == '-':  # -x
        return -1
    return int(coeff)  # 2x, -2x


def decomposition(equation):
    left, right = equation.split('=')
    left = left.strip()
    right = right.strip()
    left_term, right_term = left.split(' '), right.split(' ')
    left_len, right_len = len(left_term), len(right_term)
    p, q, r = 0, 0, 0  # px + qy + r = 0

    # 좌변 처리
    term = left_term[0]
    if 'x' in term:
        p += coefficient(term, 'x')
    elif 'y' in term:
        q += coefficient(term, 'y')
    else:
        r += int(term)

    for i in range((left_len-1)//2):
        isPlus, term = left_term[2*i+1] == '+', left_term[2*i+2]
        if 'x' in term:
            p = p + coefficient(term, 'x') if isPlus else p - coefficient(term, 'x')
        elif 'y' in term:
            q = q + coefficient(term, 'y') if isPlus else q - coefficient(term, 'y')
        else:
            r = r + int(term) if isPlus else r - int(term)
    # 우변 처리
    term = right_term[0]
    if 'x' in term:
        p -= coefficient(term, 'x')
    elif 'y' in term:
        q -= coefficient(term, 'y')
    else:
        r -= int(term)

    for i in range((right_len - 1) // 2):
        isPlus, term = right_term[2 * i + 1] == '+', right_term[2 * i + 2]
        if 'x' in term:
            p = p - coefficient(term, 'x') if isPlus else p + coefficient(term, 'x')
        elif 'y' in term:
            q = q - coefficient(term, 'y') if isPlus else q + coefficient(term, 'y')
        else:
            r = r - int(term) if isPlus else r + int(term)

    return p, q, r


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    eq1 = sys.stdin.readline().rstrip()
    a, b, c = decomposition(eq1)
    eq2 = sys.stdin.readline().rstrip()
    d, e, f = decomposition(eq2)
    last_enter = sys.stdin.readline().rstrip()
    c, f = -c, -f
    aa, bb, cc, dd, ee, ff = a == 0, b == 0, c == 0, d == 0, e == 0, f == 0
    if a * e - b * d == 0:  # 적어도 하나는 모르는 경우(무의미한 식 0=0, 불가능한 식 0=1, 일차종속)
        if not (aa or bb or dd or ee):
            print('don\'t know\ndon\'t know')
        else:
            if aa:
                if bb:
                    if cc:
                        if dd:
                            print('don\'t know')
                            if ee:
                                print('don\'t know')
                            else:
                                if f % e == 0:
                                    print(f // e)
                                else:
                                    Gcd = gcd(abs(f), abs(e))
                                    print(f"{'-' if f * e < 0 else ''}{abs(f) // Gcd}/{abs(e) // Gcd}")
                        else:
                            if ee:
                                if f % d == 0:
                                    print(f // d)
                                else:
                                    Gcd = gcd(abs(f), abs(d))
                                    print(f"{'-' if f * d < 0 else ''}{abs(f) // Gcd}/{abs(d) // Gcd}")
                            else:
                                print('don\'t know')
                            print('don\'t know')
                    else:
                        print('don\'t know\ndon\'t know')
                else:
                    print('don\'t know')
                    if ee:
                        if ff:
                            if c % b == 0:
                                print(c // b)
                            else:
                                Gcd = gcd(abs(c), abs(b))
                                print(f"{'-' if b * c < 0 else ''}{abs(c) // Gcd}/{abs(b) // Gcd}")
                        else:
                            print('don\'t know')
                    else:
                        if b * f == c * e:
                            if c % b == 0:
                                print(c // b)
                            else:
                                Gcd = gcd(abs(c), abs(b))
                                print(f"{'-' if b * c < 0 else ''}{abs(c) // Gcd}/{abs(b) // Gcd}")
                        else:
                            print('don\'t know')
            else:
                if bb:
                    if dd:
                        if ff:
                            if c % a == 0:
                                print(c // a)
                            else:
                                Gcd = gcd(abs(c), abs(a))
                                print(f"{'-' if a * c < 0 else ''}{abs(c) // Gcd}/{abs(a) // Gcd}")
                        else:
                            print('don\'t know')
                    else:
                        if a * f == c * d:
                            if c % a == 0:
                                print(c // a)
                            else:
                                Gcd = gcd(abs(c), abs(a))
                                print(f"{'-' if a * c < 0 else ''}{abs(c) // Gcd}/{abs(a) // Gcd}")
                        else:
                            print('don\'t know')
                    print('don\'t know')
                else:
                    print('don\'t know\ndon\'t know')
    else:  # 답이 존재
        x_top, y_top, bottom = c * e - b * f, a * f - c * d, a * e - b * d
        if x_top % bottom == 0:
            print(x_top // bottom)
        else:
            Gcd = gcd(abs(x_top), abs(bottom))
            print(f"{'-' if x_top * bottom < 0 else ''}{abs(x_top) // Gcd}/{abs(bottom) // Gcd}")
        if y_top % bottom == 0:
            print(y_top // bottom)
        else:
            Gcd = gcd(abs(y_top), abs(bottom))
            print(f"{'-' if y_top * bottom < 0 else ''}{abs(y_top) // Gcd}/{abs(bottom) // Gcd}")
    print()
