def add_time(start_time, duration_time, start_week=None):
    # strip the input for data
    start_hour = int(start_time.split(":")[0])
    start_minutes = int(start_time.split(":")[1].split(" ")[0])
    period = start_time.split(":")[1].split(" ")[1]

    duration_hour = int(duration_time.split(":")[0])
    duration_minutes = int(duration_time.split(":")[1])

    # sum
    sum_hour = start_hour + duration_hour
    if period == "PM":
        sum_hour += 12 # change to 24h format
    sum_minutes = start_minutes + duration_minutes

    # endtime, formatted in 24h
    end_days = int(sum_hour/24) # + int(sum_minutes/60)
    end_hours = sum_hour % 24 + int(sum_minutes/60)
    end_minutes = sum_minutes % 60

    # format to 12h
    if end_hours >= 12 and end_hours != 24:
        end_period = "PM"
        end_hours -= 12
    else:
        end_period = "AM"
    # exception 12 AM and 12 PM
    if end_hours == 24:
        end_hours = 12
        end_days += 1
    elif end_hours == 0:
        end_hours = 12

    # check if need to add a 0 for the minutes
    zero = ""
    if end_minutes < 10:
        zero = 0

    end_week = ""

    # user add weekday
    if start_week:
        weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        index_of = weekdays.index(start_week.lower())
        new_index = (index_of + end_days) % 7
        end_week = f", {weekdays[new_index]}"


    # if user don't add weekday
    days = ""
    if end_days > 1:
        days = f" ({end_days} days later)"
    elif end_days > 0:
        days = f" (next day)"
    return f"{end_hours}:{zero}{end_minutes} {end_period}{end_week.title()}{days}"

if __name__ == "__main__":
    print(add_time("11:59 PM", "24:05", "Wednesday"))