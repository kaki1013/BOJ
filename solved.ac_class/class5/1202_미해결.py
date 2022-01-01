# 가방 무게가 오름차순으로 w1, w2, ..., wk 일 때
# 가방 무게보다 작은 것들 중 최대 가치인 것을 넣으면 됨
import sys

N, K = map(int, input().split())
mv = [tuple(map(int, input().split())) for _ in range(N)]
bags = sorted([int(input()) for _ in range(K)])
