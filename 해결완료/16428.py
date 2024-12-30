A, B = map(int, input().split())
if A == 0:
    print('0\n0')
elif B > 0:
    print(A // B)
    print(A % B)
elif A % B != 0:
    q = A // B + 1
    print(A // B + 1)
    print(A - B * q)
else:
    print(A // B)
    print(A % B)
