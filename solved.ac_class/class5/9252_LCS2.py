# 9251 참고
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence#%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4longest-common-subsequence-%EC%B0%BE%EA%B8%B0
from collections import deque

s1, s2 = input(), input()
l1, l2 = len(s1), len(s2)  # row, column

# lcs(i, j) := s1[:i+1]과 s2[:j+1]의 최장 공통 부분 수열의 길이
lcs = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for i in range(l1):
    for j in range(l2):  # s1과 s2 차례로 비교
        if s1[i] == s2[j]:  # s1의 (i-1)번째와 s2의 (j-1)번째가 같으면
            lcs[i+1][j+1] = lcs[i][j] + 1  # lcs의 (i, j) = lcs의 (i-1, j-1) + 1// 두 글자를 이용하여 lcs를 1 증가
        else:  # 다르면
            lcs[i+1][j+1] = max(lcs[i+1][j], lcs[i][j+1])  # s1이나 s2의 마지막 글자 하나 제외
print(lcs[-1][-1])

q = deque([])
i, j = l1, l2  # LCS 마지막 위치부터
while lcs[i][j] != 0:  # 0을 만날 때까지
    if lcs[i][j] == lcs[i-1][j]:  # 위랑 같으면 위로 이동
        i -= 1
    elif lcs[i][j] == lcs[i][j-1]:  # 왼쪽이랑 같으면 왼쪽으로 이동
        j -= 1
    elif lcs[i][j] == lcs[i-1][j-1] + 1:  # 둘 다 아니면 대각선으로 이동
        q.extendleft(s1[i-1])  # lcs의 배열들이 길이 1씩 더 길기 때문에 하나 작은 값 저장
        i -= 1
        j -= 1
print("".join(q))
