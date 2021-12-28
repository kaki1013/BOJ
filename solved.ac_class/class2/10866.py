# 틀림, 인덱스 꼬임
import sys
N = int(input())
deq = []
left = 0
right = 0
for _ in range(N):
    arr = sys.stdin.readline().split()
    cmd = arr[0]
    if cmd == 'push_front':
        if left == 0:
            deq = [int(arr[1])] + deq
        else:
            deq[left - 1] = int(arr[1])
            left -= 1
    elif cmd == 'push_back':
        deq = deq + [int(arr[1])]
    elif cmd == 'pop_front':
        if len(deq) == right + left:
            print(-1)
        else:
            print(deq[left])
            left += 1
    elif cmd == 'pop_back':
        if len(deq) == right + left:
            print(-1)
        else:
            print(deq[-1 - right])
            right += 1
    elif cmd == 'size':
        print(len(deq) - right - left)
    elif cmd == 'empty':
        print(int(len(deq) - right - left == 0))
    elif cmd == 'front':
        if len(deq) == right + left:
            print(-1)
        else:
            print(deq[left])
    elif cmd == 'back':
        if len(deq) == right + left:
            print(-1)
        else:
            print(deq[-1 - right])