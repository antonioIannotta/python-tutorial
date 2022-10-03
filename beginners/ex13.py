starting_day = int(input("Insert the number of the day: "))

def day_of_week(number):
    if number == 0:
        print("Sunday")
    elif number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    else:
        print("No day allowed for this number!")

if starting_day >= 0 and starting_day < 7:
    stay_length = int(input("Insert the length of your stay: "))
    day = (starting_day + stay_length % 7) % 7
    print("Your day to leave is: " )
    day_of_week(day)
else:
    print("Not valid!")
