# 9. CRONOGRAMA SEMANAL DEL PROYECTO

## 9.1. Vista General del Cronograma

**Duración Total:** 24 semanas (~6 meses, incluyendo 1 semana vacacional)  
**Fecha Inicio:** 1 de diciembre de 2025  
**Fecha Fin Estimada:** 18 de mayo de 2026

```
FASE 0          VACACIONES  FASE 1                    FASE 2          
────────        ─────────   ──────────────────────    ──────────────────────    
5 sem           1 sem       10 sem                    8 sem         
███████         ░░░░░░░     ███████████████████████   ████████████████████████  
                                                          
Dic 1           Dic 23      Dic 30                    Mar 24     Mayo 18
```

**Nota:** Se incluye 1 semana de pausa vacacional (23-29 diciembre) durante las festividades de fin de año.  
**Restricción:** Juan Manuel Bigi trabaja máximo 6 horas/día (30h/semana), ajustando Fase 2 a 8 semanas.

---

## 9.2. FASE 0 - Due Diligence (Semanas 1-5)

### Semana 1 (1-7 diciembre 2025): Kick-off y Análisis Inicial

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun 1** | Kick-off meeting con stakeholders | Linda + Todos + Stakeholders | 3h | Minutas kick-off |
| **Lun-Mar** | Análisis dataset CASA en BigQuery | JMB | 8h | Inventario tablas disponibles |
| **Mar-Mie** | Seguimiento Ticket SAP-48219 (permisos) | Lucía | 4h | Status report |
| **Mie-Jue** | Prueba conectividad Power BI ↔ BigQuery | JMB | 4h | POC funcional (.pbix) |
| **Jue-Vie** | Seguimiento Tickets BQ (tablas) | Lucía | 4h | Status report |
| **Vie** | Preparación workshop priorización | Lucía + JMB | 4h | Agenda + materiales |

**Hito Semana 1:** ✅ Inventario técnico completado, status de tickets críticos

---

### Semana 2 (8-14 diciembre 2025): Workshops y Validación

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Workshop Finanzas (priorización trans) | Todos + Stakeholders | 4h + 4h stakeholders | Scoring transacciones FI/CO |
| **Mar** | Workshop Supply (priorización trans) | Todos + Stakeholders | 4h + 4h stakeholders | Scoring transacciones MM/SD |
| **Mie** | Análisis de transacciones custom (ZLEL008) | Lucía | 4h | Documentación tablas Z |
| **Jue** | Benchmarks performance BigQuery | JMB | 6h | Resultados queries |
| **Vie** | Workshop consolidación (priorización) | Todos + Stakeholders | 4h + 4h stakeholders | Backlog priorizado |

**Hito Semana 2:** ✅ Backlog de 18 transacciones priorizado y aprobado

---

### Semana 3 (15-21 diciembre 2025): Planificación Detallada

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Plan de extracción por módulo SAP | JMB | 6h | Roadmap Fase 1 |
| **Mar** | Definición arquitectura zonas (RAW/PROCESSED/CURATED) | JMB | 4h | Diagrama arquitectura |
| **Mie** | Análisis de riesgos y mitigaciones | Lucía + JMB | 4h | Matriz de riesgos |
| **Jue** | Estimación de esfuerzos Fase 1 | JMB | 4h | Matriz estimación horas |
| **Vie** | Seguimiento tickets críticos | Lucía | 4h | Status report |

**Hito Semana 3:** ✅ Plan técnico Fase 1 completo

---

### **PAUSA VACACIONAL: 23-29 diciembre 2025** 🎄

⏸️ **Semana de pausa por festividades de fin de año**
- Sin actividades programadas
- Equipo en descanso vacacional
- Proyecto se retoma el 30 de diciembre

---

### Semana 4 (30 dic 2025 - 5 enero 2026): Documentación y Preparación Go/No-Go

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Mar 30** | Documentación entregables Fase 0 | JMB | 8h | 7 documentos Fase 0 |
| **Mie 31** | Revisión interna documentos | Linda + Lucía + JMB | 4h | Documentos revisados |
| **Jue 2** | Validación con TI (David Saboya) | Lucía + JMB | 2h | Confirmaciones técnicas |
| **Vie 3** | Preparación presentación Go/No-Go | Linda + JMB | 4h | PPT (20 slides) |

**Nota:** Semana corta por festividades. Lun 30-Mie 1 (año nuevo) son días festivos en muchos países.

**Hito Semana 4:** ✅ Documentación Fase 0 completa

---

### Semana 5 (6-12 enero 2026): Go/No-Go y Cierre Fase 0

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Distribución materiales Go/No-Go | Linda | 2h | Documentos enviados |
| **Mar** | **Reunión Go/No-Go** | Todos + Stakeholders + Management | 2h | Decisión documentada |
| **Mie** | Ajustes post Go/No-Go (si aplica) | JMB | 4h | Plan actualizado |
| **Jue** | Preparación kick-off Fase 1 | Todos | 3h | Agenda Fase 1 |
| **Vie** | Cierre administrativo Fase 0 | Linda | 2h | Reporte cierre |

**Hito Semana 5:** ✅✅ Decisión Go/No-Go emitida, Fase 1 aprobada para iniciar

---

## 9.3. FASE 1 - Construcción Data Lake (Semanas 6-15)

### Semana 6 (13-19 enero 2026): Setup Infraestructura + Inicio Módulo FI

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Kick-off Fase 1 | Todos | 2h | Minutas |
| **Lun-Mar** | Setup datasets BigQuery (RAW/PROCESSED/CURATED) | JMB | 6h | Datasets configurados |
| **Mie** | Configuración conectores SAP ↔ BigQuery | JMB | 6h | Conectores activos |
| **Jue-Vie** | Inicio desarrollo FAGLL03 (mayor general) | JMB | 8h | Pipeline RAW FAGLL03 |

**Hito Semana 6:** ✅ Infraestructura BigQuery lista

---

### Semana 7 (20-26 enero 2026): Módulo FI - Parte 1

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun-Mar** | FAGLL03 - Layers PROCESSED y CURATED | JMB | 10h | Pipeline completo FAGLL03 |
| **Mie** | Validación FAGLL03 con Finanzas | Lucía + Stakeholders | 3h | Validación OK |
| **Jue-Vie** | Desarrollo FB03 (documentos contables) | JMB | 8h | Pipeline RAW/PROCESSED FB03 |

**Hito Semana 7:** ✅ FAGLL03 completo y validado

---

### Semana 8 (27 enero - 2 febrero 2026): Módulo FI - Parte 2

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | FB03 - Layer CURATED | JMB | 4h | Pipeline completo FB03 |
| **Mar** | Desarrollo F.08 (balance comprobación) | JMB | 8h | Pipeline F.08 |
| **Mie-Jue** | Desarrollo F.01 (estado situación) | JMB | 8h | Pipeline F.01 |
| **Vie** | Testing integral módulo FI | JMB + Lucía | 4h | 4 transacciones validadas |

**Hito Semana 8:** ✅ Módulo FI completo (4 transacciones)

---

### Semana 9 (3-9 febrero 2026): Módulo SD

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun-Mar** | Desarrollo VA05 (órdenes abiertas) - RAW | JMB | 8h | Pipeline RAW VA05 |
| **Mie-Jue** | VA05 - PROCESSED (joins, cálculos) | JMB | 8h | Pipeline PROCESSED VA05 |
| **Vie** | VA05 - CURATED y testing | JMB | 6h | Pipeline completo VA05 |

**Hito Semana 9:** ✅ VA05 completo y validado

---

### Semana 10 (10-16 febrero 2026): Módulo MM - Parte 1

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Validación VA05 con Supply | Lucía + Stakeholders | 2h | Validación OK |
| **Mar-Mie** | Desarrollo ME2L (purchase orders) | JMB | 10h | Pipeline completo ME2L |
| **Jue-Vie** | Desarrollo MB5B (stock materiales) | JMB | 10h | Pipeline completo MB5B |

**Hito Semana 10:** ✅ ME2L y MB5B completos

---

### Semana 11 (17-23 febrero 2026): Módulo MM - ZLEL008 (Parte 1 - Custom)

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Análisis técnico ZLEL008 (código ABAP) | Lucía + Consultor ABAP | 6h | Documentación tablas Z |
| **Mar-Mie** | Identificación tablas fuente ZLEL008 | JMB | 8h | Mapeo tablas SAP |
| **Jue-Vie** | Desarrollo pipeline RAW ZLEL008 | JMB | 8h | Pipeline RAW ZLEL008 |

**Hito Semana 11:** ✅ Análisis ZLEL008 completo, pipeline RAW funcional

---

### Semana 12 (24 febrero - 2 marzo 2026): Módulo MM - ZLEL008 (Parte 2)

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun-Mar** | ZLEL008 - Replicación lógica en BigQuery SQL | JMB | 10h | Pipeline PROCESSED |
| **Mie** | ZLEL008 - Layer CURATED | JMB | 4h | Pipeline completo ZLEL008 |
| **Jue** | Validación exhaustiva ZLEL008 | JMB + Lucía | 4h | Reconciliación SAP ↔ BQ |
| **Vie** | Ajustes ZLEL008 (si necesario) | JMB | 4h | Pipeline ajustado |

**Hito Semana 12:** ✅ ZLEL008 completo (transacción custom más compleja)

---

### Semana 13 (3-9 marzo 2026): Módulo CO

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun-Mar** | Desarrollo KSB1 (OPEX) | JMB | 12h | Pipeline completo KSB1 |
| **Mie** | Validación KSB1 con Finanzas | Lucía + Stakeholders | 2h | Validación OK |
| **Jue-Vie** | Desarrollo KE24 (CO-PA rentabilidad) | JMB | 10h | Pipeline completo KE24 |

**Hito Semana 13:** ✅ Módulo CO completo (2 transacciones)

---

### Semana 14 (10-16 marzo 2026): Testing Integral y Documentación

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Testing integral 18 transacciones | JMB + Lucía | 6h | Matriz validación |
| **Mar** | Ajustes identificados en testing | JMB | 6h | Pipelines ajustados |
| **Mie** | Documentación diccionarios de datos | JMB | 6h | 18 diccionarios |
| **Jue** | Documentación técnica arquitectura | JMB | 4h | Guía arquitectura |
| **Vie** | Documentación runbooks operativos | JMB | 4h | Runbooks |

**Hito Semana 14:** ✅ Testing completo, documentación técnica entregada

---

### Semana 15 (17-23 marzo 2026): Transacciones Restantes y Cierre Fase 1

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Desarrollo transacciones pendientes (si aplica) | JMB | 8h | Pipelines adicionales |
| **Mar** | Testing transacciones adicionales | JMB + Lucía | 4h | Validaciones |
| **Mie** | Revisión final calidad de datos | JMB | 4h | Reporte calidad |
| **Jue** | Preparación demo Fase 1 | Todos | 3h | Presentación |
| **Vie** | **Demo Fase 1 + Cierre** | Todos + Stakeholders | 2h | Aceptación Fase 1 |

**Hito Semana 15:** ✅✅ Fase 1 completa, Data Lake operativo con 18 transacciones

---

## 9.4. FASE 2 - Dashboards Power BI (Semanas 16-23)

### Semana 16 (24-30 marzo 2026): Modelado Dimensional

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Kick-off Fase 2 | Todos | 2h | Minutas |
| **Lun-Mar** | Diseño de dimensiones (8 dimensiones) | JMB | 12h | ERD dimensiones |
| **Mie-Jue** | Diseño de tablas de hechos (6 hechos) | JMB | 12h | ERD hechos |
| **Vie** | Definición de relaciones | JMB | 4h | Diagrama relaciones |

**Hito Semana 16:** ✅ Modelo dimensional diseñado

---

### Semana 17 (31 marzo - 6 abril 2026): Capa Semántica y Desarrollo Dashboards (Parte 1)

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Desarrollo vistas BigQuery (vw_ventas, vw_inventario, etc.) | JMB | 8h | 10 vistas de negocio |
| **Mar** | Validación modelo con stakeholders | Todos + Stakeholders | 3h | Modelo aprobado |
| **Mie** | Desarrollo Dashboard Financiero (página 1-2) | JMB | 8h | Dashboard 40% |
| **Jue-Vie** | Dashboard Financiero (página 3 + ajustes) | JMB | 8h | Dashboard Financiero v1 |

**Hito Semana 17:** ✅ Dashboard Financiero funcional

---

### Semana 18 (7-13 abril 2026): Desarrollo Dashboards (Parte 2)

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun-Mar** | Desarrollo Dashboard de Ventas | JMB | 10h | Dashboard Ventas v1 |
| **Mie-Jue** | Desarrollo Dashboard de Inventario | JMB | 10h | Dashboard Inventario v1 |
| **Vie** | Revisión iterativa con usuarios | Lucía + Stakeholders | 4h | Feedback |

**Hito Semana 18:** ✅ 3 dashboards funcionales

---

### Semana 19 (14-20 abril 2026): Dashboards Finales + RLS

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Desarrollo Dashboard OPEX | JMB | 8h | Dashboard OPEX v1 |
| **Mar** | Desarrollo Dashboard Ejecutivo | JMB | 8h | Dashboard Ejecutivo v1 |
| **Mie** | Desarrollo Dashboard Supply (opcional) | JMB | 6h | Dashboard Supply v1 |
| **Jue-Vie** | Configuración Row-Level Security (RLS) | JMB | 10h | RLS configurado |

**Hito Semana 19:** ✅ Todos los dashboards con RLS

---

### Semana 20 (21-27 abril 2026): UAT y Ajustes

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | UAT con Finanzas (dashboards FI, OPEX, Ejecutivo) | Todos + Stakeholders | 4h + 4h stakeholders | Feedback Finanzas |
| **Mar** | UAT con Supply (dashboards Ventas, Inventario, Supply) | Todos + Stakeholders | 4h + 4h stakeholders | Feedback Supply |
| **Mie** | Consolidación feedback y priorización ajustes | Todos | 3h | Lista ajustes |
| **Jue-Vie** | Implementación ajustes post-UAT | JMB | 12h | Dashboards ajustados |

**Hito Semana 20:** ✅ UAT completado, ajustes implementados

---

### Semana 21 (28 abril - 4 mayo 2026): Capacitación y Preparación Go-Live

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | Documentación Manual de Usuario | JMB + Lucía | 6h | Manual 30 págs |
| **Mar** | Grabación videos tutoriales (6 videos) | JMB + Lucía | 4h | 6 videos |
| **Mie AM** | Capacitación Power Users | Lucía + JMB | 4h | Certificados |
| **Mie PM** | Capacitación Usuarios Finanzas | Lucía + JMB | 3h | Certificados |
| **Jue AM** | Capacitación Usuarios Supply | Lucía + JMB | 3h | Certificados |
| **Jue PM** | Sesión de refuerzo (todos) | Lucía + JMB | 2h | Certificados |
| **Vie** | Preparación final go-live | Todos | 2h | Checklist go-live |

**Hito Semana 21:** ✅ Capacitación completa, preparación go-live

---

### Semana 22 (5-11 mayo 2026): Ajustes Finales y Testing

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun-Mar** | Ajustes finales post-UAT | JMB | 12h | Dashboards refinados |
| **Mie** | Testing integral de todos los dashboards | JMB + Lucía | 6h | Checklist completo |
| **Jue** | Validación de RLS por todos los roles | JMB | 4h | RLS verificado |
| **Vie** | Revisión final con stakeholders | Todos + Stakeholders | 4h | Aprobación final |

**Hito Semana 22:** ✅ Todos los dashboards listos para go-live

---

### Semana 23 (12-18 mayo 2026): Go-Live y Cierre del Proyecto

| Día | Actividad | Responsable | Horas | Entregable |
|-----|-----------|-------------|-------|------------|
| **Lun** | **Go-Live Power BI** 🎉 | Todos | 2h | Dashboards en producción |
| **Mar** | Monitoreo post go-live | Todos | 4h | Reporte incidentes |
| **Mie** | Elaboración entregables Fase 3 (ML Roadmap) | JMB | 6h | Documentos Fase 3 |
| **Jue** | Documentación cierre proyecto | Linda | 4h | Reporte cierre |
| **Vie AM** | Reunión de cierre con stakeholders | Todos + Stakeholders | 2h | Acta de aceptación |
| **Vie PM** | Transferencia de conocimiento a TI | JMB + David Saboya | 3h | Handover técnico |

**Hito Semana 23:** ✅✅✅ **PROYECTO CERRADO FORMALMENTE**

---

## 9.5. Resumen de Fechas Clave (Actualizado)

---

## 9.6. Cronograma Consolidado (Gantt Simplificado)

```
PROYECTO ELANCO - CENTRALIZACIÓN DE DATOS DE ANÁLISIS
Duración: 24 semanas (incl. 1 semana vacacional) | Dic 2025 - Mayo 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FASE 0: Due Diligence (Semanas 1-5)
███████████ (1-dic a 12-ene)
    │
    ├─ S1: Kick-off + análisis inicial (1-dic)
    ├─ S2: Workshops priorización
    ├─ S3: Planificación detallada
    ├─ PAUSA VACACIONAL 🎄 (23-29 dic)
    ├─ S4: Documentación
    └─ S5: Go/No-Go ✓ (12-ene)

FASE 1: Data Lake (Semanas 6-15)
            ██████████████████████████████████████ (13-ene a 23-mar)
                    │
                    ├─ S6: Setup infraestructura
                    ├─ S7-8: Módulo FI (4 trans)
                    ├─ S9: Módulo SD (1 trans)
                    ├─ S10-12: Módulo MM (3 trans, incl. custom)
                    ├─ S13: Módulo CO (2 trans)
                    ├─ S14: Testing + documentación
                    └─ S15: Cierre Fase 1 ✓ (23-mar)

FASE 2: Dashboards (Semanas 16-23) [AJUSTADO: 8 semanas]
                                                ██████████████████████████ (24-mar a 18-may)
                                                        │
                                                        ├─ S16: Modelado dimensional
                                                        ├─ S17-18: Dashboards (3+3)
                                                        ├─ S19: Dashboards (3+3) + RLS
                                                        ├─ S20: UAT + ajustes
                                                        ├─ S21: Capacitación
                                                        ├─ S22: Testing final
                                                        └─ S23: Go-Live ✓✓✓ (18-may)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HITOS CLAVE:
🎄 Vacaciones (23-29 dic) | ✓ Go/No-Go (12-ene) | ✓ Data Lake (23-mar) | ✓✓✓ Go-Live (18-may)

NOTA: Fase 2 extendida de 7 a 8 semanas para cumplir restricción de JMB (máx 6h/día)
```

---

## 9.7. Hitos Críticos y Dependencias

### Hitos de Aprobación (Gates)

| Hito | Fecha | Criterio de Aceptación | Responsable Aprobación |
|------|-------|------------------------|------------------------|
| **Go/No-Go Fase 1** | 12-ene-2026 | Permisos SAP OK, ≥12 transacciones con tablas disponibles | Management Elanco |
| **Aceptación Fase 1** | 23-mar-2026 | 18 transacciones funcionales, validación >99% | Finanzas + Supply |
| **Aceptación UAT** | 27-abr-2026 | Dashboards aprobados, RLS validado | Stakeholders |
| **Go-Live Final** | 12-may-2026 | Capacitación completa, documentación entregada | Management Elanco |
| **Cierre Formal** | 18-may-2026 | Transferencia conocimiento, acta firmada | Management Elanco |

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

⚠️ **Vacaciones de fin de año (23-29 diciembre)**
- **Impacto:** Pausa de 1 semana durante Fase 0
- **Mitigación:** ✅ **YA CONSIDERADO** - Se agregó pausa formal de 1 semana en cronograma

⚠️ **Semana Santa 2026 (13-20 abril)**
- **Impacto:** Coincide con Semana 18 (desarrollo dashboards)
- **Mitigación:** Actividades de desarrollo individual, no requieren coordinación intensa

⚠️ **Cierre mensual contable (últimos 3 días del mes)**
- **Impacto:** Stakeholders de Finanzas menos disponibles
- **Mitigación:** Evitar workshops/validaciones críticas esos días
- **Meses afectados:** Diciembre, Enero, Febrero, Marzo, Abril

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

| Semana | Lucía R. | Juan M. B. | Linda L. | Stakeholders | Horas Totales |
|--------|----------|------------|----------|--------------|---------------|
| S1-5 (Fase 0) | 4-6h/sem | 10-12h/sem | 2h/sem | 4h/sem | 20-24h/sem |
| S6-15 (Fase 1) | 3-4h/sem | 15-18h/sem | 1h/sem | 1h/sem | 20-24h/sem |
| S16-22 (Fase 2) | 2-3h/sem | 28-30h/sem | 1h/sem | 2-4h/sem | 33-38h/sem |
| S23 (Cierre) | 2h | 6h | 4h | 2h | 14h |

**Nota:** Cargas part-time respetadas. JMB trabaja máximo 6h/día (30h/sem), trabajo sostenible.

---

## 9.10. Plan de Comunicación

### Reuniones Periódicas

| Reunión | Frecuencia | Participantes | Duración | Objetivo |
|---------|------------|---------------|----------|----------|
| **Daily Stand-up** | Lun-Vie | Lucía + JMB | 15 min | Sincronización diaria |
| **Weekly Status** | Viernes | Linda + Lucía + JMB | 30 min | Reporte semanal |
| **Sprint Review** | Cada 2 sem | Todos + Stakeholders | 1h | Demo de avances |
| **Steering Committee** | Mensual | Linda + Management | 1h | Status ejecutivo |

### Reportes

| Reporte | Frecuencia | Responsable | Destinatarios |
|---------|------------|-------------|---------------|
| Status Report Semanal | Viernes | Linda | Stakeholders Elanco |
| Dashboard de Seguimiento | Continuo | Linda | Equipo proyecto |
| Reporte de Riesgos | Quincenal | Linda + JMB | Management |
| Reporte Mensual Ejecutivo | Mensual | Linda | Management Elanco |

---

*Siguiente sección: [10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md](10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md)*
