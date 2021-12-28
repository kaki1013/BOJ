# 시간초과
N = int(input())
arr = [i for i in range(1, N+1)]
ind = 0
while len(arr) != ind + 1:
    ind += 1
    arr.append(arr[ind])
    ind += 1
print(arr[-1])

# 통과
N = int(input())
arr = [i for i in range(1, N + 1)]
id = 0
while True:
    if len(arr) == id + 1:
        break
    if id % 2 == 0:
        id += 1
    else:
        arr.append(arr[id])
        id += 1
print(arr[-1])

# 숏
a=[i+1 for i in range(int(input()))]
i=0
while len(a)!=i+1:
    i%2==1 and a.append(a[i])
    i+=1
print(a[-1])