N, K = map(int, input().split())
arr = [i for i in range(N+1)]
del_arr = []
id = 1

while True:
    if len(arr) == id + 1:
        break
    if id % K == 0:
        del_arr.append(arr[id])
    else:
        arr.append(arr[id])
    id += 1

print('<', end='')
for i in range(N-1):
    print(f'{del_arr[i]}, ', end='')
print(f'{arr[-1]}>')