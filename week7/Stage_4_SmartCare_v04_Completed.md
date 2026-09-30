SmartCare v0.4 - Domain Implementation Workbook

Week 7 student resource

# 1\. UML-to-Code Trace

| UML element                              | Python element                                      | Implemented? | Notes                                           |
| ---------------------------------------- | --------------------------------------------------- | ------------ | ----------------------------------------------- |
| Patient Class                            | class Patient                                       | Yes          | Checked for blank/none                          |
| ---                                      | ---                                                 | ---          | ---                                             |
| Practitioner Class                       | class Practitioner                                  | Yes          | ID, name and specialty added                    |
| ---                                      | ---                                                 | ---          | ---                                             |
| Appointment Class                        | class Appointment                                   | Yes          | Registers with the practitioner                 |
| ---                                      | ---                                                 | ---          | ---                                             |
| Patient update_info()                    | patient.update_info(new_details)                    | Yes          | (FR-09)                                         |
| ---                                      | ---                                                 | ---          | ---                                             |
| Patient name, contact_details            | [self.name](http://self.name), self.contact_details | Yes          | Plain attributes                                |
| ---                                      | ---                                                 | ---          | ---                                             |
| Practitioner get_scheduled_appointment() | get_scheduled_appointments()                        | Yes          | Returns active ones (FR-11)                     |
| ---                                      | ---                                                 | ---          | ---                                             |
| Practitioner has_conflict(time)          | has_conflict(time)                                  | Yes          | Only conflicts with active appointments (FR-05) |
| ---                                      | ---                                                 | ---          | ---                                             |
| Practitioner - Appointment (0..\*)       | private \_appointments list                         | Yes          | add_appointment() and get_all_appointments      |
| ---                                      | ---                                                 | ---          | ---                                             |
| Appointment patient, practitioner, time  | self.patient, self.practitioner, self.time          | Yes          | Time stays as a str and blanks are rejected     |
| ---                                      | ---                                                 | ---          | ---                                             |
| Appointment status (active/cancelled)    | self.status + read-only status property             | Yes          | Plain strings active/cancelled                  |
| ---                                      | ---                                                 | ---          | ---                                             |
| Appointment cancel()                     | Appointment.cancel()                                | Yes          | Active -> cancelled and object is retained      |
| ---                                      | ---                                                 | ---          | ---                                             |
| Modify appointment (FR-12)               | \-                                                  | No           | Later stage                                     |
| ---                                      | ---                                                 | ---          | ---                                             |
| Saving data between sessions (FR-08)     | \-                                                  | No           | Later stage                                     |
| ---                                      | ---                                                 | ---          | ---                                             |

# 2\. Domain Invariants

| Class        | Invariant / rule                                              | How protected                                                    |
| ------------ | ------------------------------------------------------------- | ---------------------------------------------------------------- |
| Patient      | Name not blank when created                                   | Check in \__init_\_, raises a ValueError                         |
| ---          | ---                                                           | ---                                                              |
| Practitioner | ID, name and specialty are not blank                          | Check in \__init_\_, raises ValueError                           |
| ---          | ---                                                           | ---                                                              |
| Practitioner | No more than one active appointment at the same time          | add_appoint(0 checks with has_conflict and raises a ValueError   |
| ---          | ---                                                           | ---                                                              |
| Practitioner | Appointment list is only able to be changed by a Practitioner | Private \_appointments and get_all_appointments() returns a copy |
| ---          | ---                                                           | ---                                                              |
| Appointment  | Time is not blank                                             | Check in \__init_\_. Raises a ValueError                         |
| ---          | ---                                                           | ---                                                              |
| Appointment  | Status changes only active / cancelled                        | Private \_status, no setter and cancel() will raise a ValueError |
| ---          | ---                                                           | ---                                                              |
| Appointment  | Cancelled appointments are to be retained                     | cancel() only changes the status and nothing is being removed    |
| ---          | ---                                                           | ---                                                              |

# 3\. Composition / Inheritance Decisions

| Relationship                    | Decision                                | Rationale                                                                                   |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------- |
| Appointment - Patient           | Association                             | References a patient but is not a type of patient                                           |
| ---                             | ---                                     | ---                                                                                         |
| Appointment - Practitioner      | Association                             | References a practitioner but is not a type of, a practitioner also tracks its appointments |
| ---                             | ---                                     | ---                                                                                         |
| Practitioner - appointment list | Practitioner owns and protects the list | Matches CRC cards: Practitioner checks their own conflicts                                  |
| ---                             | ---                                     | ---                                                                                         |
| Subclasses (Doctor, nurse, etc) | Not used                                | Specialty satisfies this                                                                    |
| ---                             | ---                                     | ---                                                                                         |
| Clinic or manager class         | Not used                                | Not a confirmed requirement                                                                 |
| ---                             | ---                                     | ---                                                                                         |

# 4\. AI Pair-Programming Record

| AI contribution                                    | Conforms?   | Decision                | Reason                                                       | Verification                          |
| -------------------------------------------------- | ----------- | ----------------------- | ------------------------------------------------------------ | ------------------------------------- |
| Fields patient, practitioner, time and status      | Yes         | Accept                  | Matches the UML                                              | Normal-case test                      |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| Empty or None validation in constructor            | Yes         | Simplified and accepted | Blank-input rile                                             | Blank and None tests                  |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| Private fields, read-only status                   | Yes         | Accept                  | Protects status transition                                   | Appt.status raises an attribute error |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| Read-only properties                               | Yes         | Modified                | Simplified to plain attributes                               | Code review                           |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| AppointmentStatus enum                             | Partly      | Modified                | Kept UML's active and cancelled strings                      | Trace Table                           |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| Idempotent cancel()                                | No          | Modified                | A repeat cancel should be met with an error                  | cancel() used twice test              |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| RuntimeError branch                                | No          | Modified                | An unreachable branch and inconsistent with the ValueError's | Code review                           |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| TTPE_CHECKING imports patient/practitioner modules | No          | Reject                  | Invented its own file structure                              | Code reviewed against the project     |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| \__slots__                                         | Unnecessary | Rejected                | Not needed as it adds an extra complexity                    | Code review                           |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |
| No link to the practitioners list                  | Gap         | Personally added        | FR-05 would not be able to trigger                           | Double-booking test                   |
| ---                                                | ---         | ---                     | ---                                                          | ---                                   |

# 5\. Updated UML

Insert updated UML only if implementation revealed a justified design change. Explain every change.  

Updated UML in week 7 folder 

1. Practitioner gains an id and specialty
2. get_scheduled \_appointment() changed to get_scheduled_appointments()
3. Practitioner gains an add_appointment() and get_all_appointments(0 are new, and keeps cancelled appointments as history
4. Appointment keeps a private \_status and exposes a read-only
5. update_info takes new_details and doesn't return anything
