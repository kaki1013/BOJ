N = int(input())
string = input()
arr = []
ans = 0
for s in string:
    arr.append(ord(s) - ord('a') + 1)
for i in range(N):
    ans += arr[i] * 31 ** i
    ans %= 1234567891
print(ans)
