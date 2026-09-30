Assignment 2-Case Study

Stage 4 Lab Activities

Implementing the SmartCare Domain Layer

DESIGN FIRST -> AI PAIR PROGRAMMING -> REVIEW -> VERIFY | 1hour

# A - Revisit Approved UML

- Patient - Contact and identifying details, supports the register, search and update requirements (FR-01, 02 and 09)
- Practitioner - Identifying details, checks own scheduled appointments for time conflicts (FR-03, 05 and 11)
- Appointment - Links a practitioner, patient and a time, with a status and cancelled objects are kept (FR-04, 06, 07, 10, 12)
- Relationships: Patient 1..\* Appointment, Practitioner 1..\* Appointment (association). No inheritance or manager classes
- AppointmentStatus (scheduled/cancelled) not in previous UML, treat them as the same state and mention the rename, stage 4 brief also asks for a practitioner identifier and unique patient identification is still open

# B - Implement Patient: AI OFF

Implement Patient with type hints and basic validation.

class Patient:  
def \__init_\_(self, name: str, contact_details: str = ""):  
if not name or not name.strip():  
raise ValueError("Patient name cannot be empty")  
[self.name](http://self.name) = name.strip()  
self.contact_details = contact_details

# C - Implement Practitioner: AI OFF

Implement Practitioner with identifier, name and specialty; no database logic.  
<br/>class Practitioner:  
def \__init_\_(self, practitioner_id: str, name: str, specialty: str):  
if not practitioner_id or not name or not specialty:  
raise ValueError("Practitioner ID, name and specialty cannot be empty")  
self.practitioner_id = practitioner_id  
[self.name](http://self.name) = name  
self.specialty = specialty  
self.\_appointments = \[\]

# D - Implement Appointment: AI ON

from \__future__import annotations  
<br/>from enum import Enum  
from typing import TYPE_CHECKING  
<br/>if TYPE_CHECKING:  
\# Type-only imports prevent runtime circular-import problems.  
\# Adjust these module names to match the SmartCare project structure.  
from patient import Patient  
from practitioner import Practitioner  
<br/><br/>class AppointmentStatus(str, Enum):

"""Valid lifecycle states for an appointment."""  
<br/>ACTIVE = "active"  
CANCELLED = "cancelled"  
<br/><br/>class Appointment:  
"""Connects one patient with one practitioner at a scheduled time."""  
\__slots__ = ("\_patient", "\_practitioner", "\_time", "\_status")  
<br/>def \__init_\_(  
self,  
patient: Patient,  
practitioner: Practitioner,  
time: str,  
) -> None:  
if patient is None:  
raise ValueError("An appointment requires a patient.")  
<br/>if practitioner is None:  
raise ValueError("An appointment requires a practitioner.")  
<br/>if not isinstance(time, str):  
raise TypeError("Appointment time must be a string.")

if not time.strip():  
raise ValueError("Appointment time cannot be empty.")  
<br/>self.\_patient = patient  
self.\_practitioner = practitioner  
self.\_time = time  
self.\_status = AppointmentStatus.ACTIVE  
<br/>@property  
def patient(self) -> Patient:  
return self.\_patient  
<br/>@property  
def practitioner(self) -> Practitioner:  
return self.\_practitioner  
<br/>@property  
def time(self) -> str:  
return self.\_time  
<br/>@property  
def status(self) -> AppointmentStatus:  
return self.\_status  
<br/>def cancel(self) -> None:  
"""Transition the appointment from active to cancelled.  
Cancellation is idempotent. Calling this method on an already  
cancelled appointment leaves the appointment unchanged.  
"""

if self.\_status is AppointmentStatus.CANCELLED:  
return  
<br/>if self.\_status is not AppointmentStatus.ACTIVE:  
raise RuntimeError(  
f"Cannot cancel an appointment with status "  
F"{self.\_status.value!r}."  
)  
<br/>self.\_status = AppointmentStatus.CANCELLED

# E - Review Generated Code

Check model consistency, unsupported features, public state mutation, unnecessary inheritance, invented dependencies and error handling.

| Check                   | Finding                                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model Consistency       | Uses patient, practitioner, time(str) and status(active/cancelled) as shown in the UML and cancel(). Enum values are the active and cancelled values from the UML                                                                                                                                                                                    |
| ---                     | ---                                                                                                                                                                                                                                                                                                                                                  |
| Unsupported features    | No features added, no rescheduling, notes or reminders                                                                                                                                                                                                                                                                                               |
| ---                     | ---                                                                                                                                                                                                                                                                                                                                                  |
| Public state mutation   | All fields are private with read-only properties and status is changed through cancel()                                                                                                                                                                                                                                                              |
| ---                     | ---                                                                                                                                                                                                                                                                                                                                                  |
| Unnecessary inheritance | No unnecessary inheritance and only inherits from str and enum for the status type. Appointment is a plain class                                                                                                                                                                                                                                     |
| ---                     | ---                                                                                                                                                                                                                                                                                                                                                  |
| Invented dependencies   | A few minor dependencies. Imports patient and practitioner from modules which assume a file structure. \__slots__ is also unnecessary here.                                                                                                                                                                                                          |
| ---                     | ---                                                                                                                                                                                                                                                                                                                                                  |
| Error handling          | Rejects any patient or practitioner None, a non-string time TypeError and an empty time ValueError. Some problems found are that when canceling an already canceled appointment does not do anything. The RuntimeError branch never runs because there are only two statuses and is also inconsistent with the ValueError being used somewhere else. |
| ---                     | ---                                                                                                                                                                                                                                                                                                                                                  |

# F - Manual Behaviour Checks

| Test                        | Input                                         | Expected                               | Result |
| --------------------------- | --------------------------------------------- | -------------------------------------- | ------ |
| Valid objects               | Keeon, Dr. Heba Rawashdeh, "2025-10-05 10:00" | "Active" appointment status            | Pass   |
| ---                         | ---                                           | ---                                    | ---    |
| Blank patient name          | "", None                                      | ValueError                             | Pass   |
| ---                         | ---                                           | ---                                    | ---    |
| Double booking              | Same practitioner, same time                  | ValueError, 1 stored                   | Pass   |
| ---                         | ---                                           | ---                                    | ---    |
| Cancel active appointment   | cancel()                                      | Status "cancelled", remains in history | Pass   |
| ---                         | ---                                           | ---                                    | ---    |
| Illegal repeated transition | cancel() used twice                           | ValueError                             | Pass   |
| ---                         | ---                                           | ---                                    | ---    |
| Rebooking after cancel      | Same slot after cancellation                  | Allowed                                | Pass   |
| ---                         | ---                                           | ---                                    | ---    |
| Direct change of status     | appt.status = "active"                        | AttributeError                         | Pass   |
| ---                         | ---                                           | ---                                    | ---    |

# G - Refactor

Simplified copilots appointment, kept protections the labs needs such as blank value, kept conflict checking inside practitioner class.

# H - AI Engineering Log

| Item            | Log                                                                                                                                                                                                                                                                                                                                           |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompt          | Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML. |
| ---             | ---                                                                                                                                                                                                                                                                                                                                           |
| AI contribution | Copilot was able to generate an appointmentStatus enum and an Appointment class with the required validation, private states, read-onlys and idempotent cancel()                                                                                                                                                                              |
| ---             | ---                                                                                                                                                                                                                                                                                                                                           |
| Modified        | The enum was replaced with the plain strings from the UML, a repeat cancel() now returns a ValueError, the RuntimeError branch was replaced.                                                                                                                                                                                                  |
| ---             | ---                                                                                                                                                                                                                                                                                                                                           |
| Rejected        | Type_checking imports and \__slots__ were rejected                                                                                                                                                                                                                                                                                            |
| ---             | ---                                                                                                                                                                                                                                                                                                                                           |
| Verification    | Section F and comparison to the UML and CRC                                                                                                                                                                                                                                                                                                   |
| ---             | ---                                                                                                                                                                                                                                                                                                                                           |

# Reflection

Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?

The appointment class copilot generated actually did match the UML quite well, although I did still modify it. A significant problem was that when cancel() was used twice, it would ignore the second cancellation and then an illegal transition would be unnoticed, instead I made it raise an error. I then replaced the enum with the plain strings from the UML, simplified the property getters and rejected the type checking imports and \__slots__ which had assumed there was a file layout we did not have.  
<br/>The approved design was able to constrain the AI in a good way. Because the prompt listed what and what not to add. The output was small and easy to compare, with no added manager classes or inheritance.Testing showed that the code was not the same as the correct code where blank names, missing times etc needed specific checks.