# AI Usage Log — ADA-05 Spec-Driven Feature

Registro de interacciones asistidas por Inteligencia Artificial durante el desarrollo de la práctica ADA-05. Cada entrada documenta el contexto de la interacción, la propuesta del agente, la decisión humana tomada y el impacto tangible en los artefactos del proyecto.

---

## Entrada 1: Definición de Requisitos y Especificación de Comportamiento
- **Fecha:** 2026-09-24
- **Etapa del flujo:** Fase 1 (REQUIREMENTS.md) y Fase 2 (SPEC.md)
- **Contexto:**
  Definición inicial de los requisitos de la función Customer Search a partir de la historia de usuario planteada en la guía de la práctica.
- **Qué propuso la IA:**
  La IA propuso desglosar la necesidad del usuario en 6 requisitos funcionales (FR-01 a FR-06) y 3 no funcionales (NFR-01 a NFR-03), sugiriendo una regla de longitud mínima de 2 caracteres, búsqueda unificada en nombre y correo, y códigos de salida limpios (código 0 para éxito o resultados vacíos, código 1 para error de validación).
- **Decisión del estudiante:**
  Acepté la propuesta asegurándome de no meter complejidad innecesaria. Decidí que la solución debía ser una CLI local en Python puro con datos en JSON local, sin meter frameworks web ni bases de datos para no sobrecargar el alcance. Además, definí que las especificaciones de ingeniería se redactaran en inglés y los documentos de entrega en español.
- **Qué cambió en el producto / artefactos:**
  Se crearon `REQUIREMENTS.md` y `SPEC.md`, congelando los IDs estables `FR-01` a `FR-06`, `NFR-01` a `NFR-03` y los criterios de aceptación `AC-01` a `AC-06`.

---

## Entrada 2: Arquitectura del Sistema y Trade-offs de Implementación
- **Fecha:** 2026-09-24
- **Etapa del flujo:** Fase 3 (ARCHITECTURE.md) y Fase 4 (TASKS.md)
- **Contexto:**
  Diseño de la estructura modular del código antes de crear la línea base de Git y programar.
- **Qué propuso la IA:**
  La IA propuso una arquitectura en capas desacopladas (Presentación CLI, Servicio de búsqueda, Repositorio y Modelo) junto con un diagrama en Mermaid y el desglose de 6 tareas atómicas (T-01 a T-06). También propuso comparar el uso de JSON frente a una base de datos relacional.
- **Decisión del estudiante:**
  Aprobé el desacoplamiento por capas para poder probar la búsqueda sin depender directamente del disco, y confirmé la decisión de usar JSON plano (`data/customers.json`) para mantener el proyecto ligero y ejecutable en cualquier computadora sin dependencias pesadas.
- **Qué cambió en el producto / artefactos:**
  Se crearon `ARCHITECTURE.md` y `TASKS.md`, dejando la base lista para el commit de Git baseline antes de escribir código.

---

## Entrada 3: Implementación del Modelo, Servicio de Búsqueda y CLI
- **Fecha:** 2026-09-24
- **Etapa del flujo:** Fase 7 (T-01 a T-04)
- **Contexto:**
  Construcción progresiva del código fuente de Customer Search siguiendo las tareas definidas en `TASKS.md`.
- **Qué propuso la IA:**
  Implementar la entidad `Customer` como una `dataclass` inmutable (`frozen=True`), el cargador `CustomerRepository` con manejo explícito de errores de formato JSON, el servicio `CustomerSearchService` con validación de entradas (`ValidationError`), y la CLI en `src/cli.py` usando `argparse` con formateo de tablas ASCII alineadas.
- **Decisión del estudiante:**
  Aprobé la implementación secuencial tarea por tarea. Validé que la CLI mostrara mensajes claros en `stderr` ante errores y que no expusiera trazas internas de Python al usuario común.
- **Qué cambió en el producto / artefactos:**
  Se implementaron `src/models.py`, `src/repository.py`, `src/search.py`, `src/cli.py` y el dataset inicial `data/customers.json`, registrando un commit en Git por cada tarea completada.

---

## Entrada 4: Estrategia de Pruebas Automatizadas y Calidad
- **Fecha:** 2026-09-24
- **Etapa del flujo:** Fase 8 y 9 (T-05 y T-06)
- **Contexto:**
  Verificación automatizada de todos los criterios de aceptación y generación de evidencias finales.
- **Qué propuso la IA:**
  Crear una suite de 21 pruebas con `pytest` cubriendo modelos, repositorio, reglas de búsqueda, validaciones, códigos de salida de la CLI y una prueba de rendimiento sobre 10,000 registros para comprobar el NFR-01 (< 200 ms).
- **Decisión del estudiante:**
  Supervisé la ejecución de las pruebas. Al presentarse una discrepancia en la prueba de ordenamiento por ID (donde la aserción inicial no consideraba que el término "com" coincidía con tres correos en lugar de dos), se corrigió la aserción para reflejar el comportamiento real y verificar el orden ascendente correcto. Aprobé el resultado final con el 100% de las pruebas pasadas.
- **Qué cambió en el producto / artefactos:**
  Se crearon los archivos de prueba en `tests/`, se actualizaron `docs/traceability.md` y `results/agent-report.md`, y se completó `README.md` con las respuestas a las 12 preguntas de reflexión.
