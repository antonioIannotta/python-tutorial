from calculator_library import *


print("Hello! this is a calculator")
name = input("Insert your name: ")
surname = input("Insert your surname: ")
age = input("Insert your age: ")

print("Hello " + name + "!")

number_1 = int(input("Insert the first number: "))
number_2 = int(input("Insert the second number: "))

print_op(number_1, number_2, "sum")
print_op(number_1, number_2, "diff")
print_op(number_1, number_2, "mul")
print_op(number_1, number_2, "div")