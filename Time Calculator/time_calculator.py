def add_time(start, duration, show_day = None):

    def landing_day(day, days_later) :
        # --- When show_day != None this function traverses the list of days and lands on target day
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = day.lower(); day = day.capitalize()       # Clean up the day entry to match list entries
        index = days.index(day)
        count = 0

        while count < days_later :
            count += 1; index += 1
            if index >= len(days) : index = 0

        return days[index]

    #--- BREAK APART | Split start for time & meridiem, time for hour & minute
    #--- then duration time for hour and minute
    meri_flag = False                                  # Meridiem flip flag
    time = start.split()[0]
    meridiem = start.split()[1]
    t_hour = int(time.split(":")[0])
    t_minute = int(time.split(":")[1])
    d_hour = int(duration.split(":")[0])
    d_minute = int(duration.split(":")[1])

    #--- Calculate new time. n_days = days to advance
    new_minute = d_minute + t_minute
    new_hour = d_hour + t_hour + (new_minute // 60)

    #--- Calculate n_days
    if (new_hour / 24) < 1 and meridiem == "AM" : n_days = 0
    else : n_days = round(new_hour / 24)

    if new_minute >= 60 : new_minute -= 60

    if new_hour >= 12 :
        meri_flag = True
        flip_meri_count = (new_hour // 12)

        if flip_meri_count % 2 == 1 :
            if meridiem == "AM" : meridiem = "PM"
            elif meridiem == "PM" : meridiem = "AM"

        new_hour -= (12 * (new_hour // 12))

        if new_hour == 0 : new_hour = 12

    if show_day is not None :
        new_time = f"{new_hour}:{new_minute:02} {meridiem}, {landing_day(show_day, n_days)}"
    else :
        new_time = f"{new_hour}:{new_minute:02} {meridiem}"

    if meri_flag :
        if n_days == 1 :
            new_time = new_time + " (next day)"
        elif n_days > 1 :
            new_time = new_time + f" ({n_days} days later)"

    return new_time
