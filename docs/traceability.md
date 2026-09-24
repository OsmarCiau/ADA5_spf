# Traceability Matrix — Customer Search

Esta matriz vincula cada requisito definido en `REQUIREMENTS.md` con su especificación en `SPEC.md`, la tarea de implementación en `TASKS.md`, los archivos afectados y las pruebas correspondientes en `tests/`.

| Requirement | SPEC / AC | Task | Files | Test | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-01** (Búsqueda por nombre) | AC-01, Escenario 1 | T-03 | `src/search.py` | `tests/test_search.py::test_search_by_name_partial` | Pending | Coincidencia parcial case-insensitive |
| **FR-02** (Búsqueda por email) | AC-02, Escenario 2 | T-03 | `src/search.py` | `tests/test_search.py::test_search_by_email_partial` | Pending | Coincidencia parcial case-insensitive |
| **FR-03** (Consulta unificada) | Regla 3 | T-03, T-04 | `src/search.py`, `src/cli.py` | `tests/test_search.py::test_unified_search_matches_both` | Pending | Mismo query evalúa ambos campos |
| **FR-04** (Validación de término) | AC-04, Escenario 4 | T-04 | `src/search.py`, `src/cli.py` | `tests/test_search.py::test_query_too_short`, `tests/test_cli.py::test_cli_validation_error` | Pending | Mínimo 2 caracteres, no espacios |
| **FR-05** (Sin resultados) | AC-05, Escenario 5 | T-04 | `src/search.py`, `src/cli.py` | `tests/test_search.py::test_search_no_matches`, `tests/test_cli.py::test_cli_empty_results` | Pending | Salida informativa, exit code 0 |
| **FR-06** (Visualización tabular) | AC-06 | T-04 | `src/cli.py` | `tests/test_cli.py::test_cli_table_output` | Pending | Columnas: ID, Nombre, Email, Teléfono |
| **NFR-01** (Rendimiento <200ms) | Scope, Reglas | T-03 | `src/search.py` | `tests/test_search.py::test_search_performance` | Pending | Evaluación sobre colecciones locales |
| **NFR-02** (Simplicidad y stack) | Dependencies | T-01, T-02 | `src/`, `tests/` | Suite general `pytest` | Pending | Solo librería estándar + pytest |
| **NFR-03** (Robustez y exit codes)| Error Handling | T-04 | `src/cli.py` | `tests/test_cli.py::test_cli_exit_codes` | Pending | Exit code 0 éxito, 1 error validación |
