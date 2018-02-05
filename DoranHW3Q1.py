# charges: $1000 for ED visits, $2000 for admissions


class Patient:
    # base class
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes")


class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost = 1000  # each patient has the same cost, does not need to be defined in initialization

    def discharge(self):
        print(self.name, "Emergency Patient")


class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost = 2000

    def discharge(self):
        print(self.name, "Hospitalized Patient")


class Hospital:
    def __init__(self):
        self.patients = []
        self.cost = 0

    def admit(self, patients):
        self.patients.append(patients)

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost += patients.ecost

    def get_total_cost(self):
        return self.cost


# patients
P1 = HospitalizedPatient("P1")
P2 = HospitalizedPatient("P2")
P3 = EmergencyPatient("P3")
P4 = EmergencyPatient("P4")
P5 = EmergencyPatient("P5")

H1 = Hospital()

H1.admit(P1)
H1.admit(P2)
H1.admit(P3)
H1.admit(P4)
H1.admit(P5)

H1.discharge_all()

print(H1.get_total_cost())
