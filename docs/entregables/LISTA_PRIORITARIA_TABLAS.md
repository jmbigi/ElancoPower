# Lista Priorizada de Tablas SAP S/4HANA → BigQuery (Versión Actualizada)

Fecha: 09-nov-2025  
Estado: Actualización integrada al alcance vigente (core=24, condicional mínimo=4).  
Fuente canónica: `config/table_scope_expected.yaml` (core=24) + `docs/internos/mapeo_transacciones_tablas_detallado.csv`.

---
## 1. Resumen Ejecutivo

Se integra la reclasificación solicitada para robustecer cobertura de VA05, MB5B y KE24:

- Núcleo (core): 24 tablas
- Condicional mínimo: 4 tablas (VBEP, KONV, VBFA, MCHB)
- Opcionales: STXL, KONP, CE1XXXX/CE4XXXX (sólo si CO-PA Costing-Based)

Impacto: Se promueven a core las tablas MAKT, MARC, LFA1 y SKA1. El rango total estimado queda en 24–28 (activando condicionales mínimas).

---
## 2. Clasificación Refinada

### 2.1 Core (Núcleo Confirmado: 24)
ACDOCA, ACDOCA_T, BKPF, AUFK, CSKS, CSKA, SKA1, VBAK, VBAP, VBUK, VBUP, EKKO, EKPO, MKPF, MSEG, MARD, MBEW, MARA, MAKT, MARC, KNA1, LFA1, BUT000, T001

### 2.2 Condicional (activar según KPI / método)
| Tabla | Uso Principal | Activar Si |
|-------|---------------|-----------|
| VBEP | Fechas programadas, backlog/aging | KPI explícito de fill-rate/backorder |
| KONV | Desglose pricing | Análisis de condiciones / margen |
| VBFA | Flujo documento ventas | Pipeline Pedido→Entrega→Factura |
| MCHB | Stock por lote | KPIs por lote / caducidad |
| CE1XXXX | CO-PA reales (Costing-Based) | Método Costing-Based activo + rentabilidad por características |
| CE4XXXX | CO-PA plan (Costing-Based) | Comparación Plan vs Real requerida |
| STXL | Textos largos | Necesidad de textos documentales en reportes |

### 2.3 Opcionales (no afectan rango)
| Tabla | Uso Principal | Activar Si |
|-------|---------------|-----------|
| KONP | Soporte granular de pricing | Análisis a nivel condición histórico |

### 2.4 Excluidas (Sustituidas por S/4HANA Universal Journal)
BSEG, COEP, FAGLFLEXA, BSID, BSAD, BSIK, BSAK (redundantes al adoptar ACDOCA / vistas derivadas).

---
## 3. Árbol de Decisión Rápido (Activación Condicional)

```
Definir KPI
 ├── ¿Multi-moneda? → Sí: TCURR/TCURF
 ├── ¿Desglose condiciones precio? → Sí: KONV/KONP
 ├── ¿Fechas entrega programadas? → Sí: VBEP
 ├── ¿Funnel Pedido→Factura? → Sí: VBFA
 ├── ¿KPIs por lote? → Sí: MCHB
 ├── ¿Textos largos? → Sí: STXL
 └── Ninguna condición → No activar adicionales
```

---
## 4. Impacto de la Promoción a Core

| Tabla | Peso Estimado | Riesgo Performance | Nota |
|-------|---------------|--------------------|------|
| SKA1 | Muy ligera | Nulo | Etiquetado/jerarquía GL mejora legibilidad de estados. |
| MAKT | Media (depende de idiomas) | Bajo | Beneficio UX inmediato; controlar idiomas activos. |
| LFA1 | Pequeña | Nulo | Amplía cobertura de maestros (AP) para futuros KPIs. |
| MARC | Media | Bajo | Aporta granularidad WERKS crítica para stock/costos. |
| VBFA | Puede crecer moderado | Medio | Se mantiene condicional, activar con KPI de funnel. |

---
## 5. Próximos Pasos

1. Mantener VBEP/VBFA/KONV/MCHB como condicionales activables por KPI.
2. Monitorear costo/beneficio de idiomas en MAKT y granularidad en MARC tras primer corte de datos.
3. Ejecutar `scripts/validate_table_scope.py` tras cualquier cambio y documentar en `CORRECCIONES_APLICADAS_08NOV2025.md`.

---
## 6. Cambios Pendientes (Solo si se Aprueba Promoción)

| Acción | Archivo | Descripción |
|--------|---------|-------------|
| Añadir T001 a core | `config/table_scope_expected.yaml` | Pasar T001 de recomendada a core_tables. |
| (Opcional) Añadir SKA1 core | `config/table_scope_expected.yaml` | Solo si se confirma necesidad jerárquica. |
| (Opcional) Añadir VBFA condicional | `config/table_scope_expected.yaml` | Mover de recommended a conditional_tables. |
| Actualizar alcance | `ALCANCE_TABLAS_E_INDICES.md` | Reflejar nuevo conteo si se promueve. |
| Registrar cambio | `CORRECCIONES_APLICADAS_08NOV2025.md` | Trazabilidad. |

---
## 7. Conclusión

Actualización aplicada: core=24 con cobertura reforzada de maestros y MM; condicional mínimo=4 para robustecer VA05/MB5B/KE24 sin inflar el alcance por defecto. CO-PA Costing-Based queda opcional (CE1XXXX/CE4XXXX) y sólo se activa si corresponde.

---
*Documento actualizado – alineado con configuración canónica.*
