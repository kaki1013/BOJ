# https://ebbnflow.tistory.com/170
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

count = 0
for coin in coins:
    if coin <= K:
        count += K // coin
        K -= (K // coin) * coin
    if K == 0:
        break
print(count)
