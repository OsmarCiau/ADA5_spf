# Traceability Matrix — Customer Search

Esta matriz vincula cada requisito definido en `REQUIREMENTS.md` con su especificación en `SPEC.md`, la tarea de implementación en `TASKS.md`, los archivos afectados y las pruebas correspondientes en `tests/`.

| Requirement | SPEC / AC | Task | Files | Test | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-01** (Búsqueda por nombre) | AC-01, Escenario 1 | T-03 | `src/search.py` | `tests/test_search.py::test_search_by_name_partial` | **PASSED** | Coincidencia parcial case-insensitive verificada |
| **FR-02** (Búsqueda por email) | AC-02, Escenario 2 | T-03 | `src/search.py` | `tests/test_search.py::test_search_by_email_partial` | **PASSED** | Coincidencia parcial de dominios y usuarios |
| **FR-03** (Consulta unificada) | Regla 3 | T-03, T-04 | `src/search.py`, `src/cli.py` | `tests/test_search.py::test_unified_search_matches_both` | **PASSED** | Mismo query evalúa ambos campos simultáneamente |
| **FR-04** (Validación de término) | AC-04, Escenario 4 | T-04 | `src/search.py`, `src/cli.py` | `tests/test_search.py::test_query_validation_too_short`, `tests/test_search.py::test_query_validation_whitespace_only`, `tests/test_cli.py::test_cli_validation_error_short_query` | **PASSED** | Rechaza menos de 2 caracteres y solo espacios |
| **FR-05** (Sin resultados) | AC-05, Escenario 5 | T-04 | `src/search.py`, `src/cli.py` | `tests/test_search.py::test_search_no_matches`, `tests/test_cli.py::test_cli_empty_results` | **PASSED** | Salida amigable en stdout, exit code 0 |
| **FR-06** (Visualización tabular) | AC-06 | T-04 | `src/cli.py` | `tests/test_cli.py::test_format_table`, `tests/test_cli.py::test_cli_successful_search` | **PASSED** | Tabla ASCII con columnas ID, Name, Email, Phone, Status |
| **NFR-01** (Rendimiento <200ms) | Scope, Reglas | T-03 | `src/search.py` | `tests/test_search.py::test_search_performance` | **PASSED** | Ejecuta en < 10 ms sobre 10,000 registros |
| **NFR-02** (Simplicidad y stack) | Dependencies | T-01, T-02 | `src/`, `tests/` | Suite general `pytest` (21 pruebas) | **PASSED** | Solo biblioteca estándar de Python 3.11+ y pytest |
| **NFR-03** (Robustez y exit codes)| Error Handling | T-04 | `src/cli.py` | `tests/test_cli.py::test_cli_validation_error_short_query`, `tests/test_cli.py::test_cli_file_not_found` | **PASSED** | Exit code 0 en éxito/sin resultados, 1 en error |
