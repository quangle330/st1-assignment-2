Assignment 2 Case Study

Stage 2 Tutorial From Problems to Requirements

Week 5 | 60 minutes

# Learning goals

- Analyse stakeholders.
- Distinguish functional and non-functional requirements.
- Recognise ambiguity and unsupported requirements.
- Define scope.
- Develop user stories and acceptance criteria.
- Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

| Stakeholder                     | Need                                                                                                                           | Potential conflict                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Receptionist and other staff    | Need to be able to register the patients and locate their information later on. Able to create and cancel appointments.        | Convenience may cause a dispute with validation rules that prevent any double bookings or invalid ones.           |
| Practitioner                    | A view of accurate information regarding the appointment and scheduling that does not conflict with other active appointments. | Availability might conflict with requests to create appointments at certain times.                                |
| Patient                         | Personal details are accurate and records of appointments are correct.                                                         | Conflicts with clinic rules regarding identification, cancellations and data handling.                            |
| Clinic Manager                  | A system with reliable information about practitioners, patients and appointments.                                             | Users may require additional features whereas the upper management requests a tight scope and maintenance.        |
| System Administer or Maintainer | An easily maintainable and testable system with reliable data.                                                                 | Technical quality might require extra structures or validations where users may find inefficient and inconvenient |

# Activity 2 - Functional or non-functional?

| **Classification** | **Requirement**                                                  |
| ------------------ | ---------------------------------------------------------------- |
| **Functional**     | The system shall allow staff to cancel an appointment.           |
| **Non-Functional** | The system should remain responsive to the course-scale dataset. |
| **Functional**     | The system shall retain cancelled appointments.                  |
| **Non-Functional** | Core business logic should be independently testable.            |
| **Functional**     | The system shall search for a patient by ID.                     |

# Activity 3 - Repair Ambiguous Requirements

The system should be easy to use.

Problem: Easy to use may be different for everyone and unverifiable directly Clarification question: What core tasks must staff be completing and what usability criteria can be used to decide if the system has ease of use?

Patient search should be fast.

Problem: Fast is a very general term and unquantifiable, can't be verified later. Clarification question: What is an acceptable response time to search for patient information (2-5 seconds etc.). Is this for a filtered subset or the full patient database?

The system should securely manage data.

Problem: Securely is too vague and there is no specification of what threats need to be protected against and what needs to be protected.  
Clarification question: Who is allowed access to patient and appointment information and data, what security controls are required here?

Appointments should normally be easy to cancel.

Problem: This requirement is very ambiguous and doesn't underline who is allowed to cancel an appointment and if the record of the appointment should be kept or destroyed.  
Clarification question: What users can cancel an appointment, what conditions allow a cancel, and should the appointment remain in the history of the system?

# Activity 4 - AI Requirements Audit

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

| AI suggestion                             | Classification                  | Evidence / reason                                                                                                                        |
| ----------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Patients receive SMS reminders.           | Assumption requiring validation | Not a stated requirement, need to confirm with the client first                                                                          |
| Facial recognition login.                 | Unsupported / Out of scope      | No evidence of support for facial recognition, it must be explicitly introduced.                                                         |
| Receptionists create appointments.        | Assumption requiring validation | Staff is currently the term used in the brief, receptionists are relevant here, but exact permissions must be confirmed with the client. |
| Online payment.                           | Unsupported / Out of scope      | Payment has not been mentioned in the current brief.                                                                                     |
| Practitioners view schedules.             | Assumption requiring validation | Might be useful, however the brief does not confirm a feature where the practitioner views their own schedule.                           |
| AI recommends treatments.                 | Unsupported / Out of scope      | AI treatment is not part of any scope in this brief.                                                                                     |
| Cancelled appointments remain in history. | Confirmed                       | Retaining cancelled appointments has been a stated guidance for the system.                                                              |

# Exit question

Why is 'AI suggested it' not sufficient evidence for a requirement?

The suggestions from AI are features based on other similar systems, but not from the client of the SmartCare system itself. Stakeholder evidence is needed or assumptions must be confirmed before it can be a requirement for the system.