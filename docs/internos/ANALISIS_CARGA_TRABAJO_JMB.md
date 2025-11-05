# ⚠️ ANÁLISIS DE CARGA DE TRABAJO - JUAN MANUEL BIGI

**Fecha de análisis:** 5 de noviembre de 2025  
**Restricción:** Máximo 6 horas de trabajo por día  

---

## 🔍 PROBLEMA IDENTIFICADO

Juan Manuel Bigi ha establecido que **no trabajará más de 6 horas por día**. El cronograma actual de 23 semanas **NO ES VIABLE** con esta restricción.

---

## 📊 ANÁLISIS MATEMÁTICO

### Capacidad Máxima de JMB

```
Horas máximas por día:     6 horas
Días laborables/semana:    5 días
Horas máximas/semana:      30 horas
```

### Horas Asignadas por Fase

| Fase | Horas JMB | Semanas Actuales | Horas Disponibles | ¿Suficiente? |
|------|-----------|------------------|-------------------|--------------|
| **Fase 0** | 58h | 5 sem | 150h | ✅ HOLGADO (92h sobrantes) |
| **Fase 1** | 180h | 10 sem | 300h | ✅ HOLGADO (120h sobrantes) |
| **Fase 2** | 240h | 7 sem | 210h | ❌ **INSUFICIENTE** (-30h faltantes) |
| **TOTAL** | **478h** | **22 sem** | **660h** | ✅ En total sí alcanza |

### Semanas Necesarias (Mínimo Teórico)

```
Total horas JMB:           478 horas
Horas máximas/semana:      30 horas
Semanas mínimas:           15.9 semanas (sin buffers)
```

---

## ⚠️ PROBLEMA CRÍTICO: FASE 2

**Fase 2 - Dashboards Power BI:**
- Horas asignadas a JMB: **240 horas**
- Duración actual: **7 semanas**
- Capacidad máxima (6h/día × 5 días × 7 sem): **210 horas**
- **DÉFICIT: -30 horas** ❌

**Conclusión:** Fase 2 necesita **MÍNIMO 8 semanas** (240h ÷ 30h/sem = 8 semanas)

---

## 📅 CRONOGRAMA AJUSTADO PROPUESTO

### Opción A: Agregar 1 Semana a Fase 2 (RECOMENDADO)

```
FASE 0:    5 semanas  (1-dic a 12-ene)  ✅ 58h / 150h disponibles
PAUSA:     1 semana   (23-29 dic)        -
FASE 1:    10 semanas (13-ene a 23-mar) ✅ 180h / 300h disponibles
FASE 2:    8 semanas  (24-mar a 18-may) ✅ 240h / 240h disponibles
───────────────────────────────────────────────────────────────
TOTAL:     24 semanas (incl. 1 sem vacacional)
INICIO:    1 diciembre 2025
FIN:       18 mayo 2026 (+7 días vs cronograma actual)
```

### Opción B: Redistribuir Horas entre Fases

Reducir sobrecarga de Fase 0 y 1, asignar a Fase 2:

```
FASE 0:    4 semanas  (reducir 1 semana de holgura)
FASE 1:    9 semanas  (reducir 1 semana de holgura)
FASE 2:    8 semanas  (agregar 1 semana necesaria)
───────────────────────────────────────────────────
TOTAL:     22 semanas (incl. 1 sem vacacional)
FIN:       11 mayo 2026 (sin cambios vs actual)
```

---

## 🎯 RECOMENDACIÓN

### ✅ OPCIÓN A - Agregar 1 Semana (MÁS SEGURA)

**Ventajas:**
- ✅ Mantiene buffers de seguridad en Fase 0 y 1
- ✅ JMB trabaja cómodamente 6h/día
- ✅ Absorbe imprevistos mejor
- ✅ Reduce riesgo de burnout

**Desventajas:**
- ⚠️ Proyecto termina 7 días después (18-mayo vs 11-mayo)

### Impacto en Fechas

| Hito | Fecha Actual | Fecha Ajustada | Cambio |
|------|--------------|----------------|--------|
| Kick-off | 1-dic-2025 | 1-dic-2025 | Sin cambio |
| Go/No-Go | 12-ene-2026 | 12-ene-2026 | Sin cambio |
| Fin Fase 1 | 23-mar-2026 | 23-mar-2026 | Sin cambio |
| Fin Fase 2 | 11-may-2026 | **18-may-2026** | **+7 días** |
| Go-Live | 5-may-2026 | **12-may-2026** | **+7 días** |

---

## 📋 DESGLOSE SEMANAL FASE 2 AJUSTADA (8 SEMANAS)

Con 8 semanas, JMB trabaja **30h/semana** de forma sostenible:

| Semana | Fechas | Horas JMB | Actividad Principal |
|--------|--------|-----------|---------------------|
| S16 | 24-30 mar | 30h | Modelado dimensional |
| S17 | 31 mar - 6 abr | 30h | Capa semántica + Dash 1-2 |
| S18 | 7-13 abr | 30h | Dashboards 3-4 |
| S19 | 14-20 abr | 30h | Dashboards 5-6 |
| S20 | 21-27 abr | 30h | Dashboards 7-9 + RLS |
| S21 | 28 abr - 4 may | 30h | Dashboards 10-12 + ajustes |
| S22 | 5-11 may | 30h | UAT + correcciones |
| S23 | 12-18 may | 30h | Capacitación + Go-Live |
| **TOTAL** | **8 sem** | **240h** | ✅ Capacidad perfecta |

---

## 🔄 CAMBIOS A REALIZAR

### Documentos a Actualizar:

1. ✅ `08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md`
   - Fase 2: 7 sem → 8 sem
   - Fecha fin: 11-may → 18-may

2. ✅ `09_CRONOGRAMA_SEMANAL.md`
   - Agregar Semana 23 (12-18 mayo)
   - Redistribuir actividades Fase 2

3. ✅ `06_FASE_2_MODELADO_Y_DASHBOARDS.md`
   - Duración: 7 sem → 8 sem
   - Fecha fin: 11-may → 18-may

4. ✅ `00_PORTADA_Y_RESUMEN_EJECUTIVO.md`
   - Duración total: 23 sem → 24 sem
   - Fecha fin: 11-may → 18-may

5. ✅ `README.md`
   - Actualizar fechas

6. ✅ `VERIFICACION_CONSISTENCIA.md`
   - Actualizar hitos

7. ✅ `CRONOGRAMA_ACTUALIZADO_V1.1.md`
   - Agregar nota sobre ajuste v1.2

---

## 💡 CONSIDERACIONES ADICIONALES

### ¿Por qué NO reducir horas de JMB?

Las 478 horas de JMB son el **mínimo necesario** para:
- ✅ 18 transacciones SAP (Fase 1: 180h)
- ✅ 12 dashboards Power BI (Fase 2: 240h)
- ✅ Infraestructura y testing

**Reducir horas = Reducir alcance** (menos transacciones o dashboards)

### ¿Por qué 6h/día es razonable?

- ✅ Permite trabajo sostenible (no burnout)
- ✅ JMB puede tener otros compromisos
- ✅ Trabajo remoto part-time típico
- ✅ Permite tiempo para coordinación (Lucía, Linda)

### ¿Alternativas NO recomendadas?

❌ **JMB trabaje 8h/día:** No sostenible, riesgo de burnout  
❌ **Reducir alcance:** Cliente espera 12 dashboards  
❌ **Agregar otro desarrollador:** Incrementa costos significativamente  
❌ **Comprimir cronograma:** Reduce calidad, aumenta riesgo

---

## ✅ DECISIÓN FINAL RECOMENDADA

**OPCIÓN A: Agregar 1 semana a Fase 2**

- **Nueva duración:** 24 semanas (incl. 1 sem vacacional)
- **Nueva fecha fin:** 18 de mayo de 2026
- **JMB trabaja:** 6h/día máximo (30h/semana)
- **Buffers mantenidos:** Fase 0 y 1 con holgura
- **Riesgo:** BAJO ✅
- **Sostenibilidad:** ALTA ✅

---

## 📞 PRÓXIMA ACCIÓN

**Se requiere aprobación para:**
1. Extender Fase 2 de 7 a 8 semanas
2. Nueva fecha fin: 18 de mayo de 2026 (vs 11 de mayo)
3. Actualizar 7 documentos de la propuesta

**Beneficio:**
- Cronograma realista y sostenible
- JMB trabaja máximo 6h/día
- Proyecto completo sin comprometer calidad

---

*Análisis realizado el 5 de noviembre de 2025*  
*Versión propuesta: 1.2*
