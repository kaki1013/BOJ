N, M = map(int, input().split())
NoListen, NoSee = set(), set()
for _ in range(N):
    NoListen.add(input())
for _ in range(M):
    NoSee.add(input())

common = sorted(list(NoListen & NoSee))

print(len(common))
for name in common:
    print(name)

# https://www.acmicpc.net/source/20189660
from sys import stdin
line = stdin.readline().strip().split(' ')
N = int(line[0])
M = int(line[1])
obj = {}
count = 0
names = []
for i in range(N):
    obj[stdin.readline().strip()] = 1
for i in range(M):
    target = stdin.readline().strip()
    if target in obj:
        count += 1
        names.append(target)
print(count)
names.sort()
for name in names:
    print(name)


# https://dojinkimm.github.io/problem_solving/2019/09/26/boj-1764-deutbo.html
import sys

N, M = map(int, sys.stdin.readline().split())
N_list = [sys.stdin.readline().strip() for i in range(N)]
M_list = [sys.stdin.readline().strip() for i in range(M)]

# 교차하는 이름들을 찾는다
duplicate = list(set(N_list) & set(M_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)