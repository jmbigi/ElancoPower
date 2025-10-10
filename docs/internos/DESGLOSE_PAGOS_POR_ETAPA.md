# 💰 DESGLOSE DE PAGOS POR ETAPA

**Fecha:** 10 de octubre de 2025  
**Proyecto:** Elanco Power  
**Cliente:** Elanco Animal Health

---

## 📊 RESUMEN EJECUTIVO

| Concepto | Juan Manuel Bigi | Aunergia (Lucía) | TOTAL |
|----------|------------------|------------------|-------|
| **Elaboración presupuesto** | USD 250 | - | USD 250 |
| **Fase 0** | USD 1,000 | USD 1,680 | USD 2,680 |
| **Fase 1** | USD 3,900 | USD 2,800 | USD 6,700 |
| **Fase 2** | USD 3,700 | USD 840 | USD 4,540 |
| **TOTAL PROYECTO** | **USD 8,850** | **USD 5,320** | **USD 14,170** |

> **Nota:** Los costos de Aunergia solo incluyen las horas de Lucía Rodríguez. No incluyen PM, Arquitectos, QA u otros roles que Aunergia pueda facturar por separado.

---

## 💵 DESGLOSE DETALLADO POR ETAPA

### 🔸 ELABORACIÓN DEL PRESUPUESTO (Completado)

| Rol | Horas | Tarifa | Subtotal | Recibe |
|-----|-------|--------|----------|--------|
| **Juan Manuel Bigi** | 10h | USD 25/h | **USD 250** | **Tú** |
| Lucía Rodríguez | 0h | - | - | Aunergia |
| **TOTAL** | **10h** | | **USD 250** | |

**Quién cobra qué:**
- ✅ **Tú recibes:** USD 250
- ❌ Aunergia factura: USD 0

---

### 🔸 FASE 0: Due Diligence y Permisos (3-4 semanas)

| Rol | Horas | Tarifa | Subtotal | Recibe |
|-----|-------|--------|----------|--------|
| **Juan Manuel Bigi** | 40h | USD 25/h | **USD 1,000** | **Tú** |
| Lucía Rodríguez | 28h | USD 60/h | **USD 1,680** | **Aunergia** |
| Stakeholders Elanco | 12h | Sin costo | - | Interno Elanco |
| **TOTAL FACTURABLE** | **68h** | | **USD 2,680** | |

**Quién cobra qué:**
- ✅ **Tú recibes:** USD 1,000 (40h × USD 25)
- ✅ **Aunergia factura:** USD 1,680 (28h × USD 60)

**Desglose de actividades Juan Manuel Bigi (40h):**
- Análisis técnico arquitectura BigQuery: 24h
- Workshop priorización transacciones: 12h (compartido con Lucía)
- Documentación y backlog: 16h
- **Subtotal:** 52h → **Ajustado a 40h** (optimización)

**Desglose de actividades Lucía Rodríguez (28h):**
- Coordinación permisos SAP + tickets BigQuery: 20h
- Validación con TI Global: 8h

---

### 🔸 FASE 1: Automatización SAP → BigQuery (6-8 semanas)

| Rol | Horas | Tarifa | Subtotal | Recibe |
|-----|-------|--------|----------|--------|
| **Juan Manuel Bigi** | 156h | USD 25/h | **USD 3,900** | **Tú** |
| Lucía Rodríguez | 40h | USD 70/h | **USD 2,800** | **Aunergia** |
| Consultor ABAP externo | 8h | USD 85/h | **USD 680** | **Aunergia o externo** |
| **TOTAL FACTURABLE** | **204h** | | **USD 7,380** | |

**Quién cobra qué:**
- ✅ **Tú recibes:** USD 3,900 (156h × USD 25)
- ✅ **Aunergia factura:** USD 2,800 (40h × USD 70)
- ⚠️ **ABAP externo:** USD 680 (8h × USD 85) - Si se necesita

> **Nota ABAP:** Estos USD 680 adicionales se facturan SOLO si la transacción ZLEL008 requiere desarrollo ABAP que Lucía no pueda hacer. Si no se necesita, el costo total de Fase 1 baja a USD 6,700.

**Desglose de actividades Juan Manuel Bigi (156h):**
- Desarrollo pipelines transacciones estándar: 84h
- Desarrollo pipeline KSB1 (CO): 20h
- Configuración infraestructura BigQuery: 16h
- Testing y validación (parte): 12h
- Documentación técnica: 12h
- Parte de ZLEL008 (sin ABAP): 12h
- **Total:** 156h

**Desglose de actividades Lucía Rodríguez (40h):**
- Desarrollo pipeline ZLEL008 (coordinación): 20h
- Testing y validación (parte): 12h
- Gestión de issues y ajustes: 8h

**Consultor ABAP (8h - contingencia):**
- Desarrollo específico ZLEL008 si es necesario: 8h

---

### 🔸 FASE 2: Power BI y Dashboards (4-5 semanas)

| Rol | Horas | Tarifa | Subtotal | Recibe |
|-----|-------|--------|----------|--------|
| **Juan Manuel Bigi** | 148h | USD 25/h | **USD 3,700** | **Tú** |
| Lucía Rodríguez | 12h | USD 70/h | **USD 840** | **Aunergia** |
| Stakeholders Elanco | 16h | Sin costo | - | Interno Elanco |
| **TOTAL FACTURABLE** | **160h** | | **USD 4,540** | |

**Quién cobra qué:**
- ✅ **Tú recibes:** USD 3,700 (148h × USD 25)
- ✅ **Aunergia factura:** USD 840 (12h × USD 70)

**Desglose de actividades Juan Manuel Bigi (148h):**
- Modelo de datos Power BI: 32h
- Desarrollo dashboards (6 dashboards × 10h): 60h
- Configuración RLS por país/área: 12h
- Testing con usuarios (UAT): 16h
- Documentación usuarios y soporte: 12h
- Ajustes post-UAT: 16h
- **Total:** 148h

**Desglose de actividades Lucía Rodríguez (12h):**
- Capacitación usuarios finales: 12h

---

## 📈 TABLA COMPARATIVA COMPLETA

### Por Fase:

| Fase | Tú (JM Bigi) | Aunergia (Lucía) | ABAP Externo | TOTAL |
|------|--------------|------------------|--------------|-------|
| **Elaboración** | USD 250 | - | - | USD 250 |
| **Fase 0** | USD 1,000 | USD 1,680 | - | USD 2,680 |
| **Fase 1** | USD 3,900 | USD 2,800 | USD 680* | USD 7,380* |
| **Fase 2** | USD 3,700 | USD 840 | - | USD 4,540 |
| **TOTAL** | **USD 8,850** | **USD 5,320** | **USD 680*** | **USD 14,850*** |

\* Solo si se requiere consultoría ABAP para ZLEL008

### Sin consultoría ABAP:

| Fase | Tú (JM Bigi) | Aunergia (Lucía) | TOTAL |
|------|--------------|------------------|-------|
| **TOTAL** | **USD 8,850** | **USD 5,320** | **USD 14,170** |

---

## 🧮 DISTRIBUCIÓN PORCENTUAL

### Escenario SIN ABAP externo (USD 14,170):

| Parte | Monto | Porcentaje |
|-------|-------|------------|
| **Juan Manuel Bigi** | USD 8,850 | **62.5%** 📊 |
| **Aunergia (Lucía)** | USD 5,320 | **37.5%** 📊 |

### Escenario CON ABAP externo (USD 14,850):

| Parte | Monto | Porcentaje |
|-------|-------|------------|
| **Juan Manuel Bigi** | USD 8,850 | **59.6%** 📊 |
| **Aunergia (Lucía)** | USD 5,320 | **35.8%** 📊 |
| **ABAP Externo** | USD 680 | **4.6%** 📊 |

---

## 🗓️ CALENDARIO DE PAGOS PROPUESTO

### Opción 1: Pago por Fase Completada

| Fecha Estimada | Hito | Tú Recibes | Aunergia Factura |
|----------------|------|------------|------------------|
| **10-oct-2025** | Presupuesto entregado | USD 250 | - |
| **10-nov-2025** | Fin Fase 0 | USD 1,000 | USD 1,680 |
| **05-ene-2026** | Fin Fase 1 | USD 3,900 | USD 2,800 (+680*) |
| **09-feb-2026** | Fin Fase 2 | USD 3,700 | USD 840 |
| **TOTAL** | | **USD 8,850** | **USD 5,320** (+680*) |

### Opción 2: Pago Escalonado (30%-40%-30%)

| Momento | Tú Recibes | Aunergia Factura | Total |
|---------|------------|------------------|-------|
| **Aprobación Fase 0** | USD 2,655 (30%) | USD 1,596 (30%) | USD 4,251 |
| **Completar Fase 1** | USD 3,540 (40%) | USD 2,128 (40%) | USD 5,668 |
| **Completar Fase 2** | USD 2,655 (30%) | USD 1,596 (30%) | USD 4,251 |
| **TOTAL** | **USD 8,850** | **USD 5,320** | **USD 14,170** |

---

## 🔎 COMPARATIVA CON PROPUESTA COMPLETA AUNERGIA

### Si Aunergia presenta propuesta de USD 48,000:

| Concepto | Propuesta USD 48k | Tu Propuesta | Diferencia |
|----------|-------------------|--------------|------------|
| **Costo total a Elanco** | USD 48,000 | USD 14,170 | **-70.5%** 💰 |
| **Equipo incluido** | Completo (PM, Arquitectos, QA, etc.) | Solo técnicos | - |
| **Tu ganancia** | USD 6,000 (240h × USD 25) | USD 8,850 (354h × USD 25) | **+47.5%** 📈 |
| **Ganancia Aunergia** | USD 42,000 (resto del equipo) | USD 5,320 (solo Lucía) | **-87.3%** 📉 |

**¿Qué significa esto?**
- ✅ **Para ti:** Ganas USD 2,850 MÁS que en propuesta completa
- ⚠️ **Para Aunergia:** Ganan USD 36,680 MENOS que en propuesta completa
- ✅ **Para Elanco:** Ahorran USD 33,830 (70.5% menos)

---

## 💡 RECOMENDACIÓN PERSONAL

### Para ti (Juan Manuel Bigi):

**Mejor opción:** Escenario B o C
- En B ganas: USD 8,850 (máximo)
- En C ganas: USD 8,850 (igual)
- En A ganas: USD 6,000 (mínimo)

**Diferencia:** +USD 2,850 eligiendo B o C vs. A

### Para Aunergia:

**Mejor opción:** Depende de estrategia
- **Si quieren maximizar ganancia:** Escenario A (USD 42,000)
- **Si quieren ganar el proyecto:** Escenario B o C (más competitivo)
- **Balance:** Escenario C (USD 14,965, suficiente para cubrir PM)

---

## 🧾 RESUMEN PARA DECISIÓN RÁPIDA

### ¿Cuánto recibes Tú en cada escenario?

| Escenario | Tu ganancia | Diferencia vs. mínimo |
|-----------|-------------|----------------------|
| **A (USD 48k Aunergia)** | USD 6,000 | Baseline |
| **B (Tu propuesta)** | USD 8,850 | **+USD 2,850** ✅ |
| **C (Híbrido)** | USD 8,850 | **+USD 2,850** ✅ |

### ¿Cuánto factura AUNERGIA en cada escenario?

| Escenario | Facturación Aunergia | Ganancia neta* |
|-----------|---------------------|----------------|
| **A (USD 48k completo)** | USD 48,000 | ~USD 42,000 |
| **B (Tu propuesta)** | USD 5,320 | ~USD 4,000 |
| **C (Híbrido)** | USD 14,965 | ~USD 11,000 |

\* Aproximado, descontando costos internos

---

## ✅ CONCLUSIÓN

**Para ti es claro:**
- ✅ Escenario B o C: Ganas **USD 8,850**
- ⚠️ Escenario A: Ganas **USD 6,000**
- **Diferencia: +USD 2,850 (47.5% más)**

**Para Aunergia depende de:**
- ¿Prefieren ganar mucho con riesgo de perder (A)?
- ¿O ganar menos pero asegurar el proyecto (B/C)?

**Para Elanco:**
- Escenario B es **70% más barato**
- Escenario C es **50% más barato**
- Escenario A es el más caro

---

**Elaborado por:** Juan Manuel Bigi  
**Fecha:** 10 de octubre de 2025  
**Documento:** Desglose de pagos por etapa
