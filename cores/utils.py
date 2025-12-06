def parse_time_slots(user_input):
    result = {}
    for day, slots in user_input.items():
        cleaned = [s.strip() for s in slots.split(",") if s.strip()]
        result[day] = cleaned
    return result
