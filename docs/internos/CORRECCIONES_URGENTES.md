# LISTA DE CORRECCIONES URGENTES - PROPUESTA FINAL

**Fecha:** 5 de noviembre de 2025  
**Prioridad:** 🔴 CRÍTICA - Realizar ANTES de enviar propuesta a cliente  
**Tiempo estimado:** 2-3 horas

---

## 🚨 CORRECCIONES CRÍTICAS (OBLIGATORIAS)

### 1. 🔴 Corregir Fechas en Fase 1

**Archivo:** `docs/propuesta_final/05_FASE_1_CONSTRUCCION_DATA_LAKE.md`

**Ubicación:** Sección 5.2 - Duración y Recursos

**Cambios requeridos:**

```markdown
# ANTES (INCORRECTO):
| **Duración estimada** | 8-10 semanas (sprints de 2 semanas, con holguras para ajustes) |
| **Fecha inicio** | 16 de diciembre de 2025 |
| **Fecha fin** | 23 de febrero de 2026 |

# DESPUÉS (CORRECTO):
| **Duración estimada** | 10 semanas (sprints de 2 semanas, con holguras para ajustes) |
| **Fecha inicio** | 13 de enero de 2026 |
| **Fecha fin** | 23 de marzo de 2026 |
```

**Razón:** Las fechas no coinciden con el cronograma V1.2 actualizado.

---

### 2. 🔴 Actualizar Horas y Presupuesto de Fase 1

**Archivo:** `docs/propuesta_final/05_FASE_1_CONSTRUCCION_DATA_LAKE.md`

**Ubicación:** Sección 5.7 - Presupuesto de Fase 1

**Cambios requeridos:**

```markdown
# ANTES (INCORRECTO):
| **Horas totales** | 204 horas |

## 5.7. Presupuesto de Fase 1
| Recurso | Horas | Tarifa (USD/h) | Subtotal (USD) |
|---------|-------|----------------|----------------|
| **Juan Manuel Bigi** | 156h | $25 | $3,900 |
| **Lucía Rodríguez** | 40h | $30 | $1,200 |
| **Consultor ABAP** (contingencia) | 8h | $80-100 | $640-800 |
| **TOTAL FASE 1** | **204h** | - | **$5,740-5,900** |

# DESPUÉS (CORRECTO):
| **Horas totales** | 267 horas |

## 5.7. Presupuesto de Fase 1
| Recurso | Horas | Tarifa (USD/h) | Subtotal (USD) |
|---------|-------|----------------|----------------|
| **Juan Manuel Bigi** | 180h | $25 | $4,500 |
| **Lucía Rodríguez** | 60h | $30 | $1,800 |
| **Linda López (PM)** | 15h | $30 | $450 |
| **Consultor ABAP** | 12h | $80-100 | $960-1,200 |
| **TOTAL FASE 1** | **267h** | - | **$7,710-7,950** |
```

**Razón:** Las horas y costos no coinciden con el documento 08 (Estimación de Esfuerzos).

---

### 3. 🔴 Agregar Sección de Costos en USD

**Archivo:** `docs/propuesta_final/08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md`

**Ubicación:** Después de la sección 8.8 (Factores de Riesgo)

**Contenido a agregar:**

```markdown
---

## 8.9. PRESUPUESTO TOTAL DEL PROYECTO (USD)

### 8.9.1. Tarifas por Recurso

| Recurso | Tarifa (USD/hora) | Justificación |
|---------|-------------------|---------------|
| **Juan Manuel Bigi** | $25/h | Desarrollador BigQuery/Power BI Senior |
| **Lucía Rodríguez** | $30/h | Analista SAP Power User / Consultora |
| **Linda López** | $30/h | Project Manager |
| **Consultor ABAP** | $80-100/h | Especialista ABAP (contingencia) |

---

### 8.9.2. Presupuesto por Fase

#### Fase 0 - Due Diligence (116 horas)

| Recurso | Horas | Tarifa | Subtotal |
|---------|-------|--------|----------|
| Juan Manuel Bigi | 58h | $25/h | $1,450 |
| Lucía Rodríguez | 48h | $30/h | $1,440 |
| Linda López | 10h | $30/h | $300 |
| **SUBTOTAL FASE 0** | **116h** | - | **$3,190** |

---

#### Fase 1 - Construcción Data Lake (267 horas)

| Recurso | Horas | Tarifa | Subtotal |
|---------|-------|--------|----------|
| Juan Manuel Bigi | 180h | $25/h | $4,500 |
| Lucía Rodríguez | 60h | $30/h | $1,800 |
| Linda López | 15h | $30/h | $450 |
| Consultor ABAP | 12h | $80-100/h | $960-1,200 |
| **SUBTOTAL FASE 1** | **267h** | - | **$7,710-7,950** |

---

#### Fase 2 - Dashboards Power BI (294 horas)

| Recurso | Horas | Tarifa | Subtotal |
|---------|-------|--------|----------|
| Juan Manuel Bigi | 240h | $25/h | $6,000 |
| Lucía Rodríguez | 37h | $30/h | $1,110 |
| Linda López | 17h | $30/h | $510 |
| **SUBTOTAL FASE 2** | **294h** | - | **$7,620** |

---

### 8.9.3. PRESUPUESTO TOTAL CONSOLIDADO

| Concepto | Horas | Costo (USD) |
|----------|-------|-------------|
| **Fase 0 - Due Diligence** | 116h | $3,190 |
| **Fase 1 - Data Lake** | 267h | $7,710-7,950 |
| **Fase 2 - Dashboards** | 294h | $7,620 |
| **TOTAL PROYECTO** | **677h** | **$18,520-18,760** |

**Nota:** El rango de costo considera la contingencia de consultoría ABAP ($960-1,200).

---

### 8.9.4. Forma de Pago Propuesta

**Opción A: Pago por Hitos (RECOMENDADO)**

| Hito | Monto | % del Total | Fecha Estimada |
|------|-------|-------------|----------------|
| **Firma de contrato** | $5,556-5,628 | 30% | 1-dic-2025 |
| **Completación Fase 1** | $7,408-7,504 | 40% | 23-mar-2026 |
| **Go-Live Fase 2** | $5,556-5,628 | 30% | 18-may-2026 |
| **TOTAL** | **$18,520-18,760** | **100%** | - |

**Opción B: Pago por Fase**

| Fase | Monto | Fecha Estimada |
|------|-------|----------------|
| **Fase 0** | $3,190 | Al finalizar (12-ene-2026) |
| **Fase 1** | $7,710-7,950 | Al finalizar (23-mar-2026) |
| **Fase 2** | $7,620 | Al finalizar (18-may-2026) |
| **TOTAL** | **$18,520-18,760** | - |

---

### 8.9.5. Condiciones Comerciales

**Facturación:**
- Facturas a nombre de: **Elanco Animal Health - Operación CASA**
- Moneda: **USD (Dólares Estadounidenses)**
- Forma de pago: **Transferencia bancaria**
- Plazo de pago: **15 días desde emisión de factura**

**Términos:**
- ✅ Cotización válida por **30 días** (hasta 5-dic-2025)
- ✅ Precios en USD, no sujetos a ajuste por inflación durante el proyecto
- ✅ Soporte post-implementación: **30 días incluidos** (horario hábil)
- ⚠️ Horas adicionales por cambios de alcance: **USD $25-30/hora** según recurso

**Exclusiones de Costo:**
- ❌ Licencias de software (Google Cloud, Power BI) - Responsabilidad del cliente
- ❌ Infraestructura y servicios cloud (costos BigQuery) - Responsabilidad del cliente
- ❌ Tiempo de stakeholders Elanco para validaciones/workshops - Sin costo
- ❌ Soporte post go-live después de 30 días - Cotización separada

---

### 8.9.6. Inversión vs. Ahorro Esperado

**Inversión Total:** USD $18,520-18,760

**Ahorro Operativo Anual Estimado:**

| Concepto | Ahorro Anual |
|----------|--------------|
| Reducción horas manuales (3,620h/año × $15/h) | $54,300/año |
| Reducción errores y reproceso | $7,500/año |
| Mejor toma de decisiones (cualitativo) | No cuantificado |
| **TOTAL AHORRO TANGIBLE** | **$61,800/año** |

**ROI Esperado:**
- Inversión: $18,650 (promedio)
- Ahorro anual: $61,800
- **Retorno de inversión:** **3.6 meses** ✅
- **ROI a 3 años:** **+892%** ✅

**Análisis de Break-Even:**
- Recuperación de inversión: **~4 meses** de operación
- Beneficio neto año 1: **$43,150** (ahorro - inversión)
- Beneficio neto 3 años: **$166,750**

---

### 8.9.7. Comparativa de Opciones

**Opción 1: Este Proyecto (RECOMENDADO)**
- Inversión: $18,520-18,760
- Duración: 6 meses
- Alcance: 18 transacciones + 12 dashboards
- ROI: 3.6 meses

**Opción 2: Proyecto Reducido (Alternativa)**
- Inversión: $12,000-13,000
- Duración: 4 meses
- Alcance: 8 transacciones + 6 dashboards
- ROI: 4.5 meses
- ⚠️ Menor valor entregado

**Opción 3: Solución Interna (No recomendado)**
- Inversión: $25,000-30,000 (2 FTE × 6 meses)
- Duración: 9-12 meses
- Alcance: Similar
- ROI: 8-10 meses
- ⚠️ Mayor riesgo, menor especialización

---

*Siguiente sección: [09_CRONOGRAMA_SEMANAL.md](09_CRONOGRAMA_SEMANAL.md)*
```

**Razón:** El documento de costos NO incluye presupuesto en USD, solo horas.

---

### 4. 🔴 Completar Información de Contacto

**Archivo:** `docs/propuesta_final/00_PORTADA_Y_RESUMEN_EJECUTIVO.md`

**Ubicación:** Sección "INFORMACIÓN DE CONTACTO"

**Cambios requeridos:**

Reemplazar todos los `[Por confirmar]` con información real:

```markdown
# ANTES:
Email: [Por confirmar]  
Teléfono: [Por confirmar]

# DESPUÉS:
Email: juan.bigi@aunergia.com.ar (o el email real)
Teléfono: +54 11 XXXX-XXXX (o el teléfono real)
```

**Acción:** Solicitar a Linda López la información de contacto correcta.

---

## ⚠️ CORRECCIONES IMPORTANTES (RECOMENDADAS)

### 5. 🟡 Agregar Sección de Control de Cambios

**Archivo:** `docs/propuesta_final/08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md`

**Ubicación:** Al inicio del documento (después de título)

**Contenido a agregar:**

```markdown
## NOTA SOBRE EVOLUCIÓN DEL ALCANCE

**Esta propuesta (Noviembre 2025) representa una expansión del alcance inicial (Octubre 2025):**

| Aspecto | Octubre 2025 | Noviembre 2025 | Cambio |
|---------|--------------|----------------|--------|
| Transacciones SAP | 8 | 18 | +125% |
| Dashboards Power BI | 4-6 | 12 | +100-200% |
| Esfuerzo total | 444h | 677h | +52% |
| Duración | 16 sem | 24 sem | +50% |
| Project Management | Informal | Formalizado (Linda) | Nuevo |
| ABAP Consulting | No incluido | 12h incluidas | Nuevo |

**Justificación:**
- Alcance completo de transacciones validado con stakeholders
- 12 dashboards completos para todas las áreas de negocio
- Project Management formalizado para mejor control
- Restricción de 6h/día de trabajo para salud del equipo
- Buffers adecuados para manejo de riesgos
```

---

### 6. 🟡 Verificar Consistencia de Esfuerzo en Todo el Documento 05

**Archivo:** `docs/propuesta_final/05_FASE_1_CONSTRUCCION_DATA_LAKE.md`

**Buscar y reemplazar:**
- Todas las menciones de "204 horas" → "267 horas"
- Todas las menciones de "156h JMB" → "180h JMB"
- Todas las menciones de "40h Lucía" → "60h Lucía"

**Verificar especialmente:**
- Sección 5.4.1 (Infraestructura)
- Sección 5.4.2 a 5.4.5 (Pipelines por módulo)
- Sección 5.6 (Entregables)
- Sección 5.7 (Presupuesto)
- Sección 5.8 (Criterios de Éxito)

---

## ✅ CHECKLIST DE VERIFICACIÓN POST-CORRECCIÓN

Después de realizar las correcciones, verificar:

### Fechas
- [ ] Fase 0: 1-dic-2025 a 12-ene-2026 (5 sem)
- [ ] Fase 1: 13-ene-2026 a 23-mar-2026 (10 sem)
- [ ] Fase 2: 24-mar-2026 a 18-may-2026 (8 sem)
- [ ] Total: 24 semanas (incl. 1 sem vacacional)

### Horas por Fase
- [ ] Fase 0: 116 horas
- [ ] Fase 1: 267 horas
- [ ] Fase 2: 294 horas
- [ ] Total: 677 horas

### Horas por Recurso
- [ ] JMB: 58h + 180h + 240h = 478h
- [ ] Lucía: 48h + 60h + 37h = 145h
- [ ] Linda: 10h + 15h + 17h = 42h
- [ ] ABAP: 0h + 12h + 0h = 12h
- [ ] Total: 677h

### Costos (Nueva Sección)
- [ ] Presupuesto total: $18,520-18,760
- [ ] Forma de pago: 30/40/30
- [ ] Condiciones comerciales incluidas
- [ ] ROI calculado

### Información de Contacto
- [ ] Emails completados
- [ ] Teléfonos completados
- [ ] Direcciones actualizadas

---

## 🔧 HERRAMIENTAS PARA CORRECCIÓN

### Búsqueda y Reemplazo Global

**Archivo 05:**
```bash
# Buscar: "16 de diciembre de 2025"
# Reemplazar: "13 de enero de 2026"

# Buscar: "23 de febrero de 2026"
# Reemplazar: "23 de marzo de 2026"

# Buscar: "204 horas"
# Reemplazar: "267 horas"

# Buscar: "156h"
# Reemplazar: "180h"
```

---

## 📅 TIMELINE DE CORRECCIÓN

**Hoy (5 de noviembre):**
- ✅ Auditoría completada
- ⏳ Correcciones 1-4 (críticas) - **2 horas**

**Mañana (6 de noviembre):**
- ⏳ Correcciones 5-6 (recomendadas) - **1 hora**
- ⏳ Verificación final completa - **30 min**
- ⏳ Conversión a PDF - **15 min**

**7 de noviembre:**
- ⏳ Revisión por Linda López
- ⏳ Aprobación final
- ⏳ Envío a cliente Elanco

---

## 🎯 RESPONSABLES

| Corrección | Responsable | Deadline |
|------------|-------------|----------|
| 1. Fechas Fase 1 | Juan Manuel Bigi | 5-nov EOD |
| 2. Horas Fase 1 | Juan Manuel Bigi | 5-nov EOD |
| 3. Costos USD | Juan Manuel Bigi | 6-nov AM |
| 4. Contactos | Linda López | 6-nov AM |
| 5. Control cambios | Juan Manuel Bigi | 6-nov PM |
| 6. Verificación final | Linda López | 6-nov PM |

---

## 📞 CONTACTO PARA DUDAS

**Coordinación del proyecto:**
- Linda López (Project Manager Aunergia)

**Contenido técnico:**
- Juan Manuel Bigi (Arquitecto de Datos)

**Contenido funcional:**
- Lucía Rodríguez (Analista SAP)

---

## ✅ CRITERIO DE ACEPTACIÓN

Las correcciones se considerarán completas cuando:

1. ✅ Todas las fechas coincidan entre documentos
2. ✅ Todas las horas sumen correctamente (677h)
3. ✅ Presupuesto en USD esté completo con forma de pago
4. ✅ Información de contacto esté completa
5. ✅ No haya inconsistencias aritméticas
6. ✅ Linda López apruebe la versión final

---

**Estado:** ⏳ **PENDIENTE DE CORRECCIÓN**  
**Prioridad:** 🔴 **CRÍTICA**  
**Deadline:** **6 de noviembre de 2025, 18:00**

---

*Documento generado como resultado de la auditoría del 5 de noviembre de 2025*
