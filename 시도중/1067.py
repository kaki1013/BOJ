"""
   x1 x2 ... xn x1 x2 ... xn
1. y1 y2 ... yn
2.    y1 y2 ... yn
        ...
n.           y1 y2 ... yn
: 위 n가지 경우를 살펴보면 됨

"""
N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))


