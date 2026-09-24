# AI Usage Log — ADA-05 Spec-Driven Feature

Registro de interacciones asistidas por Inteligencia Artificial durante el desarrollo de la práctica ADA-05. Cada entrada documenta el contexto de la interacción, la propuesta del agente, la decisión humana tomada y el impacto tangible en los artefactos del proyecto.

---

## Entrada 1: Definición de Requisitos y Especificación de Comportamiento
- **Fecha:** 2026-09-24
- **Etapa del flujo:** Fase 1 (REQUIREMENTS.md) y Fase 2 (SPEC.md)
- **Contexto:**
  El estudiante solicitó aclarar de dónde surgían los requisitos y cómo estructurar formalmente las necesidades de la feature Customer Search a partir de la User Story base indicada en la guía académica.
- **Qué propuso la IA:**
  La IA propuso desglosar la User Story en 6 requisitos funcionales (FR-01 a FR-06) y 3 no funcionales (NFR-01 a NFR-03), sugiriendo una regla de longitud mínima de 2 caracteres para el término de búsqueda, búsqueda combinada simultánea en nombre y correo, y una respuesta estructurada con código de salida `0` para resultados vacíos y código `1` para errores de validación.
- **Decisión del estudiante:**
  El estudiante analizó la propuesta, cuestionó el rol de la IA en la generación de requisitos frente al rol del estudiante como tomador de decisiones, y aprobó la separación estricta: los requisitos no se inventan sino que se derivan de la historia de usuario y se congelan como contrato en `REQUIREMENTS.md` y `SPEC.md` antes de escribir código. Se acordó mantener la solución minimalista en Python puro con CLI local y persistencia en JSON.
- **Qué cambió en el producto / artefactos:**
  Se crearon formalmente `REQUIREMENTS.md` y `SPEC.md`, estableciendo los identificadores estables `FR-01` a `FR-06`, `NFR-01` a `NFR-03`, las reglas de normalización (case-insensitive, strip), y los Criterios de Aceptación `AC-01` a `AC-06`.

---

## Entrada 2: Arquitectura del Sistema y Trade-offs de Implementación
- **Fecha:** 2026-09-24
- **Etapa del flujo:** Fase 3 (ARCHITECTURE.md) y Fase 4 (TASKS.md)
- **Contexto:**
  Definición de los componentes de software, responsabilidades y el flujo de trabajo en tareas atómicas para la feature.
- **Qué propuso la IA:**
  La IA propuso una arquitectura desacoplada en 4 capas (CLI, Servicio de Búsqueda, Repositorio de Datos, Modelo de Dominio) y la partición del trabajo en 6 tareas atómicas (T-01 a T-06). Incluyó un diagrama Mermaid y un análisis de trade-offs entre persistencia en archivo JSON local frente a base de datos SQLite.
- **Decisión del estudiante:**
  El estudiante aprobó el diseño por capas y la decisión de utilizar JSON local sin dependencias externas pesadas, asegurando el cumplimiento de la restricción de herramientas gratuitas y stack minimalista (NFR-02).
- **Qué cambió en el producto / artefactos:**
  Se crearon `ARCHITECTURE.md` y `TASKS.md`, fijando la estructura modular `src/` (`models.py`, `repository.py`, `search.py`, `cli.py`) y las tareas secuenciales verificables.

---

## Entrada 3: [Pendiente de ejecución - Implementación de Dominio y Lógica de Búsqueda]
*(Esta entrada registrará las propuestas, revisiones y decisiones tomadas durante la ejecución de las tareas T-01 a T-04 con el agente).*

---

## Entrada 4: [Pendiente de ejecución - Estrategia de Pruebas Automatizadas y Revisión]
*(Esta entrada registrará las decisiones tomadas durante la ejecución de T-05 y T-06 sobre cobertura de pruebas y verificación de trazabilidad).*
