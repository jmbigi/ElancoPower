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
| **Duración estimada** | 6 semanas (Semanas 1–6 del proyecto) |
| **Fechas** | Ver cronograma unificado en `09_CRONOGRAMA_SEMANAL.md` |
| **Horas totales** | 235 horas |
| **Equipo** | Consultor BI (95h) · Funcional SAP (112h) · Project Manager (28h) · Stakeholders Elanco (12h, sin costo) |

---

## 4.3. Actividades Detalladas

### 4.3.1. Gestión de Permisos SAP y Tickets BigQuery

**Responsable:** Funcional SAP  
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

✅ **Tablas BigQuery:** Disponibles en dataset casa_bi:
- Tablas custom (ZLEL008, ZVEL015)
- Tablas CO-PA (CE1*, CE4* para KE24)
- Tabla FAGLFLEXA (mayor general)
- Validación de tablas estándar (VBAK, EKKO, BKPF, etc.)

#### Criterio Go/No-Go

⛔ **Bloqueante:** Si no se obtienen permisos SAP completos, Fase 1 NO puede iniciar.

⚠️ **Riesgo moderado:** Si faltan <6 tablas BigQuery, se puede iniciar Fase 1 con workarounds.

---

### 4.3.2. Análisis Técnico de Arquitectura BigQuery

**Responsable:** Consultor BI  
**Duración:** 24 horas  
**Semanas:** 1-2

#### Tareas

| # | Actividad | Horas | Entregable |
|---|-----------|-------|------------|
| 1 | Análisis de dataset casa_bi en BigQuery | 8h | Inventario de tablas disponibles |
| 2 | Evaluación de performance con volúmenes reales | 6h | Benchmarks de queries |
| 3 | Validación de conectividad Power BI ↔ BigQuery | 4h | Prueba de concepto funcional |
| 4 | Análisis de costos BigQuery proyectados | 4h | Estimación de costos mensual |
| 5 | Documentación de hallazgos técnicos | 2h | Reporte de viabilidad técnica |

#### Análisis Específicos

**1. Inventario de Tablas SAP en BigQuery**

Verificar disponibilidad de tablas para cada transacción:

| Transacción | Tablas Requeridas | Estado | Ticket |
|-------------|-------------------|--------|--------|
| VA05 | VBAK, VBAP, (VBEP condicional) | ⏳ Por validar | - |
| ZLEL008 | Z-tables (TBD) | ❌ No disponible | BQ-7713 |
| KSB1 | (COEP reemplazada por ACDOCA), AUFK, CSKS | ⏳ Por validar | - |
| FAGLL03 | (FAGLFLEXA/BSEG reemplazadas por ACDOCA/ACDOCA_T), BKPF | ⚠️ Parcial | BQ-7721 |
| KE24 | CE1*, CE4* (si Costing-Based) | ❌ No disponible | BQ-7713 |
| ... | ... | ... | ... |

**Nota S/4HANA:** En S/4HANA el detalle contable consolidado se gestiona en **ACDOCA/ACDOCA_T**, que sustituyen a tablas clásicas como **BSEG**, **COEP** y **FAGLFLEXA**. Las menciones a estas estructuras históricas en este documento son referenciales para trazabilidad funcional; la replicación y el modelado del MVP se basarán en ACDOCA/ACDOCA_T y, cuando aplique, en vistas derivadas para **BSID/BSAD/BSIK/BSAK**.

**2. Benchmarks de Performance**

Ejecutar queries representativos:
- Query de agregación simple: < 2 segundos y ≤ 200 MB escaneados
- Query con JOINs múltiples: < 10 segundos y ≤ 2 GB escaneados
- Query de histórico completo (24 meses): < 30 segundos y ≤ 10 GB escaneados

Si se exceden los umbrales de bytes escaneados:
1. Revisar particionamiento por fecha contable y aplicar clustering (company_code, material, país según corresponda).
2. Evaluar creación de vista materializada para agregaciones recurrentes.
3. Ajustar filtros y proyecciones de columnas (evitar SELECT * en tablas de gran volumen).

**3. Estimación de Costos**

Calcular costo mensual de:
- Almacenamiento (Active + Long-term storage)
- Procesamiento (Query processing)
- Streaming inserts (si aplica)

**Meta:** Costos BigQuery manejables según presupuesto de Elanco

---

### 4.3.3. Workshop de Priorización de Transacciones

**Responsables:** Funcional SAP + Consultor BI + Stakeholders Elanco  
**Duración:** 12 horas (equipo técnico) + 12 horas (stakeholders)  
**Semana:** 2

#### Estructura del Workshop

**Sesión 1: Finanzas (4 horas)**
- Participantes: Controller, Analistas Finanzas, Funcional SAP, Consultor BI
- Objetivo: Priorizar transacciones FI/CO
- Transacciones a revisar: FAGLL03, KSB1, KE24, FB03, F.08, F.01, FBL1N, FBL5N

**Sesión 2: Supply Chain (4 horas)**
- Participantes: Supply Manager, Planeadores, Funcional SAP, Consultor BI
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

**Responsable:** Funcional SAP + Consultor ABAP (si necesario)  
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
- Contratar consultor ABAP externo: 8-16 horas (incluido en contingencias)

---

### 4.3.5. Definición de Requisitos Técnicos Iniciales

**Responsable:** Consultor BI  
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

**Responsable:** Funcional SAP + Consultor BI  
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

**Responsables:** Project Manager + Stakeholders Elanco  
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
| 5 | ✅ BigQuery validado técnicamente (performance OK, sin limitaciones bloqueantes) | ⏳ | Consultor BI |

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
| 1 | **Backlog Definitivo de Transacciones SAP Priorizado** | 10-15 | Funcional SAP + Consultor BI |
| 2 | **Arquitectura Técnica SAP → BigQuery → Power BI Aprobada** | 15-20 | Consultor BI |
| 3 | **Checklist de Permisos Completo** (SAP + BigQuery) | 3-5 | Funcional SAP |
| 4 | **Plan de Extracción por Módulo** (MM, SD, FI, CO) | 8-10 | Consultor BI |
| 5 | **Matriz de Riesgos Actualizada** | 10-12 | Funcional SAP + Consultor BI |
| 6 | **Criterios de Calidad de Datos Definidos** | 5-8 | Consultor BI |
| 7 | **Documento Go/No-Go para Fase 1** | 5-7 | Project Manager + Stakeholders |
| 8 | **Plan Técnico Detallado Fase 1** (cronograma semanal) | 12-15 | Consultor BI |

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

### Semana 1 (6-12 ene 2026): Kick-off y Análisis Inicial

| Día | Actividad | Responsable | Horas |
|-----|-----------|-------------|-------|
| Lun | Kick-off meeting con stakeholders | Project Manager + Todos | 2h |
| Lun-Mar | Análisis dataset casa_bi BigQuery | Consultor BI | 8h |
| Mar-Mie | Seguimiento tickets SAP/BigQuery | Funcional SAP | 4h |
| Mie-Jue | Prueba conectividad Power BI | Consultor BI | 4h |
| Vie | Preparación workshop priorización | Funcional SAP + Consultor BI | 4h |

**Hito:** Hallazgos técnicos preliminares

---

### Semana 2 (13-19 ene 2026): Workshops y Validación

| Día | Actividad | Responsable | Horas |
|-----|-----------|-------------|-------|
| Lun | Workshop Finanzas (4h) | Todos | 4h + 4h stakeholders |
| Mar | Workshop Supply (4h) | Todos | 4h + 4h stakeholders |
| Mie | Análisis transacciones custom | Funcional SAP | 4h |
| Jue | Benchmarks performance BigQuery | Consultor BI | 6h |
| Vie | Workshop consolidación (4h) | Todos | 4h + 4h stakeholders |

**Hito:** Backlog priorizado aprobado

---

### Semana 3 (20 al 26 ene 2026): Planificación Detallada

| Día | Actividad | Responsable | Horas |
|-----|-----------|-------------|-------|
| Lun | Plan extracción por módulo | Consultor BI | 4h |
| Mar | Definición arquitectura zonas datos | Consultor BI | 4h |
| Mie | Análisis de riesgos | Funcional SAP + Consultor BI | 4h |
| Jue | Estimación esfuerzos Fase 1 | Consultor BI | 4h |
| Vie | Seguimiento tickets críticos | Funcional SAP | 4h |

**Hito:** Plan técnico Fase 1 completo

---

### Semana 4-5 (27 ene - 9 feb 2026): Preparación de Cierre y Go/No-Go

| Día | Actividad | Responsable | Horas |
|-----|-----------|-------------|-------|
| Mar | Revisión interna documentos | Project Manager + Funcional SAP + Consultor BI | 4h |
| Mie | Preparación presentación Go/No-Go | Project Manager + Consultor BI | 4h |
| Jue | Reunión Go/No-Go (2h) | Todos + Stakeholders | 2h |
| Vie | Ajustes post Go/No-Go | Consultor BI | 4h |

**Hito:** Decisión Go/No-Go documentada (10-feb-2026)

### Presupuesto de Fase 0 (consolidado oficial)

#### Desglose de Horas

| Recurso | Horas |
|---------|-------|
| **Consultor BI** | 95h |
| **Funcional SAP** | 112h |
| **Project Manager (PM)** | 28h |
| **Stakeholders Elanco** | 12h (sin costo) |
| **TOTAL FASE 0** | **235h** |

Nota: El detalle semanal de esta sección es orientativo. Para planificación detallada y fechas, prevalecen `08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md` y `CRONOGRAMA_DETALLADO_TAREAS.csv`.

## 4.6. Supuestos y Requisitos Específicos de Fase 0

Esta sección consolida los **supuestos y requisitos operativos críticos** que deben verificarse durante Fase 0 para habilitar el inicio de la Fase 1 sin bloqueos. Complementa y referencia las secciones `10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md` y `11_RIESGOS_Y_SUPUESTOS.md`.

### Mini-Checklist "Go Readiness" (Seguimiento Semanal)

- [ ] SLT operativo (1 tabla estándar replicada sin errores)
- [ ] Conectividad SAP → SLT → BigQuery validada (latencia < 100ms)
- [ ] Accesos BigQuery (Data Editor / Viewer / Admin) activos
- [ ] Datasets dev/qa/prod creados y etiquetados (env, area)
- [ ] ≥ 12 transacciones con tablas base disponibles o plan alternativo documentado
- [ ] Exportación masiva SAP sin límites (autorizaciones confirmadas)

### 4.6.1. Requisitos Técnicos Operativos (Semana 1–2)

| # | Requisito / Condición | Descripción de Verificación | Responsable | Estado Inicial |
|---|-----------------------|-----------------------------|-------------|----------------|
| 1 | **SLT Configurado y Operativo** | SAP SLT (Landscape Transformation Server) instalado, conectado a SAP S/4 y con al menos 1 tabla estándar replicada de prueba (log de replicación sin errores). | TI Global Elanco / SAP Basis | ⏳ |
| 2 | **Conectividad SAP → SLT → BigQuery** | Prueba de extremo a extremo: latencia < 100 ms; puertos RFC abiertos; certificados vigentes; credenciales de service account funcionales. | TI Global + TechOps | ⏳ |
| 3 | **Permisos BigQuery Equipo Proyecto** | Roles asignados: Data Editor (Funcional SAP, Consultor BI), Viewer (PM, Stakeholders), Admin (TechOps). Service account con permisos BigQuery Job User + Data Editor. | TI Elanco | ⏳ |
| 4 | **Infraestructura BigQuery Proveída** | Proyecto GCP aprobado, datasets `casa_bi_dev`, `casa_bi_qa`, `casa_bi_prod` creados, política de acceso aplicada. | TI Global Elanco | ⏳ |
| 5 | **Tablas SAP Prioritarias en Proceso de Replicación** | Solicitudes de replicación para tablas críticas (ACDOCA/ACDOCA_T, CE1*/CE4*, COBK, VBAK/VBAP, Z-tables) registradas y/o en ejecución. | TI Global / SAP Basis | ⏳ |
| 6 | **Exportación Masiva SAP Autorizada** | Perfil con autorizaciones S_TABU_DIS / S_TABU_RFC y sin límites restrictivos de volumen en extracción. | SAP Basis / TI Global | ⏳ |

#### RACI de Requisitos Técnicos Operativos

| Requisito | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|-----------|-----------------|-----------------|--------------|--------------|
| SLT Configurado y Operativo | SAP Basis | TI Global | Consultor BI | Project Manager |
| Conectividad SAP → SLT → BigQuery | TechOps | TI Global | SAP Basis | Stakeholders |
| Permisos BigQuery Equipo Proyecto | TI Elanco | TI Global | Consultor BI | Project Manager |
| Infraestructura BigQuery Proveída | TI Global | TI Global | Consultor BI | Aunergia Equipo |
| Tablas SAP Prioritarias Replicación | SAP Basis | TI Global | Funcional SAP | Project Manager |
| Exportación Masiva SAP Autorizada | SAP Basis | TI Global | Funcional SAP | Stakeholders |

### 4.6.2. Supuestos Financieros y de Licenciamiento

| Código | Supuesto | Alcance | Referencia |
|--------|----------|---------|------------|
| S-F-01 | **Costos de infraestructura no incluidos** | Almacenamiento y procesamiento BigQuery, licencias SLT y operación de conectores asumidos 100% por Elanco. | 11 (S-P-01) |
| S-F-02 | **Cliente provee herramientas y licencias** | SAP SLT, BigQuery Connector, cuentas GCP, licencias Power BI Pro ya disponibles antes de Fase 1. | 10.3 / 10.2 / 11 (nuevo) |
| S-F-03 | **Sin adquisición de software adicional** | No se requiere compra de herramientas de terceros (ETL externas, BI alternativo) para ejecutar el alcance comprometido. | 11 (S-P-04) |

### 4.6.3. Dependencias Críticas y Impacto Go/No-Go

| Dependencia | Fecha Límite Recomendada | Impacto si NO se cumple | Decisión Potencial |
|-------------|--------------------------|-------------------------|--------------------|
| SLT operativo (Requisito #1) | Fin Semana 2 | Imposibilidad de flujo de replicación; se evalúa extracción alternativa RFC (mayor esfuerzo). | ⚠️ Go Condicionado / Replanificar |
| Permisos BigQuery (Requisito #3) | Fin Semana 2 | Bloqueo en validaciones técnicas y backlog técnico; retraso ≥ 1 semana. | ⚠️ Go Condicionado |
| Infraestructura BigQuery (Requisito #4) | Semana 1 | No se puede ejecutar inventario ni benchmarks. | ⛔ No-Go temporal |
| Replicación tablas críticas (#5) ≥ 12 transacciones | Semana 3 | Alcance reducido y/o re-plan (ver criterios sección 11.9). | ⚠️ Go Ajustado /
| Exportación masiva SAP (#6) | Semana 3 | Retrasos en obtención de datasets históricos; riesgo de calidad. | ⚠️ Go Condicionado |

### 4.6.4. Validación y Evidencias

Durante Fase 0 se generarán evidencias mínimas para cada requisito:
1. Captura de pantalla de consola SLT con estado de replicación OK.
2. Log de prueba de conectividad (ping/trazado o reporte técnico interno) y latencia medida.
3. Listado de roles BigQuery asignados (export IAM / captura). 
4. Inventario de datasets y estructura inicial (`SHOW SCHEMAS` / exportación). 
5. Matriz de tablas solicitadas vs. status (archivo compartido en repositorio). 
6. Checklist de autorizaciones SAP firmado por SAP Basis.

### 4.6.5. Escenario de Contingencia (Resumen)

| Escenario | Acción Inmediata | Mitigación | Implicación Cronograma |
|-----------|------------------|------------|------------------------|
| SLT no operativo Semana 3 | Activar Plan B (extracción batch RFC) | Limitar alcance a TOP 10 transacciones | +1 a +2 semanas |
| <12 transacciones disponibles | Definir subset mínimo viable | Repriorizar backlog y documentar alcance reducido | Sin cambio si ≥10; +1 semana si <10 |
| Costos BigQuery superiores | Optimizar particiones / clustering | Monitoreo y ajuste de queries | Sin impacto técnico inicial |

### 4.6.6. Resumen Ejecutivo (Fase 0)

Para declarar Fase 0 exitosa se espera:
1. SLT probado y estable (flujo replicación base).
2. Accesos BigQuery completos (Data Editor / Viewer / Admin).
3. Infraestructura GCP con datasets listos y service account funcional.
4. Mínimo 12 transacciones con tablas base confirmadas o plan alternativo documentado.
5. Confirmación formal de que los costos de infraestructura y licencias son asumidos por Elanco.

Si alguno de los puntos 1–4 no se cumple, se activa evaluación Go/No-Go ajustada (ver 11.9).

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
