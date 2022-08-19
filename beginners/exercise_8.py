monthConversions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(monthConversions.get(1))
monthConversions.__setitem__(13, "Invented")
print(monthConversions.get(13))

cnt = 3

while cnt >= 0:
    print("Hello!")
    cnt -= 1

print("Done with loop!")
