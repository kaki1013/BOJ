# greedy : 피보나치 수 중에서 큰 것들부터 사용하여 합으로 표현
# proof: https://jeonggyun.tistory.com/232
# 참고: 증명으로는 부족
# 1. 연속인 두 피보나치 수를 포함하지 않는 합의 표현 방법은 유일 (https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem)
# 2. 최소인 방식이 연속인 두 피보나치 수를 포함한다고 가정 -> 두 연속인 피보나치 수의 합은 그 다음 피보나치수로 대체 가능하고 모순
T = int(input())
for t in range(T):
    n = int(input())
    f = [1, 1, 2, 3, 5, 8]
    while f[-1] < n:
        f.append(f[-1] + f[-2])

    stack = []
    for fi in f[::-1]:
        if n == 0:
            break
        if n >= fi:
            n -= fi
            stack.append(fi)
    print(*stack[::-1])