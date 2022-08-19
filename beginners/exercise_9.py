for letter in "Antonio":
    print(letter)

for i in range(0, 10):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

friends = ["Antonio", "Mario", "Ciccj"]

for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(index)


def exponent(b, e):
    result = 1
    for cnt in range(0, e):
        result *= b

    return result


print(exponent(2, 3) == 8)
