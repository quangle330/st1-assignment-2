Assignment 2-Case Study

Stage 3 Tutorial Activities

From Requirements to Domain Models

Week 6 | 60 minutes

# Candidate Concepts

| Candidate    | Class? | Reason                                                                                                                  |
| ------------ | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| Patient      | Yes    | Core domain entity with its own identity and data (name & contact details) and within FR-01, 02 and 09                  |
| ---          | ---    | ---                                                                                                                     |
| Practitioner | Yes    | A core domain entity with its own identity and data, within FR-03 and 11                                                |
| ---          | ---    | ---                                                                                                                     |
| Appointment  | Yes    | The central entity linking the Patient and Practitioner classes in a specified time. Needed from FR-04 to 08, 10 and 12 |
| ---          | ---    | ---                                                                                                                     |
| Name         | No     | Attribute of the Patient and Practitioner classes                                                                       |
| ---          | ---    | ---                                                                                                                     |
| Clinic       | No     | Clinic has no state or behaviour according to current confirmed requirements                                            |
| ---          | ---    | ---                                                                                                                     |
| Database     | No     | FR-08 is not to be treated as a domain class                                                                            |
| ---          | ---    | ---                                                                                                                     |
| Cancellation | No     | This is a state of the Appointment class, not a separate class                                                          |
| ---          | ---    | ---                                                                                                                     |
| Status       | No     | Attribute of the Appointment class                                                                                      |
| ---          | ---    | ---                                                                                                                     |

# CRC Cards

## Patient

| Responsibilities                                            | Collaborators |
| ----------------------------------------------------------- | ------------- |
| Provide personal details when linked to an appointment      | Appointment   |
| ---                                                         | ---           |
| Store and maintain personal identifying and contact details | N/A           |
| ---                                                         | ---           |

## Practitioner

| Responsibilities                                                              | Collaborators |
| ----------------------------------------------------------------------------- | ------------- |
| Check own active active appointments for conflicts before accepting a new one | Appointment   |
| ---                                                                           | ---           |
| Store own information for identification                                      | N/A           |
| ---                                                                           | ---           |

## Appointment

| Responsibilities                                            | Collaborators         |
| ----------------------------------------------------------- | --------------------- |
| Link exactly one Patient and one Practitioner at a set time | Patient, Practitioner |
| ---                                                         | ---                   |
| Track and change its own state (Active -> cancelled)        | N/A                   |
| ---                                                         | ---                   |

# Relationship Reasoning

Patient to Appointment: A one to many relationship as patients are able to have multiple appointments over a time but each appointment is belonging to exactly one patient.

Practitioner to Appointment: One to many relationship is evident, even though a practitioner may have multiple appointments, they never have more than one active appointment at one time.

Should Appointment inherit from Patient? No, appointments aren't a kind of patient so inheritance would not work here. The relationship is simply an association as appointments reference a patient.

Does Clinic need to own every object? A clinic class would be out of the scope, as there is no requirement for a class to own all data.

# AI Model Critique

Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

| **AI proposals**                                        | **Reason**                                                                                                                                                                          |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PatientManager, PractitionerManager, AppointmentManager | No functional requirement separates manager classes, also risk duplicating any responsibility that the existing classes hold.                                                       |
| ---                                                     | ---                                                                                                                                                                                 |
| ClinicController                                        | No functional requirement gives a clinic level coordination responsibility.                                                                                                         |
| ---                                                     | ---                                                                                                                                                                                 |
| NotificationManager                                     | SMS reminders are still classed as provisional and not confirmed by the client                                                                                                      |
| ---                                                     | ---                                                                                                                                                                                 |
| ScheduleEngine                                          | Evidence is present for the behaviour, but not for a separate class. The practitioner and appointment class already do this together, if logic becomes complex it can be revisited. |
| ---                                                     | ---                                                                                                                                                                                 |