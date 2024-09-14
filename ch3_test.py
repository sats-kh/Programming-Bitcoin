# Quiz 3.1
from ecc import FieldElement, Point, S256Field

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)

def on_curve(x, y):
    return y**2 == x**3 + a*x + b

print(on_curve(FieldElement(192, prime), FieldElement(105, prime)))
print(on_curve(FieldElement(17, prime), FieldElement(56, prime)))
print(on_curve(FieldElement(200, prime), FieldElement(119, prime)))
print(on_curve(FieldElement(1, prime), FieldElement(193, prime)))
print(on_curve(FieldElement(42, prime), FieldElement(99, prime)))

a = FieldElement(num=0, prime=223)
b = FieldElement(num=7, prime=223)
x = FieldElement(num=192, prime=223)
y = FieldElement(num=105, prime=223)

p1 = Point(x,y,a,b,)
print(p1)

import ecc
from helper import run
run(ecc.ECCTest('test_on_curve'))

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x1 = FieldElement(192, prime)
y1 = FieldElement(105, prime)
x2 = FieldElement(17, prime)
y2 = FieldElement(56, prime)

p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
print(p1+p2)

# Quiz 3.2
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x1 = FieldElement(170, prime)
y1 = FieldElement(142, prime)
x2 = FieldElement(60, prime)
y2 = FieldElement(139, prime)

p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
print(p1 + p2)

x1 = FieldElement(47, prime)
y1 = FieldElement(71, prime)
x2 = FieldElement(17, prime)
y2 = FieldElement(56, prime)

p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
print(p1 + p2)

x1 = FieldElement(143, prime)
y1 = FieldElement(98, prime)
x2 = FieldElement(76, prime)
y2 = FieldElement(66, prime)

p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
print(p1 + p2)

# Quiz 3.3
run(ecc.ECCTest('test_add'))

# Quiz 3.4
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x1 = FieldElement(192, prime)
y1 = FieldElement(105, prime)
p1 = Point(x1, y1, a, b)
print(p1 + p1 + p1)

x1 = FieldElement(143, prime)
y1 = FieldElement(98, prime)
p1 = Point(x1, y1, a, b)
print(p1 + p1)

x1 = FieldElement(47, prime)
y1 = FieldElement(71, prime)
p1 = Point(x1, y1, a, b)
print(p1 + p1 + p1 + p1 + p1 + p1+ p1+ p1+ p1+ p1+ p1+ p1+ p1+ p1+ p1+ p1+ p1+ p1+ p1+ p1 + p1)

# Quiz 3.5
prime = 223
x = FieldElement(15, prime)
y = FieldElement(86, prime)
p = Point(x, y, a, b)
print(7 * p)

from ecc import G,N, S256Point
print(N*G)

# example3.12
z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
point = S256Point(px, py)
s_inv = pow(s, N-2, N)
u = z * s_inv % N
v = r * s_inv % N
print((u*G + v*point).x.num == r)

# Quiz 3.6

px = 0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c
py = 0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34
point = S256Point(px, py)
z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4

s_inv = pow(s, N - 2 , N)
u = z * s_inv % N
v = r * s_inv % N
print((u*G + v*point).x.num == r)

z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
r = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
s = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6
s_inv = pow(s, N - 2 , N)
u = z * s_inv % N
v = r * s_inv % N
print((u*G + v*point).x.num == r)

# create signature
from helper import hash256

e = int.from_bytes(hash256(b'my secret'), 'big')
z = int.from_bytes(hash256(b'my message'), 'big')
k = 1234567890
r = (k*G).x.num
k_inv = pow(k, N-2, N)
s = (z +r*e) * k_inv % N
point = e*G
print(point)
print(hex(z))
print(hex(r))

