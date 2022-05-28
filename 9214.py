def prev(x):
    if len(str(x)) % 2:
        return x
    info = str(x)
    temp = []
    for i in range(len(info)//2):
        count, num = int(info[2*i]), info[2*i+1]
        for _ in range(count):
            temp.append(num)
    temp = int(''.join(temp))
    if temp == x:
        return x
    return prev(temp)

idx = 0
while True:
    n = int(input())
    idx += 1
    if not n:
        break
    ans = 0
    ans = prev(n)
    print(f"Test {idx}: {ans}")
