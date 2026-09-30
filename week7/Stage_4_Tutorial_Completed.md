Assignment 2 – Case Study

Stage 4 Tutorial Activities

Object-Oriented Design Decisions

Week 7 | 60 minutes

# Activity 1 - Encapsulation Review

| Class        | Protected state / invariant                                                                                                                  | Public operations                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Patient      | Name must not be blank when the patient is created                                                                                           | update_info()                                                                                  |
| ---          | ---                                                                                                                                          | ---                                                                                            |
| Practitioner | Name, ID and specialty are never empty; appointment list is private; a practitioner should never have two scheduled appointments at one time | has_conflict(), add_appointment(), get_scheduled_appointments(),<br><br>get_all_appointments() |
| ---          | ---                                                                                                                                          | ---                                                                                            |
| Appointment  | Always links one practitioner, one patient and one time; status can only change from scheduled → cancelled, never directly set from outside  | status(read only), cancel()                                                                    |
| ---          | ---                                                                                                                                          | ---                                                                                            |

# Activity 2 - Composition or Inheritance?

Appointment and Patient -> Composition/association Reason:Appointments have a patient; it is not a kind of patient25

Appointment and Practitioner -> Composition/association Reason: Appointment references one practitioner and the practitioner tracks its appointments. No"is-a" relationship

Doctor and Practitioner (hypothetical) -> Inheritance Reason: A doctor is a practitioner, so it is the one case where inheritance is defensible, but only if Doctor has a behaviour in which practitioners lack. Otherwise an attribute for specialty would be simpler, which is what is used by SmartCare

Clinic and Appointment -> Composition/association Reason: A clinic would contain appointments but no requirement gives clinic a state or behaviour.

# Activity 3 - Responsibility Allocation

Who decides whether SCHEDULED can become CANCELLED?  
The appointment class owns its status and so owns the rule, in cancel()

Who validates a patient name?  
The patient class validates, so no invalid Patient exists regardless of which UI is creating it

Should Appointment execute SQL? Why?  
No it shouldn't, persistence is an infrastructure, mixing into a domain class breaks the single responsibility which makes the class untestable without a database, and not in the approved UML

Should the UI decide whether a status transition is legal?  
The UI might display an error but the rule lives in the domain so that every entry point receives the same behaviour, so no.

# Activity 4 - AI Code Critique

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.

| #   | Design problem                                                                                                           | Correction                                                             |
| --- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| 1   | Public status mutation allows anyone bypass the rules                                                                    | Private the \_status, read-only property, and change only via cancel() |
| --- | ---                                                                                                                      | ---                                                                    |
| 2   | SQL inside cancel() mixes the persistence with logic of the domain and makes it hard to test                             | Remove SQL, persistence is handled later outside the domain classes    |
| --- | ---                                                                                                                      | ---                                                                    |
| 3   | NotificationManager dependency - SMS reminders are still provisional and there is yet to be any evidence from the client | Remove it and add it only if the requirement is confirmed              |
| --- | ---                                                                                                                      | ---                                                                    |
| 4   | PatientRecord inherit, an appointment is not a patient record                                                            | Association is best here as appointment hold a patient reference       |
| --- | ---                                                                                                                      | ---                                                                    |
| 5   | Missing input validations / type hints                                                                                   | Validate in the constructors and add type hints                        |
| --- | ---                                                                                                                      | ---                                                                    |

# Exit question

Why can code be object-oriented syntactically but still have poor object-oriented design?

The use of methods, class and inheritance only previews the syntax of object-oriented design. A good design depends on the responsibilities that are being place with the class that owns the data, state being protected and matching relationships to the domain. An AI class can look object-oriented and still expose public state, SQL and inheritance where association should be used, so it complies but breaks the encapsulation and traceability to the requirements.