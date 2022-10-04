def hours_in(seconds):
    return int(seconds / 3600)


def minutes_in(seconds):
    return int((seconds - (hours_in(seconds) * 3600)) / 60)


def seconds_in(seconds):
    return seconds - (hours_in(seconds)*3600 + minutes_in(seconds)*60)


print(hours_in(9010))
print(minutes_in(9010))
print(seconds_in(9010))
