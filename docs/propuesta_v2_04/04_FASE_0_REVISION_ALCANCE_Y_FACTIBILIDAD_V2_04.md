# 4. FASE 0 - REVISIÓN DEL ALCANCE Y FACTIBILIDAD (V2.04)

**Versión:** 2.04 (Con ABAP Developer - Cronograma Moderado)  
**Fecha:** 10 de noviembre de 2025

---

## 4.1. Objetivo de la Fase

**Validar la viabilidad técnica del proyecto** y resolver los issues identificados por TI antes de iniciar el desarrollo. Esta fase es **crítica** para asegurar que Fase 1 pueda ejecutarse sin bloqueos.

### Objetivos Específicos V2.04

1. ✅ Resolver **Issue #1:** Permisos SAP completos para power user
2. ✅ Resolver **Issue #2:** Disponibilidad de tablas SAP en BigQuery
3. ✅ Validar **Issue #3:** Capacidades reales de BigQuery vs. limitaciones reportadas
4. ✅ Priorizar definitivamente las 18 transacciones SAP
5. ✅ **[NUEVO V2.04]** Análisis profundo de transacciones custom (ZLEL008, ZVEL015) con ABAP Developer
6. ✅ **[NUEVO V2.04]** Configuración inicial de SAP SLT con ABAP Developer
7. ✅ Elaborar plan técnico detallado para Fase 1

---

## 4.2. Duración y Recursos V2.04

| Parámetro | Valor V2.04 | Cambio vs V2.02 |
|-----------|-------------|-----------------|
| **Duración estimada** | 6 semanas (Sem 0-6) | Sin cambio |
| **Fechas** | 6-ene-2026 → 16-feb-2026 | Sin cambio |
| **Horas totales** | **328 horas** | **+93h (+40%)** |
| **Equipo** | 4 recursos | +1 recurso (ABAP Dev) |

### Distribución de Horas por Recurso

| Recurso | Horas V2.04 | Horas V2.02 | Diferencia |
|---------|-------------|-------------|------------|
| **Consultor BI** | 104h | 95h | +9h |
| **ABAP Developer** | **70h** | **0h** | **+70h (NUEVO)** |
| **Funcional SAP** | 122h | 112h | +10h |
| **Project Manager** | 32h | 28h | +4h |
| **Stakeholders Elanco** | 12h | 12h | Sin cambio (sin costo) |
| **TOTAL** | **328h** | **235h** | **+93h** |

---

## 4.3. Actividades Detalladas V2.04

### 4.3.1. Gestión de Permisos SAP y Tickets BigQuery

**Responsables:** Funcional SAP + **ABAP Developer (nuevo)**  
**Duración:** 34 horas (SAP: 22h, ABAP: 12h)  
**Semanas:** 1-4 (continuo)

#### Tareas

| # | Actividad | Recurso | Horas | Entregable |
|---|-----------|---------|-------|------------|
| 1 | Seguimiento Ticket SAP-48219 (permisos MM/SD/FI/CO) | Funcional SAP | 8h | Confirmación permisos |
| 2 | Seguimiento Tickets BQ-7713 y BQ-7721 (tablas BigQuery) | Funcional SAP | 8h | Confirmación tablas |
| 3 | **Validación técnica de permisos SLT** | **ABAP Developer** | **8h** | **Permisos SLT OK** |
| 4 | **Gestión de tickets SAP críticos (Z-tables)** | **ABAP Developer** | **4h** | **Tickets resueltos** |
| 5 | Coordinación con TI Global y David Saboya | Funcional SAP | 6h | Minutas reuniones |

**Novedad V2.04:** ABAP Developer valida permisos técnicos para SAP SLT y gestiona tickets críticos relacionados con Z-tables.

#### Resultados Esperados

✅ **Permisos SAP** (validado por Funcional SAP + ABAP Developer):
- Módulo MM, SD, FI, CO con acceso completo
- **[NUEVO]** Permisos SAP SLT para replicación en tiempo real
- **[NUEVO]** Acceso a código fuente ZLEL008 y ZVEL015

✅ **Tablas BigQuery** (validado por Consultor BI + ABAP Developer):
- Tablas custom (ZLEL008, ZVEL015) identificadas
- Tablas CO-PA (CE1*, CE4* para KE24)
- ACDOCA/ACDOCA_T (Universal Journal S/4HANA)
- Validación de tablas estándar (VBAK, EKKO, BKPF, etc.)

---

### 4.3.2. Análisis Técnico de Arquitectura BigQuery

**Responsable:** Consultor BI  
**Duración:** 28 horas (+4h vs V2.02)  
**Semanas:** 1-2

#### Tareas

| # | Actividad | Horas | Entregable |
|---|-----------|-------|------------|
| 1 | Análisis de dataset casa_bi en BigQuery | 8h | Inventario tablas |
| 2 | Evaluación de performance con volúmenes reales | 8h | Benchmarks queries |
| 3 | Validación conectividad Power BI ↔ BigQuery | 4h | POC funcional |
| 4 | **Diseño arquitectura 3 capas (RAW/PROCESSED/CURATED)** | **4h** | **Diagramas** |
| 5 | Análisis de costos BigQuery proyectados | 2h | Estimación costos |
| 6 | Documentación de hallazgos técnicos | 2h | Reporte viabilidad |

**Nota S/4HANA:** En S/4HANA el detalle contable consolidado se gestiona en **ACDOCA/ACDOCA_T**, que sustituyen a tablas clásicas como **BSEG**, **COEP** y **FAGLFLEXA**. El modelo V2.04 se basará en ACDOCA/ACDOCA_T.

---

### 4.3.3. Análisis Profundo de Transacciones Custom (Z) **[NUEVO V2.04]**

**Responsable:** **ABAP Developer (principal) + Funcional SAP (apoyo)**  
**Duración:** 34 horas (ABAP: 24h, SAP: 10h)  
**Semanas:** 2-3

#### Transacciones a Analizar

**ZLEL008 - Inventario Consolidado MRP**
| Actividad | Recurso | Horas | Entregable |
|-----------|---------|-------|------------|
| Acceso al código ABAP (SE38/SE80) | ABAP Developer | 4h | Código documentado |
| Identificar tablas fuente y Z-tables | ABAP Developer | 8h | Listado tablas |
| Documentar lógica de cálculo/agregación | ABAP Developer + SAP | 6h | Especificación funcional |
| Mapear campos de salida a tablas SAP | ABAP Developer | 4h | Mapping completo |
| Definir estrategia de extracción | ABAP Developer | 2h | Plan de extracción |

**ZVEL015 - Condiciones de Precio**
| Actividad | Recurso | Horas | Entregable |
|-----------|---------|-------|------------|
| Análisis de código ABAP | ABAP Developer | 3h | Código documentado |
| Identificar tablas estándar (KONV, A-tables) o custom | ABAP Developer | 3h | Listado tablas |
| Documentar lógica pricing | ABAP Developer + SAP | 4h | Especificación |

**Resultado Crítico:** Definir si Z-transactions son extraíbles vía SLT o requieren desarrollo custom.

---

### 4.3.4. Workshop de Priorización de Transacciones

**Responsables:** Funcional SAP + Consultor BI + Stakeholders Elanco  
**Duración:** 24 horas (equipo: 12h, stakeholders: 12h)  
**Semana:** 2-3

#### Estructura del Workshop (sin cambios vs V2.02)

**Sesión 1: Finanzas (4 horas)**
- Participantes: Controller, Analistas Finanzas, Funcional SAP, Consultor BI
- Objetivo: Priorizar transacciones FI/CO
- Transacciones: FAGLL03, KSB1, KE24, FB03, F.08, F.01, FBL1N, FBL5N

**Sesión 2: Supply Chain (4 horas)**
- Participantes: Supply Manager, Planeadores, Funcional SAP, Consultor BI
- Objetivo: Priorizar transacciones MM/SD
- Transacciones: VA05, ZLEL008, ME2L, MM60, MB59, ME23N, MB5B

**Sesión 3: Consolidación (4 horas)**
- Participantes: Todos + Management
- Objetivo: Consensuar priorización final
- Entregable: Backlog definitivo aprobado

---

### 4.3.5. Configuración Inicial de SAP SLT **[NUEVO V2.04]**

**Responsable:** **ABAP Developer (principal) + SAP Basis Elanco (apoyo)**  
**Duración:** 18 horas (ABAP Developer)  
**Semanas:** 4-5

#### Tareas SAP SLT

| # | Actividad | Horas | Entregable |
|---|-----------|-------|------------|
| 1 | Validar licenciamiento SAP SLT en Elanco | 2h | Confirmación licencia |
| 2 | Configuración básica de SLT (sistema fuente → BigQuery) | 6h | SLT configurado |
| 3 | Definición de tablas para replicación inicial (2-3 tablas piloto) | 4h | Listado tablas |
| 4 | Prueba de replicación inicial (tabla pequeña) | 4h | POC replicación |
| 5 | Documentación de configuración SLT | 2h | Manual configuración |

**Meta:** Tener SLT operacional al final de Fase 0 para iniciar Fase 1 sin demoras.

---

### 4.3.6. Diseño de Arquitectura Definitiva y POC End-to-End

**Responsables:** Consultor BI + ABAP Developer + Funcional SAP  
**Duración:** 42 horas (BI: 24h, ABAP: 10h, SAP: 8h)  
**Semanas:** 5-6

#### Tareas

| # | Actividad | Recurso | Horas | Entregable |
|---|-----------|---------|-------|------------|
| 1 | Diseño arquitectura 3 capas detallada | Consultor BI | 12h | Diagramas arquitectura |
| 2 | **POC extracción SAP → SLT → BigQuery (RAW)** | **ABAP Developer** | **8h** | **Datos en RAW** |
| 3 | POC transformación RAW → PROCESSED → CURATED | Consultor BI | 8h | Datos en CURATED |
| 4 | POC dashboard Power BI con datos CURATED | Consultor BI | 4h | Dashboard demo |
| 5 | Validación funcional del POC | Funcional SAP | 6h | Aprobación funcional |
| 6 | Documentación técnica del POC | ABAP + BI | 4h | Documento técnico |

**Objetivo:** Demostrar flujo completo **SAP → SLT → BigQuery → Power BI** funcionando.

---

### 4.3.7. Documentación y Reunión Go/No-Go

**Responsables:** Todos  
**Duración:** 28 horas (BI: 8h, ABAP: 0h, SAP: 12h, PM: 8h)  
**Semana:** 6

#### Entregables Fase 0

| # | Entregable | Responsable | Páginas | Estado |
|---|-----------|-------------|---------|--------|
| 1 | Documento de arquitectura técnica definitiva | Consultor BI | 15-20 | Fase 0 |
| 2 | Backlog priorizado de 18 transacciones | Funcional SAP | 5-8 | Fase 0 |
| 3 | Listado completo de tablas SAP con volumetría | Consultor BI + ABAP | 10-15 | Fase 0 |
| 4 | **Especificación técnica Z-transactions (ZLEL008, ZVEL015)** | **ABAP Developer** | **8-12** | **Fase 0** |
| 5 | **Manual de configuración SAP SLT** | **ABAP Developer** | **5-8** | **Fase 0** |
| 6 | POC funcional validado por stakeholders | Todos | Demo | Fase 0 |
| 7 | Plan detallado de Fase 1 y Fase 2 | PM + Consultor BI | 20-30 | Fase 0 |
| 8 | Decisión Go/No-Go documentada | PM | 2-3 | Fase 0 |

---

## 4.4. Reunión Go/No-Go (Semana 6)

### Criterios de Aprobación

| Criterio | Importancia | Estado Esperado |
|----------|-------------|-----------------|
| Permisos SAP completos | ⛔ **BLOQUEANTE** | Resuelto |
| **Permisos SAP SLT operacional** | ⛔ **BLOQUEANTE** | **Configurado** |
| Tablas BigQuery ≥ 85% disponibles | ⚠️ Crítico | Resuelto o plan B |
| **Z-transactions analizadas (ZLEL008, ZVEL015)** | ⚠️ **Crítico** | **Documentadas** |
| POC técnico exitoso (SAP → BigQuery → Power BI) | ⚠️ Crítico | Funcional |
| Backlog priorizado aprobado | ✅ Importante | Aprobado |
| Presupuesto Fase 1 aprobado | ✅ Importante | Aprobado |

### Decisión Go/No-Go

**GO (Continuar a Fase 1):**
- ✅ Todos los bloqueantes resueltos
- ✅ POC técnico exitoso
- ✅ Equipo alineado (4 recursos confirmados)
- ✅ **ABAP Developer contratado y operativo**

**NO-GO (Detener o replantear):**
- ❌ Bloqueantes sin resolver
- ❌ POC técnico fallido
- ❌ Presupuesto no aprobado
- ❌ **ABAP Developer no disponible**

---

## 4.5. Riesgos Específicos de Fase 0 (V2.04)

| Riesgo | Probabilidad | Impacto | Mitigación V2.04 |
|--------|--------------|---------|------------------|
| Delay en contratación ABAP Developer | Media | Alto | Iniciar reclutamiento 2-3 sem antes kick-off |
| Tickets SAP sin resolver | Media | Alto | ABAP Developer gestiona tickets críticos |
| Z-transactions más complejas de lo estimado | Media | Medio | ABAP Developer con 24h dedicadas al análisis |
| SAP SLT no licenciado o no disponible | Baja | Crítico | Validar con SAP Basis en semana 1 |
| Stakeholders no disponibles para workshops | Media | Medio | Coordinar con 2 semanas de anticipación |

---

## 4.6. Comparativa Fase 0: V2.02 vs V2.04

| Métrica | V2.02 | V2.04 | Cambio |
|---------|-------|-------|--------|
| **Duración** | 6 semanas | 6 semanas | Sin cambio |
| **Esfuerzo** | 235h | 328h | +93h (+40%) |
| **Consultor BI** | 95h | 104h | +9h |
| **ABAP Developer** | 0h | **70h** | **+70h (NUEVO)** |
| **Funcional SAP** | 112h | 122h | +10h |
| **Project Manager** | 28h | 32h | +4h |

**Justificación del incremento:**
- +70h ABAP Developer para análisis Z-transactions y configuración SLT
- +9h Consultor BI para arquitectura 3 capas detallada
- +10h Funcional SAP para coordinación con ABAP Developer
- **Beneficio:** Menor riesgo técnico en Fase 1, Z-transactions bien entendidas, SLT operacional

---

## 4.7. Entregables Clave de Fase 0

### Documentos Técnicos
1. ✅ Arquitectura BigQuery 3 capas (RAW/PROCESSED/CURATED)
2. ✅ **Especificación técnica ZLEL008 (Inventario MRP consolidado)**
3. ✅ **Especificación técnica ZVEL015 (Pricing)**
4. ✅ **Manual de configuración SAP SLT**
5. ✅ Listado de 32-38 tablas SAP con volumetría

### Documentos Funcionales
6. ✅ Backlog priorizado de 18 transacciones SAP
7. ✅ Matriz de scoring de transacciones
8. ✅ Validación funcional del POC

### Documentos de Planificación
9. ✅ Plan detallado de Fase 1 (20 semanas, 852h)
10. ✅ Plan detallado de Fase 2 (10 semanas, 700h)
11. ✅ Acta de reunión Go/No-Go

---

**Próxima fase:** [05_FASE_1_CONSTRUCCION_DATA_LAKE_V2_04.md](05_FASE_1_CONSTRUCCION_DATA_LAKE_V2_04.md)

**Documento anterior:** [03_TRANSACCIONES_SAP_INCLUIDAS.md](03_TRANSACCIONES_SAP_INCLUIDAS.md)

---

*Versión 2.04 - Fecha: 10 de noviembre de 2025*  
*Cambios principales vs V2.02: +ABAP Developer (70h), análisis Z-transactions, configuración SLT*
