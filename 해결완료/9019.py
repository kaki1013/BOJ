from collections import deque

def D(n):
    return (2*n)%10000

def S(n):
    return (n-1)%10000

def L(n):
    d1 = n//1000
    d234 = n%1000
    return d234*10+d1

def R(n):
    d4 = n%10
    d123 = n//10
    return d4*1000+d123

func = [D, S, L, R]
commands = 'DSLR'

for _ in range(int(input())):
    A, B = map(int, input().split())

    visited = [False]*10000

    q = deque([(A, '')])
    visited[A] = True
    while q:
        curr, cmd = q.popleft()

        if curr == B:
            print(cmd)
            break

        for i in range(4):
            f = func[i]
            nxt = f(curr)
            if not visited[nxt]:
                q.append((nxt, cmd+commands[i]))
                visited[nxt] = True
