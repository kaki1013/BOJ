# 2번째 예제에서 5,5와 6,6이 있다면 양쪽에서 가는 것보다
# 한쪽에서 둘 다 끄고 오는 것이 최소 경로임
T = int(input())
for _ in range(T):
    F, R, N = map(int, input().split())
    ans = 2*F + R + 1   # 전광판을 끄기 위한 최소 거리
    rooms = [[0] for _ in range(F+1)]
    for __ in range(N):
        floor, room = map(int, input().split())
        rooms[floor].append(room)
    for room in rooms:
        temp = 100      # R은 최대 30이므로 왕복 거리는 최대 60
        room.sort()
        l = len(room)
        if l > 1:       # l == 1 이면 [0]의 초기상태, 즉 불 켜진 사무실 X
            if l == 2:  # 불 켜진 사무실 하나
                r = room[1]
                temp = min(2*r, 2*(R+1-r))
            else:       # 불 켜진 사무실 2개 이상
                for i in range(l):
                    room.append(R+1)
                    left, right = room[i], room[i+1]
                    # <--- , -><--, --><-, ---> 중 최소 이동 거리 탐색
                    temp = min(temp, 2*left+2*(R+1-right))
            ans += temp
    print(ans)