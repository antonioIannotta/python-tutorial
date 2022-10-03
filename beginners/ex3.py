time_now = int(input("Insert the current hour: "))
time_to_wait = int(input("How many time do you want to wait?  "))
res = (time_now + (time_to_wait % 24)) % 12
print("Your alarm is setted for " + str(res))

