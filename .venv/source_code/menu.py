from source_code.appointment import Appointment
from source_code.patients import Patients
from source_code.registry import load_json, save_json
import uuid 

def menu():
    while True:
        print('        WELCOME TO DENTIST OFFICE       ')
        print('        Dentist Reception Menu          ')
        print('1. Add patient')
        print('2. View current patients')
        print('3. Book Appointment')
        print('4. View Schedule')
        print('5. Cancel Appointment')
        print('6. Exit')

        choice= input ('Please choose your option: ')

        if choice== '1':
            add_patient()
        elif choice== '2':
            list_patient()
        elif choice== '3':
            book_appointment()
        elif choice== '4':
            view_schedule()
        elif choice== '5':
            cancel_appointment()
        elif choice== '6':
            print('Thank you and Goodbye.')
            break
        else:
            print("Invalid choice. Kindly choose from following given choices between 1 to 6")

def add_patient():
    pat_id= str(uuid.uuid4())[:8]
    first_n = input("Enter patient First name: ")
    last_n = input("Enter patient Last name: ")
    age = int(input("Patient Age: "))
    gender = input("Patient Gender (M/F): ")
    birthday= str(input("Patient Birthday (DD.MM.YYYY) : "))
    phone = input("Phone number: ")
    patient= Patients(pat_id, first_n, last_n, age, gender, birthday, phone)
    patients= load_json("patients.json")
    patients.append(patient.to_dict())
    save_json("patients.json", patients)
    print("Patient added successfully.") 

def list_patient():
    patients= load_json("patients.json")
    for p in patients:
        print(f"Patient ID={p['id']} | First name= {p['first_name']} Last name= {p['last_name']} | Age={p['age']} | Gender={p['gender']}")

def book_appointment():
    app_id= str(uuid.uuid4())[:8]
    pat_id = input("Enter patient ID: ").strip()
    patients= load_json("patients.json")
    patient_exist= False
    for p in patients:
        if p['id'].strip()==pat_id:
            patient_exist= True
            break
    if not patient_exist:
        print("Patient record not found, Kindly register the patient first")
        return
    date = input("Enter date (DD.MM.YYYY): ")
    time = input("Enter time (HH:MM): ")
    appointments = load_json("appointments.json")

    for appt in appointments:
        if appt['date'] == date and appt['time'] == time:
            print("Time slot already booked!")
            return
    appointment = Appointment(app_id, pat_id, date, time)
    appointments.append(appointment.to_dict())
    save_json("appointments.json", appointments)
    print("Appointment booked successfully.")


def view_schedule():
    date = input("Enter date (DD.MM.YYYY): ")
    appointments = load_json("appointments.json")
    for a in appointments:
        if a['date'] == date:
            print(f"{a['time']} | Patient ID: {a['patient_id']} | Status: {a['status']}")

def cancel_appointment():
    app_id = input("Enter appointment ID to cancel: ")
    appointments = load_json("appointments.json")
    for a in appointments:
        if a['id'] == app_id:
            a['status'] = 'cancelled'
            save_json("appointments.json", appointments)
            print("Appointment cancelled successfully.")
            return
    print("Appointment not found.")
