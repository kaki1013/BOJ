# AB=LG -> A = Ga, B = Gb, a <= b, (a, b) = 1, Gab = L
from math import gcd

G, L = map(int, input().split())
A, B = G, G
ab = L // G     # a*b -> a < b, (a, b) = 1이면서 a+b가 최소의 경우 찾으면 됨

# 초기화
m = 1+ab        # 최소인 a+b
a, b = 1, ab    # 가능한 a, b
for i in range(2, int(ab**0.5)+1):
    if ab % i == 0:
        temp_a, temp_b = i, ab // i
        if gcd(temp_a, temp_b) == 1 and temp_a <= temp_b and temp_a + temp_b < m:
            m, a, b = temp_a + temp_b, temp_a, temp_b
A *= a
B *= b
print(A, B)