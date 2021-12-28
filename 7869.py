import math
x1, y1, r1, x2, y2, r2 = map(float, input().split())
if r1 > r2:
    x1, x2 = x2, x1
    y1, y2 = y2, y1
    r1, r2 = r2, r1
power_d = (x1-x2)**2 + (y1-y2)**2
d = math.sqrt(power_d)
ans = 0

if power_d < (r1+r2)**2:
    if d+r1 <= r2:
        ans = math.pi * r1**2
    else:
        if d >= r2:  # 왜 이것만으로 가능?? -> 아래 주석에 적어놓은 것들을 이용하면 두 식이 같음을 알 수 있음
            d1, d2 = (power_d + r1 ** 2 - r2 ** 2) / (2 * d), (power_d - r1 ** 2 + r2 ** 2) / (2 * d)
            theta1, theta2 = 2 * math.acos(d1 / r1), 2 * math.acos(d2 / r2)
            ans = (r1 ** 2 / 2) * (theta1 - math.sin(theta1)) + (r2 ** 2 / 2) * (theta2 - math.sin(theta2))
        elif d < r2:
            d1, d2 = (-power_d - r1 ** 2 + r2 ** 2)/(2 * d), (power_d - r1 ** 2 + r2 ** 2)/(2 * d)   # d1은 -d1, d2는 동일
            theta1, theta2 = math.acos(d1 / r1), math.acos(d2 / r2)  # theta1은 pi-theta1, theta2는 동일
            ans = r2**2*theta2 - r2**2*math.sin(theta2)*(d2/r2) + r1**2*math.sin(theta1)*(d1/r1) + r1**2*(math.pi - theta1)

print('0.000' if ans == 0 else round(ans, 3))  # 0일 때 0.000으로 출력
