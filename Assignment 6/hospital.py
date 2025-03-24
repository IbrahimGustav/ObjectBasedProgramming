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

medical_record1 = MedicalRecord(number=1, diagnosis="Flu")
medical_record2 = MedicalRecord(number=2, diagnosis="Cold")

patient1 = Patient(name="John Doe", age=30, medical_record=medical_record1)
patient2 = Patient(name="Jane Smith", age=25, medical_record=medical_record2)

doctor1 = Doctor(name="Dr. House", specialization="Diagnostics")
doctor2 = Doctor(name="Dr. Grey", specialization="Surgery")

department1 = Department(name="Emergency")
department2 = Department(name="Cardiology")

hospital = Hospital(name="City Hospital")

hospital.add_department(department1)
hospital.add_department(department2)

department1.add_doctor(doctor1)
department2.add_doctor(doctor2)

hospital.add_patient(patient1)
hospital.add_patient(patient2)

hospital.assign_doctor(doctor1, patient1)
hospital.assign_doctor(doctor2, patient2)

print(f"Hospital: {hospital.name}")
print("Departments:")
for dept in hospital.departments:
    print(f"  - {dept.name}")
print("Doctors:")
for doc in hospital.doctors:
    print(f"  - {doc.name}, Specialization: {doc.specialization}")
print("Patients:")
for pat in hospital.patients:
    print(f"  - {pat.name}, Age: {pat.age}, Diagnosis: {pat.medical_record.diagnosis}")