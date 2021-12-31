x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
if x1 == x2 and x3 == x4:
    m1, m2 = 0, 0
else:
    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y4 - y3) / (x4 - x3)
Xarr, Yarr = sorted([x1, x2, x3, x4]), sorted([y1, y2, y3, y4])
xm1, xm2, xm3 = Xarr[0], Xarr[1], Xarr[2]
ym1, ym2, ym3 = Yarr[0], Yarr[1], Yarr[2]

if m1 == m2:
    if xm2 == xm3 and ym2 == ym3:
        print(1)
    else:
        xSameLine = {xm1, xm2} == {x1, x2} or {xm1, xm2} == {x3, x4}
        ySameLine = {ym1, ym2} == {y1, y2} or {ym1, ym2} == {y3, y4}
        if not xSameLine or not ySameLine:
            print(1)
        else:
            print(0)

else:
    x = ((y3 - m2 * x3) - (y1 - m1 * x1)) / (m1 - m2)
    y = m1 * (x - x1) + y1
    if xm2 <= x <= xm3 and ym2 <= y <= ym3:
        print(1)
    else:
        print(0)
