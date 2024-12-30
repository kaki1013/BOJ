poly = input()  # 0, (-)B, (-)Ax, (-)Ax+0, (-)Ax+B

have_no_x = True
i = 0

while True:
    if i == len(poly):
        break
    if ord(poly[i]) == 120:  # ord('x') = 120
        have_no_x = False
        A = int(poly[:i])
        if poly[-1] == 'x':
            B = 0
        else:
            B = int(poly[i+1:])
        break
    i += 1

if have_no_x:
    A, B = 0, int(poly)

if A == 0:
    if B == 0:
        print('W')
    elif B == 1:
        print('x+W')
    elif B == -1:
        print('-x+W')
    else:
        print(f'{B}x+W')

elif A == 2:
    if B == 0:
        print('xx+W')
    elif B == 1:
        print('xx+x+W')
    elif B == -1:
        print('xx-x+W')
    elif B > 0:
        print(f'xx+{B}x+W')
    elif B < 0:
        print(f'xx{B}x+W')

elif A == -2:
    if B == 0:
        print('-xx+W')
    elif B == 1:
        print('-xx+x+W')
    elif B == -1:
        print('-xx-x+W')
    elif B > 0:
        print(f'-xx+{B}x+W')
    elif B < 0:
        print(f'-xx{B}x+W')

else:
    if B == 0:
        print(f'{A//2}xx+W')
    elif B == 1:
        print(f'{A//2}xx+x+W')
    elif B == -1:
        print(f'{A // 2}xx-x+W')
    elif B > 0:
        print(f'{A // 2}xx+{B}x+W')
    elif B < 0:
        print(f'{A // 2}xx{B}x+W')