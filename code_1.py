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
data = {
    "hour": 2,
    "minute": 20,
    "am_pm": "am",
    "name": "hello",
    "Sunday": "on",
    "Monday": "on",
    "Tuesday": "on",
    "Wednesday": "on",
    "Thursday": "on",
    "Friday": "on",
    "Saturday": "on",
    "schedule_on_off": "on",
}
data["hour"] = 3
print(data["hour"])
# Print the current day
print("Current day:", days_of_week[current_day])
curr_time = time.strftime("%d-%m-%Y %I:%M:%S %p")

print(curr_time)
# am_or_pm = time.strftime("%p")
# print(am_or_pm)
