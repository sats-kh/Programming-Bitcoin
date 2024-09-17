# CHAPTER 2. Elliptic Curve
from ecc import Point
p1 = Point(-1,-1, 5, 7)

# p2 = Point(-1,-1, 5, 7)

# Quiz 2.1
# p1 = Point(2,4,5,7)
p2 = Point(-1, -1, 5, 7)
p3 = Point(18, 77, 5, 7)
# p4 = Point(5, 7, 5, 7)

# 점 덧셈
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 7)
# None은 타원곡선위에 점이 존재하지 않음, 즉 무한대를 의미
inf = Point(None, None, 5, 7)

# Quiz 2.4
# Y^2 = X^3 + 5X + 7, point 1: (2, 5), point 2:(-1,-1)
x1, x2 = 2, -1
y1, y2 = 5, -1
s = (y2 - y1) / (x2 - x1)
x3 = s**2 - x1 - x2
y3 = s * (x1 - x3) - y1
print(x3, y3)

# Quiz2.5
# Y^2 = X^3 + 5X + 7, Point 1: (-1, -1), Point 2: (-1, 1)
x1, y1 = -1, -1
a, b = 5, 7
s = (3*x1**2 + a)/ 2*y1
x3 = s**2 - 2*x1
y3 = s*(x1 - x3) - y1
