# Customer Search Feature

## Goal
Provide a fast, reliable, and verifiable command-line interface (CLI) to search customer records by name or email with support for partial and case-insensitive matching over local JSON data sources.

## Requirements Covered
- FR-01
- FR-02
- FR-03
- FR-04
- FR-05
- FR-06
- NFR-01
- NFR-02
- NFR-03

## Scope
- Search across customer records loaded from a local JSON file (`data/customers.json`).
- Partial substring matching in customer `name` and `email` attributes.
- Case-insensitive evaluation.
- Validation of search query parameters in the CLI entry point.
- Controlled error handling with canonical exit codes (`0` for successful execution, `1` for validation or file errors).
- Clean, structured tabular output in stdout.
- Comprehensive automated test suite with `pytest`.

## Out of Scope
- Graphical User Interface (GUI) or web dashboards.
- Mutation operations (creating, updating, or deleting customer records).
- User authentication and authorization.
- Persistence in external SQL or NoSQL database engines.
- Interactive cursor-based terminal pagination.

## Domain Model
The customer entity `Customer` consists of the following attributes:
- `id` (int): Unique numeric customer identifier.
- `name` (str): Full customer name (non-empty).
- `email` (str): Customer email address (non-empty, standard format).
- `phone` (str): Contact phone number.
- `status` (str): Customer account status (`active` or `inactive`).

## Search Rules
1. **Normalization:** Prior to evaluation, both search queries and customer attributes (`name`, `email`) must be converted to lowercase (`str.lower()`) and stripped of leading/trailing whitespace (`str.strip()`).
2. **Partial Matching:** A customer is considered a match if the normalized query substring is contained within the normalized `name` or `email` (`query in field`).
3. **Unified Querying:** The unified search parameter is evaluated simultaneously across both `name` and `email`.
4. **Ordering:** Matching customer records must be sorted in ascending order by `id`.
5. **Result Limiting:** A maximum of 50 records will be displayed per search query to prevent terminal buffer overflow.

## Validation Rules
1. **Minimum Length:** The normalized search query (`query.strip()`) must have a minimum length of 2 characters.
2. **Non-Empty Input:** Empty strings or strings containing only whitespace characters are strictly invalid.
3. **Data File Integrity:** The specified dataset file (`data/customers.json`) must exist and contain a valid JSON array of customer objects.

## Error Handling
1. **Query Validation Error:** When a search term fails validation rules (empty or fewer than 2 characters), the application writes to `stderr`:
   `Error: Search query must contain at least 2 non-whitespace characters.`
   and terminates with exit code `1`.
2. **Data Loading Error:** When the data file cannot be found or is corrupt JSON, the application writes to `stderr`:
   `Error: Unable to load data file: [detail]`
   and terminates with exit code `1`.
3. **No Matches Found:** When a valid query matches zero customer records, the application writes to `stdout`:
   `No customers found matching '[term]'.`
   and terminates with exit code `0` (clean run, empty result set).

## Acceptance Criteria
- **AC-01 (Search by Name):** Given a customer with name "Ana García", querying "ana" or "garcía" returns the matching record.
- **AC-02 (Search by Email):** Given a customer with email "carlos@example.com", querying "carlos@" or "example" returns the matching record.
- **AC-03 (Case Insensitivity):** Querying "ANA", "Ana", or "ana" yields identical matching results.
- **AC-04 (Query Validation):** Querying a single character (e.g., "a") or whitespace triggers a clear error message in stderr and exits with code 1.
- **AC-05 (Empty Result Set):** Querying an unmatched valid string (e.g., "notfound") outputs the informational message and exits with code 0.
- **AC-06 (Structured Display):** All matching results are formatted in a clean table with columns: ID, Name, Email, Phone, Status.

## Test Scenarios
1. **Scenario 1 — Partial Name Match:**
   - *Given* a repository with customers: `[{"id": 1, "name": "Roberto Gómez", "email": "roberto@mail.com"}, {"id": 2, "name": "Lucía Morales", "email": "lucia@mail.com"}]`.
   - *When* the user searches for "gómez".
   - *Then* only the customer with id 1 is returned.
2. **Scenario 2 — Partial Email Match:**
   - *Given* the same repository.
   - *When* the user searches for "lucia@".
   - *Then* only the customer with id 2 is returned.
3. **Scenario 3 — Case Insensitive Matching:**
   - *When* the user searches for "LUCÍA" or "lucía".
   - *Then* the customer with id 2 is returned in both cases.
4. **Scenario 4 — Short Query Validation:**
   - *When* the user searches for "x".
   - *Then* a validation error is emitted and exit code 1 is produced.
5. **Scenario 5 — Unmatched Search:**
   - *When* the user searches for "unmatched_term".
   - *Then* 0 results are returned and an informational message is shown with exit code 0.

## Constraints
- Pure Python 3.11+ implementation without external third-party runtime frameworks.
- Local CLI execution interface.

## Open Questions
N/A — All behavioral ambiguities regarding minimum query length, data sources, and exit codes have been addressed.
