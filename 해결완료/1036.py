# 1339 참고
char_to_num = dict([(chr(ord('0')+i), i) for i in range(10)]+[(chr(ord('A')+i), 10+i) for i in range(26)])
num_to_char = list(char_to_num.keys())

N = int(input())
p = 36

d = dict()
for _ in range(N):
    number = input()
    length = len(number)
    for i in range(length):
        char = number[i]
        if char in d:
            d[char] += p ** (length-1-i)
        else:
            d[char] = p ** (length-1-i)

# 바꿨을 때 증가량이 큰 문자를 변경
diff = []
for k, v in d.items():
    diff.append((k, (char_to_num['Z']-char_to_num[k]) * v))  # https://www.acmicpc.net/board/view/128261
count = sorted(diff, key=lambda x: x[1])

# get max K elements
K = int(input())
Z = 0
for _ in range(min(K, len(count))):
    char, num = count.pop()
    Z += d[char]
    del d[char]

# 변화 반영
if 'Z' in d:
    d['Z'] += Z
else:
    d['Z'] = Z

# get answer
ans = 0
for char, num in d.items():
    ans += char_to_num[char] * num

# change '36'
stack = []
if ans == 0:
    stack.append('0')
else:
    while ans:
        stack.append(num_to_char[ans % p])
        ans //= p
stack = stack[::-1]
print(''.join(stack))
