# ADA-05: Customer Search (Spec-Driven Feature)
**Ingeniería de Software asistida por IA · UADY**  
Desarrollo guiado por especificación: `requirements` → `specification` → `architecture` → `tasks` → `git baseline` → `implementation` → `tests` → `traceability`.

---

## 1. Descripción del Proyecto
Esta funcionalidad permite buscar clientes por coincidencia parcial en nombre o correo electrónico a través de una interfaz de línea de comandos (CLI) local en Python. Soporta búsquedas insensibles a mayúsculas/minúsculas, validación de consultas de entrada, salidas tabulares limpias y códigos de salida estándar para integración en scripts.

---

## 2. Estructura del Repositorio

```text
ada-05/
├── README.md               # Instrucciones de uso y 12 preguntas de reflexión
├── REQUIREMENTS.md         # Requisitos de negocio y producto (FR / NFR)
├── SPEC.md                 # Especificación técnica, reglas y criterios de aceptación
├── ARCHITECTURE.md         # Arquitectura por capas, diagrama Mermaid y trade-offs
├── TASKS.md                # Desglose de tareas atómicas T-01 a T-06
├── AGENTS.md               # Reglas operativas y Quality Gates para el agente
├── AI_USAGE_LOG.md         # Bitácora de interacciones con IA y decisiones humanas
├── data/
│   └── customers.json      # Dataset inicial de clientes
├── src/
│   ├── models.py           # Entidad de dominio Customer
│   ├── repository.py       # Carga de datos desde JSON
│   ├── search.py           # Lógica de búsqueda y validaciones
│   └── cli.py              # Entrypoint CLI y formateo de tablas
├── tests/
│   ├── test_models.py      # Pruebas del modelo Customer
│   ├── test_repository.py  # Pruebas de carga y manejo de errores de archivo
│   ├── test_search.py      # Pruebas de coincidencia, normalización y rendimiento
│   └── test_cli.py         # Pruebas de integración de la CLI y exit codes
├── docs/
│   └── traceability.md     # Matriz de trazabilidad Requisito -> Test
└── results/
    └── agent-report.md     # Reporte de ejecución del agente tarea por tarea
```

---

## 3. Instalación y Requisitos Previos

- **Python 3.11 o superior**.
- Entorno virtual recomendado con `pytest` instalado.

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate  # En Linux/macOS
# .venv\Scripts\activate   # En Windows

# Instalar pytest para pruebas
pip install pytest
```

---

## 4. Uso de la CLI

La aplicación se ejecuta como un módulo de Python usando `python3 -m src.cli`:

### Búsqueda por nombre o correo (coincidencia parcial)
```bash
python3 -m src.cli "ana"
```
**Salida esperada:**
```text
ID | Name            | Email                    | Phone            | Status
---+-----------------+--------------------------+------------------+-------
1  | Ana García      | ana.garcia@example.com   | +52 999 123 4567 | active
5  | Mariana Sánchez | msanchez@corporativo.com | +52 999 567 8901 | active
```

### Búsqueda por dominio de correo electrónico
```bash
python3 -m src.cli "empresa.mx"
```

### Búsqueda insensible a mayúsculas
```bash
python3 -m src.cli "GARCÍA"
```

### Búsqueda sin coincidencias (retorna código 0)
```bash
python3 -m src.cli "terminoquenoexiste"
# Salida: No customers found matching 'terminoquenoexiste'.
```

### Validación de errores (retorna código 1)
```bash
python3 -m src.cli "a"
# Salida en stderr: Error: Search query must contain at least 2 non-whitespace characters.
```

---

## 5. Ejecución de Pruebas Automatizadas

Para correr toda la suite de pruebas unitarias y de integración:

```bash
pytest -v
```

Todas las 21 pruebas deben pasar:
```text
tests/test_cli.py::test_format_table PASSED                              [  4%]
tests/test_cli.py::test_cli_successful_search PASSED                     [  9%]
tests/test_cli.py::test_cli_empty_results PASSED                         [ 14%]
tests/test_cli.py::test_cli_validation_error_short_query PASSED          [ 19%]
tests/test_cli.py::test_cli_validation_error_whitespace PASSED           [ 23%]
tests/test_cli.py::test_cli_file_not_found PASSED                        [ 28%]
tests/test_models.py::test_customer_creation PASSED                      [ 33%]
tests/test_models.py::test_customer_immutability PASSED                  [ 38%]
tests/test_repository.py::test_repository_loads_valid_customers PASSED   [ 42%]
tests/test_repository.py::test_repository_file_not_found PASSED          [ 47%]
tests/test_repository.py::test_repository_invalid_json PASSED            [ 52%]
tests/test_repository.py::test_repository_non_list_json PASSED           [ 57%]
tests/test_search.py::test_search_by_name_partial PASSED                 [ 61%]
tests/test_search.py::test_search_by_email_partial PASSED                [ 66%]
tests/test_search.py::test_case_insensitivity PASSED                     [ 71%]
tests/test_search.py::test_unified_search_matches_both PASSED            [ 76%]
tests/test_search.py::test_query_validation_too_short PASSED             [ 80%]
tests/test_search.py::test_query_validation_whitespace_only PASSED       [ 85%]
tests/test_search.py::test_search_no_matches PASSED                      [ 90%]
tests/test_search.py::test_search_ordering_by_id PASSED                  [ 95%]
tests/test_search.py::test_search_performance PASSED                     [100%]

============================== 21 passed in 0.05s ==============================
```

---

# 6. Preguntas de Reflexión (Sección 18)

### 1. ¿Qué diferencia hay entre requirement, specification y prompt?
El **requirement** dice qué necesita el usuario o negocio a nivel funcional y no funcional (la necesidad general, como buscar clientes). La **specification** es el contrato técnico que traduce esa necesidad en reglas exactas, casos de borde, validaciones y criterios de aceptación verificables. El **prompt** es la instrucción directa y puntual que le damos al modelo de IA para indicarle qué tarea o paso concreto debe ejecutar en el código.

### 2. ¿Qué información fue indispensable antes de programar?
Saber con exactitud qué campos tendría el cliente, cómo se evaluaban las búsquedas (si eran por coincidencia parcial y si ignoraban mayúsculas), la longitud mínima del término (2 caracteres) y qué códigos de salida debía retornar la CLI para que fuera fácil de probar y usar.

### 3. ¿Qué decisiones debieron resolverse antes de programar?
La elección de la arquitectura y la persistencia. Se decidió usar un archivo JSON local en lugar de una base de datos relacional para no meter dependencias complejas, y utilizar la biblioteca estándar con `argparse` para la CLI en vez de frameworks como Click o Typer.

### 4. ¿Qué errores evitó SPEC.md?
Evitó que la IA inventara validaciones raras con expresiones regulares complejas, que modificara los campos del modelo a su gusto o que usara librerías externas innecesarias. Al estar todo definido en `SPEC.md`, el agente fue directo a lo que se pedía.

### 5. ¿Qué problema evita separar REQUIREMENTS.md de SPEC.md?
Evita mezclar las necesidades del negocio con los detalles técnicos de implementación. Permite que los requisitos sean estables y claros para cualquier persona, mientras que la especificación traduce esos requisitos en reglas medibles y escenarios de prueba sin tener que reescribir ni duplicar el texto original.

### 6. ¿Qué papel tuvo AGENTS.md?
Funcionó como las reglas del juego y compuerta de calidad para el agente: le prohibió inventar requisitos nuevos, le exigió cambios mínimos y ordenados siguiendo `TASKS.md`, y le obligó a correr `pytest` antes y después de cada cambio para asegurar que nada se rompiera.

### 7. ¿Qué cambió durante la revisión humana?
La estandarización de idiomas (mantener las especificaciones internas en inglés y los documentos de entrega en español), la confirmación de la estructura en capas desacopladas y la corrección de un caso de prueba donde una aserción no consideraba todos los registros coincidentes.

### 8. ¿La arquitectura coincidió con el código final?
Sí, totalmente. Se respetó la separación en 4 capas planteada en `ARCHITECTURE.md`: CLI (`src/cli.py`), Servicio de Búsqueda (`src/search.py`), Modelo (`src/models.py`) y Repositorio (`src/repository.py`), cumpliendo exactamente con las responsabilidades del diagrama.

### 9. ¿Qué requisito fue más difícil de probar?
La interfaz CLI y sus códigos de salida (NFR-03 y FR-06). Probar que la CLI imprima bien la tabla en `stdout`, que los mensajes de error salgan en `stderr` y que devuelva exactamente código 1 en error y 0 en éxito requirió usar accesorios como `capsys` para capturar la salida de consola de manera controlada.

### 10. ¿Qué mejorarías en tu proceso spec-driven?
En futuras prácticas definiría desde el inicio casos de prueba de borde adicionales en `SPEC.md`, como el manejo de caracteres especiales, emojis o espacios múltiples entre palabras, para que la especificación sea aún más exhaustiva desde el primer borrador.

### 11. ¿Por qué SPEC.md puede funcionar como contrato verificable sin duplicar los requisitos?
Porque utiliza una sección de `Requirements Covered` que referencia los identificadores estables de `REQUIREMENTS.md` (por ejemplo, FR-01, FR-02). En lugar de volver a redactar la necesidad, `SPEC.md` se enfoca únicamente en definir las reglas de negocio, los criterios de aceptación medibles y los escenarios Given-When-Then que comprueban que el requisito se cumple.

### 12. ¿Qué decisiones importantes aparecen en tu AI Usage Log y cómo cambió tu criterio después de revisar las sugerencias de la IA?
Aparece la decisión de descartar bases de datos externas para mantener la solución minimalista, la división del trabajo en tareas atómicas y el ajuste de las pruebas de ordenamiento. Mi criterio cambió al comprobar que la IA no debe usarse para generar código a ciegas; si primero estableces especificaciones claras y actúas como revisor crítico, el código resultante es mucho más limpio, predecible y fácil de mantener.
