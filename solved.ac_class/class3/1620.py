# 입력받는 게 느림 / https://www.acmicpc.net/board/view/41739
'''N, M = map(int, input().split())
num_to_char = dict()
char_to_num = dict()
for i in range(N):
    name = input()
    num_to_char[i + 1] = name
    char_to_num[name] = i + 1

for _ in range(M):
    want = input()
    if 49 <= ord(want[0]) <= 57:
        print(num_to_char[int(want)])
    else:
        print(char_to_num[want])'''
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
num_to_char = dict()
char_to_num = dict()
for i in range(N):
    name = sys.stdin.readline().rstrip()
    num_to_char[i + 1] = name
    char_to_num[name] = i + 1

for _ in range(M):
    want = sys.stdin.readline().rstrip()
    if 49 <= ord(want[0]) <= 57:
        print(num_to_char[int(want)])
    else:
        print(char_to_num[want])