# 외적
[(a, b), (c, d), (e, f)] = [tuple(map(int, input().split())) for _ in range(3)]
x, y, z, w = c-a, d-b, e-a, f-b
ccw = x*w-y*z
if ccw > 0:
    print(1)
elif ccw == 0:
    print(0)
elif ccw < 0:
    print(-1)
