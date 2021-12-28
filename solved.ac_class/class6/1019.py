N = input()  # N <= 10^9
num = int(N)
ans = [0]*10

for i in range(len(N)):
    if i == 0:
        ans = [ans[i] + num//10 for i in range(10)]
        last_digit = int(N[-1])
        if last_digit != 0:
            for j in range(1, last_digit+1):
                ans[j] += 1
    else:
        h = (num // 10**(i+1) - int(N[-(i+1)] == '0')) * 10**i
        ans = [ans[i]+h for i in range(10)]
        res = num - (h * 10 + 10**i) + 1
        for j in range(1, 11):
            if res == 0:
                break
            if res >= 10**i:
                ans[j%10] += 10**i
                res -= 10**i
            else:
                ans[j%10] += res
                res = 0

print(*ans)

# naive solution
N = int(input())
ans = [0]*10
for i in range(1, N+1):
    s = str(i)
    for char in s:
        ans[int(char)] += 1
print(*ans)
