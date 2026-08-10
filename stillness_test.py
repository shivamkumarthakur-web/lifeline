readings = [1.0, 1.0, 8.0, 6.0, 5.5, 5.8, 4.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

rough_ended = False   # this tracks whether the rough/shaky part has fully ended yet
still_count = 0        # this counts calm readings, but ONLY after rough part ends

for reading in readings:
    if reading > 2.0:
        # still in the rough/shaky part (impact or sliding) - keep waiting
        rough_ended = False
    else:
        # this reading is calm
        if rough_ended == False:
            # this is the FIRST calm reading right after rough part - mark rough as ended
            rough_ended = True
        else:
            # rough part already ended before, and still calm now - count it
            still_count += 1

print("Still count after rough patch ended:", still_count)