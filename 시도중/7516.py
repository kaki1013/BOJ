"""
1/x + 1/y = 1/n
(x+y)/(xy) = (z)/(zn)
xy = (x+y)n

for i in range(int(n**0.5)+1):
    if n % i == 0:
        x, y = i, n//i
        # x = i * p, y = (n//i) * q
        # xy = (x+y)n => npq = n(i*p+(n//i)*q) => pq = (i*p + (n//i)*q)

ex.
xy = 4(x+y)
5,20
6,12
8,8
"""
t = int(input())
for scenario in range(1, t+1):
    n = int(input())

    ans = 0
    for i in range(int(n ** 0.5) + 1):
        if n % i == 0:
            x, y = i, n // i
            # x = i * p, y = (n//i) * q
            # xy = (x+y)n => npq = n(i*p+(n//i)*q) => pq = (i*p + (n//i)*q)
    print(f"Scenario #{scenario}:")
    print(ans)
    print()