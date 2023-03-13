# datetime module use

import datetime

# Get the current date and time
now = datetime.datetime.now()
print("now date", now)

# Extract the date and time separately
today = datetime.date.today()
print("today date", today)
current_time = datetime.time(now.hour, now.minute, now.second)
print("current_time", current_time)

# Create a new date and time
new_date = datetime.date(2022, 12, 25)
new_time = datetime.time(12, 0, 0)
new_datetime = datetime.datetime.combine(new_date, new_time)
print("combination", new_datetime)


# Perform date and time arithmetic
one_day = datetime.timedelta(days=1)
yesterday = today - one_day
print("timedelta print yesterday", yesterday)

# Format date and time strings
formatted_date = today.strftime("%A, %B %d, %Y")
print("today strftime", formatted_date)
formatted_time = current_time.strftime("%I:%M %p")
print("current strftime", formatted_time)
