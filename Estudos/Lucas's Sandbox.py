input_seconds = int(input())

minutes, remaining_seconds = divmod(input_seconds, 60)
hours, remaining_minutes = divmod(minutes, 60)

print("{}:{}:{}".format(hours,remaining_minutes,remaining_seconds))
