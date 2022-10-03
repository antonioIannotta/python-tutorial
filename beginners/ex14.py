def mark_to_string(mark):
    res = ""
    if int(mark) >= 75:
        res = "First"
    elif 70 <= int(mark) <= 75:
        res = "Upper second"
    elif 60 <= int(mark) < 70:
        res = "Second"
    elif 50 <= int(mark) < 60:
        res = "Third"
    elif 45 <= int(mark) < 50:
        res = "F1 Supp"
    elif 40 <= int(mark) < 45:
        res = "F2"
    elif int(mark) < 40:
        res = "F3"

    return res


print(mark_to_string(73))

