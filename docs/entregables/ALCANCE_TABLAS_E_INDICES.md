# Alcance Final de Tablas SAP e Índices (BigQuery)

Fecha: 9-nov-2025 (actualizado - reclass 32–38)
Fuente canónica: `docs/internos/mapeo_transacciones_tablas_detallado.csv`
Contexto: SAP S/4HANA replicado a Google BigQuery vía SAP SLT

---

## 1) Resumen ejecutivo

- Alcance de tablas SAP a replicar (MVP extendido): 32–38 tablas
  - 32 tablas núcleo (24 técnicas + 8 semánticas críticas)
  - Hasta 6 tablas condicionales iniciales (backlog, pricing, flujo ventas, stock por lote, CO-PA cost-based, textos largos – activación según KPI). El séptimo candidato (uno de los condicionales) puede diferirse si no hay caso de uso confirmado.
- Racional técnico: promoción de tablas semánticas (SKAT, KNB1, KNVV, LFB1, T001W, EKET, CKMLCR, CSKT) para evitar retrabajo y mejorar legibilidad/adopción temprana.
- Sustitución estructural mantenida: Universal Journal (ACDOCA/ACDOCA_T) elimina necesidad de BSEG/COEP/FAGLFLEXA.
- Estrategia de rendimiento: particionamiento + clustering (sin índices RDBMS tradicionales).

Este documento reemplaza el rango previo 24–31 y declara la nueva referencia vigente 32–38 para Fase 1.

---

## Acta de Cierre de Alcance (8-nov-2025)

| Elemento | Valor Vigente |
|----------|---------------|
| Transacciones SAP | 18 |
| Rango de Tablas (Fase 1) | 32–38 tablas |
| Núcleo | 32 tablas |
| Condicionales potenciales | 6–7 tablas (activación selectiva) |
| Dashboards | 12 |
| Esfuerzo Total | 1,590 horas |
| Duración | 42 semanas |

Notas de activación condicional:
1. CO-PA Costing-Based: activar CE1XXXX (reales) y CE4XXXX (plan) solo si el sistema utiliza Costing-Based y se requiere granularidad KE24 ampliada. Si el enfoque es exclusivamente Account-Based, ACDOCA cubre el requerimiento.
2. STXL (textos largos): requiere declustering en SLT; incluir únicamente si los dashboards definidos necesitan textos enriquecidos (descripciones extendidas / notas comerciales).
3. VBEP: activar cuando exista KPI de backlog / fechas de entrega comprometidas.
4. KONV: activar si se requiere análisis de pricing a nivel condición; KONP queda fuera del rango (opcional) para granularidad aún mayor.
5. MCHB: sólo si los KPIs solicitan stock por lote (trazabilidad / vencimientos).
6. Flujo de ventas (VBFA): incorporar para análisis pipeline OV → Entrega → Factura.

Gobernanza: cualquier modificación posterior deberá (a) registrarse en `CORRECCIONES_APLICADAS_08NOV2025.md`, (b) actualizar este documento y el Anexo Técnico, y (c) pasar validación mediante `scripts/check_consistency.py` (estado=exit 0/1 sin errores).

---

## 2) Lista de tablas por estado de inclusión

### 2.1. Núcleo Extendido (32) – incluir

FI/CO (Contable / Controlling)
- ACDOCA (Universal Journal)
- ACDOCA_T (Totales)
- BKPF (Cabecera documento FI)
- AUFK (Órdenes internas)
- CSKS (Centros de costo)
- CSKA (Elementos de costo)
- SKA1 (Plan de cuentas)
- SKAT (Textos de cuentas)
- CSKT (Textos de centros de costo)

SD (Ventas)
- VBAK (Cabecera OV)
- VBAP (Posición OV)
- VBUK (Estatus cabecera OV)
- VBUP (Estatus posición OV)
- KNB1 (Cliente por sociedad)
- KNVV (Cliente vista comercial)

MM / Logística / Compras
- EKKO (Cabecera OC)
- EKPO (Posición OC)
- EKET (Programación entregas OC)
- MKPF (Cabecera mov. material)
- MSEG (Posición mov. material)
- MARD (Stock por almacén)
- MBEW (Valorización)
- MARC (Material por planta)
- CKMLCR (Cost component split)

Maestros Generales
- MARA (Material)
- MAKT (Textos material)
- KNA1 (Cliente general)
- LFA1 (Proveedor general)
- LFB1 (Proveedor por sociedad)
- BUT000 (Business Partner)
- T001 (Sociedades)
- T001W (Plantas / centros)

### 2.2. Condicionales (6–7) – candidato_incluir

Activación por KPI / método:
- VBEP (Schedule lines / backlog / aging)
- KONV (Condiciones de precio)
- VBFA (Flujo documentos ventas)
- MCHB (Stock por lote)
- CE1XXXX (CO-PA reales Costing-Based)
- CE4XXXX (CO-PA plan Costing-Based)
- STXL (Textos largos) [puede diferirse si no hay requerimiento de textos extendidos]

Opcional fuera de rango base:
- KONP (detalle granular condiciones de precio)

### 2.3. Excluidas por S/4HANA (3)

- BSEG, COEP, FAGLFLEXA – Sustituidas por ACDOCA/ACDOCA_T

---

### 2.4. CO-PA (Condicional por Método)

- Account-Based CO-PA: cubierto por ACDOCA (recomendado en S/4HANA).
- Costing-Based CO-PA: incluir como condicionales las tablas **CE1XXXX** (reales) y **CE4XXXX** (plan) si el sistema utiliza Costing-Based y se requiere KE24 con características de rentabilidad detalladas.

## 3) Política de particionamiento y clustering (BigQuery)

Principios
- Particionar por fecha de uso natural de consulta (contabilización/creación) o por timestamp de ingesta si la tabla es principalmente maestra.
- Clusterizar por 2–4 columnas más filtradas/joineadas por los modelos/dashboards.
- Medir y ajustar tras 2–3 semanas en producción (observabilidad de bytes escaneados y latencias).

Sugerencias por grupo de tablas

FI/CO
- ACDOCA: partition por BUDAT_DATE (DATE derivado de BUDAT) o CPUDT_DATE; clustering: BUKRS, RACCT, KOSTL, PRCTR (opcional: AUFNR/SEGMENT)
- ACDOCA_T: partition por periodo fiscal (entero GJAHR_POPER) o por fecha de corte; clustering: BUKRS, RLDNR, RACCT, POPER
- BKPF: partition por BUDAT_DATE o CPUDT_DATE; clustering: BUKRS, GJAHR, BELNR, BLART
- AUFK: sin partición; clustering: AUFNR, BUKRS
- CSKS/CSKA (y SKA1 si se activa): sin partición; clustering: claves de negocio (KOSTL/KTOPL/KSTAR)

SD
- VBAK: partition ERDAT_DATE o AEDAT_DATE; clustering: VKORG, VTWEG, SPART, KUNNR
- VBAP: partition ERDAT_DATE o AEDAT_DATE; clustering: VBELN, POSNR, MATNR
- VBUK/VBUP: partition AEDAT_DATE; clustering: VBELN, POSNR, status (GBSTK/LFSTK/FKSTK)

MM
- EKKO: partition BEDAT_DATE o AEDAT_DATE; clustering: EBELN, BUKRS, LIFNR, EKGRP
- EKPO: partition AEDAT_DATE; clustering: EBELN, EBELP, MATNR, WERKS
- MKPF/MSEG: partition BUDAT_DATE; clustering (MSEG): MBLNR, MJAHR, BWART, WERKS, LGORT, MATNR
- MARD: sin partición; clustering: MATNR, WERKS, LGORT
- MBEW: sin partición; clustering: MATNR, BWKEY
- MARC: sin partición; clustering: MATNR, WERKS
- MCHB (condicional): sin partición; clustering: MATNR, WERKS, LGORT, CHARG

Maestros
- MARA: sin partición; clustering: MATNR
- MAKT: sin partición; clustering: MATNR, SPRAS
- KNA1: sin partición; clustering: KUNNR
- LFA1: sin partición; clustering: LIFNR
- BUT000: sin partición; clustering: PARTNER (o equivalente de BP)
- T001: sin partición; clustering: BUKRS

Precios / Textos (condicionales)
- KONV/KONP: partition por DATAB_DATE (validez desde) si aplica; clustering: KNUMV, KSCHL, VKORG/VTWEG
- STXL: sin partición; clustering: TDOBJECT, TDNAME, TDSPRAS (declustering en SLT requerido)

Notas
- Si SLT entrega columnas de auditoría (p. ej. _CHANGE_TYPE, _IS_DELETED, _LOAD_TS), mantenerlas para CDC y auditoría.
- Para periodos fiscales, considerar columna INT `GJAHR_POPER = GJAHR*100 + POPER` para agregaciones por periodo.

---

## 4) Decisiones y supuestos

- Plataforma objetivo: BigQuery (confirmado por antecedentes de tickets).
- Sistema fuente: SAP S/4HANA; se prioriza ACDOCA/ACDOCA_T.
- CO-PA: si es account-based, no se requieren tablas CE1*/CE4*; si es cost-based, su inclusión es condicional y crítica.
- VA05: se prioriza VBUK/VBUP para estatus; `VBEP` (schedule lines) se clasifica como condicional de alta importancia.
- Business Partner: `BUT000` es canónico. `KNA1` y `LFA1` se incluyen en el núcleo para asegurar la cobertura de datos maestros de cliente y proveedor.

---

## 5) Trazabilidad y control de cambios

- Origen de la lista: `docs/internos/mapeo_transacciones_tablas_detallado.csv` (columnas: transacción, tabla, estado_inclusion).
- Excluidas explícitas: BSEG, COEP, FAGLFLEXA.
- Cualquier cambio de alcance se registrará en `CORRECCIONES_APLICADAS_08NOV2025.md` y se reflejará en este documento y en el Anexo Técnico.

---

## 6) Anexos de referencia

- `docs/propuesta_final/ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md` (conceptos transacción vs tabla)
- `docs/propuesta_final/03_TRANSACCIONES_SAP_INCLUIDAS.md` (lista de 18 transacciones)
- `docs/propuesta_final/05_FASE_1_CONSTRUCCION_DATA_LAKE.md` (arquitectura por capas)
