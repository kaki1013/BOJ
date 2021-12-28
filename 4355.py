import sys
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    s = set(range(1, n))
    if n in range(1, 6):
        print([0, 0, 1, 2, 2, 4][n])
    else:
        for i in range(2, n+1):
            if n % i == 0:
                pass