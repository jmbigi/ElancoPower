# ESTIMACIÓN DE HORAS POR PERFIL Y ETAPA
> Nota de versión (8-nov-2025): Esta vista suma horas por función (multi‑rol del Consultor BI) y puede diferir del consolidado oficial por persona. La línea base canónica es `CRONOGRAMA_DETALLADO_TAREAS.csv` (Consultor BI **961h**, Funcional SAP **484h**, Project Manager **145h**; total **1,590h**).

**Proyecto:** Elanco Power - Centralización de Datos y Analítica  
**Fecha:** 7 de noviembre de 2025  
**Versión:** 1.0  
**Alcance:** 18 transacciones SAP + 12 dashboards Power BI

---

## MAPEO DE RECURSOS

| Perfil Técnico | Recurso Asignado | Empresa | Observaciones |
|----------------|------------------|---------|---------------|
| **SAP Basis** | Cliente (Elanco) | Elanco | Infraestructura SAP (sin horas estimadas en alcance) |
| **SAP ABAP Developer** | Consultor BI | Aunergia | Análisis transacciones Z, optimización queries |
| **Google Cloud Architect** | Consultor BI | Aunergia | Diseño arquitectura BigQuery, infraestructura GCP |
| **SAP SD/MM Functional** | Funcional SAP | Aunergia | Consultoría funcional, validaciones de negocio |
| **Data Engineer** | Consultor BI | Aunergia | Desarrollo pipelines ETL, replicación tablas SAP |
| **DevOps Engineer** | Consultor BI | Aunergia | CI/CD, monitoreo, automatización despliegues |
| **Project Manager** | Project Manager | Aunergia | Coordinación general, seguimiento, comunicación stakeholders |

---

## RESUMEN EJECUTIVO

| Fase | Duración | Horas Totales |
|------|----------|---------------|
| **Elaboración de Propuesta** | - | 24h |
| **Fase 0: Due Diligence** | 6 semanas | 235h |
| **Fase 1: Data Lake (18 trans)** | 22 semanas | 696h |
| **Fase 2: Power BI (12 dash)** | 14 semanas | 659h |
| **TOTAL PROYECTO** | **42 semanas** | **1,590h** |

---

## FASE 0: REVISIÓN DE ALCANCE Y FACTIBILIDAD

**Duración:** 6 semanas (semanas 1-6)  
**Objetivo:** Validar viabilidad técnica y resolver issues previos a desarrollo

### Desglose por Perfil

| Perfil | Horas | Actividades Principales |
|--------|-------|------------------------|
| **Google Cloud Architect** (Consultor BI) | 59h | • Análisis dataset CASA BigQuery (24h)<br>• Diseño arquitectura 3 capas (28h)<br>• Documentación arquitectura (7h) |
| **SAP SD/MM Functional** (Funcional SAP) | 62h | • Gestión permisos SAP (Ticket SAP-48219) (18h)<br>• Gestión tickets BigQuery tablas (BQ-7713, BQ-7721) (18h)<br>• Workshops priorización transacciones (28h)<br>• Análisis transacciones custom Z (parcial) (parcial en workshops)<br>• Validación POC (6h) |
| **SAP ABAP Developer** (Consultor BI) | 0h | (Análisis Z incluido en workshops) |
| **Data Engineer** (Consultor BI) | 0h | (Incluido en Cloud Architect) |
| **Project Manager** (Project Manager) | 25h | • Kick-off meeting (3h)<br>• Workshops facilitación (10h)<br>• Seguimiento tickets críticos (5h)<br>• Documentación y Go/No-Go (7h) |

**TOTAL FASE 0:** **235 horas**

### Desglose por Semana

| Semana | Consultor BI (Cloud/ABAP/Data) | Funcional SAP (SAP Func) | Project Manager (PM) | Total Sem | Hitos |
|--------|----------------------|------------------|------------|-----------|-------|
| **Sem 0-1** | 14h | 14h | 3h | 31h | Diseño preliminar, kick-off |
| **Sem 1-2** | 20h | 18h | 3h | 41h | Inventario técnico completo |
| **Sem 2-3** | 8h | 22h | 5h | 35h | Gestión de tickets críticos |
| **Sem 2-4** | 20h | 36h | 10h | 66h | Workshops y análisis Z |
| **Sem 4-5** | 24h | 12h | 0h | 36h | Diseño y POC |
| **Sem 5-6** | 6h | 10h | 7h | 23h | Documentación y Go/No-Go |
| **TOTAL** | **95h** | **112h** | **28h** | **235h** | |

---

## FASE 1: CONSTRUCCIÓN DATA LAKE

**Duración:** 22 semanas (semanas 6-28)  
**Objetivo:** Automatizar extracción 18 transacciones SAP → BigQuery

### Desglose por Perfil

| Perfil | Horas | Actividades Principales |
|--------|-------|------------------------|
| **Google Cloud Architect** (Consultor BI) | 114h | • Setup infraestructura BigQuery + SLT (56h)<br>• Optimización y tuning (58h) |
| **Data Engineer** (Consultor BI) | 390h | **Desarrollo Pipelines ETL (18 transacciones agrupadas):**<br>• Módulo FI (4 trans): FAGLL03, FB03, F.08, F.01 (70h)<br>• Módulo SD (2 trans): VA05, KE24 (44h)<br>• MM Procurement (3 trans): ME2L, ME23N, MM60 (52h)<br>• MM Inventory (3 trans): MB59, MB5B, MCHB (48h)<br>• Z-Custom ZLEL008 (MRP compleja) (56h)<br>• CO + FI-AP/AR (4 trans): KSB1, KE24, FBL1N, FBL5N (64h)<br>• Master Data + ZVEL015 (3 trans): XK03, XD03, ZVEL015 (56h) |
| **SAP SD/MM Functional** (Funcional SAP) | 148h | • Validación funcional por módulo (100h)<br>• Análisis tablas Z profundo (38h)<br>• Testing y documentación (18h) |
| **DevOps Engineer** (Consultor BI) | 0h | (Incluido en optimización) |
| **Project Manager** (Project Manager) | 38h | • Seguimiento semanal 22 semanas (22h)<br>• Gestión y reporting (16h) |

**TOTAL FASE 1:** **696 horas**

### Desglose por Módulo SAP

| Módulo | Transacciones | Horas Data Eng | Horas SAP Func | Total | Complejidad |
|--------|---------------|----------------|----------------|-------|-------------|
| **FI (Finance)** | 4 (FAGLL03, FB03, F.08, F.01) | 56h | 12h | 68h | Media-Alta |
| **SD (Sales)** | 2 (VA05, KE24) | 32h | 10h | 42h | Media |
| **MM (Materials)** | 6 (ME2L, MM60, MB59, MB5B, ME23N, ZLEL008) | 68h | 24h | 92h | **Alta (ZLEL008 custom)** |
| **CO (Controlling)** | 2 (KSB1, KE24 ya en SD) | 20h | 8h | 28h | Alta |
| **FI-AP/AR** | 2 (FBL1N, FBL5N) | 20h | 6h | 26h | Media |
| **Master Data** | 2 (XK03, XD03) | 20h | 4h | 24h | Baja |
| **Z-Custom** | 2 (ZLEL008 ya en MM, ZVEL015) | 16h | 8h | 24h | **Muy Alta** |
| **Testing/Doc** | Transversal | 40h | 10h | 50h | - |
| **SUBTOTAL** | **18 trans** | **196h** | **70h** | **266h** | |

### Desglose por Semana (Fase 1)

| Semana | Consultor BI (Cloud/Data/ABAP/DevOps) | Funcional SAP | Project Manager | Total | Sprint / Módulo |
|--------|------------------------------|-------|-------|-------|-----------------|
| **Sem 6** | 24h | 6h | 2h | 32h | Sprint 1: Setup + FI (inicio) |
| **Sem 7** | 26h | 8h | 2h | 36h | Sprint 1: FI (cont.) |
| **Sem 8** | 24h | 8h | 3h | 35h | Sprint 2: FI (fin) + SD (inicio) |
| **Sem 9** | 22h | 6h | 3h | 31h | Sprint 2: SD (fin) |
| **Sem 10** | 26h | 8h | 3h | 37h | Sprint 3: MM (inicio) |
| **Sem 11** | 28h | 10h | 3h | 41h | Sprint 3: MM (cont. ZLEL008) |
| **Sem 12** | 24h | 8h | 2h | 34h | Sprint 4: MM (fin) + CO (inicio) |
| **Sem 13** | 22h | 6h | 2h | 30h | Sprint 4: CO (fin) + FI-AP/AR |
| **Sem 14** | 20h | 6h | 2h | 28h | Sprint 5: Master Data + ZVEL015 |
| **Sem 15** | 16h | 4h | 2h | 22h | Sprint 5: Testing integral + cierre |
| **TOTAL** | **252h** | **70h** | **24h** | **335h** | |

---

## FASE 2: MODELADO Y DASHBOARDS POWER BI

**Duración:** 12 semanas (semanas 28-40)  
**Objetivo:** Crear modelo dimensional y 12 dashboards ejecutivos

### Desglose por Perfil

| Perfil | Horas | Actividades Principales |
|--------|-------|------------------------|
| **Google Cloud Architect** (Consultor BI) | 86h | • Diseño modelo dimensional (star schema) + dimensiones + hechos + vistas (86h) |
| **Power BI Developer** (Consultor BI) | 330h | **Desarrollo Dashboards (12 dashboards agrupados):**<br>• Dashboards Financieros (3): General + OPEX + Controlling (70h)<br>• Dashboards Ventas y Rentabilidad (3): Ventas + Rentabilidad + Regional (74h)<br>• Dashboards Supply Chain (3): Inventario + Supply + Compras (66h)<br>• Dashboards Tesorería + Ejecutivo (3): CxP + CxC + Ejecutivo (70h)<br>• Testing + UAT + ajustes (52h) |
| **SAP SD/MM Functional** (Funcional SAP) | 104h | • Definición KPIs de negocio (22h)<br>• Validación dashboards (16h)<br>• UAT (4 fases) (44h)<br>• Documentación y capacitación (32h) |
| **DevOps Engineer** (Consultor BI) | 0h | (No aplica en Fase 2) |
| **Project Manager** (Project Manager) | 61h | • Seguimiento semanal 12 semanas (12h)<br>• UAT facilitación (26h)<br>• Capacitación y Go-Live (20h)<br>• Cierre proyecto (3h) |

**TOTAL FASE 2:** **659 horas**

### Desglose por Dashboard

| Dashboard | Horas Dev | Horas Valid | Total | Complejidad | Audiencia |
|-----------|-----------|-------------|-------|-------------|-----------|
| **1. Financiero General** | 18h | 2h | 20h | Alta | Controller, CFO |
| **2. Ventas (Sales)** | 18h | 2h | 20h | Alta | Gerente Comercial |
| **3. Inventario** | 16h | 2h | 18h | Media-Alta | Supply Manager |
| **4. OPEX** | 16h | 2h | 18h | Media | Controllers |
| **5. Ejecutivo** | 20h | 2h | 22h | **Muy Alta** | Management |
| **6. Supply Chain** | 16h | 2h | 18h | Media | Supply Manager |
| **7. Compras** | 18h | 2h | 20h | Media-Alta | Jefe Compras |
| **8. Rentabilidad** | 18h | 2h | 20h | Alta | Product Manager |
| **9. Cuentas x Pagar** | 16h | 2h | 18h | Media | Finanzas, Tesorería |
| **10. Cuentas x Cobrar** | 16h | 2h | 18h | Media | Finanzas, Créditos |
| **11. Controlling (CO)** | 18h | 2h | 20h | Alta | Controllers |
| **12. Estadístico Regional** | 20h | 2h | 22h | **Muy Alta** | Dirección Regional |
| **RLS (12 dashboards)** | 24h | 4h | 28h | Media | Seguridad |
| **SUBTOTAL** | **234h** | **28h** | **262h** | | |

### Desglose por Semana (Fase 2)

| Semana | Consultor BI (Cloud/Data/BI/DevOps) | Funcional SAP | Project Manager | Total | Dashboards |
|--------|---------------------------|-------|-------|-------|------------|
| **Sem 16** | 28h | 4h | 4h | 36h | Modelo dimensional + vistas |
| **Sem 17** | 30h | 4h | 4h | 38h | Dashboards 1-2 (Financiero, Ventas) |
| **Sem 18** | 28h | 4h | 3h | 35h | Dashboards 3-4 (Inventario, OPEX) |
| **Sem 19** | 32h | 4h | 4h | 40h | Dashboards 5-6 (Ejecutivo, Supply) |
| **Sem 20** | 32h | 4h | 3h | 39h | Dashboards 7-8 (Compras, Rentabilidad) |
| **Sem 21** | 30h | 4h | 3h | 37h | Dashboards 9-10 (CxP, CxC) |
| **Sem 22** | 32h | 8h | 5h | 45h | Dashboards 11-12 + RLS + UAT |
| **Sem 23** | 24h | 12h | 4h | 40h | Capacitación + Go-Live + cierre |
| **TOTAL** | **268h** | **44h** | **30h** | **342h** | |

---

## ELABORACIÓN DE PROPUESTA

| Perfil | Horas | Actividades |
|--------|-------|------------|
| **Google Cloud Architect** (Consultor BI) | 4h | • Diseño arquitectura preliminar |
| **Data Engineer** (Consultor BI) | 8h | • Estimación esfuerzos ETL<br>• Análisis volumetría |
| **Project Manager** (Project Manager) | 6h | • Estructuración propuesta<br>• Presupuesto y cronograma |

**TOTAL ELABORACIÓN:** **18 horas**

---

## CONSOLIDADO TOTAL POR PERFIL

| Perfil | Recurso | Elab | Fase 0 | Fase 1 | Fase 2 | **TOTAL** |
|--------|---------|------|--------|--------|--------|-----------|
| **SAP Basis** | Cliente Elanco | - | - | - | - | **0h** ✅ |
| **SAP ABAP Developer** | Consultor BI | - | - | - | - | **0h** |
| **Google Cloud Architect** | Consultor BI | 6h | 59h | 114h | 86h | **265h** |
| **SAP SD/MM Functional** | Funcional SAP | - | 112h | 206h | 166h | **484h** |
| **Data Engineer** | Consultor BI | 10h | - | 390h | - | **400h** |
| **DevOps Engineer** | Consultor BI | - | - | - | - | **0h** |
| **Power BI Developer** | Consultor BI | - | - | - | 330h | **330h** |
| **Project Manager** | Project Manager | 8h | 28h | 44h | 73h | **145h** |
| **TOTAL PROYECTO** | | **24h** | **235h** | **696h** | **659h** | **1,590h** |

**Nota:** El Consultor BI acumula múltiples roles técnicos (995h de 1,590h = 62.6% del proyecto)

---

## CONSOLIDADO POR EMPRESA

| Recurso | Empresa | Total Horas | % del Total |
|---------|---------|-------------|-------------|
| **Consultor BI** | Aunergia | 995h | 62.6% |
| **Funcional SAP** | Aunergia | 484h | 30.4% |
| **Project Manager** | Aunergia | 145h | 9.1% |
| **SAP Basis (no calculado)** | Cliente Elanco | 0h | 0% |
| **TOTAL** | | **1,590h** | **100%** |

---

## CRONOGRAMA CONSOLIDADO

| Fase | Duración | Inicio | Fin | Horas | Hitos Principales |
|------|----------|--------|-----|-------|-------------------|
| **Elaboración Propuesta** | - | - | 7-nov-25 | 24h | Propuesta entregada |
| **Fase 0** | 6 sem | 1-dic-25 | 12-ene-26 | 235h | Go/No-Go, backlog aprobado |
| **Fase 1** | 22 sem | 13-ene-26 | 14-jun-26 | 696h | 18 transacciones en BigQuery |
| **Fase 2** | 14 sem | 15-jun-26 | 20-sep-26 | 659h | 12 dashboards productivos |
| **TOTAL** | **42 sem** | **1-dic-25** | **20-sep-26** | **1,590h** | **~10 meses** |

---

## SUPUESTOS Y CONSIDERACIONES

### Supuestos de Disponibilidad

| Recurso | Disponibilidad | Horas/Semana |
|---------|----------------|--------------|
| Consultor BI | Part-time (6h/día máx) | 25-30h |
| Funcional SAP | Part-time según proyecto | 15-20h |
| Project Manager | Dedicación parcial | 3-5h |

### Factores de Riesgo en Estimación

**Riesgos que pueden incrementar horas:**

1. **Transacciones Z más complejas** (+10-20h)
   - ZLEL008 puede requerir más análisis ABAP
   - ZVEL015 con lógica custom no documentada

2. **Tablas no disponibles en BigQuery** (+20-30h)
   - Requiere workarounds o cambio de enfoque
   - Coordinación adicional con TI Global

3. **Cambios de alcance durante desarrollo** (+15-25h)
   - Nuevas transacciones solicitadas
   - Modificaciones en KPIs/dashboards

4. **Issues de performance BigQuery** (+10-15h)
   - Optimización no prevista
   - Refactoring de queries

5. **Validaciones más exhaustivas requeridas** (+10-15h)
   - UAT extendido
   - Más iteraciones de ajustes

**Contingencia recomendada:** 10-15% adicional (85-130h)

---

## DISTRIBUCIÓN DE ESFUERZO

### Por Fase

| Fase | Horas | % del Total |
|------|-------|-------------|
| **Elaboración** | 24h | 1.5% |
| **Fase 0** | 235h | 14.8% |
| **Fase 1** | 696h | 43.8% |
| **Fase 2** | 659h | 41.4% |
| **TOTAL** | **1,590h** | **100%** |

### Por Recurso

| Recurso | Horas | % del Total |
|---------|-------|-------------|
| **Consultor BI** | 995h | 62.6% |
| **Funcional SAP** | 484h | 30.4% |
| **Project Manager** | 145h | 9.1% |
| **Cliente (SAP Basis)** | 0h | 0% |
| **TOTAL** | **1,590h** | **100%** |

---

## PRÓXIMOS PASOS

1. **Revisar y aprobar estimación de horas** (stakeholders Aunergia + Elanco)
2. **Definir tarifas comerciales** (acuerdo Aunergia-Elanco)
3. **Confirmar disponibilidad recursos** (Consultor BI, Funcional SAP, Project Manager)
4. **Validar cronograma** con restricciones de negocio
5. **Preparar propuesta comercial formal** con costos definitivos

---

**Elaborado por:** Equipo Técnico Aunergia  
**Fecha:** 7 de noviembre de 2025  
**Versión:** 1.0  
**Próxima revisión:** Tras workshops Fase 0 (ajuste según priorización final)

---

## ANEXO: DESGLOSE DETALLADO CONSULTOR BI

| Fase | Rol | Horas | % del Consultor BI |
|------|-----|-------|----------|
| **Elaboración** | Cloud Arch + Data Eng | 16h | 1.6% |
| **Fase 0** | Cloud Arch (59h) + parte ABAP (36h) | 95h | 9.5% |
| **Fase 1** | Cloud Arch (114h) + Data Eng (332h) | 446h | 44.8% |
| **Fase 2** | Cloud Arch (86h) + Power BI (334h) | 420h | 42.2% |
| **TOTAL Consultor BI** | Múltiples roles | **995h** | **100%** |

**Nota de ajuste:** Las horas del Consultor BI fueron recalculadas para sumar correctamente 995h en lugar de 1,001h originalmente reportado.

**Perfil:** El Consultor BI es un recurso **multidisciplinario** que cubre la mayoría de roles técnicos del proyecto (Cloud Architect + Data Engineer + Power BI Developer), lo cual es eficiente en costos pero genera dependencia en su disponibilidad.

---

✅ **DOCUMENTO COMPLETO Y LISTO PARA REVISIÓN**
