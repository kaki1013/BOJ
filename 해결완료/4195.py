# 참고: https://www.acmicpc.net/board/view/48489
# 참고: https://www.acmicpc.net/board/view/65195
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        p[a] = b
        temp = number[a] + number[b]
        number[a], number[b] = temp, temp


T = int(input())
for _ in range(T):
    F = int(input())
    name_to_idx = dict()
    number = dict()     # 집합 원소 개수 빠르게 세기 위함
    count = 0
    p = []
    for f in range(F):
        a, b = input().split()
        if a not in name_to_idx:
            name_to_idx[a] = count
            number[count] = 1
            p.append(count)
            count += 1
        if b not in name_to_idx:
            name_to_idx[b] = count
            number[count] = 1
            p.append(count)
            count += 1
        a, b = name_to_idx[a], name_to_idx[b]
        a, b = find(a), find(b)
        union(a, b)
        print(number[b])
