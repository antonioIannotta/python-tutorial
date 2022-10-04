import math


def compare(num1, num2):
    if num1 > num2:
        return 1
    elif num1 == num2:
        return 0
    else:
        return -1


def hypotenuse(leg1, leg2):
    return math.sqrt(leg1*leg1 + leg2*leg2)


def slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)


def is_factor(num1, num2):
    return num2 % num1 == 0


print(compare(5, 4))
print(compare(7, 7))
print(compare(2, 3))
print(compare(42, 1))

print(hypotenuse(3, 4))
print(hypotenuse(12, 5))
print(hypotenuse(24, 7))
print(hypotenuse(9, 12))

print(slope(5, 3, 4, 2))
print(slope(1, 2, 3, 2))
print(slope(1, 2, 3, 3))
print(slope(2, 4, 1, 2))

print(is_factor(3, 12))
print(not is_factor(5, 12))
print(is_factor(7, 14))
print(not is_factor(7, 15))
print(is_factor(1, 15))
print(is_factor(15, 15))
print(not is_factor(25, 15))

