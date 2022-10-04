import sys

def turn_clockwise(compass_point):
    if compass_point == "N":
        return "E"
    elif compass_point == "E":
        return "S"
    elif compass_point == "S":
        return "W"
    elif compass_point == "W":
        return "N"
    else:
        return "Illegal compass point!"


print(turn_clockwise("N"))
print(turn_clockwise("rubbish"))
