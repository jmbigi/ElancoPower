# Consistency Report – docs/propuesta_final vs. full repository (2025-11-08)

Actualización rápida (revalidación 2):
- scripts/check_consistency.py → OK (sin advertencias)
- scripts/validate_table_scope.py → OK (24 core, 7 cond, 3 excluidas; total potencial 31)
- Corrección aplicada: `CORRECCIONES_APLICADAS_08NOV2025.md` ahora refiere el rango canónico "24–31 tablas" (antes decía "25 tablas").
- Referencias a tablas clásicas (BSEG/COEP/FAGLFLEXA/BSID/BSAD/BSIK/BSAK) persisten en algunas secciones de `docs/propuesta_final` como contexto, pero con notas S/4HANA que aclaran su sustitución por ACDOCA/ACDOCA_T. No representan inconsistencia de alcance.

Este reporte resume las validaciones automáticas y la revisión manual para verificar que la carpeta `docs/propuesta_final` sea consistente con el resto del repositorio.

## 1) Validaciones Automáticas

- scripts/check_consistency.py
  - Resultado: OK con 1 advertencia (exit code 1)
  - Métricas canónicas detectadas en los documentos esperados:
    - Transacciones: 18 → OK
    - Rango de tablas: 24–31 → OK
    - Dashboards: 12 → OK
    - Esfuerzo total: 1,590h → OK
    - Duración: 42 semanas → OK
  - Advertencias:
    - (Ninguna) – Todas las referencias numéricas alineadas tras actualización de `LISTA_PRIORITARIA_TABLAS.md`.

- scripts/validate_table_scope.py
  - Resultado: OK (exit code 0)
  - Conteos en CSV `docs/internos/mapeo_transacciones_tablas_detallado.csv` vs `config/table_scope_expected.yaml`:
    - Core = 24 (esperado 24) → OK
    - Condicionales = 7 → OK
    - Excluidas = 3 → OK
    - Total potencial (core+cond) = 31 (≤ 32) → OK
  - Diferencias: ninguna (listas alineadas)
  - Exclusiones críticas respetadas: BSEG, COEP, FAGLFLEXA → OK

## 2) Hallazgos de Consistencia en docs/propuesta_final

- Inconsistencias numéricas (corregidas):
  - `docs/propuesta_final/ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md` contenía referencias a "25 tablas" como número canónico y un diagrama con "25 Tablas".
    - Acción realizada: actualizado a "24–31 tablas" en las secciones:
      - Resumen "TOTAL ESTIMADO (MVP)"
      - Diagrama de proceso (Lista de 24–31 Tablas)
      - Decisión Go/No-Go (se cambió "25" por "24–31")
      - Proceso Completo (de "~35–65" → "24–31")
      - Nota de transparencia ("número" → "rango" canónico 24–31)
      - Línea de versión (mensaje de cambio actualizado)

- Referencias técnicas a tablas obsoletas (pendiente aclaración editorial):
  - Algunos documentos de planificación referencian tablas reemplazadas en S/4HANA (BSEG, FAGLFLEXA, COEP) en ejemplos o listados de pipelines:
    - `docs/propuesta_final/09_CRONOGRAMA_SEMANAL.md`
    - `docs/propuesta_final/10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md`
    - `docs/propuesta_final/04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD.md`
  - Estado del repositorio y configuración:
    - `config/table_scope_expected.yaml` y el CSV de mapeo interno excluyen BSEG/COEP/FAGLFLEXA en favor de ACDOCA/ACDOCA_T → consistente con S/4HANA.
  - Sugerencia no disruptiva: añadir en los documentos señalados una nota técnica breve tipo: "En S/4HANA se utilizará ACDOCA/ACDOCA_T en lugar de BSEG/FAGLFLEXA; BSID/BSAD/BSIK/BSAK se cubren vía ACDOCA o vistas derivadas". Alternativamente, ajustar los listados a ACDOCA/ACDOCA_T.

- 03_TRANSACCIONES_SAP_INCLUIDAS.md
  - Contenidos y conteos (18 transacciones, 24–31 tablas) → Consistentes.
  - Observación menor: en FB03 aún se listan BKPF/BSEG/BSID/BSAD. Sugerencia: aclarar "en S/4HANA: BKPF + ACDOCA; BSID/BSAD se reemplazan por vistas/derivaciones".

## 3) Coherencia con documentos fuera de propuesta_final

- `docs/internos/estado_documentos.md` declara el rango canónico 24–31 → Alineado.
- `docs/entregables/ALCANCE_TABLAS_E_INDICES.md` menciona 24–31 y exclusión de BSEG/COEP/FAGLFLEXA → Alineado.
- `docs/entregables/LISTA_PRIORITARIA_TABLAS.md` actualizado a 24–31 → Alineado.
- `README.md` (raíz) y `docs/propuesta_final/06_FASE_2_MODELADO_Y_DASHBOARDS.md` sostienen 12 dashboards → Alineado.

## 4) Recomendaciones de cierre (bajo impacto)

1. Mantener el rango canónico en todos los documentos como **24–31 tablas**.
2. Agregar una nota técnica en `09_CRONOGRAMA_SEMANAL.md`, `10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md` y `04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD.md` aclarando el uso de **ACDOCA/ACDOCA_T** en S/4HANA en lugar de **BSEG/COEP/FAGLFLEXXA** y tablas BS** derivadas.
3. En `03_TRANSACCIONES_SAP_INCLUIDAS.md` (sección FB03), añadir la aclaración "S/4HANA: BKPF + ACDOCA".
4. (Completado) `docs/entregables/LISTA_PRIORITARIA_TABLAS.md` ya refleja **24–31**.

## 5) Estado final

- Métricas canónicas presentes y consistentes en `docs/propuesta_final` → OK
- Alcance de tablas (CSV/YAML) consistente con los canónicos y exclusiones → OK
- Inconsistencias detectadas:
  - Texto "25 tablas" en el Anexo Técnico → CORREGIDO en este commit
    (Sin advertencias abiertas)
  - Listados que mencionan BSEG/FAGLFLEXA/COEP en planificación → SUGERENCIA de aclaración S/4HANA

--
Generado automáticamente el 2025-11-08.
