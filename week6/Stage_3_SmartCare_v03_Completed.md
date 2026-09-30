SmartCare v0.3 - Domain Model Workbook

Week 6 student resource

# Requirement-to-Concept Trace

| Requirement                                                                              | Concept                          | State/behaviour                                                                                                                                                  | Decision  |
| ---------------------------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| FR-01: The system allows patient registration by staff.                                  | Patient                          | At registration, create a Patient object and validate the name is not empty before creation                                                                      | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-02: The system allows patient searching by staff.                                     | Patient                          | At search, compare the input against stored names/details of patients, return a match or "not found".                                                            | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-03: The system allows practitioner registration by staff.                             | Practitioner                     | At registration create a Practitioner object and validate name is not empty before creation                                                                      | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-04: The system allows appointment creation by staff.                                  | Appointment                      | At creation, build an appointment linking together a patient, practitioner and time, "active is the default status.                                              | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-05: The system prevents conflicting appointments for one practitioner.                | Appointment/ Practitioner        | At creation before FR-04 is completed, check practitioner's existing active appointments for the matching time. If found, discontinue creation and return error. | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-06: The system allows staff to cancel appointments.                                   | Appointment                      | At cancellation, change the existing appointment's status from "active" to "cancelled". The object is stored rather than deleted.                                | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-07: The system retains the cancelled appointments in an appointment history.          | Appointment                      | After cancellation, the cancelled object remains in the appointments list under a "cancelled status" and remains viewable.                                       | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-08: The system preserves relevant data from patients, practitioners and appointments. | Patient/Practitioner/Appointment | At the start and end of the program, read and write to persistent storage so data is preserved between use. Not implemented yet.                                 | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-09: The system allows patient information to be updated by staff.                     | Patient                          | At edit, locate an existing Patient via FR-02 search, then overwrite one or more of its attributes.                                                              | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-10: The system allows existing appointments to be viewed by staff.                    | Appointment                      | At display, loop through all stored Appointments and print/return.                                                                                               | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-11: The system allows a practitioner's schedule to be viewed by staff.                | Practitioner/Appointment         | At display, filter the appointment list to those linked to a matched practitioner.                                                                               | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |
| FR-12: The system allows the modification of appointments by staff.                      | Appointment                      | At edit time, change an existing Appointment's practitioner or time field. This will re-run FR-05 to check for conflicts before change is accepted.              | Confirmed |
| ---                                                                                      | ---                              | ---                                                                                                                                                              | ---       |

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

## Optional class

| Responsibilities | Collaborators |
| ---------------- | ------------- |
|                  |               |
| ---              | ---           |
|                  |               |
| ---              | ---           |

# UML Class Diagram

Inside week 6 folder.

# Design Rationale

The chosen classes, Patient, Practitioner and Appointment were selected because they are the three mentioned concepts that have a distinct data and behaviour directly tied to the confirmed requirements, they also appear as nouns performing actions across such requirements. Attributes and checks (name, contact info, status, conflict) were kept on the classes that own the relevant date instead of separating into manager classes.

# AI Design Review Record

| AI suggestion                                               | Evidence      | Decision | Reason                                                                                                                                                                              | Model change                             |
| ----------------------------------------------------------- | ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Add a status field to appointment (active/cancelled)        | FR-06 & FR-07 | Accepted | Required, cancellation must be able to change status without deletion of the record, so the appointment class needs a status attribute to support this.                             | Appointment class gains status attribute |
| ---                                                         | ---           | ---      | ---                                                                                                                                                                                 | ---                                      |
| Add ScheduleEngine for conflict/schedule logic              | FR-05, FR-11  | Modified | Evidence is present for the behaviour, but not for a separate class. The practitioner and appointment class already do this together, if logic becomes complex it can be revisited. | None at the moment                       |
| ---                                                         | ---           | ---      | ---                                                                                                                                                                                 | ---                                      |
| Add NotificationManager for reminders                       | None          | Rejected | SMS reminders are still classed as provisional and not confirmed by the client                                                                                                      | None                                     |
| ---                                                         | ---           | ---      | ---                                                                                                                                                                                 | ---                                      |
| Add ClinicController                                        | None          | Rejected | No functional requirement gives a clinic level coordination responsibility.                                                                                                         | None                                     |
| ---                                                         | ---           | ---      | ---                                                                                                                                                                                 | ---                                      |
| Make Appointment inherit from Patient                       | None          | Rejected | Appointment is not a type of patient, but an association.                                                                                                                           | None                                     |
| ---                                                         | ---           | ---      | ---                                                                                                                                                                                 | ---                                      |
| Add PatientManager, PractitionerManager, AppointmentManager | None          | Rejected | No functional requirement separates manager classes, also risk duplicating any responsibility that the existing classes hold.                                                       | None                                     |
| ---                                                         | ---           | ---      | ---                                                                                                                                                                                 | ---                                      |