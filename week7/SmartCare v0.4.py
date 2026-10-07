# SmartCare v0.4
#Simple domain classes

class Patient:
    def __init__(self, name: str, contact_details: str = ""):
        if not name or not name.strip():
            raise ValueError("Patient name cannot be empty")
        self.name = name.strip()
        self.contact_details = contact_details

    def update_info(self, new_details: str):
        self.contact_details = new_details


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id or not name or not specialty:
            raise ValueError("Practitioner ID, name and specialty cannot be empty")
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty
        self._appointments = []

    def has_conflict(self, time: str) -> bool:
        for appt in self._appointments:
            if appt.time == time and appt.status == "active":
                return True
        return False

    def add_appointment(self, appointment):
        if self.has_conflict(appointment.time):
            raise ValueError("Practitioner already has an appointment at that time")
        self._appointments.append(appointment)

    def get_scheduled_appointments(self) -> list:
        return [a for a in self._appointments if a.status == "active"]

    def get_all_appointments(self) -> list:
        #returns a list including cancelled appointments
        return list(self._appointments)

class Appointment:
    def __init__(self, patient: Patient, practitioner: Practitioner, time: str):
        if not time or not time.strip():
            raise ValueError("Appointment time cannot be empty")
        self.patient = patient
        self.practitioner = practitioner
        self.time = time.strip()
        self._status = "active"
        practitioner.add_appointment(self)

    @property
    def status(self) -> str:
        return self._status

    def cancel(self):
        if self._status != "active":
            raise ValueError("Only an active appointment is able to be cancelled")
        self._status = "cancelled"

"""SmartCare testing
and lab activities"""

def expect_error(action, label):
    try:
        action()
        print("Fail:", label)
    except ValueError as e:
        print("PASS:", label, "->", e)

keeon = Patient("Keeon Dang", "0400 123 456")
will = Patient("Will Boulding")
doc = Practitioner("D1", "Dr. Heba Rawashdeh", "GP")

# normal output
appt = Appointment(keeon, doc, "2025-10-05 10:00")
print("Pass: Normal appointment is", appt.status)

#invalid inputs
expect_error(lambda: Patient(""), "blank patient name")
expect_error(lambda: Patient(None), "None patient name")
expect_error(lambda: Appointment(will, doc, ""), "blank time")
expect_error(lambda: Appointment(will, doc, None), "None time")

#double booking example
expect_error(lambda: Appointment(will, doc, "2025-10-05 10:00"), "double booking")
print("PASS" if len(doc.get_all_appointments()) == 1 else "Fail", ": only 1 stored")

#cancel, history and an illegal repeat
appt.cancel()
print("PASS" if appt.status == "cancelled" else "Fail", ": cancelled")
print("PASS" if len(doc.get_all_appointments()) == 1 else "Fail", ": kept in history")
print("PASS" if doc.get_scheduled_appointments() == [] else "Fail", ": no active left")
expect_error(appt.cancel, "cancel twice")
 
#slot is cancelled then rebooked
Appointment(will, doc, "2025-10-05 10:00")
print("Pass: rebook after cancel")
 
#status unable to be set directly
try:
    appt.status = "active"
    print("FAIL: status was changed directly")
except AttributeError:
    print("PASS: status cannot be set directly")
