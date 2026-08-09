def calculate_confidence(impact_strength,speed_drop,stillness_seconds):
    confidence=0
    if impact_strength>4:
        confidence+=30
    if speed_drop>=20:
        confidence+=40
    if stillness_seconds>10:
        confidence+=30
    return confidence


def check_alert(confidence):
    if confidence>=70:
        return "Trigger confirmation alert!"
    else:
        return "No alert needed!"


test_cases = [
    {"name": "Real bike accident", "impact": 6, "speed_drop": 25, "stillness": 12},
    {"name": "Victim conscious, picks up phone fast", "impact": 6, "speed_drop": 25, "stillness": 0},
    {"name": "Dancing hard", "impact": 5, "speed_drop": 0, "stillness": 0},
    {"name": "Phone thrown on bed", "impact": 3, "speed_drop": 0, "stillness": 20},
    {"name": "Just sleeping normally", "impact": 0, "speed_drop": 0, "stillness": 20},
]
for case in test_cases:
    confidence = calculate_confidence(case["impact"], case["speed_drop"], case["stillness"])
    result = check_alert(confidence)
    print(f"{case['name']}: confidence={confidence} -> {result}")
