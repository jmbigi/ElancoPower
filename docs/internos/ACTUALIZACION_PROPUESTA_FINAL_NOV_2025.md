# ACTUALIZACIÓN DE PROPUESTA FINAL - 7 DE NOVIEMBRE 2025

**Fecha de Revisión:** 7 de noviembre de 2025  
**Revisado por:** Sistema de Control de Calidad  
**Objetivo:** Alinear propuesta final con antecedentes reales del proyecto

---

## 🎯 RESUMEN EJECUTIVO

Se ha realizado una revisión exhaustiva de la carpeta `/docs/propuesta_final/` para corregir inconsistencias con los antecedentes documentados en las fuentes primarias. La propuesta contenía información inflada y no realista que no coincidía con:

1. El presupuesto real de USD 8,850 (solo JM Bigi)
2. El alcance inicial de 8 transacciones prioritarias
3. Las horas reales estimadas (354h vs 677h)
4. La disponibilidad part-time del recurso

---

## 📊 PROBLEMAS IDENTIFICADOS Y CORREGIDOS

### 1. **Presupuesto Inflado**

**ANTES (Incorrecto):**
- Total: USD 48,000
- Equipo completo: 677 horas
- Incluía PM, QA, múltiples desarrolladores

**AHORA (Correcto):**
- Total: USD 8,850 (solo JM Bigi)
- 354 horas de desarrollo técnico
- Horas de Lucía/Linda facturadas por separado

**Fuente:** `PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`

---

### 2. **Alcance Sobrestimado**

**ANTES (Incorrecto):**
- 18 transacciones SAP en alcance inicial
- 12 dashboards Power BI
- Implementación completa en primera fase

**AHORA (Correcto):**
- **8 transacciones MVP** (Prioridad 1 y 2):
  - VA05 (Sales Order)
  - ZLEL008 (Inventario consolidado)
  - KSB1 (OPEX)
  - FAGLL03 (Mayor General)
  - KE24 (Venta CO-PA)
  - FB03 (Documentos)
  - F.08 (Balance Comprobación)
  - F.01 (Estado Situación)
- **10 transacciones** documentadas para fases futuras
- **4-6 dashboards** en MVP

**Fuente:** `ALCANCE_TRANSACCIONES_SAP_DATA_LAKE.txt` + Audio Lucía 09-oct-2025

---

### 3. **Cronograma Irreal**

**ANTES (Incorrecto):**
- 24 semanas (~6 meses)
- Equipo completo trabajando full-time
- Inicio inmediato sin considerar restricciones

**AHORA (Correcto):**
- **13-17 semanas** (~4 meses)
- Part-time 20-25h/semana (JM Bigi)
- **Inicio condicionado** a resolución de:
  - Ticket SAP-48219 (permisos)
  - Tickets BQ-7713 y BQ-7721 (tablas)
- Inicio propuesto: 14-dic-2025
- Fin estimado: 09-abr-2026

**Fuente:** `PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md` Sección 5

---

### 4. **Roles y Responsabilidades Confusos**

**ANTES (Incorrecto):**
- Presentaba a todo el equipo Aunergia como parte del proyecto
- No distinguía entre roles incluidos y no incluidos
- Horas de todos mezcladas

**AHORA (Correcto):**
- **Incluido en USD 8,850:**
  - ✅ Juan Manuel Bigi: 354h desarrollo técnico
  
- **NO incluido (factura separada Aunergia):**
  - ❌ Lucía Rodríguez: ~80h consultoría SAP
  - ❌ Linda López: PM según necesidad
  - ❌ QA formal/Compliance
  - ❌ Arquitectura empresarial

- **Contingencia ABAP:**
  - ⚠️ 8-16h si necesario: USD 640-1,600

**Fuente:** `ANALISIS_DIFERENCIAS_PRESUPUESTOS.md`

---

### 5. **Fechas Obsoletas**

**ANTES (Incorrecto):**
- Referencias genéricas a "noviembre 2025"
- Sin fechas específicas
- Cronogramas sin anclar a realidad

**AHORA (Correcto):**
- Fecha elaboración: 7-nov-2025
- Validez oferta: hasta 7-dic-2025
- Inicio propuesto: 14-dic-2025
- Pausa vacacional: 23-29 dic 2025
- Fin estimado: 09-abr-2026

**Fuente:** Fecha actual del sistema + cronograma realista

---

## 📝 DOCUMENTOS ACTUALIZADOS

### ✅ Actualizado Completamente

1. **00_PORTADA_Y_RESUMEN_EJECUTIVO.md**
   - Control de versiones actualizado (v2.0)
   - Alcance ajustado a 8 transacciones MVP
   - Recursos y presupuesto corregidos
   - Duración ajustada a 13-17 semanas
   - Beneficios recalculados para MVP
   - Equipo claramente diferenciado

---

## ⏳ PENDIENTES DE ACTUALIZACIÓN

Los siguientes documentos **REQUIEREN REVISIÓN Y AJUSTE** para mantener consistencia:

### Prioridad Alta (críticos):

2. **08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md**
   - ⚠️ Cambiar de 677h a 354h
   - ⚠️ Eliminar roles no incluidos
   - ⚠️ Ajustar costos a USD 8,850
   - ⚠️ Clarificar qué está incluido y qué no

3. **09_CRONOGRAMA_SEMANAL.md**
   - ⚠️ Ajustar de 24 sem a 13-17 sem
   - ⚠️ Fechas específicas (14-dic-2025 inicio)
   - ⚠️ Disponibilidad part-time JMB

4. **04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD.md**
   - ⚠️ Ajustar horas de 80h a 40h JMB
   - ⚠️ Fechas específicas
   - ⚠️ Go/No-Go condicionado a tickets

5. **12_ENTREGABLES_Y_CONDICIONES_COMERCIALES.md**
   - ⚠️ Costos USD 8,850
   - ⚠️ Forma de pago actualizada
   - ⚠️ Clarificar exclusiones

### Prioridad Media:

6. **05_FASE_1_CONSTRUCCION_DATA_LAKE.md**
   - ⚠️ Alcance 8 transacciones (no 18)
   - ⚠️ Horas 156h JMB

7. **06_FASE_2_MODELADO_Y_DASHBOARDS.md**
   - ⚠️ 4-6 dashboards (no 12)
   - ⚠️ Horas 148h JMB

8. **03_TRANSACCIONES_SAP_INCLUIDAS.md**
   - ⚠️ Clarificar MVP (8) vs Futuro (10)

### Prioridad Baja:

9. **01_CONTEXTO_Y_SITUACION_ACTUAL.md** - ✅ Ya está correcto
10. **02_ALCANCE_GENERAL_DE_LA_PROPUESTA.md**
11. **07_FASE_3_MODELOS_PREDICTIVOS.md**
12. **10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md**
13. **11_RIESGOS_Y_SUPUESTOS.md**

---

## 🔍 PRINCIPIOS DE LA REVISIÓN

### 1. Fidelidad a Fuentes Primarias

✅ Todos los cambios están basados en:
- Audio Lucía (09-oct-2025)
- Correo David Saboya (09-oct-2025)
- CSV Transacciones SAP
- Que_se_va_a_usar.txt
- PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md

❌ Se eliminaron estimaciones sin sustento

### 2. Claridad en Alcance

✅ Diferencia clara entre:
- Incluido en USD 8,850 (JM Bigi)
- No incluido (Aunergia factura aparte)
- Contingencias (ABAP externo)

### 3. Realismo en Cronograma

✅ Considera:
- Disponibilidad part-time (20-25h/sem)
- Issues pendientes (SAP, BigQuery)
- Pausa vacacional
- Go/No-Go condicionado

### 4. Transparencia

✅ Documento de versión 2.0 indica:
- "Revisada y ajustada a realidad del proyecto"
- Control de cambios documentado
- Razones de los ajustes explicadas

---

## 💰 COMPARATIVA PRESUPUESTO

### Versión 1.0 (Incorrecta):

| Concepto | Valor |
|----------|-------|
| Costo Total | USD 48,000 |
| Horas Totales | 677h |
| Equipo | Completo (PM, QA, Dev, etc.) |
| Alcance | 18 transacciones + 12 dashboards |
| Duración | 24 semanas |

### Versión 2.0 (Correcta):

| Concepto | Valor |
|----------|-------|
| **Costo Total (JMB)** | **USD 8,850** |
| **Horas JMB** | **354h** |
| **Equipo incluido** | **Solo JM Bigi** |
| **Alcance MVP** | **8 transacciones + 4-6 dashboards** |
| **Duración** | **13-17 semanas** |

**Diferencia:** -81.5% en costo (USD 39,150 menos)

---

## 📋 RECOMENDACIONES

### Para Aunergia:

1. **Decidir modelo de negocio:**
   - Opción A: USD 8,850 (solo JMB) + facturación separada Lucía/Linda
   - Opción B: USD 48,000 (equipo completo Aunergia)
   - Opción C: USD ~25,000 (híbrido)

2. **Completar actualización de documentos pendientes** (listados arriba)

3. **Comunicar claramente al cliente** qué está incluido y qué no

### Para Elanco:

1. **Revisar alcance MVP** (8 transacciones)
2. **Confirmar presupuesto** USD 8,850 vs otras opciones
3. **Priorizar resolución de tickets** SAP-48219, BQ-7713, BQ-7721
4. **Aprobar inicio** condicionado a Go/No-Go

---

## ✅ CHECKLIST DE CONSISTENCIA

### Documentos Consistentes:
- ✅ `00_PORTADA_Y_RESUMEN_EJECUTIVO.md`
- ✅ `PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`
- ✅ `RESUMEN_EJECUTIVO_PARA_LUCIA.md`
- ✅ `ANALISIS_DIFERENCIAS_PRESUPUESTOS.md`

### Documentos Inconsistentes (requieren actualización):
- ⚠️ `08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md`
- ⚠️ `09_CRONOGRAMA_SEMANAL.md`
- ⚠️ `04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD.md`
- ⚠️ `12_ENTREGABLES_Y_CONDICIONES_COMERCIALES.md`
- ⚠️ `05_FASE_1_CONSTRUCCION_DATA_LAKE.md`
- ⚠️ `06_FASE_2_MODELADO_Y_DASHBOARDS.md`
- ⚠️ `03_TRANSACCIONES_SAP_INCLUIDAS.md`

---

## 🎯 PRÓXIMOS PASOS

1. **Inmediato:**
   - [ ] Revisar y aprobar estos cambios
   - [ ] Decidir modelo de negocio (A/B/C)
   - [ ] Actualizar documentos pendientes

2. **Esta semana:**
   - [ ] Presentar propuesta v2.0 a Elanco
   - [ ] Seguimiento tickets críticos
   - [ ] Confirmar disponibilidad JMB

3. **Próximas 2 semanas:**
   - [ ] Aprobación presupuesto
   - [ ] Kick-off Fase 0 (14-dic-2025)
   - [ ] Evaluación Go/No-Go

---

## 📞 CONTACTO

**Para consultas sobre esta actualización:**
- Juan Manuel Bigi (autor técnico)
- Lucía Rodríguez (coordinación Aunergia)
- Linda López (PM Aunergia)

---

**Elaborado por:** Sistema de Control de Calidad  
**Fecha:** 7 de noviembre de 2025  
**Versión:** 1.0  
**Estado:** ✅ Revisión Fase 1 completada (1 de 13 documentos actualizados)

---

## ANEXO: FUENTES CONSULTADAS

1. ✅ `/inputs/conversaciones_con_lucia.md` (Audio 09-oct-2025)
2. ✅ `/inputs/correo_1_de_lucia.md` (Email David Saboya)
3. ✅ `/inputs/Attach_2_Correo_1_Transacciones SAP.csv`
4. ✅ `/inputs/Que_se_va_a_usar.txt`
5. ✅ `/docs/entregables/PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`
6. ✅ `/docs/entregables/RESUMEN_EJECUTIVO_PARA_LUCIA.md`
7. ✅ `/docs/internos/ANALISIS_DIFERENCIAS_PRESUPUESTOS.md`
8. ✅ `/docs/internos/checklist_permisos_y_licencias.md`
9. ✅ `/docs/internos/AUDITORIA_FINAL_CONSOLIDACION.md`

**Todas las fuentes fueron revisadas y validadas para garantizar la consistencia.**

---

✅ **FIN DEL DOCUMENTO DE ACTUALIZACIÓN**
