import sys
arr = []
N = int(input())
pop_index = 0
for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        arr.append(int(s[1]))
    elif s[0] == 'pop':
        if len(arr) == pop_index:
            print(-1)
        else:
            print(arr[pop_index])
            pop_index += 1
    elif s[0] == 'size':
        print(len(arr)-pop_index)
    elif s[0] == 'empty':
        print(int(len(arr) == pop_index))
    elif s[0] == 'front':
        if len(arr) == pop_index:
            print(-1)
        else:
            print(arr[pop_index])
    elif s[0] == 'back':
        if len(arr) == pop_index:
            print(-1)
        else:
            print(arr[-1])