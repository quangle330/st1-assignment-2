SmartCare v0.2 - Requirements Specification Template

# Problem and Scope

SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history.  
Management wants a small, maintainable patient, practitioner and appointment system.

In scope

- Register patients
- Register practitioners
- Patient search
- Create appointments
- Cancel Appointments
- Prevent conflicting appointments for one practitioner
- Cancelled appointments are retained in the system's history
- Preserve any relevant information and data regarding patients, practitioners and appointments between sessions

Out of scope

- Online payment
- Facial recognition
- Insurance processing
- AI treatment recommendation
- Larger features that are not supported by the client's brief

Provisional

- SMS reminders
- Performance targets
- Data-retention rules
- Staff roles and permissions
- Schedule view for practitioners

# 2\. Stakeholders

| Stakeholder                     | Need                                                                                                                           | Evidence                                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| Receptionist and other staff    | Need to be able to register the patients and locate their information later on. Able to create and cancel appointments.        | Brief states staff experience double bookings and have difficulty in accessing patient information.                   |
| Practitioner                    | A view of accurate information regarding the appointment and scheduling that does not conflict with other active appointments. | Practitioners are explicitly managed by the system, and the guidance includes prevention of confliction appointments. |
| Patient                         | Personal details are accurate and records of appointments are correct.                                                         | Required by the system to manage information and appointments                                                         |
| Clinic Manager                  | A system with reliable information about practitioners, patients and appointments.                                             | Client brief states management wants a small and maintainable system                                                  |
| System Administer or Maintainer | An easily maintainable and testable system with reliable data.                                                                 | Maintainability and testability are outlined in the guidance.                                                         |

# 3\. Functional Requirements

FR-01: The system allows patient registration by staff.

FR-02: The system allows patient searching by staff.

FR-03: The system allows practitioner registration by staff.

FR-04: The system allows appointment creation by staff.

FR-05: The system prevents conflicting appointments for one practitioner.

FR-06: The system allows staff to cancel appointments.

FR-07: The system retains the cancelled appointments in an appointment history.

FR-08: The system preserves relevant data from patients, practitioners and appointments.

FR-09: The system allows patient information to be updated by staff.

FR-10: The system allows existing appointments to be viewed by staff.

FR-11: The system allows a practitioner's schedule to be viewed by staff.

FR-12: The system allows the modification of appointments by staff.

# 4\. Non-Functional Requirements

NFR-01: Maintainability – The system will keep patient, practitioner and appointment business logic organised, so that a change does not require unrelated functions to be rewritten.

NFR-02: Testability – Core business logic will be testable without depending on a GUI.

NFR-03: Data integrity – The system will maintain consistent information of patients, practitioners and appointments during normal operations, including consistent appointment status.

NFR-04: Security – The system will restrict creation of data, editing and cancellation of appointments to authorised staff roles.

# 5\. User Stories

US-01: As a receptionist, I want to register a patient, so that appointments can be made and managed by the clinic for that patient.

US-02: As a receptionist, I want to search for a patient so that I can access the correct patient information in a timely manner.

US-03: As a receptionist, I want to create appointments for practitioners, so that patients may be scheduled for consultations.

US-04: As a receptionist, I want to update patient information, so that patient records are consistent and accurate over time.

# 6\. Acceptance Criteria

**AC-01: Successfully creating appointments  
GIVEN** registered practitioner and patient, and the practitioner bas no existing active appointments at the requested time.  
**WHEN** staff create an appointment request.  
**THEN** recorded as an active appointment.

**AC-02: Patient Searching**  
**GIVEN** one or more patients have been registered in the system.  
**WHEN** staff search within the system using a patient name or details.  
**THEN** the system returns patient records matching the criteria or notifies that no matches were found.

**AC-03: Retained cancellations in history**  
**GIVEN** active appointment currently exists.  
**WHEN** authorised staff cancels an active appointment.  
**THEN** appointment is marked as cancel and remains in the appointment history.

# 7\. Assumptions and Open Questions

1\. Staff members are responsible for registering patients, practitioners and the management of appointments.

2\. Data of patients, practitioners and appointments must be available after the system is closed and reopened.

3\. Cancelled appointments should remain visible in the appointment history and not deleted from the system.

4\. What information is required when registering the patient.

5\. Which staff roles are authorized to create, modify or cancel appointments?

6\. What specific data is preserved between sessions?

7\. What defines a conflicting appointment for a practitioner?

# 8\. AI Requirements Review Record

| AI Suggestion                                                             | Classification | Evidence Used                                                                                      | Explanation                                                                                            | AI Suggestion                                                             |
| ------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Define required patient registration information.                         | Accepted       | FR-01 allows patient registration but does not specify required data.                              | The requirement is ambiguous and difficult to test without defining what information must be recorded. | Define required patient registration information.                         |
| Define patient search criteria.                                           | Accepted       | FR-02 and AC-02 refer to searching by patient name or details, but "details" is not defined.       | Clarification improves consistency and testability.                                                    | Define patient search criteria.                                           |
| Define what constitutes a conflicting appointment.                        | Accepted       | FR-05 requires prevention of conflicting appointments but does not define a conflict.              | The requirement cannot be reliably implemented or tested without clarification.                        | Define what constitutes a conflicting appointment.                        |
| Clarify the meaning of "relevant data" in FR-08.                          | Accepted       | FR-08 requires preservation of "relevant data" without specifying what data.                       | The wording is subjective and not measurable.                                                          | Clarify the meaning of "relevant data" in FR-08.                          |
| Clarify whether practitioner schedule viewing is in scope or provisional. | Accepted       | FR-11 includes schedule viewing, while "Schedule view for practitioners" is listed as provisional. | There is an inconsistency between the functional requirements and scope.                               | Clarify whether practitioner schedule viewing is in scope or provisional. |