def prime_test(n):
	if n in [1, 2]:
		return bool(n - 1)
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True


M, N = map(int, input().split())
for num in range(M, N + 1):
	if prime_test(num):
		print(num)