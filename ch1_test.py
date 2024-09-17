# CHAPTER 1. Finite Field
from ecc import FieldElement

a = FieldElement(3, 7)
b = FieldElement(5, 7)
print(a == b)

print(a == a)

# Quiz 1.1
print(a != a)

# Quiz 1.2
def modualr_addition(num1=0, num2=0, num3=0, p=1):
    return (num1 + num2 + num3)%p
print(modualr_addition(44, 33, p=57))
print(modualr_addition(9, -29, p=57))
print(modualr_addition(17, 42, 49, 57))
print(modualr_addition(41, 30, 38, 57))


a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a+b)
print(a-b)

# Quiz 1.4
print((95*45*31)%97)
print((17*13*19*44)%97)
print((127*77**49)%97)

# Quiz 1.5
results = {}
for i in [1,3,7,13,18]:
    result = []
    for j in range(0,19):
        result.append((i*j)%19)
    results[i] = sorted(result)

# Quiz 1.6
a = FieldElement(6, 13)
b = FieldElement(8, 13)
print(a**3)

# Quiz 1.7
results = {}
for j in [7, 11, 17, 31]:
    result = []
    for i in range(1, j):
        result.append(i**(j-1)%j)
    results[j] = sorted(result)

# Quiz 1.8
# 3/f24
print((3*pow(24,29) % 31))
# 17^-3
print(pow(17, 27, 31))
# 4^-4 * f11
print((pow(4, 26) * 11) % 31)
