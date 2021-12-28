"""
음이 아닐 수들이므로 산술-기하 부등식을 이용하여 구할 수 있다
S/n >= P^(1/n)
S^n/n^n >= P
S^n >= P * n^n
"""
S, P = map(int, input().split())
n = 0
while S**n < P * n**n:
    n += 1
print(n)