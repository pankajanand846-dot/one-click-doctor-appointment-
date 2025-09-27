# utils.py
import json

# Suggest specialist based on symptoms
def suggest_specialist(symptoms):
    symptoms = symptoms.lower()
    if "fever" in symptoms or "cough" in symptoms:
        return "General Physician"
    if "tooth" in symptoms:
        return "Dentist"
    if "skin" in symptoms or "rash" in symptoms:
        return "Dermatologist"
    if "stomach" in symptoms:
        return "Gastroenterologist"
    return "General Physician"

# Load doctors and their available slots
def load_doctors():
    return {
        "General Physician": [
            {"name": "Dr. Sharma", "slots": ["10AM", "11AM", "12PM"]},
            {"name": "Dr. Das", "slots": ["1PM", "2PM", "3PM"]},
            {"name": "Dr. Mehta", "slots": ["4PM", "5PM"]}
        ],
        "Dentist": [
            {"name": "Dr. Rao", "slots": ["1PM", "2PM", "3PM"]},
            {"name": "Dr. Iyer", "slots": ["4PM", "5PM", "6PM"]}
        ],
        "Dermatologist": [
            {"name": "Dr. Kapoor", "slots": ["3PM", "4PM", "5PM"]},
            {"name": "Dr. Verma", "slots": ["6PM", "7PM"]}
        ],
        "Gastroenterologist": [
            {"name": "Dr. Singh", "slots": ["5PM", "6PM", "7PM"]},
            {"name": "Dr. Gupta", "slots": ["8AM", "9AM", "10AM"]}
        ]
    }

# Save a booking to appointments.json
def save_booking(booking):
    try:
        with open("appointments.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(booking)
    with open("appointments.json", "w") as f:
        json.dump(data, f, indent=4)

