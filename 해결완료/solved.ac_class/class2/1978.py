N = int(input())
arr = list(map(int, input().split()))
count = 0

for n in arr:
    if n == 1:
        continue
    if n == 2 or n == 3:
        count += 1
        continue
    for factor in range(2, int(n ** 0.5) + 1):
        if n % factor == 0:
            break
        if factor == int(n ** 0.5):
            count += 1
print(count)
