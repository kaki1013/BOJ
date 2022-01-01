# 서로 다른 L개의 알파벳 소문자들로 구성
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열
# 암호로 사용했을 법한 문자의 종류는 C가지
def dfs(now, r):    # now : 지금 살펴볼 문자의 idx, r : 현재 고른 문자의 개수
    if r + (C - now) < L:   # 고른 문자 + 고를 수 있는 문자의 최대 개수
        return
    if r == L:  # 다 고른 상황
        aeiou = 0
        for i in range(L):
            if chosen[i] in ['a', 'e', 'i', 'o', 'u']:
                aeiou += 1
        if aeiou >= 1 and L-aeiou >= 2:
            print(''.join(chosen))
        return
    for i in range(now, C):
        chosen.append(alpha[i])
        dfs(i+1, r+1)
        chosen.pop()

L, C = map(int, input().split())
alpha = sorted(input().split())
chosen = []
dfs(0, 0)