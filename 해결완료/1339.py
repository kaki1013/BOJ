N = int(input())

d = dict()
for _ in range(N):
    number = input()
    length = len(number)
    for i in range(length):
        char = number[i]
        if char in d:
            d[char] += 10 ** (length-1-i)
        else:
            d[char] = 10 ** (length-1-i)

ans = 0
arr = sorted(list(d.values()), reverse=True)
for i in range(len(arr)):
    ans += arr[i] * (9-i)
print(ans)
