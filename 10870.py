n = int(input())
a = 0
b = 1

for _ in range(n):
    temp = a + b
    a = b
    b = temp

print(a)