# input
N, M = map(int, input().split())  # (y, x)
arr = []
for _ in range(N):
	line = list(input())
	arr.append(line)

# compare
lineW = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
lineB = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
ansW = []
ansB = []
for i in range(8):
	if i % 2 == 0:
		ansW.append(lineW)
		ansB.append(lineB)
	else:
		ansW.append(lineB)
		ansB.append(lineW)

# check
minW = 64
minB = 64
for i in range(N - 7):
	for j in range(M - 7):  # 좌상단 점 (y=j,x=i) 지정
		checkW = 0
		checkB = 0
		for k in range(8):
			for l in range(8):  # 보드 (k, l) 위치 체크
				if not arr[i+k][j+l] == ansW[k][l]:
					checkW += 1
				if not arr[i+k][j+l] == ansB[k][l]:
					checkB += 1
		minW, minB = min(minW, checkW), min(minB, checkB)

# answer
print(min(minW, minB))