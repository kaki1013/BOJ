from sys import stdin
input = stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2, -1, -1):
    for j in range(i+1):
        if triangle[i+1][j] > triangle[i+1][j+1]:
            triangle[i][j] += triangle[i+1][j]
        else:
            triangle[i][j] += triangle[i+1][j+1]

print(triangle[0][0])

'''
import sys

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))

accum = []
for i in range(n):
    accum = [max(a + c, b + c) for a, b, c in zip([0] + accum, accum + [0], triangle[i])]
print(max(accum))'''