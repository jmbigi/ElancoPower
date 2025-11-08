# 9. CRONOGRAMA SEMANAL DEL PROYECTO

## 9.1. Vista General del Cronograma

**Duración Total:** 42 semanas (~10 meses)  
**Inicio:** Semana 0 (6 de enero 2026)  
**Finalización:** Semana 42 (Mediados de octubre 2026)

```
FASE 0          FASE 1                                           FASE 2          
────────        ──────────────────────────────────────────────   ──────────────────────────    
6 sem           22 sem                                           14 sem         
███████         ██████████████████████████████████████████████   ████████████████████████████  
                                                          
Sem 0-6         Sem 6-28                                         Sem 28-42 (ajustado a nuevo inicio)
```

**Restricción:** Consultor BI trabaja máximo 6 horas/día (30h/semana). Cronograma comprimido manteniendo las mismas 1,590 horas totales.

---

## 9.2. FASE 0 - Due Diligence (Semanas 0-6) (Inicio 6-ene-2026)

### Semana 0: Diseño Arquitectura Preliminar y Estimación

**Actividades principales:**
- Diseño arquitectura BigQuery 3 capas + conectividad SAP SLT (Consultor BI: 6h, Funcional SAP: 4h)
- Análisis volumetría y complejidad 18 transacciones SAP (Consultor BI: 8h, Funcional SAP: 6h)

**Horas totales:** 24h (Consultor BI: 14h, Funcional SAP: 10h)

### Semana 1: Kick-off y Alineamiento

**Actividades principales:**
- Kick-off meeting con stakeholders (3h + 4h + 3h = 10h)
- Inicio inventario técnico completo

**Horas totales:** 10h

### Semanas 1-3: Inventario Técnico Completo

**Actividades principales:**
- Revisión dataset CASA BigQuery
- Análisis permisos SAP y estado actual
- Listado tablas por módulo y documentación
- **Horas totales:** 41h (Consultor BI: 20h, Funcional SAP: 18h, Project Manager: 3h)

### Semanas 2-3: Gestión de Tickets Críticos

**Actividades principales:**
- Revisión problemas detectados (permisos, tablas faltantes)
- Seguimiento tickets SAP y BigQuery
- **Horas totales:** 35h (Consultor BI: 8h, Funcional SAP: 22h, Project Manager: 5h)

### Semanas 2-4: Workshops y Análisis Z

**Actividades principales:**
- Workshops priorización 18 transacciones
- Análisis profundo ZLEL008 y ZVEL015
- Definición tablas Z
- **Horas totales:** 66h (Consultor BI: 20h, Funcional SAP: 36h, Project Manager: 10h)

### Semanas 4-5: Diseño y POC

**Actividades principales:**
- Arquitectura 3 capas definitiva
- POC técnico end-to-end
- Validación funcional SAP
- **Horas totales:** 36h (Consultor BI: 24h, Funcional SAP: 12h)

### Semanas 5-6: Documentación y Go/No-Go

**Actividades principales:**
- Documento arquitectura
- Backlog priorizado
- Listado completo tablas SAP
- Plan detallado
- **Reunión Go/No-Go**
- **Horas totales:** 23h (Consultor BI: 6h, Funcional SAP: 10h, Project Manager: 7h)

**Hito Semana 6:** ✅✅ Decisión Go/No-Go emitida, Fase 1 aprobada para iniciar

**TOTAL FASE 0:** 235h (Consultor BI: 95h, Funcional SAP: 112h, Project Manager: 28h)  
Inicio efectivo: 6-ene-2026 (considera feriados y disponibilidad inicial)

---

## 9.3. FASE 1 - Construcción Data Lake (Semanas 6-28) (Inicio estimado segunda mitad febrero 2026 tras Fase 0)

### Semanas 6-8: Setup Infraestructura Completa

**Actividades principales:**
- Datasets BigQuery + particionamiento
- Service accounts + conectores SAP SLT
- Cloud Functions + validación accesos tablas SAP
- **Horas totales:** 73h (Consultor BI: 60h, Funcional SAP: 6h, Project Manager: 7h)
- **Hito:** ✅ Infraestructura BigQuery lista

### Semanas 8-11: Pipelines Módulo FI (4 transacciones)

**Transacciones:** FAGLL03, FB03, F.08, F.01
**Tablas SAP:** FAGLFLEXA, BKPF, BSEG, FAGLFLEXT, SKA1, BSID, BSAD
- Desarrollo + validación + testing
- **Horas totales:** 89h (Consultor BI: 60h, Funcional SAP: 26h, Project Manager: 3h)
- **Hito:** ✅ Módulo FI completo

### Semanas 11-13: Pipelines Módulo SD (2 transacciones)

**Transacciones:** VA05, KE24
**Tablas SAP:** VBAK, VBAP, VBEP, KNA1, CE1xxxx, CE4xxxx
- Desarrollo + validación + testing
- **Horas totales:** 61h (Consultor BI: 38h, Funcional SAP: 20h, Project Manager: 3h)
- **Hito:** ✅ Módulo SD completo

### Semanas 13-15: Pipelines MM Procurement (3 transacciones)

**Transacciones:** ME2L, ME23N, MM60
**Tablas SAP:** EKKO, EKPO, MBEW, CKMLCR
- Desarrollo + validación + testing
- **Horas totales:** 71h (Consultor BI: 44h, Funcional SAP: 24h, Project Manager: 3h)
- **Hito:** ✅ MM Procurement completo

### Semanas 15-17: Pipelines MM Inventory (3 transacciones)

**Transacciones:** MB59, MB5B, MCHB
**Tablas SAP:** MSEG, MARD, MCHB
- Desarrollo + validación + testing
- **Horas totales:** 65h (Consultor BI: 42h, Funcional SAP: 20h, Project Manager: 3h)
- **Hito:** ✅ MM Inventory completo

### Semanas 17-20: Pipeline ZLEL008 (custom Inventario consolidado)

**Transacción custom compleja**
**Z-tables** suministradas por SAP Functional
- Análisis + desarrollo + validación funcional + testing extendido
- **Horas totales:** 77h (Consultor BI: 48h, Funcional SAP: 26h, Project Manager: 3h)
- **Hito:** ✅ ZLEL008 completo (transacción custom más compleja)

### Semanas 20-23: Pipelines CO y FI-AP/AR (4 transacciones)

**Transacciones:** KSB1, KE24 análisis, FBL1N, FBL5N
**Tablas SAP:** COBK, COEP, AUFK, BSIK, BSAK
- Desarrollo + validación + testing
- **Horas totales:** 92h (Consultor BI: 56h, Funcional SAP: 30h, Project Manager: 6h)
- **Hito:** ✅ Módulo CO y AP/AR completo

### Semanas 23-26: Pipelines Master Data y ZVEL015

**Transacciones:** XK03, XD03, ZVEL015 (pricing)
**Tablas SAP:** LFA1, LFB1, LFM1, KNA1, KNB1, KNVV + Z-pricing
- Desarrollo + validación + testing
- **Horas totales:** 82h (Consultor BI: 48h, Funcional SAP: 28h, Project Manager: 6h)
- **Hito:** ✅ Master Data y ZVEL015 completo

### Semanas 26-28: Optimización y Automatización

**Actividades principales:**
- Tuning queries + CI/CD + monitoreo
- Testing integral 18 transacciones
- Validación funcional SAP
- Documentación técnica
- **Horas totales:** 86h (Consultor BI: 50h, Funcional SAP: 26h, Project Manager: 10h)
- **Hito:** ✅✅ Fase 1 completa, Data Lake operativo con 18 transacciones

**TOTAL FASE 1:** 696h (Consultor BI: 446h, Funcional SAP: 206h, Project Manager: 44h)

---

## 9.4. FASE 2 - Dashboards Power BI (Semanas 28-42) (Inicio aproximado julio 2026)

### Semanas 28-30: Modelo Dimensional Completo

**Actividades principales:**
- Star schema: 8 dimensiones + 6 tablas hechos
- Vistas SQL + capa semántica
- Definición KPIs con SAP Functional
- **Horas totales:** 116h (Consultor BI: 86h, Funcional SAP: 22h, Project Manager: 8h)
- **Hito:** ✅ Modelo dimensional diseñado y validado

### Semanas 30-32: Dashboards Financieros (3)

**Dashboards:** Financiero General, OPEX, Controlling
**Definición SAP Functional + desarrollo**
**Tablas:** BKPF, BSEG, FAGLFLEXA, COEP, COBK
- 3 dashboards con RLS
- **Horas totales:** 82h (Consultor BI: 64h, Funcional SAP: 14h, Project Manager: 4h)
- **Hito:** ✅ Dashboards Financieros completos

### Semanas 30-32: Dashboards Ventas y Rentabilidad (3) - EN PARALELO

**Dashboards:** Ventas, Rentabilidad, Regional
**Definición SAP Functional + desarrollo**
**Tablas:** VBAK, VBAP, CE1xxxx
- 3 dashboards con RLS
- **Horas totales:** 86h (Consultor BI: 68h, Funcional SAP: 14h, Project Manager: 4h)
- **Hito:** ✅ Dashboards Ventas completos

### Semanas 30-32: Dashboards Supply Chain (3) - EN PARALELO

**Dashboards:** Inventario, Supply Chain, Compras
**Definición SAP Functional + desarrollo**
**Tablas:** MARD, MCHB, MSEG, EKKO, EKPO
- 3 dashboards con RLS
- **Horas totales:** 78h (Consultor BI: 62h, Funcional SAP: 12h, Project Manager: 4h)
- **Hito:** ✅ Dashboards Supply Chain completos

### Semanas 32-35: Dashboards Tesorería y Ejecutivo (3)

**Dashboards:** CxP, CxC, Dashboard Ejecutivo
**Definición SAP Functional + desarrollo**
**Tablas:** BSIK, BSAK, BSID, BSAD + consolidado
- 3 dashboards con RLS
- **Horas totales:** 87h (Consultor BI: 66h, Funcional SAP: 14h, Project Manager: 7h)
- **Hito:** ✅ 12 dashboards completos con RLS

### Semanas 35-39: Testing y UAT Completo

**Actividades principales:**
- Testing integrado + coordinación SAP Functional
- 4 fases UAT (Financiero + Comercial + Supply + Ejecutivo)
- Ajustes post-UAT
- **Horas totales:** 122h (Consultor BI: 41h, Funcional SAP: 55h, Project Manager: 26h)
- **Hito:** ✅ UAT completado, dashboards validados

### Semanas 39-42: Ajustes Finales, Documentación, Capacitación y Go-Live

**Actividades principales:**
- Documentación funcional con SAP Functional
- Capacitación usuarios
- Preparación + Go-Live
- Cierre proyecto
- **Horas totales:** 88h (Consultor BI: 33h, Funcional SAP: 35h, Project Manager: 20h)
- **Hito:** ✅✅✅ **PROYECTO CERRADO FORMALMENTE - GO-LIVE EXITOSO**

**TOTAL FASE 2:** 659h según tareas CSV (distribución: Consultor BI: 420h, Funcional SAP: 166h, Project Manager: 73h)

---

## 9.5. Resumen de Hitos Clave

| Hito | Semana | Descripción |
|------|--------|-------------|
| **Inicio Proyecto** | Semana 0 (6-ene-2026) | Kick-off y diseño preliminar |
| **Go/No-Go** | Semana 6 (mediados feb 2026) | Decisión de continuar a Fase 1 |
| **Fin Fase 1** | Semana 28 (mediados jul 2026) | Data Lake operativo con 18 transacciones |
| **Fin UAT** | Semana 39 (sept 2026) | Dashboards validados |
| **Go-Live** | Semana 42 (oct 2026) | Sistema en producción |
| **Cierre Formal** | Semana 42 | Proyecto completado |

---

## 9.6. Cronograma Consolidado (Gantt Simplificado)

```
PROYECTO ELANCO - CENTRALIZACIÓN DE DATOS DE ANÁLISIS
Duración: 42 semanas | ~10 meses
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FASE 0: Due Diligence (Semanas 0-6)
███████████████ 
    │
    ├─ S0-1: Diseño arquitectura + kick-off
    ├─ S1-3: Inventario técnico completo
    ├─ S2-3: Gestión tickets críticos
    ├─ S2-4: Workshops y análisis Z
    ├─ S4-5: Diseño y POC
    └─ S5-6: Documentación y Go/No-Go ✓

FASE 1: Data Lake (Semanas 6-28)
               ████████████████████████████████████████████████████████████████
                    │
                    ├─ S6-8: Setup infraestructura (73h)
                    ├─ S8-11: Módulo FI - 4 trans (89h)
                    ├─ S11-13: Módulo SD - 2 trans (61h)
                    ├─ S13-15: MM Procurement - 3 trans (71h)
                    ├─ S15-17: MM Inventory - 3 trans (65h)
                    ├─ S17-20: ZLEL008 custom (77h)
                    ├─ S20-23: CO y FI-AP/AR - 4 trans (92h)
                    ├─ S23-26: Master Data y ZVEL015 (82h)
                    └─ S26-28: Optimización (86h) ✓

FASE 2: Dashboards (Semanas 28-42)
                                                                              ██████████████████████████████████
                                                                                    │
                                                                                    ├─ S28-30: Modelo dimensional (116h)
                                                                                    ├─ S30-32: 9 Dashboards paralelos (246h)
                                                                                    ├─ S32-35: Dashboards finales (87h)
                                                                                    ├─ S35-39: Testing y UAT (122h)
                                                                                    └─ S39-42: Capacitación y Go-Live (88h) ✓✓✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HITOS CLAVE:
✓ Go/No-Go (S6) | ✓ Data Lake (S28) | ✓ UAT (S39) | ✓✓✓ Go-Live (S42)

ESFUERZO TOTAL: 1,590 horas | Consultor BI: 961h | Funcional SAP: 484h | Project Manager: 145h
Cronograma comprimido 25% manteniendo mismas horas
```

---

## 9.7. Hitos Críticos y Dependencias

### Hitos de Aprobación (Gates)

| Hito | Semana | Criterio de Aceptación | Responsable Aprobación |
|------|--------|------------------------|------------------------|
| **Go/No-Go Fase 1** | Mes 1, Semana 5 | Permisos SAP OK, ≥12 transacciones con tablas disponibles | Management Elanco |
| **Aceptación Fase 1** | Mes 3, Semana 15 | 18 transacciones funcionales, validación >99% | Finanzas + Supply |
| **Aceptación UAT** | Mes 5, Semana 20 | Dashboards aprobados, RLS validado | Stakeholders |
| **Go-Live Final** | Mes 6, Semana 23 | Capacitación completa, documentación entregada | Management Elanco |
| **Cierre Formal** | Mes 6, Semana 23 | Transferencia conocimiento, acta firmada | Management Elanco |

### Dependencias Críticas

| Actividad | Depende De | Riesgo si se Retrasa |
|-----------|------------|---------------------|
| Inicio Fase 1 | Go/No-Go aprobado | ⛔ Bloquea proyecto completo |
| Desarrollo pipelines Fase 1 | Permisos SAP + Tablas BigQuery | ⚠️ Retrasa 2-4 semanas |
| Inicio Fase 2 | Fase 1 completada | ⚠️ Retrasa todo Fase 2 |
| UAT | Dashboards desarrollados | ⚠️ Retrasa go-live |
| Go-Live | UAT aprobado + Capacitación | ⛔ Bloquea puesta en producción |

---

## 9.8. Consideraciones de Calendario

### Periodos de Riesgo

⚠️ **Vacaciones de fin de año**
- **Impacto:** Pausa de 1 semana durante Fase 0 (Semana 4)
- **Mitigación:** ✅ **YA CONSIDERADO** - Se agregó pausa formal de 1 semana en cronograma

⚠️ **Festividades locales**
- **Impacto:** Pueden coincidir con semanas de desarrollo dashboards
- **Mitigación:** Actividades de desarrollo individual, no requieren coordinación intensa

⚠️ **Cierres mensuales contables**
- **Impacto:** Stakeholders de Finanzas menos disponibles últimos días del mes
- **Mitigación:** Evitar workshops/validaciones críticas durante cierres mensuales

### Flexibilidad del Cronograma

**Holguras incorporadas:**
- Fase 0: 1 semana de buffer
- Fase 1: 2 semanas de buffer (considerando complejidad)
- Fase 2: 1 semana de buffer

**Ajustes permitidos:**
- Duración mínima: 21 semanas (todo fluye perfecto + vacaciones)
- Duración esperada: 23 semanas (escenario realista + vacaciones)
- Duración máxima: 25 semanas (con contingencias + vacaciones)

---

## 9.9. Recursos por Semana

### Carga de Trabajo por Persona

| Fase | Funcional SAP | Consultor BI | Project Manager | Promedio Semanal |
|------|--------------|-------------|----------------|------------------|
| S0-6 (Fase 0) | 112h / 6sem = 19h/sem | 95h / 6sem = 16h/sem | 28h / 6sem = 5h/sem | Total: 40h/sem |
| S6-28 (Fase 1) | 206h / 22sem = 9h/sem | 446h / 22sem = 20h/sem | 44h / 22sem = 2h/sem | Total: 31h/sem |
| S28-42 (Fase 2) | 166h / 14sem = 12h/sem | 420h / 14sem = 30h/sem | 73h / 14sem = 5h/sem | Total: 47h/sem |

**Nota:** El Consultor BI trabaja máximo 30h/semana (6h/día), cumplido en todas las fases. Fase 2 es la más intensiva para este rol.

---

## 9.10. Plan de Comunicación

### Reuniones Periódicas

| Reunión | Frecuencia | Participantes | Duración | Objetivo |
|---------|------------|---------------|----------|----------|
| **Daily Stand-up** | Lun-Vie | Funcional SAP + Consultor BI | 15 min | Sincronización diaria |
| **Weekly Status** | Viernes | Project Manager + Funcional SAP + Consultor BI | 30 min | Reporte semanal |
| **Sprint Review** | Cada 2 sem | Todos + Stakeholders | 1h | Demo de avances |
| **Steering Committee** | Mensual | Project Manager + Management | 1h | Status ejecutivo |

### Reportes

| Reporte | Frecuencia | Responsable | Destinatarios |
|---------|------------|-------------|---------------|
| Status Report Semanal | Viernes | Project Manager | Stakeholders Elanco |
| Dashboard de Seguimiento | Continuo | Project Manager | Equipo proyecto |
| Reporte de Riesgos | Quincenal | Project Manager + Consultor BI | Management |
| Reporte Mensual Ejecutivo | Mensual | Project Manager | Management Elanco |

---

*Siguiente sección: [10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md](10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md)*
