def print_op(num1, num2, operation_type):
    if str(operation_type).__eq__("sum"):
        sum = num1 + num2
        print_helper("sum", num1, num2, sum)
    elif str(operation_type).__eq__("diff"):
        diff = num1 - num2
        print_helper("diff", num1, num2, diff)
    elif str(operation_type).__eq__("mul"):
        mul = num1 * num2
        print_helper("mul", num1, num2, mul)
    elif str(operation_type).__eq__("div"):
        div = num1 / num2
        print_helper("div", num1, num2, div)


def print_helper(op, num1, num2, result):
    print("The " + op + " between " + str(num1) + " and " + str(num2) + " is: " + str(result))