speed_readings = [20, 20, 19, 21, 3, 2, 2, 2, 2, 2]

highest_speed = max(speed_readings)
lowest_speed_after = min(speed_readings)

speed_drop = highest_speed - lowest_speed_after
print("Speed drop:", speed_drop)