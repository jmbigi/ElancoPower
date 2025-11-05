# 9. CRONOGRAMA SEMANAL DEL PROYECTO

## 9.1. Vista General del Cronograma

**Duración Total:** 24 semanas (~6 meses, incluyendo 1 semana vacacional)  
**Inicio:** Mes 1, Semana 1  
**Finalización:** Mes 6, Semana 23

```
FASE 0          VACACIONES  FASE 1                    FASE 2          
────────        ─────────   ──────────────────────    ──────────────────────    
5 sem           1 sem       10 sem                    8 sem         
███████         ░░░░░░░     ███████████████████████   ████████████████████████  
                                                          
Mes 1           Sem 4       Mes 2                     Mes 4      Mes 6
Sem 1-5         (pausa)     Sem 6-15                  Sem 16-23
```

**Nota:** Se incluye 1 semana de pausa vacacional durante festividades de fin de año (incluida en el cronograma).  
**Restricción:** Juan Manuel Bigi trabaja máximo 6 horas/día (30h/semana), ajustando Fase 2 a 8 semanas.

---

## 9.2. FASE 0 - Due Diligence (Mes 1, Semanas 1-5)

### Semana 1: Kick-off y Análisis Inicial

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Kick-off meeting con stakeholders | Linda + Todos + Stakeholders | 3h | Minutas kick-off |
| Análisis dataset CASA en BigQuery | JMB | 8h | Inventario tablas disponibles |
| Seguimiento Ticket SAP-48219 (permisos) | Lucía | 4h | Status report |
| Prueba conectividad Power BI ↔ BigQuery | JMB | 4h | POC funcional (.pbix) |
| Seguimiento Tickets BQ (tablas) | Lucía | 4h | Status report |
| Preparación workshop priorización | Lucía + JMB | 4h | Agenda + materiales |

**Hito Semana 1:** ✅ Inventario técnico completado, status de tickets críticos

---

### Semana 2: Workshops y Validación

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Workshop Finanzas (priorización trans) | Todos + Stakeholders | 4h + 4h stakeholders | Scoring transacciones FI/CO |
| Workshop Supply (priorización trans) | Todos + Stakeholders | 4h + 4h stakeholders | Scoring transacciones MM/SD |
| Análisis de transacciones custom (ZLEL008) | Lucía | 4h | Documentación tablas Z |
| Benchmarks performance BigQuery | JMB | 6h | Resultados queries |
| Workshop consolidación (priorización) | Todos + Stakeholders | 4h + 4h stakeholders | Backlog priorizado |

**Hito Semana 2:** ✅ Backlog de 18 transacciones priorizado y aprobado

---

### Semana 3: Planificación Detallada

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Plan de extracción por módulo SAP | JMB | 6h | Roadmap Fase 1 |
| Definición arquitectura zonas (RAW/PROCESSED/CURATED) | JMB | 4h | Diagrama arquitectura |
| Análisis de riesgos y mitigaciones | Lucía + JMB | 4h | Matriz de riesgos |
| Estimación de esfuerzos Fase 1 | JMB | 4h | Matriz estimación horas |
| Seguimiento tickets críticos | Lucía | 4h | Status report |

**Hito Semana 3:** ✅ Plan técnico Fase 1 completo

---

### **PAUSA VACACIONAL (Durante Semana 4)** 🎄

⏸️ **Semana de pausa por festividades de fin de año**
- Sin actividades programadas
- Equipo en descanso vacacional
- Proyecto se retoma después de la pausa

---

### Semana 4: Documentación y Preparación Go/No-Go

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Documentación entregables Fase 0 | JMB | 8h | 7 documentos Fase 0 |
| Revisión interna documentos | Linda + Lucía + JMB | 4h | Documentos revisados |
| Validación con TI (David Saboya) | Lucía + JMB | 2h | Confirmaciones técnicas |
| Preparación presentación Go/No-Go | Linda + JMB | 4h | Presentación |

**Nota:** Semana post-vacacional, puede tener días festivos según país.

**Hito Semana 4:** ✅ Documentación Fase 0 completa

---

### Semana 5: Go/No-Go y Cierre Fase 0

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Distribución materiales Go/No-Go | Linda | 2h | Documentos enviados |
| **Reunión Go/No-Go** | Todos + Stakeholders + Management | 2h | Decisión documentada |
| Ajustes post Go/No-Go (si aplica) | JMB | 4h | Plan actualizado |
| Preparación kick-off Fase 1 | Todos | 3h | Agenda Fase 1 |
| Cierre administrativo Fase 0 | Linda | 2h | Reporte cierre |

**Hito Semana 5:** ✅✅ Decisión Go/No-Go emitida, Fase 1 aprobada para iniciar

---

## 9.3. FASE 1 - Construcción Data Lake (Mes 2-3, Semanas 6-15)

### Semana 6: Setup Infraestructura + Inicio Módulo FI

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Kick-off Fase 1 | Todos | 2h | Minutas |
| Setup datasets BigQuery (RAW/PROCESSED/CURATED) | JMB | 6h | Datasets configurados |
| Configuración conectores SAP ↔ BigQuery | JMB | 6h | Conectores activos |
| Inicio desarrollo FAGLL03 (mayor general) | JMB | 8h | Pipeline RAW FAGLL03 |

**Hito Semana 6:** ✅ Infraestructura BigQuery lista

---

### Semana 7: Módulo FI - Parte 1

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| FAGLL03 - Layers PROCESSED y CURATED | JMB | 10h | Pipeline completo FAGLL03 |
| Validación FAGLL03 con Finanzas | Lucía + Stakeholders | 3h | Validación OK |
| Desarrollo FB03 (documentos contables) | JMB | 8h | Pipeline RAW/PROCESSED FB03 |

**Hito Semana 7:** ✅ FAGLL03 completo y validado

---

### Semana 8: Módulo FI - Parte 2

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| FB03 - Layer CURATED | JMB | 4h | Pipeline completo FB03 |
| Desarrollo F.08 (balance comprobación) | JMB | 8h | Pipeline F.08 |
| Desarrollo F.01 (estado situación) | JMB | 8h | Pipeline F.01 |
| Testing integral módulo FI | JMB + Lucía | 4h | 4 transacciones validadas |

**Hito Semana 8:** ✅ Módulo FI completo (4 transacciones)

---

### Semana 9: Módulo SD

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Desarrollo VA05 (órdenes abiertas) - RAW | JMB | 8h | Pipeline RAW VA05 |
| VA05 - PROCESSED (joins, cálculos) | JMB | 8h | Pipeline PROCESSED VA05 |
| VA05 - CURATED y testing | JMB | 6h | Pipeline completo VA05 |

**Hito Semana 9:** ✅ VA05 completo y validado

---

### Semana 10: Módulo MM - Parte 1

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Validación VA05 con Supply | Lucía + Stakeholders | 2h | Validación OK |
| Desarrollo ME2L (purchase orders) | JMB | 10h | Pipeline completo ME2L |
| Desarrollo MB5B (stock materiales) | JMB | 10h | Pipeline completo MB5B |

**Hito Semana 10:** ✅ ME2L y MB5B completos

---

### Semana 11: Módulo MM - ZLEL008 (Parte 1 - Custom)

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Análisis técnico ZLEL008 (código ABAP) | Lucía + Consultor ABAP | 6h | Documentación tablas Z |
| Identificación tablas fuente ZLEL008 | JMB | 8h | Mapeo tablas SAP |
| Desarrollo pipeline RAW ZLEL008 | JMB | 8h | Pipeline RAW ZLEL008 |

**Hito Semana 11:** ✅ Análisis ZLEL008 completo, pipeline RAW funcional

---

### Semana 12: Módulo MM - ZLEL008 (Parte 2)

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| ZLEL008 - Replicación lógica en BigQuery SQL | JMB | 10h | Pipeline PROCESSED |
| ZLEL008 - Layer CURATED | JMB | 4h | Pipeline completo ZLEL008 |
| Validación exhaustiva ZLEL008 | JMB + Lucía | 4h | Reconciliación SAP ↔ BQ |
| Ajustes ZLEL008 (si necesario) | JMB | 4h | Pipeline ajustado |

**Hito Semana 12:** ✅ ZLEL008 completo (transacción custom más compleja)

---

### Semana 13: Módulo CO

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Desarrollo KSB1 (OPEX) | JMB | 12h | Pipeline completo KSB1 |
| Validación KSB1 con Finanzas | Lucía + Stakeholders | 2h | Validación OK |
| Desarrollo KE24 (CO-PA rentabilidad) | JMB | 10h | Pipeline completo KE24 |

**Hito Semana 13:** ✅ Módulo CO completo (2 transacciones)

---

### Semana 14: Testing Integral y Documentación

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Testing integral 18 transacciones | JMB + Lucía | 6h | Matriz validación |
| Ajustes identificados en testing | JMB | 6h | Pipelines ajustados |
| Documentación diccionarios de datos | JMB | 6h | 18 diccionarios |
| Documentación técnica arquitectura | JMB | 4h | Guía arquitectura |
| Documentación runbooks operativos | JMB | 4h | Runbooks |

**Hito Semana 14:** ✅ Testing completo, documentación técnica entregada

---

### Semana 15: Transacciones Restantes y Cierre Fase 1

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Desarrollo transacciones pendientes (si aplica) | JMB | 8h | Pipelines adicionales |
| Testing transacciones adicionales | JMB + Lucía | 4h | Validaciones |
| Revisión final calidad de datos | JMB | 4h | Reporte calidad |
| Preparación demo Fase 1 | Todos | 3h | Presentación |
| **Demo Fase 1 + Cierre** | Todos + Stakeholders | 2h | Aceptación Fase 1 |

**Hito Semana 15:** ✅✅ Fase 1 completa, Data Lake operativo con 18 transacciones

---

## 9.4. FASE 2 - Dashboards Power BI (Mes 4-6, Semanas 16-23)

### Semana 16: Modelado Dimensional

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Kick-off Fase 2 | Todos | 2h | Minutas |
| Diseño de dimensiones (8 dimensiones) | JMB | 12h | ERD dimensiones |
| Diseño de tablas de hechos (6 hechos) | JMB | 12h | ERD hechos |
| Definición de relaciones | JMB | 4h | Diagrama relaciones |

**Hito Semana 16:** ✅ Modelo dimensional diseñado

---

### Semana 17: Capa Semántica y Desarrollo Dashboards (Parte 1)

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Desarrollo vistas BigQuery (vw_ventas, vw_inventario, etc.) | JMB | 8h | 10 vistas de negocio |
| Validación modelo con stakeholders | Todos + Stakeholders | 3h | Modelo aprobado |
| Desarrollo Dashboard Financiero (página 1-2) | JMB | 8h | Dashboard 40% |
| Dashboard Financiero (página 3 + ajustes) | JMB | 8h | Dashboard Financiero v1 |

**Hito Semana 17:** ✅ Dashboard Financiero funcional

---

### Semana 18: Desarrollo Dashboards (Parte 2)

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Desarrollo Dashboard de Ventas | JMB | 10h | Dashboard Ventas v1 |
| Desarrollo Dashboard de Inventario | JMB | 10h | Dashboard Inventario v1 |
| Revisión iterativa con usuarios | Lucía + Stakeholders | 4h | Feedback |

**Hito Semana 18:** ✅ 3 dashboards funcionales

---

### Semana 19: Dashboards Finales + RLS

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Desarrollo Dashboard OPEX | JMB | 8h | Dashboard OPEX v1 |
| Desarrollo Dashboard Ejecutivo | JMB | 8h | Dashboard Ejecutivo v1 |
| Desarrollo dashboards adicionales (Supply, Compras, etc.) | JMB | 6h | Dashboards adicionales v1 |
| Configuración Row-Level Security (RLS) | JMB | 10h | RLS configurado |

**Hito Semana 19:** ✅ Todos los dashboards con RLS

---

### Semana 20: UAT y Ajustes

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| UAT con Finanzas (dashboards FI, OPEX, Ejecutivo) | Todos + Stakeholders | 4h + 4h stakeholders | Feedback Finanzas |
| UAT con Supply (dashboards Ventas, Inventario, Supply) | Todos + Stakeholders | 4h + 4h stakeholders | Feedback Supply |
| Consolidación feedback y priorización ajustes | Todos | 3h | Lista ajustes |
| Implementación ajustes post-UAT | JMB | 12h | Dashboards ajustados |

**Hito Semana 20:** ✅ UAT completado, ajustes implementados

---

### Semana 21: Capacitación y Preparación Go-Live

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Documentación Manual de Usuario | JMB + Lucía | 6h | Manual usuarios |
| Grabación videos tutoriales (6 videos) | JMB + Lucía | 4h | 6 videos |
| Capacitación Power Users | Lucía + JMB | 4h | Certificados |
| Capacitación Usuarios Finanzas | Lucía + JMB | 3h | Certificados |
| Capacitación Usuarios Supply | Lucía + JMB | 3h | Certificados |
| Sesión de refuerzo (todos) | Lucía + JMB | 2h | Certificados |
| Preparación final go-live | Todos | 2h | Checklist go-live |

**Hito Semana 21:** ✅ Capacitación completa, preparación go-live

---

### Semana 22: Ajustes Finales y Testing

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| Ajustes finales post-UAT | JMB | 12h | Dashboards refinados |
| Testing integral de todos los dashboards | JMB + Lucía | 6h | Checklist completo |
| Validación de RLS por todos los roles | JMB | 4h | RLS verificado |
| Revisión final con stakeholders | Todos + Stakeholders | 4h | Aprobación final |

**Hito Semana 22:** ✅ Todos los dashboards listos para go-live

---

### Semana 23: Go-Live y Cierre del Proyecto

| Actividad | Responsable | Horas | Entregable |
|-----------|-------------|-------|------------|
| **Go-Live Power BI** 🎉 | Todos | 2h | Dashboards en producción |
| Monitoreo post go-live | Todos | 4h | Reporte incidentes |
| Elaboración entregables Fase 3 (ML Roadmap) | JMB | 6h | Documentos Fase 3 |
| Documentación cierre proyecto | Linda | 4h | Reporte cierre |
| Reunión de cierre con stakeholders | Todos + Stakeholders | 2h | Acta de aceptación |
| Transferencia de conocimiento a TI | JMB + David Saboya | 3h | Handover técnico |

**Hito Semana 23:** ✅✅✅ **PROYECTO CERRADO FORMALMENTE**

---

## 9.5. Resumen de Hitos Clave

| Hito | Semana | Descripción |
|------|--------|-------------|
| **Inicio Proyecto** | Mes 1, Sem 1 | Kick-off y análisis inicial |
| **Go/No-Go** | Mes 1, Sem 5 | Decisión de continuar a Fase 1 |
| **Fin Fase 1** | Mes 3, Sem 15 | Data Lake operativo |
| **Fin UAT** | Mes 5, Sem 20 | Dashboards validados |
| **Go-Live** | Mes 6, Sem 23 | Sistema en producción |
| **Cierre Formal** | Mes 6, Sem 23 | Proyecto completado |

---

## 9.6. Cronograma Consolidado (Gantt Simplificado)

```
PROYECTO ELANCO - CENTRALIZACIÓN DE DATOS DE ANÁLISIS
Duración: 24 semanas (incl. 1 semana vacacional) | ~6 meses
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FASE 0: Due Diligence (Semanas 1-5)
███████████ (Mes 1)
    │
    ├─ S1: Kick-off + análisis inicial
    ├─ S2: Workshops priorización
    ├─ S3: Planificación detallada
    ├─ PAUSA VACACIONAL 🎄 (Sem 4)
    ├─ S4: Documentación
    └─ S5: Go/No-Go ✓

FASE 1: Data Lake (Semanas 6-15)
            ██████████████████████████████████████ (Mes 2-3)
                    │
                    ├─ S6: Setup infraestructura
                    ├─ S7-8: Módulo FI (4 trans)
                    ├─ S9: Módulo SD (1 trans)
                    ├─ S10-12: Módulo MM (3 trans, incl. custom)
                    ├─ S13: Módulo CO (2 trans)
                    ├─ S14: Testing + documentación
                    └─ S15: Cierre Fase 1 ✓

FASE 2: Dashboards (Semanas 16-23)
                                                ██████████████████████████ (Mes 4-6)
                                                        │
                                                        ├─ S16: Modelado dimensional
                                                        ├─ S17-18: Dashboards (Parte 1)
                                                        ├─ S19: Dashboards (Parte 2) + RLS
                                                        ├─ S20: UAT + ajustes
                                                        ├─ S21: Capacitación
                                                        ├─ S22: Testing final
                                                        └─ S23: Go-Live ✓✓✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HITOS CLAVE:
🎄 Vacaciones (Sem 4) | ✓ Go/No-Go (Sem 5) | ✓ Data Lake (Sem 15) | ✓✓✓ Go-Live (Sem 23)

NOTA: Fase 2 de 8 semanas para cumplir restricción de JMB (máx 6h/día)
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
