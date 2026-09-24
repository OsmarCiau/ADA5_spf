# Reporte de Ejecución del Agente (Agent Report)

## Agente / Versión
- **Agente:** Antigravity / Gemini 3.8 Flash (High)
- **Entorno:** macOS, Python 3.14 (venv), zsh

## Contexto Inicial
El proyecto inició desde cero (*greenfield*) para construir la función **Customer Search** como parte de la actividad académica ADA-05 de Ingeniería de Software asistida por IA (UADY). Se siguió estrictamente la metodología guiada por especificación (*spec-driven*): `requirements` → `specification` → `architecture` → `tasks` → `git baseline` → `implementation` → `tests` → `traceability`.

## Secuencia de Tareas

### T-01 Configuración Inicial del Proyecto (Project setup)
- **Qué hizo el agente:** Creó la estructura de directorios (`src/`, `tests/`, `data/`, `docs/`, `results/`), los inicializadores de paquete `src/__init__.py` y `tests/__init__.py`, y el archivo de datos inicial `data/customers.json` con 12 registros variados para pruebas.
- **Revisión humana:** Se validó la sintaxis del JSON con `python3 -m json.tool` y se confirmó que cubriera nombres con tildes, mayúsculas y correos de distintos dominios.
- **Pruebas:** Validación sintáctica de JSON aprobada (`JSON OK`).

### T-02 Modelo de Dominio y Persistencia (Domain model)
- **Qué hizo el agente:** Implementó la entidad `Customer` como un `@dataclass(frozen=True)` en `src/models.py` y la clase `CustomerRepository` en `src/repository.py` con manejo de excepciones `FileNotFoundError` y `ValueError` para JSON malformado.
- **Revisión humana:** Se verificó la inmutabilidad de la entidad y la carga correcta de los 12 clientes sin errores.
- **Pruebas:** Script de verificación en consola cargando exitosamente los 12 clientes.

### T-03 Lógica de Búsqueda (Search logic)
- **Qué hizo el agente:** Creó `CustomerSearchService` y la excepción de dominio `ValidationError` en `src/search.py`. Implementó la normalización a minúsculas (`strip().lower()`), coincidencia parcial en nombre y correo, y ordenamiento ascendente por ID.
- **Revisión humana:** Se confirmó que la búsqueda coincidiera tanto en nombres como en correos con el mismo término unificado.
- **Pruebas:** Verificación programática con casos de prueba para "ana", "example.com" y rechazo de consultas de un solo carácter.

### T-04 Validación y Manejo de Errores (Validation and errors)
- **Qué hizo el agente:** Implementó la interfaz de línea de comandos en `src/cli.py` con `argparse`. Añadió el formateo de tablas de texto alineadas y el control de códigos de salida: código `0` para búsquedas válidas (con o sin resultados) y código `1` para errores de validación o fallas de archivo, con mensajes descriptivos en `stderr`.
- **Revisión humana:** Se probaron consultas válidas, consultas sin coincidencias y consultas inválidas directamente en la consola.
- **Pruebas:** Pruebas directas de CLI: `python3 -m src.cli "ana"` (exit code 0), `python3 -m src.cli "noexiste123"` (exit code 0), y `python3 -m src.cli "a"` (exit code 1).

### T-05 Pruebas Automatizadas (Tests)
- **Qué hizo el agente:** Implementó 21 pruebas unitarias y de integración distribuidas en `tests/test_models.py`, `tests/test_repository.py`, `tests/test_search.py` y `tests/test_cli.py`. Cubrió todos los criterios de aceptación (AC-01 a AC-06) y verificó el rendimiento de NFR-01 (< 200 ms).
- **Revisión humana:** Se analizó una falla en la aserción de ordenamiento en `test_search_ordering_by_id`, detectando que el término "com" coincidía con 3 clientes y no solo 2. Se corrigió la expectativa del test.
- **Pruebas:** `pytest -v` ejecutado con 21 pruebas pasadas al 100% en 0.05 segundos.

### T-06 Documentación y Trazabilidad (Documentation)
- **Qué hizo el agente:** Actualizó la matriz de trazabilidad en `docs/traceability.md` con todos los requisitos en estado PASSED, completó las 4 entradas de `AI_USAGE_LOG.md`, consolidó el reporte del agente y redactó el `README.md` con las 12 preguntas de reflexión resueltas.
- **Revisión humana:** Revisión integral de coherencia entre requisitos, especificaciones, código, pruebas y respuestas de reflexión.
- **Pruebas:** Verificación de enlaces Markdown y formato general del repositorio.

## Problemas Encontrados
1. **Entorno de pytest:** La máquina no contaba con `pytest` instalado de manera global en el intérprete de Python del sistema. Se solucionó creando un entorno virtual `.venv` e instalando `pytest` localmente, agregando `.venv` a `.gitignore`.
2. **Aserción en test de ordenamiento:** En `test_search_ordering_by_id`, la aserción inicial esperaba los IDs `[1, 3]` para la búsqueda "com", pero el dataset de prueba contenía tres clientes con ese dominio (`roberto@mail.com`, `lucia@mail.com`, `ana.garcia@example.com`). Se ajustó la aserción a `[1, 2, 3]`, confirmando que el algoritmo ordenó correctamente de forma ascendente.

## Intervenciones Humanas
1. Revisión inicial de los requisitos y decisión de enfocar la solución en una CLI minimalista en Python puro con persistencia JSON.
2. Aprobación de la estructura del proyecto y los planes de trabajo antes de generar código.
3. Estandarización de idiomas: especificaciones de ingeniería en inglés y entregables académicos en español formal.
4. Supervisión de la corrección del caso de prueba en T-05 y validación final de los resultados.

## Cambios en Requisitos y Especificaciones
No hubo cambios en los requisitos una vez aprobados en `REQUIREMENTS.md` y `SPEC.md`. El desarrollo se apegó en todo momento al contrato original.

## Verificación Final
- **Pruebas automatizadas:** 21 pruebas pasadas exitosamente con `pytest` en 0.05 segundos.
- **Criterios de aceptación:** 100% cubiertos y trazados en `docs/traceability.md`.
- **Rendimiento (NFR-01):** Búsqueda sobre 10,000 registros completada en menos de 10 ms (límite máximo permitido: 200 ms).
- **Control de errores (NFR-03):** Códigos de salida limpios sin stack traces visibles.

## Lecciones Aprendidas
1. Tener una especificación detallada (`SPEC.md`) antes de programar elimina la ambigüedad y evita que el agente tome decisiones arbitrarias o introduzca dependencias innecesarias.
2. Trabajar tarea por tarea con pruebas intermedias permite detectar detalles de diseño o aserciones incorrectas de forma inmediata, facilitando la corrección sin afectar el resto del sistema.
3. El rol del desarrollador no es sustituido por la IA, sino que pasa a ser el de revisor crítico, asegurando que el código generado cumpla con los estándares de calidad y la arquitectura acordada.
