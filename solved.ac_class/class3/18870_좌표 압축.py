# 범위가 큰 수들끼리의 대소 비교 등/ 몇번째로 큰 수인지만 체크
N = int(input())
arr = list(map(int, input().split()))
arr_sorted = sorted(arr)
arr_dict = dict()

key = 0
for n in arr_sorted:
    if n not in arr_dict:
        arr_dict[n] = key
        key += 1

for n in arr:
    print(arr_dict[n], end=' ')