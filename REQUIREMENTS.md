# Requirements — Customer Search

## User Story
As a user,
I want to search customers by name or email,
so that I can quickly find the customer record I need.

## Functional Requirements
FR-01: The system must allow searching customers by partial name match (case-insensitive).
FR-02: The system must allow searching customers by partial email match (case-insensitive).
FR-03: The system must support a unified search query where a single term searches across both name and email fields simultaneously.
FR-04: The system must validate the search query, rejecting empty inputs, strings composed exclusively of whitespace, or queries with an effective length of less than 2 characters.
FR-05: The system must handle queries yielding no results by displaying an informative message without raising unhandled exceptions or system errors.
FR-06: The system must present matching customer records in a structured, readable terminal format, displaying ID, name, email, phone, and status.

## Non-Functional Requirements
NFR-01: Performance: Search operations must execute in less than 200 ms for local datasets containing up to 10,000 customer records.
NFR-02: Maintainability and Simplicity: The solution must run on Python 3.11+ using exclusively the standard library for business logic and CLI presentation, requiring only pytest as an external dependency for testing.
NFR-03: Robustness and Usability: On validation errors or invalid CLI input, the application must output a clean descriptive error message to stderr and return exit code 1, without exposing internal Python tracebacks.

## Open Questions
Q-01: What is the default data source for the customer records?
Answer: A local JSON file (`data/customers.json`) loaded into memory to ensure zero external infrastructure setup.
Q-02: Should terminal output be constrained to prevent buffer flooding?
Answer: Yes, by default the system will return up to 50 matching records and indicate if additional records match the criteria.

## Constraints / Assumptions
C-01: The system must be delivered as a local Python command-line interface (CLI) without requiring paid third-party APIs or cloud services.
A-01: Customer dataset files are encoded in UTF-8 and each customer record possesses a unique numeric identifier.
