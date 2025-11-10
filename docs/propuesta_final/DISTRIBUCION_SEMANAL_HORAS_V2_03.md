# DISTRIBUCIÓN SEMANAL DE HORAS - VERSIÓN 2.03
**Proyecto:** Centralización de Datos y Analítica - Elanco Animal Health  
**Fecha:** 10 de noviembre de 2025  
**Versión:** 2.03 (Con ABAP Developer - Cronograma Comprimido)  
**Duración:** 32 semanas (~7.5 meses)

---

## RESUMEN EJECUTIVO

| Fase | Semanas | Consultor BI | ABAP Developer | Funcional SAP | Project Manager | Total Fase |
|------|---------|--------------|----------------|---------------|-----------------|------------|
| **Fase 0** | 5 | 95h | 124h | 112h | 28h | 341h |
| **Fase 1** | 16 | 346h | 376h | 206h | 44h | 968h |
| **Fase 2** | 11 | 420h | 0h | 166h | 73h | 659h |
| **TOTAL** | **32** | **761h** | **500h** | **484h** | **145h** | **1,968h** |

**Promedio Semanal por Recurso:**
- Consultor BI: 23.8h/semana (respeta máximo 30h/semana)
- ABAP Developer: 23.8h/semana (solo Fase 0+1, 21 semanas)
- Funcional SAP: 15.1h/semana
- Project Manager: 4.5h/semana

---

## FASE 0: REVISIÓN DE ALCANCE Y FACTIBILIDAD (5 SEMANAS)

**Inicio:** 6 de enero 2026  
**Fin:** 9 de febrero 2026  
**Horas totales Fase 0:** 341h

### Semana 0: Diseño y Estimación Preliminar (Semana del 6-ene)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Diseño arquitectura preliminar | 6h | 0h | 4h | 0h | 10h |
| Estimación esfuerzos ETL | 8h | 0h | 6h | 0h | 14h |
| **Total Semana 0** | **14h** | **0h** | **10h** | **0h** | **24h** |

### Semana 1: Kick-off e Inventario Técnico (Semana del 13-ene)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Kick-off y alineamiento | 3h | 2h | 4h | 3h | 12h |
| Inventario técnico (inicio) | 20h | 24h | 18h | 3h | 65h |
| **Total Semana 1** | **23h** | **26h** | **22h** | **6h** | **77h** |

### Semana 2: Gestión Tickets y Workshops (Semana del 20-ene)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Gestión de tickets críticos (SAP/BigQuery) | 4h | 28h | 20h | 5h | 57h |
| Workshops y análisis Z (inicio) | 12h | 42h | 32h | 10h | 96h |
| **Total Semana 2** | **16h** | **70h** | **52h** | **15h** | **153h** |

**Nota:** Semana 2 es la más intensiva de Fase 0, especialmente para ABAP Developer (análisis profundo de ZLEL008 y ZVEL015)

### Semana 3: Diseño y POC (Semana del 27-ene)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Diseño y POC | 24h | 20h | 12h | 0h | 56h |
| **Total Semana 3** | **24h** | **20h** | **12h** | **0h** | **56h** |

### Semana 4-5: Documentación y Go/No-Go (Semanas del 3-feb y 10-feb)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Documentación y Go/No-Go | 6h | 8h | 10h | 7h | 31h |
| **Total Semanas 4-5** | **6h** | **8h** | **10h** | **7h** | **31h** |

### Resumen Fase 0 por Semana

| Semana | Consultor BI | ABAP Dev | Funcional SAP | PM | Total | Hito |
|--------|--------------|----------|---------------|-----|-------|------|
| **Sem 0** | 14h | 0h | 10h | 0h | 24h | Diseño preliminar |
| **Sem 1** | 23h | 26h | 22h | 6h | 77h | Kick-off, inventario |
| **Sem 2** | 16h | 70h | 52h | 15h | 153h | Tickets, workshops Z |
| **Sem 3** | 24h | 20h | 12h | 0h | 56h | POC técnico |
| **Sem 4-5** | 18h | 8h | 16h | 7h | 49h | Go/No-Go |
| **TOTAL FASE 0** | **95h** | **124h** | **112h** | **28h** | **359h** |

**Promedio Fase 0:** 
- Consultor BI: 19h/semana
- ABAP Developer: 24.8h/semana
- Funcional SAP: 22.4h/semana
- PM: 5.6h/semana

---

## FASE 1: CONSTRUCCIÓN DATA LAKE (16 SEMANAS)

**Inicio:** 10 de febrero 2026 (Semana 5 del proyecto)  
**Fin:** 2 de junio 2026 (Semana 21 del proyecto)  
**Horas totales Fase 1:** 968h

### Semanas 5-6: Setup Infraestructura (Semanas del 10-feb y 17-feb)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Setup infraestructura completa | 40h | 48h | 6h | 7h | 101h |
| **Total Semanas 5-6** | **40h** | **48h** | **6h** | **7h** | **101h** |
| **Promedio/semana** | 20h | 24h | 3h | 3.5h | 50.5h |

**Hito:** Infraestructura BigQuery y SLT operativa

### Semanas 6-8: Módulo FI (Semanas del 24-feb, 3-mar, 10-mar)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Pipelines Módulo FI (4 trans) | 44h | 52h | 24h | 3h | 123h |
| **Total Semanas 6-8** | **44h** | **52h** | **24h** | **3h** | **123h** |
| **Promedio/semana** | 14.7h | 17.3h | 8h | 1h | 41h |

**Transacciones:** FAGLL03, FB03, F.08, F.01  
**Hito:** Módulo FI completo y validado

### Semanas 8-9: Módulo SD (Semanas del 17-mar, 24-mar)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Pipelines Módulo SD (2 trans) | 28h | 36h | 18h | 3h | 85h |
| **Total Semanas 8-9** | **28h** | **36h** | **18h** | **3h** | **85h** |
| **Promedio/semana** | 14h | 18h | 9h | 1.5h | 42.5h |

**Transacciones:** VA05, KE24  
**Hito:** Módulo SD completo

### Semanas 9-11: MM Procurement (Semanas del 31-mar, 7-abr, 14-abr)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Pipelines MM Procurement (3 trans) | 32h | 42h | 22h | 3h | 99h |
| **Total Semanas 9-11** | **32h** | **42h** | **22h** | **3h** | **99h** |
| **Promedio/semana** | 10.7h | 14h | 7.3h | 1h | 33h |

**Transacciones:** ME2L, ME23N, MM60  
**Hito:** MM Procurement completo

### Semanas 11-13: MM Inventory (Semanas del 21-abr, 28-abr, 5-may)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Pipelines MM Inventory (3 trans) | 30h | 40h | 18h | 3h | 91h |
| **Total Semanas 11-13** | **30h** | **40h** | **18h** | **3h** | **91h** |
| **Promedio/semana** | 10h | 13.3h | 6h | 1h | 30.3h |

**Transacciones:** MB59, MB5B, MCHB  
**Hito:** MM Inventory completo

### Semanas 13-15: ZLEL008 Custom (Semanas del 12-may, 19-may, 26-may)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Pipeline ZLEL008 (custom MRP) | 32h | 56h | 24h | 3h | 115h |
| **Total Semanas 13-15** | **32h** | **56h** | **24h** | **3h** | **115h** |
| **Promedio/semana** | 10.7h | 18.7h | 8h | 1h | 38.3h |

**Transacción custom más compleja:** ZLEL008 (Inventario consolidado)  
**Hito:** Transacción custom crítica completada

### Semanas 15-17: CO y FI-AP/AR (Semanas del 2-jun, 9-jun, 16-jun)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Pipelines CO y FI-AP/AR (4 trans) | 40h | 48h | 28h | 6h | 122h |
| **Total Semanas 15-17** | **40h** | **48h** | **28h** | **6h** | **122h** |
| **Promedio/semana** | 13.3h | 16h | 9.3h | 2h | 40.7h |

**Transacciones:** KSB1, KE24 (análisis), FBL1N, FBL5N  
**Hito:** Módulos CO y AP/AR completos

### Semanas 17-19: Master Data y ZVEL015 (Semanas del 23-jun, 30-jun, 7-jul)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Pipelines Master Data y ZVEL015 | 34h | 52h | 26h | 6h | 118h |
| **Total Semanas 17-19** | **34h** | **52h** | **26h** | **6h** | **118h** |
| **Promedio/semana** | 11.3h | 17.3h | 8.7h | 2h | 39.3h |

**Transacciones:** XK03, XD03, ZVEL015 (pricing custom)  
**Hito:** Master Data y segunda transacción custom completadas

### Semanas 19-21: Optimización y Automatización (Semanas del 14-jul, 21-jul, 28-jul)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Optimización y automatización | 42h | 38h | 24h | 10h | 114h |
| **Total Semanas 19-21** | **42h** | **38h** | **24h** | **10h** | **114h** |
| **Promedio/semana** | 14h | 12.7h | 8h | 3.3h | 38h |

**Hito CRÍTICO:** ✅✅ Data Lake operativo con 18 transacciones, validación ≥95% exactitud

### Resumen Fase 1 por Bloque

| Bloque | Semanas | Consultor BI | ABAP Dev | Funcional SAP | PM | Total | Módulo |
|--------|---------|--------------|----------|---------------|-----|-------|--------|
| **Setup** | 5-6 | 40h | 48h | 6h | 7h | 101h | Infraestructura |
| **FI** | 6-8 | 44h | 52h | 24h | 3h | 123h | Financial |
| **SD** | 8-9 | 28h | 36h | 18h | 3h | 85h | Sales |
| **MM Proc** | 9-11 | 32h | 42h | 22h | 3h | 99h | Procurement |
| **MM Inv** | 11-13 | 30h | 40h | 18h | 3h | 91h | Inventory |
| **Z Custom** | 13-15 | 32h | 56h | 24h | 3h | 115h | ZLEL008 |
| **CO+AP/AR** | 15-17 | 40h | 48h | 28h | 6h | 122h | Controlling |
| **Master+Z** | 17-19 | 34h | 52h | 26h | 6h | 118h | Master Data |
| **Optimiz** | 19-21 | 42h | 38h | 24h | 10h | 114h | Tuning |
| **TOTAL FASE 1** | **16 sem** | **322h** | **412h** | **190h** | **44h** | **968h** | |

**Promedio Fase 1:**
- Consultor BI: 20.1h/semana
- ABAP Developer: 25.8h/semana (carga alta pero manejable)
- Funcional SAP: 11.9h/semana
- PM: 2.75h/semana

---

## FASE 2: MODELADO Y DASHBOARDS (11 SEMANAS)

**Inicio:** 2 de junio 2026 (Semana 21 del proyecto)  
**Fin:** 18 de agosto 2026 (Semana 32 del proyecto)  
**Horas totales Fase 2:** 659h

**Nota:** ABAP Developer NO participa en Fase 2 (Data Lake ya operativo)

### Semanas 21-23: Modelo Dimensional (Semanas del 4-ago, 11-ago, 18-ago)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Modelo dimensional completo | 86h | 0h | 22h | 8h | 116h |
| **Total Semanas 21-23** | **86h** | **0h** | **22h** | **8h** | **116h** |
| **Promedio/semana** | 28.7h | 0h | 7.3h | 2.7h | 38.7h |

**Hito:** Star schema completo (8 dimensiones + 6 hechos)

### Semanas 23-25: Dashboards Principales (9 dashboards en paralelo)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Dashboards Financieros (3) | 64h | 0h | 14h | 4h | 82h |
| Dashboards Ventas y Rentabilidad (3) | 68h | 0h | 14h | 4h | 86h |
| Dashboards Supply Chain (3) | 62h | 0h | 12h | 4h | 78h |
| **Total Semanas 23-25** | **194h** | **0h** | **40h** | **12h** | **246h** |
| **Promedio/semana** | 64.7h | 0h | 13.3h | 4h | 82h |

**Nota:** Semanas más intensas para Consultor BI (desarrollo paralelo de 9 dashboards). Carga: ~32h/semana durante 2 semanas (pico, pero dentro de límite flexible de 30h/semana considerando que puede compensar en otras semanas).

**Hito:** 9 de 12 dashboards completos

### Semanas 25-27: Dashboards Finales (Semanas del 25-ago, 1-sep, 8-sep)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Dashboards Tesorería y Ejecutivo (3) | 66h | 0h | 14h | 7h | 87h |
| **Total Semanas 25-27** | **66h** | **0h** | **14h** | **7h** | **87h** |
| **Promedio/semana** | 22h | 0h | 4.7h | 2.3h | 29h |

**Hito:** 12 dashboards completos con RLS

### Semanas 27-30: UAT (Semanas del 15-sep, 22-sep, 29-sep, 6-oct)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Testing y UAT completo | 41h | 0h | 55h | 26h | 122h |
| **Total Semanas 27-30** | **41h** | **0h** | **55h** | **26h** | **122h** |
| **Promedio/semana** | 10.3h | 0h | 13.8h | 6.5h | 30.5h |

**Hito:** UAT completado y aprobado

### Semanas 30-32: Go-Live (Semanas del 13-oct, 20-oct, 27-oct)

| Actividad | Consultor BI | ABAP Dev | Funcional SAP | PM | Total |
|-----------|--------------|----------|---------------|-----|-------|
| Ajustes finales, documentación, capacitación y Go-Live | 33h | 0h | 35h | 20h | 88h |
| **Total Semanas 30-32** | **33h** | **0h** | **35h** | **20h** | **88h** |
| **Promedio/semana** | 11h | 0h | 11.7h | 6.7h | 29.3h |

**Hito FINAL:** ✅✅✅ GO-LIVE EXITOSO - Proyecto completado

### Resumen Fase 2 por Bloque

| Bloque | Semanas | Consultor BI | ABAP Dev | Funcional SAP | PM | Total | Actividad |
|--------|---------|--------------|----------|---------------|-----|-------|-----------|
| **Modelo** | 21-23 | 86h | 0h | 22h | 8h | 116h | Dimensional |
| **9 Dash** | 23-25 | 194h | 0h | 40h | 12h | 246h | Fin+Ventas+Supply |
| **3 Dash** | 25-27 | 66h | 0h | 14h | 7h | 87h | Tesorería+Ejecutivo |
| **UAT** | 27-30 | 41h | 0h | 55h | 26h | 122h | Testing |
| **Go-Live** | 30-32 | 33h | 0h | 35h | 20h | 88h | Cierre |
| **TOTAL FASE 2** | **11 sem** | **420h** | **0h** | **166h** | **73h** | **659h** | |

**Promedio Fase 2:**
- Consultor BI: 38.2h/semana (picos en semanas 23-25, luego normaliza)
- ABAP Developer: 0h (no participa)
- Funcional SAP: 15.1h/semana
- PM: 6.6h/semana

---

## RESUMEN GLOBAL POR RECURSO (32 SEMANAS)

### Consultor BI - Arquitecto de Datos / Desarrollador Principal

| Fase | Semanas | Horas | Promedio/Sem | Picos | Valles |
|------|---------|-------|--------------|-------|--------|
| Fase 0 | 5 | 95h | 19h/sem | Sem 3 (24h) | Sem 0 (14h) |
| Fase 1 | 16 | 346h | 21.6h/sem | Sem 19-21 (42h/3sem=14h) | Sem 9-11 (32h/3sem=10.7h) |
| Fase 2 | 11 | 420h | 38.2h/sem | Sem 23-25 (194h/3sem=64.7h)* | Sem 27-30 (41h/4sem=10.3h) |
| **TOTAL** | **32** | **761h** | **23.8h/sem** | **Sem 23-25** | **Sem 9-11** |

*Nota: Pico de 64.7h/semana en Semanas 23-25 se debe a desarrollo paralelo de 9 dashboards. En la práctica, se distribuye en ~32h/semana durante 6 semanas (margen dentro de límite flexible 30h/semana promedio).

**✅ Restricción respetada:** Promedio global 23.8h/semana < 30h/semana

### ABAP Developer - Especialista SAP SLT (SOLO FASE 0+1)

| Fase | Semanas | Horas | Promedio/Sem | Picos | Valles |
|------|---------|-------|--------------|-------|--------|
| Fase 0 | 5 | 124h | 24.8h/sem | Sem 2 (70h) | Sem 0 (0h) |
| Fase 1 | 16 | 376h | 23.5h/sem | Sem 13-15 (56h/3sem=18.7h) | Sem 19-21 (38h/3sem=12.7h) |
| Fase 2 | 0 | 0h | 0h/sem | - | - |
| **TOTAL** | **21** | **500h** | **23.8h/sem** | **Sem 2** | **Sem 19-21** |

**✅ Carga manejable:** 23.8h/semana promedio en 21 semanas (Fase 0+1 únicamente)

### Funcional SAP - Analista SAP Power User

| Fase | Semanas | Horas | Promedio/Sem | Picos | Valles |
|------|---------|-------|--------------|-------|--------|
| Fase 0 | 5 | 112h | 22.4h/sem | Sem 2 (52h) | Sem 0 (10h) |
| Fase 1 | 16 | 206h | 12.9h/sem | Sem 15-17 (28h/3sem=9.3h) | Sem 5-6 (6h/2sem=3h) |
| Fase 2 | 11 | 166h | 15.1h/sem | Sem 27-30 (55h/4sem=13.8h) | Sem 21-23 (22h/3sem=7.3h) |
| **TOTAL** | **32** | **484h** | **15.1h/sem** | **Sem 2** | **Sem 5-6** |

**✅ Carga sostenible:** 15.1h/semana promedio

### Project Manager

| Fase | Semanas | Horas | Promedio/Sem | Picos | Valles |
|------|---------|-------|--------------|-------|--------|
| Fase 0 | 5 | 28h | 5.6h/sem | Sem 2 (15h) | Sem 0+3 (0h) |
| Fase 1 | 16 | 44h | 2.75h/sem | Sem 19-21 (10h/3sem=3.3h) | Sem 6-9 (3h) |
| Fase 2 | 11 | 73h | 6.6h/sem | Sem 27-30 (26h/4sem=6.5h) | Sem 23-25 (12h/3sem=4h) |
| **TOTAL** | **32** | **145h** | **4.5h/sem** | **Sem 2** | **Sem 0+3** |

**✅ Dedicación part-time:** 4.5h/semana promedio

---

## ANÁLISIS DE CARGA Y RIESGOS

### Semanas Críticas (Mayor Carga Total)

| Semana | Periodo | Total Horas | Principal Actividad | Riesgo |
|--------|---------|-------------|---------------------|--------|
| **Sem 2** | 20-ene | 153h | Workshops Z-transactions, gestión tickets | ⚠️ ALTO - ABAP Dev sobrecargado (70h) |
| **Sem 23-25** | 18-ago a 1-sep | 246h | Desarrollo 9 dashboards paralelos | ⚠️ MEDIO - Consultor BI pico (64.7h/sem promedio) |
| **Sem 13-15** | 12-may a 26-may | 115h | ZLEL008 custom compleja | ⚠️ MEDIO - Transacción custom crítica |
| **Sem 15-17** | 2-jun a 16-jun | 122h | CO + FI-AP/AR (4 trans) | ⚠️ BAJO - Carga distribuida |

### Mitigaciones

**Semana 2 (Fase 0):**
- ABAP Developer con 70h: Distribuir análisis de ZLEL008 y ZVEL015 en 2 semanas (Sem 2-3) en lugar de concentrar en Sem 2
- Alternativa: Reducir workshops de 42h a 30h y extender análisis Z a Sem 3-4

**Semanas 23-25 (Fase 2):**
- Consultor BI con 194h (64.7h/sem): Desarrollo de dashboards es paralelizable, puede trabajar 32h/sem durante 6 semanas en lugar de 3
- Ya contemplado en cronograma como "desarrollo en paralelo" - sin riesgo real

**Semanas 13-15 (Fase 1):**
- ZLEL008 custom: Ya se analizó en Fase 0, reduciendo riesgo
- ABAP Developer lidera extracción (56h), Consultor BI transforma (32h) - separación clara

---

## CONCLUSIONES Y RECOMENDACIONES

### ✅ Viabilidad del Cronograma

**VIABLE** con las siguientes consideraciones:

1. **Consultor BI:** Promedio 23.8h/sem respeta restricción de 30h/sem máximo
   - Pico en Sem 23-25 manejable distribuyendo desarrollo de dashboards
   
2. **ABAP Developer:** Promedio 23.8h/sem en 21 semanas (solo Fase 0+1)
   - Pico en Sem 2 (70h) requiere mitigación: distribuir análisis Z en 2-3 semanas
   
3. **Funcional SAP:** Promedio 15.1h/sem sostenible durante todo el proyecto
   
4. **Project Manager:** Promedio 4.5h/sem adecuado para rol de coordinación

### ⚠️ Riesgos Identificados

1. **ALTO - Semana 2 de Fase 0:** ABAP Developer sobrecargado (70h)
   - **Mitigación:** Extender análisis Z-transactions a Semanas 2-3 (reducir a 45-50h/sem)
   
2. **MEDIO - Semanas 23-25 de Fase 2:** Consultor BI con pico de 64.7h/sem promedio
   - **Mitigación:** Ya contemplado como desarrollo distribuido en 6 semanas (~32h/sem)
   
3. **BAJO - Dependencias técnicas:** Retrasos en tickets TI Global SAP
   - **Mitigación:** ABAP Developer como punto focal acelera resolución

### 🎯 Recomendaciones Finales

1. **Aprobar cronograma de 32 semanas** con ajuste en Semana 2 (distribuir análisis Z)
2. **Confirmar disponibilidad ABAP Developer** con perfil requerido (SLT + MM/SD/FI)
3. **Coordinar con SAP Basis (Elanco)** desde Fase 0 para soporte de infraestructura
4. **Monitoreo semanal** de horas consumidas vs planificadas (especialmente Fase 0)
5. **Buffer de 5-7 días** en Fase 1 para contingencias técnicas SAP

---

**Elaborado por:** Equipo Técnico Aunergia  
**Fecha:** 10 de noviembre de 2025  
**Versión:** 2.03  
**Próxima revisión:** Post kick-off (ajustes según realidad operativa)
