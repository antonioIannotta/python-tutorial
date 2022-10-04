def days_in_month(month):
    days = 0
    if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
        days = 31
    elif month == "April" or month == "June" or month == "September" or month == "November":
        days = 30
    elif month == "February":
        days = 28
    else:
        days = -1

    return days


print(days_in_month("February"))
print(days_in_month("December"))
