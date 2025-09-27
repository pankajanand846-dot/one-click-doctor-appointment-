import streamlit as st
from email.message import EmailMessage
import smtplib

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="Doctor Appointment", page_icon="🩺", layout="wide")

# -----------------------
# Email Setup (CHANGE THESE)
# -----------------------
EMAIL_USER = "dassachidananda06@gmail.com"       # <-- your Gmail
EMAIL_PASS = "ksyx qmrz egcx pmjy"     # <-- your 16-char App Password
DOCTOR_EMAIL = "nishantchoudhary1628@gmail.com"   # <-- friend's Gmail

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

# -----------------------
# Session State
# -----------------------
if "patient_submitted" not in st.session_state:
    st.session_state.patient_submitted = False
if "appointment_done" not in st.session_state:
    st.session_state.appointment_done = False
if "appointment_details" not in st.session_state:
    st.session_state.appointment_details = None

# -----------------------
# Header
# -----------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #007BFF;'>🩺 Doctor Appointment System</h1>
    <h4 style='text-align: center; color: gray;'>Book your doctor instantly — no waiting, no confusion!</h4>
    <br>
    """,
    unsafe_allow_html=True,
)

# -----------------------
# Patient Form
# -----------------------
if not st.session_state.patient_submitted:
    st.subheader("👤 Patient Details")
    with st.form("patient_form"):
        patient_name = st.text_input("Full Name")
        patient_contact = st.text_input("Contact Number")
        patient_symptoms = st.text_area("Describe Your Symptoms")
        submitted = st.form_submit_button("➡️ Continue")

    if submitted:
        if patient_name and patient_contact and patient_symptoms:
            st.session_state.patient_submitted = True
            st.session_state.patient_name = patient_name
            st.session_state.patient_contact = patient_contact
            st.session_state.patient_symptoms = patient_symptoms
        else:
            st.error("⚠️ Please fill all fields before continuing!")

# -----------------------
# Doctor Selection
# -----------------------
elif not st.session_state.appointment_done:
    st.subheader("👨‍⚕️ Available Doctors")
    st.caption("Choose your doctor and preferred time slot")

    doctors = [
        {"name": "Dr. Sharma", "specialty": "Cardiologist", "rating": "⭐⭐⭐⭐⭐", "slots": ["10:00 AM", "12:00 PM", "3:00 PM"]},
        {"name": "Dr. Das", "specialty": "Neurologist", "rating": "⭐⭐⭐⭐", "slots": ["11:00 AM", "1:00 PM", "4:00 PM"]},
        {"name": "Dr. Verma", "specialty": "Orthopedic", "rating": "⭐⭐⭐⭐⭐", "slots": ["9:00 AM", "2:00 PM", "5:00 PM"]},
    ]

    for doc in doctors:
        with st.container():
            st.markdown(f"### {doc['name']} ({doc['specialty']})")
            st.markdown(f"⭐ Rating: {doc['rating']}")
            slot = st.selectbox(f"Select Slot for {doc['name']}", doc["slots"], key=doc["name"])

            if st.button(f"📅 Confirm with {doc['name']}", key=f"book_{doc['name']}"):
                try:
                    # Email content
                    subject = f"New Appointment Request: {doc['name']}"
                    body = f"""
                    Patient Name: {st.session_state.patient_name}
                    Contact: {st.session_state.patient_contact}
                    Symptoms: {st.session_state.patient_symptoms}
                    Doctor: {doc['name']} ({doc['specialty']})
                    Slot: {slot}
                    """

                    # Send email
                    send_email(DOCTOR_EMAIL, subject, body)

                    # Save appointment details
                    st.session_state.appointment_done = True
                    st.session_state.appointment_details = {
                        "doctor": doc['name'],
                        "specialty": doc['specialty'],
                        "slot": slot
                    }
                    st.success("✅ Appointment request sent successfully!")
                    st.balloons()
                    st.rerun()  # ✅ Fixed

                except Exception as e:
                    st.error(f"⚠️ Error while booking appointment: {e}")

# -----------------------
# Confirmation Screen
# -----------------------
elif st.session_state.appointment_done:
    details = st.session_state.appointment_details
    st.success(f"✅ Appointment Confirmed with {details['doctor']} ({details['specialty']}) at {details['slot']}")
    st.balloons()

    st.subheader("🏆 Our Achievements")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("👨‍⚕️ Doctors", "5000+")
    with col2:
        st.metric("📅 Appointments", "100K+")
    with col3:
        st.metric("⏰ Availability", "24/7")

    if st.button("🔄 Book Another Appointment"):
        st.session_state.patient_submitted = False
        st.session_state.appointment_done = False
        st.rerun()  # ✅ Fixed

# -----------------------
# Footer
# -----------------------
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray;'>
    Made with ❤️ using Streamlit | Hackathon Project
    </p>
    """,
    unsafe_allow_html=True,
)








