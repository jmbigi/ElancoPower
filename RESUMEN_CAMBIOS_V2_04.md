# RESUMEN DE CAMBIOS - VERSIÓN 2.04
**Fecha:** 10 de noviembre de 2025  
**Proyecto:** Centralización de Datos y Analítica - Elanco Animal Health

---

## OBJETIVO DE LA VERSIÓN 2.04

**Equilibrar:**
- ✅ Reducción moderada de cronograma: -6 semanas (no -10)
- ✅ Incremento controlado de esfuerzo: +290h (+18%, no +378h/+24%)
- ✅ Carga sostenible de Consultor BI: 26h/semana (no comprimir demasiado)
- ✅ ABAP Developer con rol reducido: 270h (no 436h)

---

## COMPARATIVA DE VERSIONES

### Tabla Resumen

| Métrica | V 2.02 Original | V 2.03 Agresiva | V 2.04 Optimizada | Delta V2.04 vs V2.02 |
|---------|-----------------|-----------------|-------------------|----------------------|
| **Duración** | 42 semanas | 32 semanas | **36 semanas** | **-6 sem (-14.3%)** |
| **Esfuerzo Total** | 1,590h | 1,968h | **1,880h** | **+290h (+18.2%)** |
| **Consultor BI** | 961h | 761h | **935h** | **-26h (-2.7%)** |
| **ABAP Developer** | 0h | 436h | **270h** | **+270h (NUEVO)** |
| **Funcional SAP** | 484h | 484h | **512h** | **+28h (+5.8%)** |
| **Project Manager** | 145h | 145h | **163h** | **+18h (+12.4%)** |
| **Go-Live** | Oct 2026 | Ago 2026 | **Sep 2026** | **-1 mes** |
| **BI h/semana** | 22.9h | 23.8h | **26.0h** | **+3.1h/sem** |
| **ABAP h/semana** | N/A | 23.8h (21 sem) | **10.4h (26 sem)** | **Carga baja** |

### Análisis de Trade-offs

**V2.03 (Agresiva):**
- ✅ Máxima reducción de tiempo (-10 semanas)
- ❌ Alto incremento de costo (+378h, +24%)
- ❌ ABAP Developer casi tiempo completo (23.8h/sem)
- ⚠️ Riesgo de coordinación alta (4 recursos con alta dedicación)

**V2.04 (Optimizada):**
- ✅ Buena reducción de tiempo (-6 semanas)
- ✅ Incremento moderado de costo (+290h, +18%)
- ✅ ABAP Developer en rol de consultoría (10.4h/sem)
- ✅ Consultor BI con carga sostenible (26h/sem)
- ✅ Mejor balance costo-beneficio

---

## CAMBIOS EN EL ABAP DEVELOPER

### Reducción de Responsabilidades (436h → 270h)

**V2.03: ABAP Developer "Full-Time" (436h)**
- Configuración completa y profunda de SAP SLT
- Extracción detallada de todas las transacciones
- Monitoreo continuo y proactivo de SLT
- Gestión intensiva de todos los tickets SAP
- Análisis exhaustivo de Z-transactions
- Desarrollo de scripts ABAP custom si necesario

**V2.04: ABAP Developer "Consultoría Especializada" (270h)**
- ✅ Configuración inicial de SAP SLT (crítico)
- ✅ Análisis profundo de Z-transactions (ZLEL008, ZVEL015)
- ✅ Apoyo puntual en extracción de datos complejos
- ✅ Consultoría en tickets SAP críticos
- ✅ Validación técnica de extracción SAP → RAW
- ❌ NO monitoreo continuo (lo hace Consultor BI + SAP Basis)
- ❌ NO gestión de todos los tickets (solo los críticos)
- ❌ NO desarrollo ABAP custom (se usa solo SLT estándar)

### Distribución de 270h del ABAP Developer

| Fase | Actividad | Horas V2.03 | Horas V2.04 | Reducción | Justificación |
|------|-----------|-------------|-------------|-----------|---------------|
| **Fase 0** | Análisis SLT inicial | 24h | 16h | -8h | Consultoría básica, no setup completo |
| **Fase 0** | Gestión tickets SAP | 28h | 12h | -16h | Solo tickets críticos, resto SAP Functional |
| **Fase 0** | Análisis Z-transactions | 42h | 24h | -18h | Análisis enfocado, no exhaustivo |
| **Fase 0** | Configuración SLT POC | 20h | 18h | -2h | Mantener calidad POC |
| **Fase 1** | Setup infraestructura SLT | 48h | 20h | -28h | Setup básico, Consultor BI completa |
| **Fase 1** | Extracción FI (4 trans) | 52h | 28h | -24h | Apoyo puntual, BI hace más |
| **Fase 1** | Extracción SD (2 trans) | 36h | 18h | -18h | Apoyo puntual |
| **Fase 1** | Extracción MM Proc (3) | 42h | 20h | -22h | Apoyo puntual |
| **Fase 1** | Extracción MM Inv (3) | 40h | 18h | -22h | Apoyo puntual |
| **Fase 1** | Extracción ZLEL008 | 56h | 32h | -24h | Reducir pero mantener calidad (crítico) |
| **Fase 1** | Extracción CO/AP/AR (4) | 48h | 24h | -24h | Apoyo puntual |
| **Fase 1** | Extracción Master+ZVEL | 52h | 28h | -24h | Apoyo puntual |
| **Fase 1** | Optimización SLT | 38h | 12h | -26h | Consultoría, no monitoreo continuo |
| **Fase 2** | (No participa) | 0h | 0h | 0h | Solo Fase 0 + Fase 1 |
| **TOTAL** | | **436h** | **270h** | **-166h** | **-38% reducción** |

---

## CAMBIOS EN EL CONSULTOR BI

### Comparativa de Carga de Trabajo

| Versión | Total Horas | Semanas | H/Semana Prom | Carga Máxima Sem | Comentario |
|---------|-------------|---------|---------------|------------------|------------|
| **V2.02** | 961h | 42 sem | 22.9h/sem | ~30h/sem | Original, sin ABAP Dev |
| **V2.03** | 761h | 32 sem | 23.8h/sem | ~30h/sem | Comprimido, ABAP hace SAP |
| **V2.04** | 935h | 36 sem | 26.0h/sem | ~28h/sem | **Óptimo, carga sostenible** |

**Análisis V2.04:**
- ✅ Promedio 26h/sem: cómodo, permite calidad
- ✅ Picos máximos ~28h/sem: manejables, NO excede 30h/sem
- ✅ BI se enfoca 100% en BigQuery + Power BI (su especialidad)
- ✅ No hace extracción SAP (ABAP Developer apoya)
- ✅ Tiempo para optimización y documentación

### Redistribución de Tareas BI

**V2.02: BI hace TODO (961h)**
- Extracción SAP
- Transformación BigQuery
- Modelo dimensional
- 12 Dashboards Power BI
- Documentación

**V2.04: BI se enfoca en valor (935h)**
- ❌ NO extracción SAP (ABAP Developer)
- ✅ Transformación BigQuery (especialidad)
- ✅ Modelo dimensional (especialidad)
- ✅ 12 Dashboards Power BI (especialidad)
- ✅ Documentación + capacitación
- ✅ **26h adicionales para:**
  - Mayor profundidad en optimización BigQuery
  - Dashboards más elaborados
  - Mejor documentación

---

## CAMBIOS EN EL CRONOGRAMA

### Duración por Fase

| Fase | V 2.02 | V 2.03 | V 2.04 | Delta V2.04 vs V2.02 |
|------|--------|--------|--------|----------------------|
| **Fase 0** | 6 sem | 5 sem | **6 sem** | **0 sem** (mantener calidad) |
| **Fase 1** | 22 sem | 16 sem | **20 sem** | **-2 sem** (leve optimización) |
| **Fase 2** | 14 sem | 11 sem | **10 sem** | **-4 sem** (optimización UAT) |
| **TOTAL** | **42 sem** | **32 sem** | **36 sem** | **-6 sem (-14.3%)** |

### Estrategia de Compresión V2.04

**Fase 0 (6 sem, sin cambio):**
- ⚠️ NO comprimir: análisis de calidad es crítico
- ABAP Developer analiza Z-transactions en paralelo
- POC con calidad, no apresurado

**Fase 1 (20 sem, -2 sem):**
- Paralelización moderada: ABAP extrae RAW, BI transforma
- NO comprimir demasiado (riesgo de bugs)
- Módulos desarrollados con leve overlap (no secuencial puro)

**Fase 2 (10 sem, -4 sem):**
- Desarrollo de dashboards optimizado (3 grupos en paralelo)
- UAT más eficiente (data ya validada en Fase 1)
- Reducción de ajustes post-UAT (mejor calidad en Fase 1)

### Fechas Clave V2.04

| Hito | Fecha | Semana |
|------|-------|--------|
| **Inicio** | 6 de enero 2026 | Sem 0 |
| **Fin Fase 0 (Go/No-Go)** | 16 de febrero 2026 | Sem 6 |
| **Fin Fase 1 (Data Lake)** | 5 de julio 2026 | Sem 26 |
| **Go-Live Producción** | 13 de septiembre 2026 | Sem 36 |

**Comparativa Go-Live:**
- V2.02: 15 de octubre 2026
- V2.03: 18 de agosto 2026
- V2.04: 13 de septiembre 2026
- **Adelanto:** 1 mes vs V2.02, 1 mes después de V2.03

---

## ANÁLISIS COSTO-BENEFICIO

### Inversión Incremental V2.04 vs V2.02

**Incremento de Esfuerzo:**
- +290h (Consultor BI: -26h, ABAP: +270h, SAP: +28h, PM: +18h)
- +18.2% de presupuesto
- ABAP Developer: 270h × tarifa ABAP

**Beneficios Cuantificables:**
1. **Ahorro operativo (adelantar Go-Live 1 mes):**
   - Elimina ~100h de operación manual en septiembre 2026
   - Reduce riesgo de errores manuales (costo de corrección)

2. **Reducción de riesgo técnico:**
   - ABAP Developer especialista en SLT (tecnología crítica)
   - Z-transactions con análisis profesional (ZLEL008, ZVEL015)
   - Menor probabilidad de delays por problemas SAP

3. **Calidad superior:**
   - Consultor BI con carga sostenible (26h/sem)
   - Mayor tiempo para optimización y documentación
   - Dashboards más elaborados y pulidos

4. **Tiempo de mercado:**
   - Insights de negocio disponibles 1 mes antes
   - Decisiones basadas en datos desde septiembre vs octubre

### Break-Even

**Cálculo Conservador:**
290h inversión / 100h ahorro operativo = **2.9 meses** post-Go-Live

**Cálculo Considerando Valor Intangible:**
Si se considera:
- Valor de insights tempranos (decisiones de negocio)
- Reducción de riesgo de delays (costo de oportunidad)
- Mayor calidad (menos correcciones post-Go-Live)

**Break-even realista: 1.5-2 meses** post-Go-Live

### ROI Proyectado

| Escenario | Break-Even | ROI 12 meses | ROI 24 meses |
|-----------|------------|--------------|--------------|
| **Conservador** | 2.9 meses | 1.2x | 1.5x |
| **Moderado** | 2.0 meses | 1.5x | 2.0x |
| **Optimista** | 1.5 meses | 2.0x | 3.0x |

---

## RIESGOS Y MITIGACIÓN

### Riesgos de V2.04

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| ABAP Developer no disponible | Media | Alto | Lead time 2-3 sem, comenzar reclutamiento YA |
| ABAP 270h insuficientes | Baja | Medio | Z-transactions analizadas en Fase 0, ajustar si necesario |
| Coordinación 4 recursos | Baja | Bajo | ABAP solo 10h/sem, bajo overhead |
| Tickets SAP sin resolver | Media | Medio | Fase 0 completa (6 sem) para resolver |
| Cronograma 36 sem muy ajustado | Baja | Medio | Buffer en Fase 2, 2 semanas de contingencia |

### Ventajas de V2.04 vs V2.03

| Aspecto | V2.03 (Agresiva) | V2.04 (Optimizada) | Ventaja V2.04 |
|---------|------------------|---------------------|---------------|
| Presupuesto | +378h (+24%) | +290h (+18%) | ✅ -88h más económica |
| Cronograma | 32 sem | 36 sem | ⚠️ +4 sem (pero realista) |
| ABAP Dev | 23.8h/sem | 10.4h/sem | ✅ Más fácil de contratar |
| Consultor BI | 23.8h/sem | 26.0h/sem | ⚠️ +2.2h/sem (pero sostenible) |
| Riesgo coord | Alto (4 full) | Medio (1 part-time) | ✅ Menor overhead |
| Calidad | Presión alta | Presión moderada | ✅ Mayor calidad |

---

## PRÓXIMOS PASOS RECOMENDADOS

### Decisión Elanco

**Comparar 3 opciones:**

1. **V2.02 Original (Baseline):**
   - Duración: 42 semanas
   - Esfuerzo: 1,590h
   - Costo: $$$
   - Go-Live: Octubre 2026
   - Riesgo: Consultor BI sobrecargado

2. **V2.03 Agresiva:**
   - Duración: 32 semanas (-10 sem)
   - Esfuerzo: 1,968h (+378h)
   - Costo: $$$$ (+24%)
   - Go-Live: Agosto 2026
   - Riesgo: Coordinación compleja, ABAP casi full-time

3. **V2.04 Optimizada (RECOMENDADA):**
   - Duración: 36 semanas (-6 sem)
   - Esfuerzo: 1,880h (+290h)
   - Costo: $$$$ (+18%)
   - Go-Live: Septiembre 2026
   - Riesgo: Equilibrado, carga sostenible

### Checklist Aprobación V2.04

**De parte de Elanco:**
- [ ] Aprobación de cronograma 36 semanas (Go-Live: 13-sep-2026)
- [ ] Aprobación de presupuesto adicional (+290h = +18%)
- [ ] Confirmación de disponibilidad SAP Basis (Elanco)
- [ ] Provisión de accesos SAP y BigQuery antes del kick-off
- [ ] Disponibilidad de stakeholders para workshops y UAT

**De parte de Aunergia:**
- [ ] Reclutamiento de ABAP Developer (lead time 2-3 semanas)
- [ ] Perfil: 5+ años ABAP, 2+ años SLT, módulos MM/SD/FI
- [ ] Preparación de ambientes desarrollo/testing
- [ ] Coordinación de kick-off (6 de enero 2026)

---

## ARCHIVOS GENERADOS PARA V2.04

| Archivo | Ubicación | Descripción |
|---------|-----------|-------------|
| **CRONOGRAMA_DETALLADO_TAREAS_V2_04.csv** | `/docs/propuesta_final/` | 25 tareas, 36 semanas, 4 recursos |
| **RESUMEN_PROPUESTA_FINAL_V2_04.txt** | `/ElancoPower/` | Resumen ejecutivo completo |
| **RESUMEN_CAMBIOS_V2_04.md** | `/ElancoPower/` | Este documento |

---

## RECOMENDACIÓN FINAL

**Aunergia recomienda la VERSIÓN 2.04** por:

✅ **Equilibrio óptimo:** costo (+18%) vs tiempo (-14%)  
✅ **Carga sostenible:** Consultor BI 26h/sem (no sobrecargado)  
✅ **ABAP Developer especialista:** 270h enfocadas en lo crítico  
✅ **Riesgo controlado:** cronograma realista de 36 semanas  
✅ **ROI positivo:** break-even en 2-3 meses post-Go-Live  
✅ **Calidad garantizada:** recursos con tiempo para hacer bien el trabajo  

**Go-Live: 13 de septiembre de 2026** (1 mes antes que V2.02)

---

**Elaborado por:** Equipo Técnico Aunergia  
**Fecha:** 10 de noviembre de 2025  
**Versión:** 2.04 (Optimizada)  
**Validez:** 30 días (hasta 10 de diciembre de 2025)
