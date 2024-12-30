# sol1 : 파이썬 집합 자료형
import sys
M = int(sys.stdin.readline().rstrip())
s = set()
for _ in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    if len(cmd) == 1 and cmd == ['all']:
        s = set(range(1, 21))
    elif len(cmd) == 1 and cmd == ['empty']:
        s = set()
    elif len(cmd) == 2:
        cmd, x = cmd[0], int(cmd[1])
        if cmd == 'add':
            if x not in s:
                s.add(x)
        elif cmd == 'remove':
            if x in s:
                s.remove(x)
        elif cmd == 'check':
            print(int(x in s))
        elif cmd == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)

# sol2 : TF 배열
import sys

M = int(sys.stdin.readline().rstrip())
TF_arr = [False for _ in range(21)]
for _ in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    if len(cmd) == 1 and cmd == ['all']:
        TF_arr = [True for _ in range(21)]
    elif len(cmd) == 1 and cmd == ['empty']:
        TF_arr = [False for _ in range(21)]
    elif len(cmd) == 2:
        cmd, x = cmd[0], int(cmd[1])
        if cmd == 'add':
            TF_arr[x] = True
        elif cmd == 'remove':
            TF_arr[x] = False
        elif cmd == 'check':
            print(int(TF_arr[x]))
        elif cmd == 'toggle':
            if TF_arr[x]:
                TF_arr[x] = False
            else:
                TF_arr[x] = True

# sol3: 비트마스킹
import sys

M = int(sys.stdin.readline().rstrip())
state = 0
for _ in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    if len(cmd) == 2:
        cmd, x = cmd[0], int(cmd[1])
        if cmd == 'add':
            state |= (1 << x)
        elif cmd == 'remove':
            state &= ~(1 << x)
        elif cmd == 'check':
            print(int((state & (1 << x)) != 0))
        elif cmd == 'toggle':
            state ^= (1 << x)
    else:
        if cmd[0] == 'all':
            state = (1 << 21)-1  # shift 연산에서 x-1이 아닌 x만큼 shift, 즉 0부터 20까지 '21개'의 수들을 관리함
        elif cmd[0] == 'empty':
            state = 0
