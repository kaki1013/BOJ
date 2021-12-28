from math import cos
r, h, d1, A1, d2, A2 = map(float, input().split())
l = (r*r + h*h) ** 0.5
A = abs(A1-A2)
theta = A * r / l

dist = d1**2 + d2**2 - 2*d1*d2*cos(theta)
dist **= 0.5
print(dist)
