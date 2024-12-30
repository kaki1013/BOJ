def unzip(s):
    length = len(s)

    stack = []
    l, r = -1, -1
    for i in range(length):
        if s[i] == '(':
            stack.append(i)
            if l == -1:
                l = i
        elif s[i] == ')':
            stack.pop()
            if stack == [] and r == -1:
                r = i
                break
    # print(s, l, r)
    if l != -1 and r != -1:
        # print(s, l, r, (l-1), int(s[l-1])*unzip(s[l+1:r]), unzip(s[r+1:]))
        return (l-1) + int(s[l-1])*unzip(s[l+1:r])+unzip(s[r+1:])
    return length


# print(unzip("1()66(5)"))

S = input()
print(unzip(S))
