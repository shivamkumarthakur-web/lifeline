def get_impact_strength(accel_readings):
    return max(accel_readings)


def get_speed_drop(speed_readings):
    return max(speed_readings) - min(speed_readings)


def get_stillness_count(readings):
    rough_ended = False
    still_count = 0
    for reading in readings:
        if reading > 2.0:
            rough_ended = False
        else:
            if rough_ended == False:
                rough_ended = True
            else:
                still_count += 1
    return still_count


def calculate_confidence(impact_strength, speed_drop, stillness_seconds):
    confidence = 0
    if impact_strength > 4:
        confidence += 30
    if speed_drop >= 20:
        confidence += 40
    if stillness_seconds > 10:
        confidence += 30
    return confidence


def check_alert(confidence):
    if confidence >= 70:
        return "Trigger confirmation alert!"
    else:
        return "No alert needed!"


test_cases = [
    {
        "name": "Real bike accident (with sliding)",
        "accel": [1.0, 1.0, 8.0, 6.0, 5.5, 5.8, 4.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        "speed": [25, 25, 24, 26, 2, 1, 1, 1, 1, 1],
        "motion": [1.0, 1.0, 8.0, 6.0, 5.5, 5.8, 4.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    },
    {
        "name": "Victim conscious, picks phone back up",
        "accel": [1.0, 1.0, 6.5, 1.0, 1.0, 2.3, 1.8, 2.5, 1.9, 2.1],
        "speed": [20, 20, 19, 21, 3, 2, 2, 2, 2, 2],
        "motion": [1.0, 1.0, 6.5, 1.0, 1.0, 2.3, 1.8, 2.5, 1.9, 2.1],
    },
    {
        "name": "Dancing hard",
        "accel": [1.0, 5.0, 1.0, 4.5, 1.0, 5.2, 1.0, 4.8, 1.0, 5.0],
        "speed": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "motion": [1.0, 5.0, 1.0, 4.5, 1.0, 5.2, 1.0, 4.8, 1.0, 5.0],
    },
    {
        "name": "Phone thrown on bed",
        "accel": [1.0, 1.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        "speed": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "motion": [1.0, 1.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    },
]

for case in test_cases:
    impact_strength = get_impact_strength(case["accel"])
    speed_drop = get_speed_drop(case["speed"])
    stillness_seconds = get_stillness_count(case["motion"])

    confidence = calculate_confidence(impact_strength, speed_drop, stillness_seconds)
    result = check_alert(confidence)

    print(f"{case['name']}: impact={impact_strength}, speed_drop={speed_drop}, stillness={stillness_seconds}, confidence={confidence} -> {result}")