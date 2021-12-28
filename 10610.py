N = int(input())
n_string = str(N)
digit_list = [int(n) for n in n_string]
set_n = set(digit_list)

if 0 in set_n and sum(digit_list) % 3 == 0:
    digit_list.sort(reverse=True)
    for i in range(len(n_string)-1):
        print(digit_list[i], end='')
    print(digit_list[-1])
else:
    print(-1)
