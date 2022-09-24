t_hour = 8; d_hour = 466.4
meridiem = "PM"
flip_meridiem = 0

print(f"Meridiem = {meridiem}")
new_hour = t_hour + d_hour

if new_hour >= 12 :
    flip_meridiem = new_hour // 12
    if flip_meridiem % 2 != 0 :
        if meridiem == "AM" : meridiem = "PM"

print(f"new_hour = {new_hour}, flip_meridiem = {flip_meridiem}, meridiem = {meridiem}")


