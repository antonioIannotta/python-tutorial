def day_name(num):
    if num == 0:
        return "Sunday"
    elif num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"


def day_num(name):
    num = 0
    if name == "Sunday":
        num = 0
    elif name == "Monday":
        num = 1
    elif name == "Tuesday":
        num = 2
    elif name == "Wednesday":
        num = 3
    elif name == "Thursday":
        num = 4
    elif name == "Friday":
        num = 5
    elif name == "Saturday":
        num = 6
    else:
        num = -1

    return num


def day_add(name, delta):
    if delta >= 0:
        num = day_num(name)
        if num >= 0:
            day = (num + (delta % 7)) % 7
            return day_name(day)
    elif delta < 0:
        num = day_num(name)
        if num >= 0:
            day = (num - (abs(delta) % 7)) % 7
            return day_name(day)


print(day_add("Monday", 4))
print(day_add("Tuesday", 0))
print(day_add("Tuesday", 14))
print(day_add("Sunday", 100))
print(day_add("Sunday", -1))
print(day_add("Sunday", -7))
print(day_add("Tuesday", -100))



