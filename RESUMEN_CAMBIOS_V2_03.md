# RESUMEN DE CAMBIOS - VERSIÓN 2.03
**Fecha:** 10 de noviembre de 2025  
**Proyecto:** Centralización de Datos y Analítica - Elanco Animal Health

---

## CAMBIOS PRINCIPALES

### 1. NUEVO RECURSO: ABAP DEVELOPER

**Justificación:**
- Consultor BI NO puede trabajar más de 30h/semana (restricción no negociable)
- Para comprimir cronograma se requiere especialista en SAP/SLT
- Separación de responsabilidades: SAP vs BigQuery/Power BI

**Características del ABAP Developer:**
- **Horas totales:** 436h (22.1% del proyecto)
- **Dedicación:** 15-20h/semana
- **Duración:** 21 semanas (solo Fase 0 y Fase 1)
- **Expertise requerido:** 
  - SAP ABAP (5+ años)
  - SAP SLT (2+ años) - CRÍTICO
  - Módulos MM, SD, FI
  - Análisis de transacciones custom (ZLEL008, ZVEL015)

**Responsabilidades:**
- Configuración y monitoreo de SAP SLT
- Extracción de datos desde SAP → BigQuery (zona RAW)
- Análisis profundo de transacciones custom
- Gestión de tickets SAP con TI Global
- Coordinación con SAP Basis (Elanco)
- NO toca BigQuery ni Power BI

---

## 2. REDISTRIBUCIÓN DE HORAS

### Comparativa por Recurso

| Recurso | V 2.02 | V 2.03 | Delta | Comentario |
|---------|--------|--------|-------|------------|
| **Consultor BI** | 961h | 761h | -200h | Respeta 30h/sem, enfoque 100% BigQuery/Power BI |
| **ABAP Developer** | 0h | 436h | +436h | NUEVO recurso especializado SAP/SLT |
| **Funcional SAP** | 484h | 484h | 0h | Sin cambio, colabora con ABAP Dev |
| **Project Manager** | 145h | 145h | 0h | Sin cambio |
| **SAP Basis (Cliente)** | 0h | 0h | 0h | Provisto por Elanco (sin costo proyecto) |
| **TOTAL** | **1,590h** | **1,968h** | **+378h (+24%)** | Incremento controlado |

### Distribución por Fase

| Fase | V 2.02 | V 2.03 | Delta | Semanas V2.02 | Semanas V2.03 | Delta Sem |
|------|--------|--------|-------|---------------|---------------|-----------|
| **Fase 0** | 235h | 341h | +106h | 6 sem | 5 sem | -1 sem |
| **Fase 1** | 696h | 968h | +272h | 22 sem | 16 sem | -6 sem |
| **Fase 2** | 659h | 659h | 0h | 14 sem | 11 sem | -3 sem |
| **TOTAL** | **1,590h** | **1,968h** | **+378h** | **42 sem** | **32 sem** | **-10 sem (-24%)** |

---

## 3. CRONOGRAMA COMPRIMIDO

### Fechas Clave

| Hito | V 2.02 | V 2.03 | Adelanto |
|------|--------|--------|----------|
| **Inicio** | 6-ene-2026 | 6-ene-2026 | - |
| **Fin Fase 0** | 17-feb-2026 (sem 6) | 9-feb-2026 (sem 5) | 1 semana |
| **Fin Fase 1** | 21-jul-2026 (sem 28) | 2-jun-2026 (sem 21) | 7 semanas |
| **Go-Live** | 15-oct-2026 (sem 42) | 18-ago-2026 (sem 32) | **10 semanas** |

### Reducción de Duración por Fase

**Fase 0:** 6 sem → 5 sem (-17%)
- Gestión de tickets más eficiente (ABAP Dev como punto focal SAP)
- Análisis Z-transactions acelerado (especialista ABAP)

**Fase 1:** 22 sem → 16 sem (-27%)
- Paralelización real: ABAP Dev extrae de SAP, Consultor BI transforma en BigQuery
- Configuración SLT por especialista (reduce riesgo de delays)
- Desarrollo de pipelines acelerado por separación de roles

**Fase 2:** 14 sem → 11 sem (-21%)
- Optimización de desarrollo de dashboards
- UAT más eficiente (Data Lake ya validado en Fase 1)

---

## 4. SEPARACIÓN DE RESPONSABILIDADES

### Consultor BI (761h - 38.7%)

**SE ENFOCA EN:**
- ✅ Arquitectura BigQuery (3 capas: RAW/PROCESSED/CURATED)
- ✅ Desarrollo de pipelines de transformación (PROCESSED → CURATED)
- ✅ Modelo dimensional (star schema)
- ✅ Desarrollo de 12 dashboards Power BI
- ✅ Optimización de queries BigQuery
- ✅ Capacitación en Power BI

**YA NO HACE:**
- ❌ Extracción desde SAP (ahora ABAP Developer)
- ❌ Configuración de SLT (ahora ABAP Developer)
- ❌ Gestión de tickets SAP (ahora ABAP Developer)
- ❌ Análisis de transacciones custom Z (ahora ABAP Developer lidera)

### ABAP Developer (436h - 22.1%)

**SE ENFOCA EN:**
- ✅ Configuración y monitoreo de SAP SLT
- ✅ Extracción de datos desde SAP → BigQuery (zona RAW)
- ✅ Análisis profundo de transacciones custom (ZLEL008, ZVEL015)
- ✅ Gestión de tickets SAP con TI Global
- ✅ Coordinación con SAP Basis (Elanco)
- ✅ Validación de replicación SAP ↔ BigQuery

**NO HACE:**
- ❌ Desarrollo en BigQuery (Consultor BI)
- ❌ Desarrollo de dashboards Power BI (Consultor BI)
- ❌ Transformaciones de datos (Consultor BI)

### Funcional SAP (484h - 24.6%)

**SE MANTIENE:**
- ✅ Validaciones funcionales de negocio
- ✅ Definición de KPIs con stakeholders
- ✅ Colabora con ABAP Developer en análisis funcional (Fase 0 y 1)
- ✅ UAT y capacitación (Fase 2)
- ✅ Documentación funcional

**CAMBIO DE COLABORACIÓN:**
- Antes: Colaboraba principalmente con Consultor BI
- Ahora: Colabora con ABAP Developer (Fase 0+1) y Consultor BI (Fase 2)

---

## 5. VENTAJAS DE LA VERSIÓN 2.03

### Ventajas Técnicas

1. ✅ **Consultor BI protegido:** Mantiene 30h/semana (restricción respetada)
2. ✅ **Especialización SAP SLT:** Reduce riesgo de configuración incorrecta
3. ✅ **Análisis profundo de Z-transactions:** Especialista ABAP dedicado
4. ✅ **Paralelización real:** Trabajo simultáneo SAP (ABAP) y BigQuery (Consultor BI)
5. ✅ **Separación clara de roles:** SAP vs Cloud/BI
6. ✅ **Gestión eficiente de tickets:** Punto focal técnico con TI Global

### Ventajas de Negocio

1. 🚀 **Go-Live 10 semanas antes:** Mediados agosto vs mediados octubre
2. 💰 **ROI positivo:** Beneficios operativos 10 semanas antes
3. ⏱️ **Menor time-to-market:** 32 semanas vs 42 semanas (-24%)
4. 📊 **Beneficios más tempranos:** Reducción 70% tiempo manual desde agosto
5. 🛡️ **Menor riesgo técnico:** Especialista en transacciones custom

### Análisis de Inversión

| Concepto | Valor |
|----------|-------|
| **Inversión adicional** | +378 horas (+24% esfuerzo) |
| **Ahorro temporal** | -10 semanas (-24% duración) |
| **Beneficio operativo por semana** | ~15 horas/semana ahorradas (reducción 70% de 20h/sem) |
| **Beneficios acumulados 10 semanas** | ~150 horas ahorradas |
| **Break-even** | ~2.5 meses post go-live |
| **Beneficio neto año 1** | ~630 horas (52 sem - 10 sem adelanto - 2.5 meses break-even = ~42 sem × 15h) |

**Conclusión:** Inversión de 378h se recupera en 2.5 meses. Beneficio neto año 1 supera ampliamente la inversión adicional.

---

## 6. RIESGOS MITIGADOS

### V 2.02: Riesgos Identificados

1. ⚠️ **Consultor BI sobrecargado:** 961h en 42 semanas (22.9h/sem promedio, pero con picos de 35-40h/sem)
2. ⚠️ **Transacciones custom (ZLEL008, ZVEL015):** Análisis superficial sin especialista ABAP
3. ⚠️ **Configuración SLT:** Consultor BI no especialista en SLT (riesgo de configuración incorrecta)
4. ⚠️ **Gestión de tickets SAP:** Sin punto focal técnico especializado

### V 2.03: Mitigaciones Aplicadas

1. ✅ **Consultor BI protegido:** 761h en 32 semanas (23.8h/sem promedio, respeta 30h/sem)
2. ✅ **Especialista ABAP dedicado:** Análisis profundo de transacciones custom (124h en Fase 0)
3. ✅ **Configuración SLT por experto:** ABAP Developer con 2+ años experiencia SLT
4. ✅ **Punto focal técnico SAP:** ABAP Developer gestiona todos los tickets SAP con TI Global

---

## 7. ARCHIVOS CREADOS/ACTUALIZADOS

### Archivos Nuevos (Versión 2.03)

1. **CRONOGRAMA_DETALLADO_TAREAS_V2_03.csv**
   - 25 tareas con columna adicional para ABAP Developer
   - Cronograma comprimido a 32 semanas
   - Distribución detallada por semana y recurso

2. **RESUMEN_PROPUESTA_FINAL_V2_03.txt**
   - Resumen ejecutivo completo con nuevo modelo
   - Comparativa vs versión 2.02
   - Análisis de costo-beneficio

3. **DISTRIBUCION_SEMANAL_HORAS_V2_03.md**
   - Distribución detallada semana a semana
   - Análisis de cargas y picos
   - Recomendaciones de mitigación

4. **respuesta_pregunta_01.md** (actualizado)
   - Respuesta a 4 preguntas con nueva propuesta v2.03
   - 4 Job Descriptions (incluye ABAP Developer)
   - Recomendación fundamentada de v2.03

5. **RESUMEN_CAMBIOS_V2_03.md** (este archivo)
   - Consolidado de todos los cambios
   - Comparativas detalladas
   - Justificaciones técnicas y de negocio

### Archivos Originales (Se mantienen como referencia)

- CRONOGRAMA_DETALLADO_TAREAS.csv (versión 2.02)
- RESUMEN_PROPUESTA_FINAL.txt (versión 2.02)
- Todos los demás archivos de docs/propuesta_final/

---

## 8. PRÓXIMOS PASOS

### Acciones Inmediatas

**De parte de Aunergia:**
- [ ] Identificar candidato ABAP Developer con perfil requerido (SLT + MM/SD/FI)
- [ ] Validar disponibilidad de Consultor BI para 761h en 32 semanas
- [ ] Generar diagramas de arquitectura técnica (2-3 días)
- [ ] Preparar presentación ejecutiva v2.02 vs v2.03

**De parte de Elanco:**
- [ ] Revisión y aprobación de propuesta versión 2.03
- [ ] Decisión sobre inversión adicional (+378h = +24% presupuesto)
- [ ] Confirmación de disponibilidad recurso SAP Basis (Elanco) desde Fase 0
- [ ] Aprobación de cronograma comprimido (32 semanas)

### Validación Técnica

- [ ] Confirmar que TI Global puede proveer permisos SAP en 2-3 semanas (crítico Fase 0)
- [ ] Confirmar que SAP Basis (Elanco) estará disponible para soporte SLT
- [ ] Validar que BigQuery tiene capacidad para procesamiento requerido
- [ ] Confirmar que las 8 licencias Power BI Pro están activas

### Kick-off (Si se aprueba v2.03)

- [ ] Contratar ABAP Developer (lead time: 2-3 semanas)
- [ ] Kick-off meeting: 6 de enero 2026
- [ ] Setup de accesos: SAP, BigQuery, Power BI
- [ ] Coordinación con SAP Basis para Fase 0

---

## 9. RECOMENDACIÓN FINAL

**Recomendamos APROBAR VERSIÓN 2.03** por las siguientes razones:

1. 🎯 **Respeta restricción del Consultor BI** (30h/semana no negociable)
2. 🚀 **Go-Live 10 semanas antes** (valor estratégico alto)
3. 🛡️ **Reduce riesgo técnico SAP** (especialista SLT + transacciones custom)
4. 💼 **Separación profesional de roles** (especialización técnica)
5. 💰 **ROI positivo en 2.5 meses** (beneficios operativos tempranos)
6. ⚡ **Paralelización efectiva** (aceleración real, no forzada)

**Inversión adicional justificada:**
- +378 horas (+24%) se recupera en 2.5 meses post go-live
- 10 semanas de beneficios operativos adelantados
- Beneficio neto año 1: ~630 horas ahorradas (vs 378h invertidas)
- Relación beneficio/inversión: 1.67x (excelente)

**Valor intangible:**
- Menor riesgo de delays por issues técnicos SAP
- Mayor calidad de configuración SLT (especialista)
- Análisis profundo de transacciones custom (ZLEL008, ZVEL015)
- Consultor BI enfocado 100% en BigQuery/Power BI (mayor calidad dashboards)

---

## 10. CONTACTO

Para preguntas o aclaraciones sobre esta propuesta:

**Equipo Técnico Aunergia**  
Email: [contacto]  
Fecha límite respuesta: 10 de diciembre de 2025 (30 días validez propuesta)

---

**Elaborado por:** Equipo Técnico Aunergia  
**Fecha:** 10 de noviembre de 2025  
**Versión:** 2.03  
**Status:** Pendiente aprobación cliente
