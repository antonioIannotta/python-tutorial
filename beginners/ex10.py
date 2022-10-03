def sum_to(number):
    res = 0
    counter = 0

    while counter <= number:
        res += counter
        counter += 1

    return res


print(sum_to(10))
