T=int(input())
for _ in range(T):
	H, W, N = map(int, input().split())
	ans = ((N-1) % H + 1) * 100 + ((N - 1) // H + 1)
	print(ans)