# 알고리즘 트레이닝 p.271
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
