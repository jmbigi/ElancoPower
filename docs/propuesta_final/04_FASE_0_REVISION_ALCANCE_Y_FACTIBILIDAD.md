# 4. FASE 0 - REVISIÓN DEL ALCANCE Y FACTIBILIDAD

## 4.1. Objetivo de la Fase

**Validar la viabilidad técnica del proyecto** y resolver los issues identificados por TI antes de iniciar el desarrollo. Esta fase es **crítica** para asegurar que Fase 1 pueda ejecutarse sin bloqueos.

### Objetivos Específicos

1. ✅ Resolver **Issue #1:** Permisos SAP completos para power user
2. ✅ Resolver **Issue #2:** Disponibilidad de tablas SAP en BigQuery
3. ✅ Validar **Issue #3:** Capacidades reales de BigQuery vs. limitaciones reportadas
4. ✅ Priorizar definitivamente las 18 transacciones SAP
5. ✅ Elaborar plan técnico detallado para Fase 1

---

## 4.2. Duración y Recursos

| Parámetro | Valor |
|-----------|-------|
| **Duración estimada** | 4-5 semanas |
| **Fecha inicio** | 1 de diciembre de 2025 |
| **Fecha fin** | 15 de diciembre de 2025 |
| **Horas totales** | 80 horas |
| **Equipo** | Lucía Rodríguez (28h) + Juan Manuel Bigi (40h) + Stakeholders Elanco (12h) |

---

## 4.3. Actividades Detalladas

### 4.3.1. Gestión de Permisos SAP y Tickets BigQuery

**Responsable:** Lucía Rodríguez  
**Duración:** 20 horas  
**Semanas:** 1-4 (continuo)

#### Tareas

| # | Actividad | Horas | Entregable |
|---|-----------|-------|------------|
| 1 | Seguimiento Ticket SAP-48219 (permisos MM/SD/FI/CO) | 8h | Confirmación de permisos completos |
| 2 | Seguimiento Tickets BQ-7713 y BQ-7721 (tablas BigQuery) | 8h | Confirmación de tablas disponibles |
| 3 | Coordinación con TI Global y David Saboya | 4h | Minutas de reuniones |

#### Resultados Esperados

✅ **Permisos SAP:** Power user con acceso completo a:
- Módulo MM (Materials Management)
- Módulo SD (Sales & Distribution)
- Módulo FI (Financial Accounting)
- Módulo CO (Controlling)
- Autorización para exportación masiva de datos

✅ **Tablas BigQuery:** Disponibles en dataset CASA:
- Tablas custom (ZLEL008, ZVEL015)
- Tablas CO-PA (CE1*, CE4* para KE24)
- Tabla FAGLFLEXA (mayor general)
- Validación de tablas estándar (VBAK, EKKO, BKPF, etc.)

#### Criterio Go/No-Go

⛔ **Bloqueante:** Si no se obtienen permisos SAP completos, Fase 1 NO puede iniciar.

⚠️ **Riesgo moderado:** Si faltan <6 tablas BigQuery, se puede iniciar Fase 1 con workarounds.

---

### 4.3.2. Análisis Técnico de Arquitectura BigQuery

**Responsable:** Juan Manuel Bigi  
**Duración:** 24 horas  
**Semanas:** 1-2

#### Tareas

| # | Actividad | Horas | Entregable |
|---|-----------|-------|------------|
| 1 | Análisis de dataset CASA en BigQuery | 8h | Inventario de tablas disponibles |
| 2 | Evaluación de performance con volúmenes reales | 6h | Benchmarks de queries |
| 3 | Validación de conectividad Power BI ↔ BigQuery | 4h | Prueba de concepto funcional |
| 4 | Análisis de costos BigQuery proyectados | 4h | Estimación de costos mensual |
| 5 | Documentación de hallazgos técnicos | 2h | Reporte de viabilidad técnica |

#### Análisis Específicos

**1. Inventario de Tablas SAP en BigQuery**

Verificar disponibilidad de tablas para cada transacción:

| Transacción | Tablas Requeridas | Estado | Ticket |
|-------------|-------------------|--------|--------|
| VA05 | VBAK, VBAP, VBEP | ⏳ Por validar | - |
| ZLEL008 | Z-tables (TBD) | ❌ No disponible | BQ-7713 |
| KSB1 | COBK, COEP, AUFK | ⏳ Por validar | - |
| FAGLL03 | FAGLFLEXA, BKPF, BSEG | ⚠️ Parcial | BQ-7721 |
| KE24 | CE1*, CE4* | ❌ No disponible | BQ-7713 |
| ... | ... | ... | ... |

**2. Benchmarks de Performance**

Ejecutar queries representativos:
- Query de agregación simple: < 2 segundos
- Query con JOINs múltiples: < 10 segundos
- Query de histórico completo (24 meses): < 30 segundos

**3. Estimación de Costos**

Calcular costo mensual de:
- Almacenamiento (Active + Long-term storage)
- Procesamiento (Query processing)
- Streaming inserts (si aplica)

**Meta:** < USD $500/mes en costos BigQuery

---

### 4.3.3. Workshop de Priorización de Transacciones

**Responsables:** Lucía Rodríguez + Juan Manuel Bigi + Stakeholders Elanco  
**Duración:** 12 horas (equipo técnico) + 12 horas (stakeholders)  
**Semana:** 2

#### Estructura del Workshop

**Sesión 1: Finanzas (4 horas)**
- Participantes: Controller, Analistas Finanzas, Lucía, JMB
- Objetivo: Priorizar transacciones FI/CO
- Transacciones a revisar: FAGLL03, KSB1, KE24, FB03, F.08, F.01, FBL1N, FBL5N

**Sesión 2: Supply Chain (4 horas)**
- Participantes: Supply Manager, Planeadores, Lucía, JMB
- Objetivo: Priorizar transacciones MM/SD
- Transacciones a revisar: VA05, ZLEL008, ME2L, MM60, MB59, ME23N, MB5B

**Sesión 3: Consolidación (4 horas)**
- Participantes: Todos + Management
- Objetivo: Consensuar priorización final
- Entregable: Backlog definitivo aprobado

#### Metodología de Priorización

**Matriz de Scoring (1-5 por criterio):**

| Transacción | Impacto Negocio (40%) | Frecuencia Uso (25%) | Complejidad (20%) | Dependencias (15%) | Score Final |
|-------------|-----------------------|----------------------|-------------------|--------------------|-------------|
| VA05 | 5 | 5 | 3 | 4 | 4.45 |
| ZLEL008 | 5 | 4 | 1 | 5 | 4.05 |
| ... | ... | ... | ... | ... | ... |

**Clasificación:**
- Score ≥ 4.0: **Prioridad 1** (implementar primero en Fase 1)
- Score 3.0-3.9: **Prioridad 2** (implementar después si hay tiempo)
- Score < 3.0: **Prioridad 3** (postergar a fase futura)

---

### 4.3.4. Análisis de Transacciones Custom (Z)

**Responsable:** Lucía Rodríguez + Consultor ABAP (si necesario)  
**Duración:** 8 horas  
**Semana:** 2-3

#### Transacciones a Analizar

**ZLEL008 - Inventario Consolidado**
- Acceder al código ABAP (SE38 o SE80)
- Identificar tablas fuente que consulta
- Documentar lógica de cálculo/agregación
- Mapear campos de salida a tablas SAP estándar

**ZVEL015 - Condiciones de Precio**
- Mismo análisis que ZLEL008
- Identificar si usa tablas estándar (KONV, A-tables) o custom

#### Contingencia

Si el análisis requiere conocimientos ABAP especializados:
- Contratar consultor ABAP externo: 8-16 horas
- Costo: USD $640-$1,600 (incluido en contingencias)

---

### 4.3.5. Definición de Requisitos Técnicos Iniciales

**Responsable:** Juan Manuel Bigi  
**Duración:** 16 horas  
**Semana:** 2-3

#### Tareas

| # | Actividad | Horas | Entregable |
|---|-----------|-------|------------|
| 1 | Documentación de backlog técnico | 4h | User stories técnicos |
| 2 | Plan de extracción por módulo SAP | 4h | Roadmap de implementación |
| 3 | Definición de arquitectura de zonas (RAW/PROCESSED/CURATED) | 4h | Diagrama de arquitectura |
| 4 | Definición de criterios de calidad de datos | 2h | Catálogo de validaciones |
| 5 | Estimación de esfuerzos por transacción | 2h | Matriz de estimación |

#### Plan de Extracción por Módulo

**Orden propuesto de implementación en Fase 1:**

**Sprint 1-2 (Semanas 1-4):** Módulo FI - Financial Accounting
- FAGLL03 (mayor general)
- FB03 (documentos contables)
- F.08 (balance comprobación)
- F.01 (balance general)

**Sprint 3-4 (Semanas 5-8):** Módulo SD - Sales & Distribution
- VA05 (órdenes abiertas)

**Sprint 5-6 (Semanas 9-12):** Módulo MM - Materials Management
- ZLEL008 (inventario consolidado - custom)
- ME2L (purchase orders)
- MB5B (stock materiales)

**Sprint 7 (Semanas 13-14):** Módulo CO - Controlling
- KSB1 (OPEX / órdenes CO)
- KE24 (CO-PA rentabilidad)

**Sprint 8 (Reserva):** Ajustes y transacciones adicionales

---

### 4.3.6. Elaboración de Plan de Riesgos y Mitigaciones

**Responsable:** Lucía Rodríguez + Juan Manuel Bigi  
**Duración:** 8 horas  
**Semana:** 3

#### Riesgos Identificados (Ver detalle en sección 11)

**Top 5 Riesgos:**

1. **Tablas no disponibles en BigQuery** (Probabilidad: Alta, Impacto: Alto)
2. **Limitaciones reales de BigQuery** (Probabilidad: Media, Impacto: Alto)
3. **Permisos SAP insuficientes** (Probabilidad: Media, Impacto: Alto)
4. **Complejidad de transacciones custom** (Probabilidad: Media, Impacto: Medio)
5. **Cambios de alcance** (Probabilidad: Media, Impacto: Medio)

Cada riesgo incluye:
- Descripción detallada
- Probabilidad e impacto
- Plan de mitigación
- Plan de contingencia
- Responsable de monitoreo

---

### 4.3.7. Reunión Go/No-Go para Fase 1

**Responsables:** Linda López + Stakeholders Elanco  
**Duración:** 2 horas  
**Fecha:** 7 de diciembre de 2025 (Semana 4)

#### Criterios de Decisión Go/No-Go

**Criterios OBLIGATORIOS (Go solo si TODOS se cumplen):**

| # | Criterio | Estado | Responsable Validación |
|---|----------|--------|----------------------|
| 1 | ✅ Permisos SAP completos confirmados | ⏳ | TI Global |
| 2 | ✅ Mínimo 12 de 18 transacciones con tablas disponibles en BigQuery | ⏳ | TI Global |
| 3 | ✅ Accesos Data Editor activos para equipo desarrollo | ⏳ | TI Elanco |
| 4 | ✅ Backlog priorizado y aprobado por stakeholders | ⏳ | Finanzas/Supply |
| 5 | ✅ BigQuery validado técnicamente (performance OK, sin limitaciones bloqueantes) | ⏳ | Juan Manuel Bigi |

**Decisiones Posibles:**

**✅ GO - Continuar con Fase 1**
- Todos los criterios obligatorios cumplidos
- Iniciar Fase 1 la siguiente semana

**⏸️ GO CONDICIONADO - Continuar con plan B**
- 1-2 criterios NO cumplidos pero con workaround definido
- Ejemplo: Solo 10 transacciones disponibles → iniciar con esas 10
- Iniciar Fase 1 con alcance ajustado

**❌ NO-GO - Replantear proyecto**
- 3+ criterios NO cumplidos
- Evaluación de alternativas:
  - Migrar a Azure Data Lake
  - Extracción RFC directa sin BigQuery
  - Replantear alcance completo

---

## 4.4. Entregables de Fase 0

### 4.4.1. Documentos Formales

| # | Entregable | Páginas | Responsable |
|---|------------|---------|-------------|
| 1 | **Backlog Definitivo de Transacciones SAP Priorizado** | 10-15 | Lucía + JMB |
| 2 | **Arquitectura Técnica SAP → BigQuery → Power BI Aprobada** | 15-20 | JMB |
| 3 | **Checklist de Permisos Completo** (SAP + BigQuery) | 3-5 | Lucía |
| 4 | **Plan de Extracción por Módulo** (MM, SD, FI, CO) | 8-10 | JMB |
| 5 | **Matriz de Riesgos Actualizada** | 10-12 | Lucía + JMB |
| 6 | **Criterios de Calidad de Datos Definidos** | 5-8 | JMB |
| 7 | **Documento Go/No-Go para Fase 1** | 5-7 | Linda + Stakeholders |
| 8 | **Plan Técnico Detallado Fase 1** (cronograma semanal) | 12-15 | JMB |

### 4.4.2. Artefactos Técnicos

- Inventario de tablas BigQuery (Excel/CSV)
- Benchmarks de performance (resultados de queries)
- Prueba de concepto Power BI ↔ BigQuery (archivo .pbix)
- Scripts SQL de validación (repositorio Git)
- Análisis de transacciones custom (documentos técnicos)

### 4.4.3. Presentaciones

- Presentación de hallazgos técnicos (PPT - 20 slides)
- Presentación Go/No-Go (PPT - 15 slides)
- Dashboard de seguimiento de Fase 0 (Excel/Power BI)

---

## 4.5. Cronograma Semanal de Fase 0

### Semana 1 (11-17 nov 2025): Kick-off y Análisis Inicial

| Día | Actividad | Responsable | Horas |
|-----|-----------|-------------|-------|
| Lun | Kick-off meeting con stakeholders | Linda + Todos | 2h |
| Lun-Mar | Análisis dataset CASA BigQuery | JMB | 8h |
| Mar-Mie | Seguimiento tickets SAP/BigQuery | Lucía | 4h |
| Mie-Jue | Prueba conectividad Power BI | JMB | 4h |
| Vie | Preparación workshop priorización | Lucía + JMB | 4h |

**Hito:** Hallazgos técnicos preliminares

---

### Semana 2 (18-24 nov 2025): Workshops y Validación

| Día | Actividad | Responsable | Horas |
|-----|-----------|-------------|-------|
| Lun | Workshop Finanzas (4h) | Todos | 4h + 4h stakeholders |
| Mar | Workshop Supply (4h) | Todos | 4h + 4h stakeholders |
| Mie | Análisis transacciones custom | Lucía | 4h |
| Jue | Benchmarks performance BigQuery | JMB | 6h |
| Vie | Workshop consolidación (4h) | Todos | 4h + 4h stakeholders |

**Hito:** Backlog priorizado aprobado

---

### Semana 3 (25 nov - 1 dic 2025): Planificación Detallada

| Día | Actividad | Responsable | Horas |
|-----|-----------|-------------|-------|
| Lun | Plan extracción por módulo | JMB | 4h |
| Mar | Definición arquitectura zonas datos | JMB | 4h |
| Mie | Análisis de riesgos | Lucía + JMB | 4h |
| Jue | Estimación esfuerzos Fase 1 | JMB | 4h |
| Vie | Seguimiento tickets críticos | Lucía | 4h |

**Hito:** Plan técnico Fase 1 completo

---

### Semana 4 (2-8 dic 2025): Cierre y Go/No-Go

| Día | Actividad | Responsable | Horas |
|-----|-----------|-------------|-------|
| Lun | Documentación entregables Fase 0 | JMB | 6h |
| Mar | Revisión interna documentos | Linda + Lucía + JMB | 4h |
| Mie | Preparación presentación Go/No-Go | Linda + JMB | 4h |
| Jue | Reunión Go/No-Go (2h) | Todos + Stakeholders | 2h |
| Vie | Ajustes post Go/No-Go | JMB | 4h |

**Hito:** Decisión Go/No-Go documentada

### Presupuesto de Fase 0

#### Desglose de Horas

| Recurso | Horas |
|---------|-------|
| **Juan Manuel Bigi** | 40h |
| **Lucía Rodríguez** | 28h |
| **Linda López (PM)** | 8h |
| **Stakeholders Elanco** | 12h (sin costo) |
| **TOTAL FASE 0** | **76h** |

## 4.7. Criterios de Éxito de Fase 0

✅ **Fase 0 se considera exitosa si:**

1. Se emite decisión **Go/No-Go documentada** basada en criterios objetivos
2. Si es Go: Plan técnico Fase 1 completo y aprobado
3. Backlog de transacciones priorizado y consensuado
4. Issues de permisos/tablas resueltos (o plan B definido)
5. Riesgos identificados y mitigaciones planificadas
6. Presupuesto y cronograma Fase 1 validados

---

*Siguiente sección: [05_FASE_1_CONSTRUCCION_DATA_LAKE.md](05_FASE_1_CONSTRUCCION_DATA_LAKE.md)*
