from math import pow


def greet(name):
    print("Hello " + name + "!")


def max_num(num1, num2, num3):
    max = 0
    if num1 >= num2 and num1 >= num3:
        max = num1
    elif num2 >= num1 and num2 >= num3:
        max = num2
    elif num3 >= num1 and num3 >= num2:
        max = num3
    return max


def cube(number):
    return pow(number, 3)


print(max_num(4, 2, 3))
greet("Antonio")
print(cube(10))

is_male = False
is_tall = True

if is_male or is_tall:
    print("Is male!")
else:
    print("Is female!")
