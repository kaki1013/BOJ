T = int(input())
for _ in range(T):
    ps = input()
    stack = []
    Valid = True
    for parenthesis in ps:
        if parenthesis == '(':
            stack.append(0)
        elif len(stack) == 0:
            Valid = False
            print('NO')
            break
        else:
            stack.pop()
    if len(stack) == 0 and Valid:
        print('YES')
    elif len(stack) > 0:
        print('NO')