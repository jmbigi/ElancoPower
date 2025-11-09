# CONSISTENCY_REPORT — 2025-11-09

Estado general: CONSISTENTE para `docs/propuesta_final` vs. el resto del repositorio.

## Resumen ejecutivo
- Revisión profunda `docs/propuesta_final`: 0 warnings, 0 errores críticos.
- Revisión global de métricas canónicas en el repo: OK. 1 warning no bloqueante en un archivo de reporte histórico.
- Validación de alcance de tablas SAP (CSV vs YAML): OK. Núcleo=24, Condicionales=7, Potencial total=31.

## Detalle de ejecuciones

### 1) Propuesta Final (deep)
Herramienta: `scripts/check_propuesta_final_consistency.py`

- Archivos analizados en `docs/propuesta_final`: 16
- Totales por fases: horas 235+696+659 = 1590 (OK); semanas 6+22+14 = 42 (OK)
- Métricas canónicas detectadas por archivo según expectativa: todas presentes
- Rangos obsoletos (19–25, 24–28, 20–26, etc.): no se detectaron como advertencia; solo aparecen con contexto histórico válido

Conclusión: `docs/propuesta_final` está consistente y autocontenida.

### 2) Consistencia global de métricas
Herramienta: `scripts/check_consistency.py`

- Métricas canónicas validadas: transacciones=18, tablas=24–31, dashboards=12, horas=1590, semanas=42 → OK en documentos esperados
- Warnings (no bloqueantes):
  - `CONSISTENCY_REPORT_2025-11-08_v2.md`: contiene ejemplos/textos con patrones (“25 tablas”, “24–28”, “19–25”, “116h”) dentro del reporte. No afecta a propuesta ni a entregables; es un reporte histórico explicativo.

Exit code: 1 (solo por warnings informativos en reporte histórico)

### 3) Alcance de Tablas SAP (CSV↔YAML)
Herramienta: `scripts/validate_table_scope.py`

- Core (CSV): 24 (esperado 24) → OK
- Condicionales (CSV): 7 → OK
- Excluidas (CSV): 3 → OK
- Potencial total (core+cond): 31 (≤ 32) → OK
- Diferencias: ninguna (sin extras, sin faltantes, sin excluidas marcadas erróneamente)

Exit code: 0

## Observaciones
- Las menciones a rangos previos (p. ej., “24–28” o “19–25”) en `docs/propuesta_final` están correctamente señaladas como histórico/actualización y acompañadas del rango vigente “24–31”, por lo que no constituyen inconsistencia.
- Los únicos avisos provienen de archivos de reporte (“CONSISTENCY_REPORT_*”) que documentan patrones buscados o cambios; no requieren acción adicional.

## Conclusión
A 2025-11-09, la carpeta `docs/propuesta_final` es consistente con el conjunto del proyecto y con las definiciones canónicas (18 transacciones, 24–31 tablas, 12 dashboards, 1590 horas, 42 semanas). No hay inconsistencias que requieran corrección.
