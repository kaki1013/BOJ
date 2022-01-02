# A, B, A+B, A+2B, 2A+3B, 3A+5B
# 1 0) 1 1 2 3 f(n)
# 0 1) 1 2 3 5 f(n+1)
f = [0, 1, 1]
while len(f) != 35:
    f.append(f[-1] + f[-2])
D, K = map(int, input().split())
a, b = f[D - 2], f[D - 1]  # A, B의 계수에 해당하는 피보나치 수
breaker = False
for B in range(1, 10 ** 5 + 1):
    y = K - b * B   # y=aA=K-bB
    if y % a == 0 and y//a <= B:    # A는 반복문 필요 없이 산술적인 계산으로 O(1)에 확인 가능
        A = y//a
        print(f'{A}\n{B}')
        break
