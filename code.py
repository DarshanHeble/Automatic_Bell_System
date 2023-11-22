import time

# Get the current time as a struct_time object
current_time = time.localtime()

# Get the day of the week as an integer (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
current_day = current_time.tm_wday

days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# Print the current day
print("Current day:", days_of_week[current_day])
curr_time = time.strftime("%d-%m-%Y %I:%M:%S %p")

print(curr_time)
# am_or_pm = time.strftime("%p")
# print(am_or_pm)
