Assignment 2 – Case Study Lab

Stage 2 Lab Activities

SmartCare Requirements Engineering

AI OFF -> AI ON -> VERIFY | 1 hour

# Learning objectives

- Analyse the SmartCare client brief.
- Identify stakeholders and scope.
- Write functional and non-functional requirements.
- Develop user stories and Given-When-Then acceptance criteria.
- Use AI to critique requirements without allowing it to invent stakeholder needs.
- Produce SmartCare Requirements Specification v1.0.

# Part A - Client Brief: AI OFF

SmartCare uses spreadsheets and paper records.  
<br/>Staff report duplicate bookings,  
difficulty finding patient information,  
inconsistent appointment status  
and limited appointment history.

Management wants a small, maintainable patient, practitioner and appointment system.

# Part B - Stakeholders and Scope: AI OFF

| Stakeholder                     | Need                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Receptionist and other staff    | Need to be able to register the patients and locate their information later on. Able to create and cancel appointments.        |
| Practitioner                    | A view of accurate information regarding the appointment and scheduling that does not conflict with other active appointments. |
| Patient                         | Personal details are accurate and records of appointments are correct.                                                         |
| Clinic Manager                  | A system with reliable information about practitioners, patients and appointments.                                             |
| System Administer or Maintainer | An easily maintainable and testable system with reliable data.                                                                 |

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

# Part C - Functional Requirements: AI OFF

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

# Part D - Non-Functional Requirements: AI OFF

NFR-01: Maintainability – The system will keep patient, practitioner and appointment business logic organised, so that a change does not require unrelated functions to be rewritten.

NFR-02: Testability – Core business logic will be testable without depending on a GUI.

NFR-03: Data integrity – The system will maintain consistent information of patients, practitioners and appointments during normal operations, including consistent appointment status.

NFR-04: Security – The system will restrict creation of data, editing and cancellation of appointments to authorised staff roles.

# Part E - User Stories and Acceptance Criteria: AI OFF

US-01: As a receptionist, I want to register a patient, so that appointments can be made and managed by the clinic for that patient.

US-02: As a receptionist, I want to search for a patient so that I am able to access the correct patient information in a timely manner.

US-03: As a receptionist, I want to create appointments for practitioners, so that patients may be scheduled for consultations.

US-04: As a receptionist, I want to update patient information, so that patient records are consistent and accurate over time.

Acceptance Criteria

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

# Part F - AI Requirements Review: AI ON

Prompt: Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

AI provided with the required scope and the prompt to provide suggestions for the SmartCare Case study.  
Unsupported suggestions must not automatically become requirements.

# Part G - VERIFY the AI Review

| AI Suggestion                                                             | Classification | Evidence Used                                                                                                               | Explanation                                                                                            |
| ------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Define required patient registration information.                         | Accepted       | FR-01 allows patient registration but does not specify required data.                                                       | The requirement is ambiguous and difficult to test without defining what information must be recorded. |
| Define patient search criteria.                                           | Accepted       | FR-02 and AC-02 refer to searching by patient name or details, but "details" is not defined.                                | Clarification improves consistency and testability.                                                    |
| Define what constitutes a conflicting appointment.                        | Accepted       | FR-05 requires prevention of conflicting appointments but does not define a conflict.                                       | The requirement cannot be reliably implemented or tested without clarification.                        |
| Clarify the meaning of "relevant data" in FR-08.                          | Accepted       | FR-08 requires preservation of "relevant data" without specifying what data.                                                | The wording is subjective and not measurable.                                                          |
| Clarify whether practitioner schedule viewing is in scope or provisional. | Accepted       | FR-11 includes schedule viewing, while "Schedule view for practitioners" is listed as provisional.                          | There is an inconsistency between the functional requirements and scope.                               |
| Clarify authorised staff roles and permissions.                           | Modified       | NFR-04 requires authorised staff roles, while roles and permissions are listed as provisional.                              | Role-based access is supported, but specific roles require stakeholder confirmation.                   |
| Define valid appointment statuses.                                        | Accepted       | The brief mentions inconsistent appointment status, while the requirements reference active and cancelled appointments only | A clear set of statuses would improve consistency and data integrity.                                  |
| Should duplicate patient records be prevented?                            | Unverified     | The brief mentions duplicate bookings, not duplicate patient records.                                                       | Additional stakeholder validation is needed because this issue is not explicitly stated.               |
| Add online payment.                                                       | Rejected       | Payment is not part of the client's brief.                                                                                  | Compared against the defined in scope list.                                                            |

# Part H - Finalise SmartCare v0.2

Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user stories, acceptance criteria, assumptions/open questions and selected AI review evidence.  
<br/>**Completed in Stage_2_Smartcare_v02_Completed.md**

# Reflection

In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirement changed after review? Why must requirements have evidence?

After identifying the main requirements for SmartCare based around the patients, practitioners and appointments. The review by AI outlined the ambiguous areas, such as the term staff, which does not specifically identify which roles within the clinic actually have permissions to create and cancel appointments and what data is considered relevant for long term storage.  
<br/>Some suggestions were supported by evidence while others required some more further validation. For example, clarifying appointment conflict rules and search criteria was supported by existing functional requirements. However, suggestions such as the prevention of duplicate records or defining how long retained appointments were not able to be confirmed by the brief alone.  
<br/>After the review I accepted several clarifications to improve requirement quality. I added some open questions and identified inconsistencies between the functional requirements and provisional scope.

The exercise demonstrated why requirements must be supported by evidence. AI can be useful for identifying ambiguities, inconsistencies and testability concerns. It can also suggest ideas that are not present in the client brief and these should only be included when traced to stakeholder needs or assumptions that require validation.