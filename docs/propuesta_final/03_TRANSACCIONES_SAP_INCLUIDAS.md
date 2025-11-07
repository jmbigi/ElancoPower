# 3. TRANSACCIONES SAP INCLUIDAS EN LA PROPUESTA

## 3.1. Nota Importante sobre Transacciones vs. Tablas SAP

**Aclaración Técnica Fundamental:**

En este documento se hace referencia a "transacciones SAP" como punto de partida para identificar los datos requeridos por el negocio. Sin embargo, es importante entender que:

✅ **Lo que se replica son TABLAS SAP, no transacciones**

- Las **transacciones SAP** (VA05, KSB1, FAGLL03, etc.) son **interfaces de usuario** que consultan y muestran datos almacenados en tablas de la base de datos SAP
- Lo que se implementará mediante **SAP SLT (Landscape Transformation Server)** es la **replicación de las tablas subyacentes** que contienen los datos mostrados por esas transacciones
- Por ejemplo: La transacción **VA05** consulta las tablas **VBAK, VBAP, VBEP**, y son estas tablas las que se replicarán a BigQuery

**Proceso Técnico:**

```
TRANSACCIÓN SAP (UI)          TABLAS SAP (Datos)         REPLICACIÓN SLT
┌──────────────┐              ┌──────────────┐           ┌──────────────┐
│   VA05       │              │  VBAK        │           │  BigQuery    │
│ (Órdenes     │──consulta──▶ │  VBAP        │──SLT────▶ │  raw_vbak    │
│  Abiertas)   │              │  VBEP        │           │  raw_vbap    │
│              │              │              │           │  raw_vbep    │
└──────────────┘              └──────────────┘           └──────────────┘
```

**Por lo tanto:**
- Cuando mencionamos "18 transacciones", en realidad nos referimos a "los datos de las tablas asociadas a estas 18 transacciones"
- El análisis en **Fase 0** identificará las **tablas SAP específicas** que deben replicarse
- La replicación se configura **tabla por tabla** en SLT, no "transacción por transacción"

---

## 3.2. Resumen Estadístico

**Total de transacciones identificadas:** 18  
**Fuente:** Attach_2_Correo_1_Transacciones SAP.csv (normalizado)  
**Validación:** 100% de transacciones provienen de documento original de Elanco

### Distribución por Prioridad

| Prioridad | Cantidad | Porcentaje | Estimado de Tablas SAP |
|-----------|----------|------------|------------------------|
| **Prioridad 1 (Críticas)** | 4 | 22% | ~15-20 tablas |
| **Prioridad 2 (Importantes)** | 4 | 22% | ~15-20 tablas |
| **Pendientes de clasificar** | 10 | 56% | ~40-50 tablas |
| **TOTAL** | **18** | **100%** | **~70-90 tablas SAP** |

**Nota:** Una transacción puede requerir múltiples tablas. Por ejemplo, VA05 requiere al menos 3 tablas (VBAK, VBAP, VBEP).

### Distribución por Módulo SAP

| Módulo | Descripción | Transacciones |
|--------|-------------|---------------|
| **FI** | Financial Accounting | 6 transacciones |
| **CO** | Controlling | 2 transacciones |
| **SD** | Sales & Distribution | 2 transacciones |
| **MM** | Materials Management | 5 transacciones |
| **Z-Custom** | Transacciones customizadas | 2 transacciones |
| **MD** | Master Data | 1 transacción |

### Áreas de Negocio Involucradas

| Área | Transacciones Asignadas | Priorización Completada |
|------|------------------------|------------------------|
| **Finanzas** | 8 | ✅ Sí |
| **Supply Chain** | 1 | ✅ Sí |
| **Supply-Finanzas** | 1 | ✅ Sí |
| **Sin asignar** | 8 | ⏳ Pendiente Workshop Fase 0 |

---

## 3.2. PRIORIDAD 1 - Transacciones Críticas

### 3.2.1. VA05 - Sales Order / Órdenes Abiertas

**Código:** VA05  
**Módulo SAP:** SD (Sales & Distribution)  
**Área:** Supply Chain / Finanzas  
**Prioridad:** ⭐⭐⭐ CRÍTICA

#### Descripción
Transacción para consultar órdenes de venta abiertas (pendientes de facturación o entrega). Permite visualizar el backlog de órdenes, montos comprometidos y fechas de entrega programadas.

#### Datos Clave
- **Tablas SAP principales:** VBAK (cabecera), VBAP (posiciones), VBEP (schedule lines)
- **Campos críticos:**
  - Número de orden (VBELN)
  - Cliente (KUNNR)
  - Material (MATNR)
  - Cantidad (KWMENG)
  - Valor neto (NETWR)
  - Fecha entrega (EDATU)
  - Status (GBSTK, LFSTK)

#### Uso de Negocio
- **Finanzas:** Proyección de ingresos, revenue recognition
- **Supply:** Planificación de despachos, gestión de backlog
- **Management:** KPI de órdenes abiertas por cliente/producto

#### Frecuencia de Actualización Propuesta
**Diaria** (batch nocturno) - Los datos deben estar disponibles cada mañana

#### Complejidad de Implementación
**Media** - Transacción estándar con múltiples tablas relacionadas

#### Volumen Estimado
- Registros históricos: ~500K-1M órdenes (24 meses)
- Crecimiento mensual: ~20K-30K órdenes nuevas

---

### 3.2.2. ZLEL008 - Inventario Consolidado

**Código:** ZLEL008  
**Módulo SAP:** Z-Custom (Transacción customizada Elanco)  
**Área:** Supply Chain - Finanzas  
**Prioridad:** ⭐⭐⭐ CRÍTICA

#### Descripción
Transacción **custom** desarrollada específicamente para Elanco que consolida información de inventarios de todos los centros y almacenes. Proporciona visión unificada del stock disponible, en tránsito, reservado y bloqueado.

#### Datos Clave
- **Tablas SAP:** Por determinar (requiere análisis de transacción Z)
- **Posibles tablas:** MARD (stock por almacén), MSKA (stock especial), MSEG (movimientos)
- **Campos críticos:**
  - Material (MATNR)
  - Centro (WERKS)
  - Almacén (LGORT)
  - Stock disponible (LABST)
  - Stock en tránsito
  - Stock bloqueado (SPEME)
  - Valorización (SALK3)

#### Uso de Negocio
- **Supply:** Visibilidad de inventarios consolidados por país
- **Finanzas:** Valorización de inventarios para balance
- **Planeación:** Decisiones de transferencias entre centros

#### Frecuencia de Actualización Propuesta
**Diaria** (batch nocturno) - Inventarios al cierre del día anterior

#### Complejidad de Implementación
**Alta** - Transacción custom requiere:
- Análisis de código ABAP para identificar tablas fuente
- Posible consultoría ABAP especializada (8-16 horas)
- Validación con power user que conoce la lógica

#### Volumen Estimado
- Registros históricos: ~100K-200K registros (24 meses)
- Crecimiento mensual: ~5K-8K registros

#### Observaciones
⚠️ **Riesgo:** Las tablas de esta transacción custom pueden no estar disponibles en BigQuery (Issue #2 reportado por David Saboya). **Ticket BQ-7713 pendiente** de aprobación por TI Global.

---

### 3.2.3. KSB1 - OPEX / Órdenes CO

**Código:** KSB1  
**Módulo SAP:** CO (Controlling)  
**Área:** Finanzas  
**Prioridad:** ⭐⭐⭐ CRÍTICA

#### Descripción
Reporte de partidas reales de órdenes de costos (órdenes internas de CO). Utilizado para análisis de gastos operativos (OPEX) por centro de costo, naturaleza del gasto y cuenta contable.

#### Datos Clave
- **Tablas SAP principales:** COBK (cabecera doc CO), COEP (partidas individuales), AUFK (maestro de órdenes)
- **Campos críticos:**
  - Orden CO (AUFNR)
  - Centro de costo (KOSTL)
  - Elemento de costo (KSTAR)
  - Importe en moneda local (WTGBTR)
  - Importe en moneda grupo (WOGBTR)
  - Fecha contabilización (BUDAT)
  - Clase de costo (KOART)

#### Uso de Negocio
- **Finanzas:** Control presupuestario de OPEX
- **Controllers:** Análisis de desviaciones vs. budget
- **Management:** Dashboard de gastos operativos por área

#### Frecuencia de Actualización Propuesta
**Semanal** (lunes) - Suficiente para control presupuestario

#### Complejidad de Implementación
**Alta** - Módulo CO con múltiples dimensiones y lógica compleja

#### Volumen Estimado
- Registros históricos: ~2M-3M partidas (24 meses)
- Crecimiento mensual: ~80K-100K partidas

---

### 3.2.4. FAGLL03 - Mayor General

**Código:** FAGLL03  
**Módulo SAP:** FI (Financial Accounting)  
**Área:** Finanzas  
**Prioridad:** ⭐⭐⭐ CRÍTICA

#### Descripción
Visualización de partidas individuales del libro mayor (General Ledger). Transacción fundamental para análisis contable detallado, conciliaciones y auditoría.

#### Datos Clave
- **Tablas SAP principales:** FAGLFLEXA (partidas individuales nuevo GL), BKPF (cabecera documento), BSEG (segmento documento)
- **Campos críticos:**
  - Sociedad (BUKRS)
  - Cuenta de mayor (RACCT)
  - Ejercicio/periodo (RYEAR, POPER)
  - Importe en moneda sociedad (HSL)
  - Importe en moneda grupo (KSL)
  - Centro de beneficio (PRCTR)
  - Segmento (SEGMENT)

#### Uso de Negocio
- **Finanzas:** Balance de comprobación, estados financieros
- **Auditoría:** Trazabilidad de movimientos contables
- **Consolidación:** Reportes corporativos

#### Frecuencia de Actualización Propuesta
**Diaria** (batch nocturno) - Datos contables del día anterior

#### Complejidad de Implementación
**Media-Alta** - Tabla FAGLFLEXA de gran volumen, requiere filtros eficientes

#### Volumen Estimado
- Registros históricos: ~5M-10M partidas (24 meses)
- Crecimiento mensual: ~200K-400K partidas

#### Observaciones
⚠️ **Riesgo:** Tabla FAGLFLEXA puede no estar completa en BigQuery. **Ticket BQ-7721 pendiente** de validación con TI Global.

---

## 3.3. PRIORIDAD 2 - Transacciones Importantes

### 3.3.1. KE24 - Venta / CO-PA

**Código:** KE24  
**Módulo SAP:** CO (Controlling) - CO-PA (Profitability Analysis)  
**Área:** Finanzas  
**Prioridad:** ⭐⭐ IMPORTANTE

#### Descripción
Reporte de partidas individuales de CO-PA (Cuenta de Resultados). Análisis de rentabilidad por segmentos (cliente, producto, canal, región).

#### Datos Clave
- **Tablas SAP principales:** CE1xxxx (partidas reales), CE4xxxx (partidas plan)
- **Campos críticos:**
  - Cliente (KUNNR)
  - Material (MATNR)
  - Canal de distribución (VTWEG)
  - Ventas netas (VV100)
  - Costo de ventas (VV110)
  - Margen bruto (calculado)

#### Uso de Negocio
- **Finanzas:** Análisis de rentabilidad por producto/cliente
- **Comercial:** Decisiones de pricing y descuentos
- **Management:** P&L por segmento de negocio

#### Frecuencia de Actualización Propuesta
**Semanal** (lunes) - Análisis de rentabilidad no requiere diario

#### Complejidad de Implementación
**Alta** - CO-PA con estructuras dinámicas (CE tables varían por company code)

#### Volumen Estimado
- Registros históricos: ~1M-2M partidas (24 meses)
- Crecimiento mensual: ~40K-80K partidas

---

### 3.3.2. FB03 - Documentos de Venta

**Código:** FB03  
**Módulo SAP:** FI (Financial Accounting)  
**Área:** Finanzas  
**Prioridad:** ⭐⭐ IMPORTANTE

#### Descripción
Visualización de documentos contables (facturas, notas de crédito, pagos). Transacción de consulta para análisis de documentos individuales.

#### Datos Clave
- **Tablas SAP principales:** BKPF (cabecera), BSEG (posiciones), BSID/BSAD (partidas deudores)
- **Campos críticos:**
  - Número documento (BELNR)
  - Tipo documento (BLART)
  - Cliente/Proveedor (KUNNR/LIFNR)
  - Importe (DMBTR)
  - Fecha documento (BLDAT)
  - Fecha contabilización (BUDAT)

#### Uso de Negocio
- **Finanzas:** Análisis de cuentas por cobrar/pagar
- **Tesorería:** Gestión de cobranzas
- **Auditoría:** Revisión de documentos contables

#### Frecuencia de Actualización Propuesta
**Diaria** (batch nocturno)

#### Complejidad de Implementación
**Media** - Tablas estándar bien documentadas

#### Volumen Estimado
- Registros históricos: ~1M-2M documentos (24 meses)
- Crecimiento mensual: ~40K-80K documentos

---

### 3.3.3. F.08 - Balance de Comprobación

**Código:** F.08  
**Módulo SAP:** FI (Financial Accounting)  
**Área:** Finanzas  
**Prioridad:** ⭐⭐ IMPORTANTE

#### Descripción
Balance de comprobación (Trial Balance) por cuenta de mayor. Resume saldos iniciales, movimientos del periodo y saldos finales.

#### Datos Clave
- **Tablas SAP principales:** FAGLFLEXA (partidas), FAGLFLEXT (totales periodo)
- **Campos críticos:**
  - Cuenta de mayor (RACCT)
  - Saldo inicial
  - Debe/Haber periodo
  - Saldo final

#### Uso de Negocio
- **Finanzas:** Estados financieros mensuales
- **Controllers:** Cierre contable
- **Auditoría:** Validación de saldos

#### Frecuencia de Actualización Propuesta
**Mensual** (al cierre) - Suficiente para reportes financieros

#### Complejidad de Implementación
**Media** - Requiere lógica de cálculo de saldos

#### Volumen Estimado
- Registros: ~5K-10K cuentas por periodo

---

### 3.3.4. F.01 - Estado de Situación

**Código:** F.01  
**Módulo SAP:** FI (Financial Accounting)  
**Área:** Finanzas  
**Prioridad:** ⭐⭐ IMPORTANTE

#### Descripción
Balance General (Balance Sheet) con estructura jerárquica de cuentas.

#### Datos Clave
- **Tablas SAP principales:** FAGLFLEXA, SKA1 (plan de cuentas)
- **Campos críticos:**
  - Cuenta de mayor (RACCT)
  - Grupo de cuentas
  - Saldos por periodo

#### Uso de Negocio
- **Finanzas:** Balance General mensual
- **Management:** Análisis de estructura financiera
- **Corporativo:** Consolidación regional

#### Frecuencia de Actualización Propuesta
**Mensual** (al cierre)

#### Complejidad de Implementación
**Media** - Similar a F.08

#### Volumen Estimado
- Registros: ~3K-5K cuentas de balance por periodo

---

## 3.4. PENDIENTES DE CLASIFICAR (Sin prioridad asignada)

Las siguientes **10 transacciones** están identificadas en el documento original pero **no tienen prioridad asignada**. Se clasificarán durante el **Workshop de Fase 0** con Finanzas, Supply Chain y TechOps.

### 3.4.1. ME2L - Purchase Orders (PO)

**Código:** ME2L  
**Módulo SAP:** MM (Materials Management)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Lista de pedidos de compra por proveedor. Utilizada para seguimiento de órdenes de compra abiertas.

**Tablas SAP principales:** EKKO (cabecera OC), EKPO (posiciones OC)

---

### 3.4.2. MM60 - Standard Cost (Costos Estándar)

**Código:** MM60  
**Módulo SAP:** MM (Materials Management)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Visualización de costos estándar de materiales por centro.

**Tablas SAP principales:** MBEW (valorización), CKMLCR (componentes de costo)

---

### 3.4.3. MB59 - Movimientos de Material

**Código:** MB59  
**Módulo SAP:** MM (Materials Management)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Análisis de stock por fecha de recepción (SLED/BBD analysis).

**Tablas SAP principales:** MSEG (movimientos), MARD (stocks)

---

### 3.4.4. ZVEL015 - Condiciones de Precio

**Código:** ZVEL015  
**Módulo SAP:** Z-Custom  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Transacción custom para consulta de condiciones de pricing.

**Tablas SAP:** Por determinar (transacción Z)

⚠️ **Riesgo:** Transacción custom, puede requerir análisis ABAP.

---

### 3.4.5. ME23N - Display Purchase Order

**Código:** ME23N  
**Módulo SAP:** MM (Materials Management)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Visualización individual de pedidos de compra.

**Tablas SAP principales:** EKKO, EKPO

---

### 3.4.6. FBL1N - Vendor Line Items

**Código:** FBL1N  
**Módulo SAP:** FI (Financial Accounting)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Partidas individuales de proveedores (cuentas por pagar).

**Tablas SAP principales:** BSIK (partidas abiertas), BSAK (partidas compensadas)

---

### 3.4.7. FBL5N - Customer Line Items

**Código:** FBL5N  
**Módulo SAP:** FI (Financial Accounting)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Partidas individuales de clientes (cuentas por cobrar).

**Tablas SAP principales:** BSID (partidas abiertas), BSAD (partidas compensadas)

---

### 3.4.8. MB5B - Stock for Material

**Código:** MB5B  
**Módulo SAP:** MM (Materials Management)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Stock de materiales por centro/almacén.

**Tablas SAP principales:** MARD, MCHB (lotes)

---

### 3.4.9. XK03 - Display Vendor Master

**Código:** XK03  
**Módulo SAP:** MD (Master Data)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Visualización de maestro de proveedores.

**Tablas SAP principales:** LFA1 (general), LFB1 (datos sociedad), LFM1 (datos organización compras)

---

### 3.4.10. XD03 - Display Customer Master

**Código:** XD03  
**Módulo SAP:** MD (Master Data)  
**Área:** Por asignar  
**Prioridad:** ⏳ Pendiente

#### Descripción Preliminar
Visualización de maestro de clientes.

**Tablas SAP principales:** KNA1 (general), KNB1 (datos sociedad), KNVV (datos ventas)

---

## 3.5. Estrategia de Priorización para Fase 0

Durante el **Workshop de Fase 0** (estimado semana 2), se priorizarán las 10 transacciones pendientes utilizando los siguientes criterios:

### Criterios de Priorización

| Criterio | Peso | Descripción |
|----------|------|-------------|
| **Impacto en negocio** | 40% | ¿Qué tan crítica es para toma de decisiones? |
| **Frecuencia de uso** | 25% | ¿Con qué frecuencia se consulta actualmente? |
| **Complejidad técnica** | 20% | ¿Qué tan fácil es implementar? (inverso) |
| **Dependencias** | 15% | ¿Es prerequisito para otras transacciones? |

### Metodología de Priorización

1. **Entrevistas por área:**
   - Finanzas: 2 horas
   - Supply Chain: 2 horas
   - TechOps: 1 hora

2. **Scoring de transacciones:**
   - Cada stakeholder califica de 1-5 cada criterio
   - Se promedian scores por área
   - Se calcula score ponderado final

3. **Clasificación resultante:**
   - Score ≥ 4.0: Prioridad 1 (agregar a críticas)
   - Score 3.0-3.9: Prioridad 2 (agregar a importantes)
   - Score < 3.0: Prioridad 3 (postergar a fase futura)

### Resultado Esperado

**Objetivo:** Clasificar las 10 transacciones en:
- ✅ **6-8 transacciones** incluidas en Fase 1 (total 12-14 transacciones)
- ⏸️ **2-4 transacciones** postergadas para fase futura

**Criterio Go/No-Go para Fase 1:**
- Mínimo **12 de 18 transacciones** con tablas confirmadas en BigQuery
- Si menos de 12 disponibles: Evaluar plan B (Azure Data Lake o extracción RFC)

---

## 3.6. Observaciones Importantes

### 3.6.1. Fuente de Datos

✅ **Todas las 18 transacciones** provienen del archivo original **"Attach_2_Correo_1_Transacciones SAP.csv"** proporcionado por Lucía Rodríguez (Elanco).

✅ **No se han agregado transacciones adicionales** sin confirmación de Elanco.

### 3.6.2. Duplicados Eliminados

Durante la normalización se eliminaron duplicados:
- **VA05** (aparecía 2 veces: "Sales Order" y "Órdenes Abiertas")
- **KE24** (aparecía 2 veces: ambas como "Venta")
- **FB03** (aparecía 2 veces: ambas como "Documentos de Venta")
- **ME2L** (aparecía 2 veces: "PO" y sin descripción)

### 3.6.3. Inconsistencias de Formato

Corregidas durante normalización:
- **xk03 → XK03** (minúsculas a mayúsculas)
- **xd03 → XD03** (minúsculas a mayúsculas)

### 3.6.4. Pendientes de Confirmación con TI Global

Para cada transacción se debe validar en Fase 0:

1. ✅ **Identificación de tablas SAP subyacentes** - Determinar todas las tablas que consulta cada transacción
2. ✅ **Nombres exactos de tablas SAP** a replicar mediante SLT
3. ✅ **Campos clave** requeridos para análisis (pueden replicarse subconjuntos de campos)
4. ✅ **Relaciones entre tablas** (claves foráneas, joins necesarios)
5. ✅ **Frecuencia de replicación SLT** adecuada (tiempo real, batch diario, etc.)
6. ✅ **Disponibilidad en dataset CASA** de BigQuery (confirmar que tablas ya están siendo replicadas)
7. ✅ **Volúmenes estimados** de datos (24 meses históricos + crecimiento)
8. ✅ **Lógica de cálculo** en transacciones custom (Z) que debe recrearse en BigQuery

### 3.6.5. Transacciones Custom (Z)

⚠️ **Riesgo elevado** para:
- **ZLEL008** - Inventario consolidado
- **ZVEL015** - Condiciones de precio

**Mitigación:**
- Análisis de código ABAP en Fase 0
- Presupuesto de contingencia para consultoría ABAP (8-16 horas)
- Coordinación con equipo ABAP de Elanco (si disponible)

---

## 3.7. Próximos Pasos (Fase 0)

### Semana 1-2 de Fase 0

1. ✅ **Workshop de priorización** con stakeholders (4 horas)
2. ✅ **Mapeo de transacciones a tablas SAP** - Identificar todas las tablas subyacentes por transacción
3. ✅ **Análisis de transacciones custom** (ZLEL008, ZVEL015) - Ingeniería reversa para identificar tablas
4. ✅ **Validación de disponibilidad de tablas** en BigQuery con TI Global
5. ✅ **Análisis de relaciones entre tablas** (joins, claves foráneas)
6. ✅ **Estimación de volúmenes** por tabla SAP
7. ✅ **Definición de SLAs** de replicación SLT

### Entregable Clave

📋 **"Mapeo Completo: Transacciones → Tablas SAP → BigQuery"**
- 18 transacciones clasificadas por prioridad
- Listado completo de tablas SAP requeridas (~70-90 tablas)
- Confirmación de disponibilidad de cada tabla en BigQuery
- Estimación de esfuerzo por tabla (configuración SLT, validación, transformaciones)
- Orden de implementación para Fase 1
- Identificación de riesgos técnicos por tabla

---

*Siguiente sección: [04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD.md](04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD.md)*
