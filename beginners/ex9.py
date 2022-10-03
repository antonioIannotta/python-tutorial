xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("Each number on a new line")
for x in xs:
    print(x)

print("Each number and its square")
for x in xs:
    print("Number: " + str(x) + " Square: " + str(x**2))

print("Print the total and product")
total = 0
product = 1
for x in xs:
    total += x
    product *= x
print("Total: " + str(total))
print("Product: " + str(product))

