N = int(input())
Number_Card = list(map(int, input().split()))
M = int(input())
To_find = list(map(int, input().split()))
count_dict = dict()

for number in Number_Card:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

for find in To_find:
    if find in count_dict:
        print(count_dict[find], end=' ')
    else:
        print(0, end=' ')
