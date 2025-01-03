"""
observe 1:
최소 개수의 추로 표현하는 방법 : 2진수
1, 2, 4, 8, ...
1 <= n <= 1000
1 <= w_i <= 1,000,000
이므로

해당 조건에서 사용해야 하는 추의 무게는
1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2^11, ..., 2^19=524288
로 20가지이고

해당 조건에서 최대로 표현 가능한 무게는
1, 3, 7, 15, ..., 2^20-1

이런 식으로 50*(2^20-1)까지 나타낼 수 있음

observe 2:
1 1 2 3 6 7 30

1 1이 있을 때 : 2까지 표현 가능 -> 2가 들어오면 4까지 표현가능
1 1 2가 있을 때 : 4까지 표현 가능 -> 4이하인 x가 들어오면 4+x까지 표현가능
1 1 2 x가 있을 때 : 4+x까지 표현 가능 -> 4+x이하인 y가 들어오면 4+x+y까지 표현 가능
...
1 1 2 3 6 7이 있을 때 : 20까지 표현 가능 -> 20이하인 z가 들어오면 20+z까지 표현 가능 / 아니라면 20+1이 답

greedy!
정당성
a1, a2, .., an 으로 1부터 x(=sum)까지 표현가능하다고 가정.
새로운 y(=a_n+1)가 x+1이하라면 1부터 x+y까지 표현 가능하고, x+y+1은 표현 불가능하다.
pf.
1부터 x+y까지 표현 가능함은 자명함 -> y<=t<=x+y에 대해 t-y를 포현하는 방법에서 y를 추가로 쓰면 됨
x+y+1은 표현 불가능함을 귀류법으로 증명하자.
가능한 방법의 경우는 2가지
(1) 해당 방법이 y를 사용 : 해당 방법에서 y만 제외하면, x+1을 표현하는 방법인데 이는 x가 최대 표현 가능 수라는 것에 모순
(2) 해당 방법이 y를 사용 x : 가정에 의해, 1 <= x+y+1 <= x이지만 이는 모순(a1부터 an까지만 사용하여 표현 가능하므로 1부터 x까지 중에 하나여야 함)

"""

N = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

possible = 0
while arr:
    tmp = arr.pop()
    if tmp <= possible + 1:
        possible += tmp
    else:
        break

print(possible + 1)
