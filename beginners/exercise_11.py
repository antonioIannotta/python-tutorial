try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Invalid division!")
except ValueError:
    print("Invalid input!")