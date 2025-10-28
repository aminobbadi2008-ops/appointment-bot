from flask import Flask, request, jsonify
from nlp import extract_info
from scheduler import schedule_appointment
from notifier import send_notification

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    customer_input = request.form.get("SpeechResult", "") or request.form.get("Body", "")
    
    appointment_type, dentist, time_slot = extract_info(customer_input)
    appointment = schedule_appointment(appointment_type, dentist, time_slot)
    
    if appointment:
        send_notification(appointment, "sms")
        response = f"Your appointment with {appointment['dentist']} at {appointment['time_slot']} has been scheduled."
    else:
        response = "Sorry, that slot is not available."
    
    return jsonify({"response": response})

@app.route("/")
def home():
    return "Dental Appointment Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)