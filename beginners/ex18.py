def to_secs(hours, minutes, seconds):
    result = 0
    if 0 <= hours <= 23:
        result += hours * 3600

    if 0 <= minutes <= 59:
        result += minutes * 60

    result += seconds

    return result


print(to_secs(2, 30, 10))

