# Tasks

## T-01 Project setup
- Goal: Set up base project directory structure, package initializers, and create a representative initial dataset in `data/customers.json`.
- Files:
  - `data/customers.json`
  - `src/__init__.py`
  - `tests/__init__.py`
- Acceptance: Package directories exist and `data/customers.json` contains at least 10 realistic customer records with fields `id`, `name`, `email`, `phone`, `status`.
- Verification: Visual inspection and JSON schema/syntax validation with `python3 -m json.tool data/customers.json`.

## T-02 Domain model
- Goal: Implement the typed domain entity `Customer` and the data access repository `CustomerRepository` for loading customers from JSON.
- Files:
  - `src/models.py`
  - `src/repository.py`
- Acceptance: `Customer` is implemented with `@dataclass`; `CustomerRepository` deserializes JSON records into `Customer` objects, handling missing file and corrupted JSON errors gracefully.
- Verification: Execution of `python3 -c "from src.models import Customer; from src.repository import CustomerRepository"`.

## T-03 Search logic
- Goal: Implement `CustomerSearchService` with partial substring matching, case-insensitive normalization, and field evaluation across name and email.
- Files:
  - `src/search.py`
- Acceptance: `search(query)` filters records matching `query` within `name` or `email` (normalized) and returns results sorted by `id`.
- Verification: Programmatic test verifying queries like "ana" and "example.com" return the expected customer objects.

## T-04 Validation and errors
- Goal: Implement input validation rules, custom domain exception `ValidationError`, and the command-line interface entry point (`src/cli.py`).
- Files:
  - `src/search.py`
  - `src/cli.py`
- Acceptance: Queries under 2 characters or whitespace-only raise `ValidationError`. `src/cli.py` parses arguments, displays formatted tables, and returns exit code 1 for validation/data errors, and exit code 0 for valid runs (even when 0 matches found).
- Verification: CLI invocation `python3 -m src.cli "a"` returns exit code 1 with stderr message; `python3 -m src.cli "ana"` returns exit code 0 with formatted table.

## T-05 Tests
- Goal: Construct an automated test suite with pytest covering domain models, repository, search service, validations, and end-to-end CLI execution.
- Files:
  - `tests/test_models.py`
  - `tests/test_repository.py`
  - `tests/test_search.py`
  - `tests/test_cli.py`
- Acceptance: 100% of Acceptance Criteria (AC-01 through AC-06) and test scenarios from `SPEC.md` are covered. All tests pass with zero failures or warnings.
- Verification: Run `pytest -v`.

## T-06 Documentation
- Goal: Finalize all delivery documents: complete traceability matrix, agent execution report, user guide, and reflection questions.
- Files:
  - `docs/traceability.md`
  - `results/agent-report.md`
  - `README.md`
  - `AI_USAGE_LOG.md`
- Acceptance: Traceability matrix maps Requirements → Spec/AC → Task → Files → Test → Status; `agent-report.md` documents task sequence; `AI_USAGE_LOG.md` records at least 4 significant entries; `README.md` details installation, usage, and answers all 12 reflection questions.
- Verification: Coherence check across all documents with valid Markdown links.
