# sol1: 위키백과(1번째 링크) 또는 위키하우(2번째 링크)의 파트3 '변의 길이가 다른 다각형 넓이 구하기' 참고
# https://ko.wikipedia.org/wiki/%EB%8B%A4%EA%B0%81%ED%98%95#%EB%84%93%EC%9D%B4
# https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0
import sys
N = int(sys.stdin.readline().rstrip())
points = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
points.append(points[0])

ans1, ans2 = 0, 0
for i in range(N):
    ans1 += points[i][0] * points[i+1][1]
    ans2 += points[i][1] * points[i+1][0]
ans = abs(ans1 - ans2)/2
print(ans)

# sol2: ccw 알고리즘
# https://ip99202.github.io/posts/%EB%B0%B1%EC%A4%80-2166-%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98-%EB%A9%B4%EC%A0%81/
import sys
N = int(sys.stdin.readline().rstrip())
points = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

ans = 0
for i in range(1, N-1):
    triangle_multi = points[0][0]*points[i][1] + points[i][0]*points[i+1][1] + points[i+1][0]*points[0][1]
    triangle_multi -= points[i][0]*points[0][1] + points[i+1][0]*points[i][1] + points[0][0]*points[i+1][1]
    ans += triangle_multi
ans = abs(ans)/2
print(ans)