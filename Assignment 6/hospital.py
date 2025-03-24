class MedicalRecord:
    def __init__(self, number, diagnosis):
        self.number = number
        self.diagnosis = diagnosis

class Patient:
    def __init__(self, name, age, medical_record):
        self.name = name
        self.age = age
        self.medical_record = medical_record

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []

    def assign_patient(self, patient):
        self.patients.append(patient)

class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

class Hospital:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.patients = []
        self.doctors = []
        self.medical_records = []

    def add_department(self, department):
        self.departments.append(department)

    def add_patient(self, patient):
        self.patients.append(patient)

    def discharge_patient(self, patient):
        self.patients.remove(patient)

    def get_patients(self):
        return self.patients

    def add_medical_record(self, medical_record):
        self.medical_records.append(medical_record)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_doctors(self):
        return self.doctors

    def assign_doctor(self, doctor, patient):
        doctor.assign_patient(patient)