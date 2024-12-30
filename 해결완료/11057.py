# 10Hn = (10+n-1)Cn = (9+n)Cn
from math import factorial as f
n = int(input())
print((f(9+n)//f(9)//f(n))%10007)