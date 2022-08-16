from math import pow


def greet(name):
    print("Hello " + name + "!")


def cube(number):
    return pow(number, 3)


greet("Antonio")
print(cube(10))

is_male = False
is_tall = True

if is_male or is_tall:
    print("Is male!")
else:
    print("Is female!")
