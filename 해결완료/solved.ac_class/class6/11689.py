n = int(input())
nn = n
p = []

i = 2
while i <= int(n**0.5)+1:
    while n % i == 0:
        p.append(i)
        n //= i
    i += 1
if n != 1:
    p.append(n)
p = list(set(p))

ans = nn
for pp in p:
    ans = ans // pp * (pp-1)
print(ans)
