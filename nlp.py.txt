def extract_info(customer_input):
    text = customer_input.lower()
    appointment_type = None
    dentist = None
    time_slot = None

    for word in ["checkup", "cleaning", "root canal", "filling", "braces"]:
        if word in text:
            appointment_type = word

    for name in ["john", "jess", "arthur", "ali"]:
        if name in text:
            dentist = name.capitalize()

    for time in ["10am", "12pm", "2pm", "6pm"]:
        if time in text:
            time_slot = time

    return appointment_type, dentist, time_slot