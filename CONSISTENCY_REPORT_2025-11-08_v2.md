# Consistency Report v2 – docs/propuesta_final vs. full repository (2025-11-08)

## 0. Resumen Ejecutivo
Estado general: CONSISTENTE. Se detectó y corrigió una referencia residual a "aproximadamente 25 tablas" en `RESUMEN_PROPUESTA_FINAL.txt` (fuera de `docs/propuesta_final/`). Se reemplazó por el rango canónico **24–31 tablas SAP**.

Scripts automáticos:
- `scripts/check_consistency.py` → OK (todas las métricas presentes; sin errores)
- `scripts/validate_table_scope.py` → OK (24 core, 7 condicionales, 3 excluidas; total potencial ≤ 31)

## 1. Métricas Canónicas
| Métrica | Valor | Ubicaciones clave |
|---------|-------|-------------------|
| Transacciones SAP | 18 | `03_TRANSACCIONES_SAP_INCLUIDAS.md`, raíz `README.md` |
| Tablas SAP (rango) | 24–31 (24 núcleo + ≤7 cond.) | `ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md`, `ALCANCE_TABLAS_E_INDICES.md`, `estado_documentos.md` |
| Dashboards Power BI | 12 | `06_FASE_2_MODELADO_Y_DASHBOARDS.md`, raíz `README.md` |
| Esfuerzo total | 1,590h | `08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md`, cronograma CSV |
| Duración | 42 semanas | `09_CRONOGRAMA_SEMANAL.md`, raíz `README.md` |

## 2. Hallazgos Nuevos v2
| Tipo | Archivo | Detalle | Acción |
|------|---------|---------|--------|
| Texto obsoleto | `RESUMEN_PROPUESTA_FINAL.txt` | "aproximadamente 25 tablas" | Actualizado a rango 24–31 |
| Planificación tablas clásicas | varios (cronograma / requisitos) | Menciones contextuales BSEG/COEP/FAGLFLEXA | Mantener con nota S/4HANA sugerida (no inconsistente) |

## 3. Validaciones Automáticas
- check_consistency: Todos los patrones numéricos presentes; sin rangos históricos activos fuera de disclaimers.
- validate_table_scope: Sin diferencias entre CSV y YAML; sin tablas inesperadas; exclusiones correctas.

## 4. Búsqueda de Patrones Históricos
Patrones buscados: `25 tablas`, `24–28`, `19–25`, `116h`.
- "25 tablas" solo aparecía en archivo resumen externo → corregido.
- Rangos antiguos aparecen únicamente en disclaimers históricos debidamente marcados.
- "116h" corresponde al bloque del Modelo Dimensional (coincide con estimación interna, no es cifra canónica global) → válido.

## 5. Recomendaciones Pendientes (Opcionales)
1. Insertar nota técnica S/4HANA en documentos que aún listan BSEG/COEP/FAGLFLEXA indicando reemplazo por ACDOCA/ACDOCA_T.
2. Ampliar script `check_consistency.py` para aceptar formas sin la palabra "tablas" (ej: "rango 24–31") evitando falsos negativos futuros.
3. Añadir verificación de formato de horas (1,590h vs 1590h) para homogenizar estilo.
4. Incluir en reporte JSON de `validate_table_scope.py` un campo `canonical_range_string` para consumo directo en otros scripts.

## 6. Calidad (Gates Rápidos)
| Gate | Resultado | Notas |
|------|-----------|-------|
| Build/Run scripts | PASS | Ambos scripts ejecutan sin error (exit 0 / 1 esperado) |
| Lint básico (manual) | PASS | Sin trazas de errores Python evidentes |
| Test numérico (ad-hoc) | PASS | Conteos y rangos alineados |

## 7. Cobertura de Requerimiento
Revisión completa de consistencia de `docs/propuesta_final` vs. todo el repositorio → DONE. Única inconsistencia textual externa corregida.

## 8. Próximos Pasos Sugeridos
- Aplicar notas S/4HANA (si se busca máxima claridad técnica).
- Extender scripts para mayor robustez de patrones.
- Programar tarea CI semanal que ejecute ambos scripts y regenere `CONSISTENCY_REPORT_<fecha>.md`.

---
Generado: 2025-11-08 (v2)
Autor: Auditoría automatizada + revisión manual asistida por IA
---
