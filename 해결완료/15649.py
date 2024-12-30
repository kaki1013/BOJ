# 15650과 다른 점: 1,2 와 2,1이 다름(고른 수열이 오름차순일 필요 X)
# 참고: https://jiwon-coding.tistory.com/21  // pop하고 다시 dfs 하지 않음
def dfs(selected):
    if len(selected) == M:
        print(*selected)
        return
    for i in range(1, N+1):
        if i not in selected:
            selected.append(i)
            dfs(selected)
            selected.pop()


N, M = map(int, input().split())
dfs([])

# sol2
from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join,permutations(li, M)))))

