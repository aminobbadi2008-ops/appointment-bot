def is_available(dentist, time_slot):
    # For now, assume everyone is always free
    return True

def get_duration(appointment_type):
    if appointment_type in ["cleaning", "checkup"]:
        return "30 minutes"
    elif appointment_type in ["root canal", "filling"]:
        return "1 hour"
    elif appointment_type == "braces":
        return "2 hours"
    return "unknown"

def schedule_appointment(appointment_type, dentist, time_slot):
    if not (appointment_type and dentist and time_slot):
        return None
    if is_available(dentist, time_slot):
        return {
            "type": appointment_type,
            "dentist": dentist,
            "time_slot": time_slot,
            "duration": get_duration(appointment_type)
        }
    return None