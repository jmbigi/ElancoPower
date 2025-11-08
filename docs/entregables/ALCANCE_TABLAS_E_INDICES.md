# Alcance Final de Tablas SAP e Índices (BigQuery)

Fecha: 8-nov-2025
Fuente canónica: `docs/internos/mapeo_transacciones_tablas_detallado.csv`
Contexto: SAP S/4HANA replicado a Google BigQuery vía SAP SLT

---

## 1) Resumen ejecutivo

- Alcance de tablas SAP a replicar (MVP): 19–25 tablas
  - 19 tablas núcleo (core) obligatorias
  - hasta 6 tablas condicionales (según casos de uso)
- Racional técnico: uso de ACDOCA/ACDOCA_T (S/4HANA) para sustituir BSEG/COEP/FAGLFLEXA y reducir drásticamente el volumen de tablas sin perder cobertura funcional.
- Índices en BigQuery: se implementan como particionamiento y clustering por tabla. No se crean índices tipo RDBMS.

Este documento reemplaza cualquier rango anterior (~35–65, ~70–90, ~76–85) y se declara como referencia vigente para cantidad de tablas e índices en Fase 1.

---

## 2) Lista de tablas por estado de inclusión

### 2.1. Núcleo (19) – incluir

FI/CO
- ACDOCA (Universal Journal)
- ACDOCA_T (Totales)
- BKPF (Cabecera documento FI)
- AUFK (Órdenes internas)
- CSKS (Maestro centros de costo)
- CSKA (Maestro elementos de costo)

SD
- VBAK (Cabecera OV)
- VBAP (Posición OV)
- VBUK (Estatus cabecera OV)
- VBUP (Estatus posición OV)

MM
- EKKO (Cabecera OC)
- EKPO (Posición OC)
- MKPF (Cabecera mov. material)
- MSEG (Posición mov. material)
- MARD (Stock por almacén)
- MBEW (Valorización)

Maestros
- MARA (Maestro material)
- KNA1 (Maestro cliente)
- BUT000 (Business Partner)

Nota: `MARD` figura dos veces por diferentes descripciones en el mapeo, pero cuenta 1 sola vez.

### 2.2. Condicionales (6) – candidato_incluir

- MAKT (Textos de material) – solo si se requieren descripciones legibles en UX
- MCHB (Stock por lote) – solo si se requieren KPIs a nivel de lote
- SKA1 (Plan de cuentas) – si se requieren jerarquías contables en reportes
- KONV, KONP (Condiciones de precio) – si se requiere pricing histórico a detalle
- STXL (Textos largos, cluster) – si se necesitan textos de documentos; requiere declustering

### 2.3. Excluidas por S/4HANA (3)

- BSEG, COEP, FAGLFLEXA – Sustituidas por ACDOCA/ACDOCA_T

---

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
- CSKS/CSKA/SKA1: sin partición; clustering: claves de negocio (KOSTL/KTOPL/KSTAR según aplique)

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
- MCHB (condicional): sin partición; clustering: MATNR, WERKS, LGORT, CHARG

Maestros
- MARA: sin partición; clustering: MATNR
- KNA1: sin partición; clustering: KUNNR
- BUT000: sin partición; clustering: PARTNER (o equivalente de BP)
- MAKT (condicional): sin partición; clustering: MATNR, SPRAS

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
- CO-PA: si es account-based, no se requieren tablas CE1*/CE4*; si es cost-based, se evaluará fuera del MVP.
- VA05: prioriza VBUK/VBUP para estatus; `VBEP` (schedule lines) se evaluará en Fase 0 si es imprescindible para KPIs.
- Business Partner: `BUT000` es canónico; `KNA1/LFA1` se utilizan como vistas de compatibilidad. En MVP se incluye `KNA1`; `LFA1` se mantiene fuera salvo requerimiento de P2P.

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
