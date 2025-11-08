# SOLUCIÓN SLT EXPANDIDA - 18 TRANSACCIONES SAP

**Versión:** 2.0 - Alcance Completo  
**Fecha:** 7 de noviembre de 2025  
**Basado en:** Solución Piloto VA05 (v1.0) + Attach_2 CSV del Funcional SAP  
**Estado:** 📋 PROPUESTA PARA REVISIÓN

---

## 🎯 VISIÓN GENERAL

Este documento expande la **Solución Piloto VA05** para cubrir las **18 transacciones SAP** identificadas en el archivo `Attach_2_Correo_1_Transacciones SAP.csv` de Elanco.

### Estrategia de Implementación por Fases

```
FASE 0: Piloto VA05
  └─► 1 transacción, 6 tablas, 70 días-persona, 10 semanas
      Estado: ✅ DOCUMENTADO Y LISTO

FASE 1: Transacciones Críticas (Prioridad 1)
  └─► 4 transacciones, 16-21 tablas, 240-295 días-persona, 33-41 semanas
      Estado: 📋 ESTE DOCUMENTO

FASE 2: Transacciones Importantes (Prioridad 2)
  └─► 2 transacciones, 5-7 tablas, 95-125 días-persona, 13-17 semanas
      Estado: 📋 ESTE DOCUMENTO

FASE 3: Transacciones Complementarias
  └─► 12 transacciones, 20-25 tablas, 300 días-persona, 20-25 semanas
      Estado: 📋 ESTE DOCUMENTO
```

---

## 📊 RESUMEN EJECUTIVO: 18 TRANSACCIONES

### Distribución por Módulo SAP

| Módulo | Transacciones | % del Total | Esfuerzo Estimado |
|--------|---------------|-------------|-------------------|
| **FI** (Financial Accounting) | 6 | 33% | 280-340 días |
| **MM** (Materials Management) | 5 | 28% | 180-220 días |
| **CO** (Controlling) | 2 | 11% | 105-140 días |
| **SD** (Sales & Distribution) | 2 | 11% | 80-95 días |
| **Z-Custom** (Transacciones Elanco) | 2 | 11% | 100-140 días |
| **MD** (Master Data) | 1 | 6% | 15-20 días |
| **TOTAL** | **18** | **100%** | **660-845 días-persona** |

### Inversión Total Estimada

| Concepto | Valor |
|----------|-------|
| **Esfuerzo RRHH Total** | 660-845 días-persona |
| **Duración Total** | 66-83 semanas (15-19 meses) |
| **Infraestructura (Año 1-2)** | $82,800 - $87,400 |
| **Consultoría Especializada (Trans. Z)** | $2,500 - $5,000 |
| **Contingencia (15%)** | A calcular sobre RRHH |

---

## 📋 CATÁLOGO COMPLETO DE 18 TRANSACCIONES

---

## FASE 0 - PILOTO ✅

### T01. VA05 - Sales Order / Órdenes Abiertas

**Prioridad:** ⭐⭐⭐ CRÍTICA  
**Módulo:** SD (Sales & Distribution)  
**Estado:** ✅ **COMPLETAMENTE DOCUMENTADO**

#### Tablas SAP (6 tablas)
1. VBAK - Sales Document: Header Data
2. VBAP - Sales Document: Item Data
3. VBUK - Sales Document: Header Status and Administrative Data
4. VBUP - Sales Document: Item Status
5. KNA1 - General Data in Customer Master
6. MARA - General Material Data

#### Esfuerzo
- **Días-persona:** 70
- **Duración:** 10 semanas
- **Equipo:** 7 personas

#### Entregables
- ✅ 50+ scripts (bash, python, ABAP, SQL)
- ✅ Vista VA05_SALES_ORDERS
- ✅ Dashboard de KPIs
- ✅ Sistema de monitoreo 24/7
- ✅ Documentación completa

#### Referencia
Ver documentos completos en carpeta `solucion_slt_completa/`:
- `Solucion_SLT_CONNECTOR_Y_PLAN_VA05.md` (PARTE 1)
- `Solucion_SLT_CONNECTOR_Y_PLAN_VA05_PARTE2.md` (PARTE 2)

---

## FASE 1 - TRANSACCIONES CRÍTICAS (PRIORIDAD 1)

---

### T02. ZLEL008 - Inventario Consolidado

**Prioridad:** ⭐⭐⭐ CRÍTICA  
**Módulo:** Z-Custom (Transacción desarrollada por Elanco)  
**Área:** Supply Chain + Finanzas  
**Estado:** 📋 REQUIERE ANÁLISIS

#### Descripción
Transacción custom que consolida información de inventarios de todos los centros y almacenes de Elanco. Proporciona visión unificada del stock disponible, en tránsito, reservado y bloqueado.

#### Tablas SAP Estimadas (3-5 tablas)
**⚠️ PENDIENTE DE ANÁLISIS ABAP**

Tablas probables (a confirmar):
1. MARD - Storage Location Data for Material
2. MSKA - Sales Order Stock
3. MCHB - Batch Stocks
4. MSEG - Document Segment: Material (opcional)
5. + Tablas custom adicionales (Z-tables)

#### Análisis Requerido en Fase 0
```abap
* Ejecutar en sistema SAP fuente:
* 1. Transacción SE93: Ver programa asignado a ZLEL008
* 2. Transacción SE38: Revisar código del programa
* 3. Identificar:
*    - SELECT statements (tablas fuente)
*    - JOINs y vistas utilizadas
*    - Lógica de cálculo de inventario consolidado
*    - Campos de salida
```

#### Campos Clave Estimados
- Material (MATNR)
- Centro (WERKS)
- Almacén (LGORT)
- Stock disponible (LABST)
- Stock en calidad (INSME)
- Stock bloqueado (SPEME)
- Stock en tránsito
- Valorización (SALK3 / MBEWH)
- Fecha última actualización

#### Esfuerzo Estimado
- **Análisis ABAP:** 8-16 horas (Fase 0)
- **Implementación:** 50-70 días-persona
- **Duración:** 7-10 semanas
- **Equipo:** 6-7 personas

#### Riesgos Identificados
- 🔴 **ALTO:** Tablas pueden no estar disponibles en BigQuery (Ticket BQ-7713 pendiente)
- 🟡 **MEDIO:** Lógica custom puede requerir recreación en BigQuery (stored procedures)
- 🟡 **MEDIO:** Consultoría ABAP puede requerirse si documentación no existe

#### Plan de Mitigación
1. **Semana 1 Fase 0:** Solicitar documentación técnica a equipo ABAP Elanco
2. **Semana 2 Fase 0:** Análisis de código fuente si no hay documentación
3. **Semana 3 Fase 0:** Validar tablas con TI Global
4. **Plan B:** Si tablas no disponibles, extraer vía SLT directo (sin BigQuery Connector)

#### Entregables
- Vista ZLEL008_INVENTORY_CONSOLIDATED
- Dashboard de stock consolidado por centro
- Alertas de stock crítico
- Reconciliación vs. SAP

---

### T03. KSB1 - OPEX / Órdenes CO

**Prioridad:** ⭐⭐⭐ CRÍTICA  
**Módulo:** CO (Controlling)  
**Área:** Finanzas  
**Estado:** 📋 DOCUMENTACIÓN PENDIENTE

#### Descripción
Reporte de partidas reales de órdenes de costos (órdenes internas de CO). Utilizado para análisis de gastos operativos (OPEX) por centro de costo, naturaleza del gasto y cuenta contable.

#### Tablas SAP (4-6 tablas)
1. **COBK** - CO Object: Document Header
2. **COEP** - CO Object: Line Items (Actual)
3. **AUFK** - Order Master Data
4. **CSKS** - Cost Center Master Data
5. **CSKA** - Cost Elements (Texts)
6. **TKA01** - Controlling Area (opcional)

#### Campos Clave
**De COEP (partidas individuales):**
- Orden CO (AUFNR)
- Centro de costo (KOSTL)
- Elemento de costo (KSTAR)
- Importe en moneda local (WTGBTR)
- Importe en moneda grupo (WOGBTR)
- Cantidad (MENGE)
- Unidad (MEINS)
- Fecha contabilización (BUDAT)
- Periodo fiscal (PERIO)
- Ejercicio (GJAHR)
- Clase de costo (KOART)
- Sociedad (BUKRS)

**De AUFK (maestro de órdenes):**
- Orden (AUFNR)
- Tipo de orden (AUART)
- Descripción (KTEXT)
- Centro de costo responsable (KOSTV)
- Status sistema (ASTNR)
- Usuario responsable (BNAME)

#### Vista BigQuery Propuesta
```sql
-- view_ksb1_opex_orders.sql
CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.KSB1_OPEX_ORDERS` AS
WITH order_items AS (
  SELECT
    coep.AUFNR as orden_co,
    coep.KOSTL as centro_costo,
    coep.KSTAR as elemento_costo,
    coep.WTGBTR as importe_local,
    coep.WOGBTR as importe_grupo,
    coep.MENGE as cantidad,
    coep.MEINS as unidad,
    coep.BUDAT as fecha_contabilizacion,
    PARSE_DATE('%Y%m%d', coep.BUDAT) as fecha_parsed,
    coep.PERIO as periodo,
    coep.GJAHR as ejercicio,
    coep.BUKRS as sociedad,
    coep.BELNR as documento,
    coep.BUZEI as posicion
  FROM `elanco-power-analytics.SAP_CO_REPLICAS.COEP` coep
  WHERE coep.KOART = '01'  -- Solo partidas de costo
),
order_master AS (
  SELECT
    AUFNR as orden_co,
    AUART as tipo_orden,
    KTEXT as descripcion_orden,
    KOSTV as centro_costo_responsable,
    ASTNR as status_sistema,
    BNAME as usuario_responsable,
    ERDAT as fecha_creacion,
    AEDAT as fecha_modificacion
  FROM `elanco-power-analytics.SAP_CO_REPLICAS.AUFK`
),
cost_center_master AS (
  SELECT
    KOSTL as centro_costo,
    KTEXT as descripcion_centro_costo,
    VERAK as responsable,
    KOSAR as clase_centro_costo
  FROM `elanco-power-analytics.SAP_CO_REPLICAS.CSKS`
  WHERE DATBI >= CURRENT_DATE()  -- Solo vigentes
)
SELECT
  -- Identificadores
  oi.orden_co,
  oi.documento,
  oi.posicion,
  
  -- Datos de la orden
  om.tipo_orden,
  om.descripcion_orden,
  om.usuario_responsable,
  om.status_sistema,
  
  -- Centro de costo
  oi.centro_costo,
  cc.descripcion_centro_costo,
  cc.responsable as responsable_centro_costo,
  
  -- Elemento de costo
  oi.elemento_costo,
  -- TODO: Join con CSKA para descripción de elemento de costo
  
  -- Importes
  oi.importe_local,
  oi.importe_grupo,
  oi.cantidad,
  oi.unidad,
  
  -- Fechas
  oi.fecha_contabilizacion,
  oi.fecha_parsed,
  oi.periodo,
  oi.ejercicio,
  EXTRACT(MONTH FROM oi.fecha_parsed) as mes,
  EXTRACT(QUARTER FROM oi.fecha_parsed) as trimestre,
  
  -- Organización
  oi.sociedad,
  
  -- Campos calculados
  CASE 
    WHEN om.status_sistema = 'CLSD' THEN 'Cerrada'
    WHEN om.status_sistema = 'REL' THEN 'Liberada'
    ELSE 'Otra'
  END as status_texto,
  
  -- Timestamp
  CURRENT_TIMESTAMP() as last_updated

FROM order_items oi
LEFT JOIN order_master om ON oi.orden_co = om.orden_co
LEFT JOIN cost_center_master cc ON oi.centro_costo = cc.centro_costo;
```

#### Vista de KPIs Agregados
```sql
-- view_ksb1_opex_kpis.sql
CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.KSB1_OPEX_KPIS` AS
SELECT
  ejercicio,
  periodo,
  mes,
  trimestre,
  sociedad,
  centro_costo,
  descripcion_centro_costo,
  responsable_centro_costo,
  
  -- Agregaciones
  COUNT(DISTINCT orden_co) as total_ordenes,
  COUNT(*) as total_partidas,
  SUM(importe_grupo) as total_opex_grupo,
  AVG(importe_grupo) as promedio_importe,
  MAX(importe_grupo) as max_importe,
  
  -- Por status
  COUNTIF(status_texto = 'Cerrada') as ordenes_cerradas,
  COUNTIF(status_texto = 'Liberada') as ordenes_liberadas,
  
  -- Totales por status
  SUM(CASE WHEN status_texto = 'Cerrada' THEN importe_grupo ELSE 0 END) as opex_cerrado,
  SUM(CASE WHEN status_texto = 'Liberada' THEN importe_grupo ELSE 0 END) as opex_abierto

FROM `elanco-power-analytics.SAP_ANALYTICS.KSB1_OPEX_ORDERS`
GROUP BY 1,2,3,4,5,6,7,8
ORDER BY ejercicio DESC, periodo DESC;
```

#### Esfuerzo Estimado
- **Días-persona:** 60-80
- **Duración:** 8-11 semanas
- **Equipo:** 7-8 personas (agregar CO Functional)

#### Roles Adicionales vs. VA05
- +1 **SAP CO Functional** (15-20 días): Validación lógica CO, testing funcional

#### Volumen Estimado
- Registros históricos: 2M-3M partidas (24 meses)
- Crecimiento mensual: 80K-100K partidas
- Tamaño estimado: 5-8 GB

#### Riesgos
- 🟡 **MEDIO:** Módulo CO más complejo que SD
- 🟡 **MEDIO:** Múltiples dimensiones de análisis
- 🟢 **BAJO:** Tablas estándar bien documentadas

---

### T04. FAGLL03 - Mayor General

**Prioridad:** ⭐⭐⭐ CRÍTICA  
**Módulo:** FI (Financial Accounting)  
**Área:** Finanzas  
**Estado:** ⚠️ VALIDACIÓN PENDIENTE (Ticket BQ-7721)

#### Descripción
Visualización de partidas individuales del libro mayor (General Ledger). Transacción fundamental para análisis contable detallado, conciliaciones y auditoría.

#### Tablas SAP (3-4 tablas)
1. **FAGLFLEXA** - General Ledger: Actual Line Items ⚠️ **VALIDAR DISPONIBILIDAD**
2. **BKPF** - Accounting Document Header
3. **BSEG** - Accounting Document Segment
4. **SKA1** - G/L Account Master (Chart of Accounts)

#### ⚠️ RIESGO CRÍTICO: Tabla FAGLFLEXA

**Issue:** Tabla FAGLFLEXA puede no estar completa en BigQuery  
**Ticket:** BQ-7721 pendiente con TI Global  
**Impacto:** Puede bloquear implementación de módulo FI

**Acciones Requeridas en Fase 0:**
1. **Semana 1:** Validar disponibilidad completa de FAGLFLEXA en dataset CASA
2. **Semana 2:** Si no disponible → Escalar a TI Global para habilitación
3. **Plan B:** Extraer FAGLFLEXA directamente vía SLT (bypass BigQuery Connector)

#### Campos Clave (de FAGLFLEXA)
- Sociedad (RBUKRS)
- Cuenta de mayor (RACCT)
- Ejercicio (RYEAR)
- Periodo (POPER)
- Versión (RVERS)
- Tipo ledger (RLDNR)
- Moneda (RCUR)
- Importe en moneda sociedad (HSL)
- Importe en moneda grupo (KSL)
- Importe en moneda transacción (TSL)
- Centro de beneficio (PRCTR)
- Segmento (SEGMENT)
- Partner profit center (PPRCTR)

#### Vista BigQuery Propuesta
```sql
-- view_fagll03_general_ledger.sql
CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.FAGLL03_GENERAL_LEDGER` AS
WITH gl_items AS (
  SELECT
    RBUKRS as sociedad,
    RACCT as cuenta_mayor,
    LTRIM(RACCT, '0') as cuenta_mayor_sin_ceros,
    RYEAR as ejercicio,
    POPER as periodo,
    RLDNR as ledger,
    RCUR as moneda,
    HSL as importe_moneda_sociedad,
    KSL as importe_moneda_grupo,
    TSL as importe_moneda_transaccion,
    PRCTR as centro_beneficio,
    SEGMENT as segmento,
    PPRCTR as partner_profit_center,
    BELNR as documento,
    BUZEI as posicion,
    BUDAT as fecha_contabilizacion,
    BLDAT as fecha_documento
  FROM `elanco-power-analytics.SAP_FI_REPLICAS.FAGLFLEXA`
  WHERE RLDNR = '0L'  -- Ledger principal
    AND RBUKRS IN ('1000', '1010')  -- Sociedades Elanco
),
gl_master AS (
  SELECT
    SAKNR as cuenta_mayor,
    TXT50 as descripcion_cuenta,
    KTOKS as grupo_cuentas,
    XBILK as indicador_balance
  FROM `elanco-power-analytics.SAP_FI_REPLICAS.SKAT`
  WHERE SPRAS = 'E'  -- Idioma inglés
)
SELECT
  -- Identificadores
  gli.documento,
  gli.posicion,
  
  -- Organización
  gli.sociedad,
  gli.cuenta_mayor,
  gli.cuenta_mayor_sin_ceros,
  glm.descripcion_cuenta,
  glm.grupo_cuentas,
  glm.indicador_balance,
  
  -- Dimensiones financieras
  gli.centro_beneficio,
  gli.segmento,
  gli.partner_profit_center,
  
  -- Periodo
  gli.ejercicio,
  gli.periodo,
  CONCAT(CAST(gli.ejercicio AS STRING), '-', 
         LPAD(CAST(gli.periodo AS STRING), 2, '0')) as periodo_contable,
  
  -- Fechas
  gli.fecha_contabilizacion,
  PARSE_DATE('%Y%m%d', gli.fecha_contabilizacion) as fecha_contable_parsed,
  gli.fecha_documento,
  PARSE_DATE('%Y%m%d', gli.fecha_documento) as fecha_documento_parsed,
  
  -- Importes
  gli.importe_moneda_sociedad,
  gli.importe_moneda_grupo,
  gli.importe_moneda_transaccion,
  gli.moneda,
  gli.ledger,
  
  -- Clasificación
  CASE 
    WHEN glm.indicador_balance = 'X' THEN 'Balance'
    ELSE 'Resultados'
  END as tipo_cuenta,
  
  -- Timestamp
  CURRENT_TIMESTAMP() as last_updated

FROM gl_items gli
LEFT JOIN gl_master glm ON gli.cuenta_mayor = glm.cuenta_mayor;
```

#### Balance de Comprobación (Trial Balance)
```sql
-- view_fagll03_trial_balance.sql
CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.FAGLL03_TRIAL_BALANCE` AS
SELECT
  sociedad,
  ejercicio,
  periodo,
  cuenta_mayor,
  cuenta_mayor_sin_ceros,
  descripcion_cuenta,
  grupo_cuentas,
  tipo_cuenta,
  
  -- Saldos agregados
  SUM(importe_moneda_sociedad) as saldo_moneda_sociedad,
  SUM(importe_moneda_grupo) as saldo_moneda_grupo,
  
  -- Debe y Haber
  SUM(CASE WHEN importe_moneda_grupo > 0 THEN importe_moneda_grupo ELSE 0 END) as debe,
  SUM(CASE WHEN importe_moneda_grupo < 0 THEN ABS(importe_moneda_grupo) ELSE 0 END) as haber,
  
  -- Saldo neto
  SUM(importe_moneda_grupo) as saldo_neto,
  
  -- Conteo de movimientos
  COUNT(*) as numero_movimientos,
  
  -- Fechas
  MIN(fecha_contable_parsed) as fecha_primer_movimiento,
  MAX(fecha_contable_parsed) as fecha_ultimo_movimiento

FROM `elanco-power-analytics.SAP_ANALYTICS.FAGLL03_GENERAL_LEDGER`
GROUP BY 1,2,3,4,5,6,7,8
HAVING ABS(saldo_neto) > 0.01  -- Excluir saldos cero (tolerancia centavos)
ORDER BY sociedad, ejercicio DESC, periodo DESC, cuenta_mayor;
```

#### Esfuerzo Estimado
- **Días-persona:** 60-75
- **Duración:** 8-10 semanas
- **Equipo:** 7-8 personas (agregar FI Functional)

#### Roles Adicionales vs. VA05
- +1 **SAP FI Functional** (15-20 días): Validación contable, plan de cuentas, reconciliaciones

#### Volumen Estimado
- Registros históricos: 5M-10M partidas (24 meses)
- Crecimiento mensual: 200K-400K partidas
- Tamaño estimado: 15-25 GB
- **⚠️ Tabla FAGLFLEXA es una de las más grandes en SAP**

#### Riesgos
- 🔴 **CRÍTICO:** FAGLFLEXA puede no estar disponible en BigQuery
- 🟡 **MEDIO:** Volumen muy alto requiere optimización agresiva
- 🟡 **MEDIO:** Múltiples ledgers y versiones aumentan complejidad

---

## FASE 2 - TRANSACCIONES IMPORTANTES (PRIORIDAD 2)

---

### T05. KE24 - Venta / CO-PA (Profitability Analysis)

**Prioridad:** ⭐⭐ IMPORTANTE  
**Módulo:** CO (Controlling) - CO-PA  
**Área:** Finanzas  
**Estado:** 📋 DOCUMENTACIÓN PENDIENTE

#### Descripción
Reporte de partidas individuales de CO-PA (Cuenta de Resultados). Análisis de rentabilidad por segmentos: cliente, producto, canal, región.

#### Tablas SAP (2-3 tablas)
1. **CE1xxxx** - CO-PA Actual Line Items (tabla dinámica por company code)
   - Ejemplo: CE11000 (company code 1000)
2. **CE4xxxx** - CO-PA Plan Line Items (opcional)
3. **CEPCT** - Master Data Texts for Characteristics

#### ⚠️ COMPLEJIDAD ESPECIAL: Tablas Dinámicas

Las tablas CO-PA se crean dinámicamente por sociedad:
- Sociedad 1000 → Tabla CE11000
- Sociedad 1010 → Tabla CE11010
- etc.

**Implicación:** Requiere vista UNION ALL de múltiples tablas.

#### Campos Clave Típicos (varían por configuración CO-PA)
- Ejercicio (GJAHR)
- Periodo (POPER)
- Organización de ventas (VKORG)
- Canal de distribución (VTWEG)
- Sector (SPART)
- Cliente (KUNNR)
- Material (MATNR)
- País (LAND1)
- Región (REGIO)
- **Campos de valor (VVxxx):**
  - VV100: Ventas netas
  - VV110: Costo de ventas
  - VV120: Descuentos
  - VV200: Margen bruto (calculado)

#### Vista BigQuery Propuesta
```sql
-- view_ke24_copa_profitability.sql
CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.KE24_COPA_PROFITABILITY` AS
-- NOTA: Ajustar nombres de tablas CE1xxxx según sociedades de Elanco
WITH copa_1000 AS (
  SELECT
    '1000' as sociedad,
    GJAHR as ejercicio,
    POPER as periodo,
    VKORG as organizacion_ventas,
    VTWEG as canal_distribucion,
    SPART as sector,
    KUNNR as cliente,
    MATNR as material,
    LAND1 as pais,
    REGIO as region,
    VV100 as ventas_netas,
    VV110 as costo_ventas,
    VV120 as descuentos,
    (VV100 - VV110) as margen_bruto,
    WAERS as moneda
  FROM `elanco-power-analytics.SAP_CO_REPLICAS.CE11000`
),
copa_1010 AS (
  SELECT
    '1010' as sociedad,
    GJAHR as ejercicio,
    POPER as periodo,
    VKORG as organizacion_ventas,
    VTWEG as canal_distribucion,
    SPART as sector,
    KUNNR as cliente,
    MATNR as material,
    LAND1 as pais,
    REGIO as region,
    VV100 as ventas_netas,
    VV110 as costo_ventas,
    VV120 as descuentos,
    (VV100 - VV110) as margen_bruto,
    WAERS as moneda
  FROM `elanco-power-analytics.SAP_CO_REPLICAS.CE11010`
),
copa_all AS (
  SELECT * FROM copa_1000
  UNION ALL
  SELECT * FROM copa_1010
  -- Agregar más sociedades según sea necesario
),
customer_master AS (
  SELECT
    KUNNR as cliente,
    NAME1 as nombre_cliente,
    LAND1 as pais_cliente
  FROM `elanco-power-analytics.SAP_SD_REPLICAS.KNA1`
),
material_master AS (
  SELECT
    MATNR as material,
    MAKTX as descripcion_material,
    MTART as tipo_material,
    MATKL as grupo_materiales
  FROM `elanco-power-analytics.SAP_MM_REPLICAS.MARA` m
  LEFT JOIN `elanco-power-analytics.SAP_MM_REPLICAS.MAKT` t 
    ON m.MATNR = t.MATNR AND t.SPRAS = 'E'
)
SELECT
  -- Organización
  c.sociedad,
  c.organizacion_ventas,
  c.canal_distribucion,
  c.sector,
  
  -- Periodo
  c.ejercicio,
  c.periodo,
  CONCAT(CAST(c.ejercicio AS STRING), '-', 
         LPAD(CAST(c.periodo AS STRING), 2, '0')) as periodo_contable,
  
  -- Cliente
  c.cliente,
  LTRIM(c.cliente, '0') as cliente_sin_ceros,
  cm.nombre_cliente,
  cm.pais_cliente,
  
  -- Material
  c.material,
  LTRIM(c.material, '0') as material_sin_ceros,
  mm.descripcion_material,
  mm.tipo_material,
  mm.grupo_materiales,
  
  -- Geografía
  c.pais,
  c.region,
  
  -- Valores
  c.ventas_netas,
  c.costo_ventas,
  c.descuentos,
  c.margen_bruto,
  c.moneda,
  
  -- Cálculos
  SAFE_DIVIDE(c.margen_bruto, c.ventas_netas) * 100 as margen_bruto_pct,
  CASE
    WHEN SAFE_DIVIDE(c.margen_bruto, c.ventas_netas) >= 0.40 THEN 'Alto (>=40%)'
    WHEN SAFE_DIVIDE(c.margen_bruto, c.ventas_netas) >= 0.25 THEN 'Medio (25-40%)'
    WHEN SAFE_DIVIDE(c.margen_bruto, c.ventas_netas) >= 0.10 THEN 'Bajo (10-25%)'
    ELSE 'Muy Bajo (<10%)'
  END as clasificacion_margen,
  
  -- Timestamp
  CURRENT_TIMESTAMP() as last_updated

FROM copa_all c
LEFT JOIN customer_master cm ON c.cliente = cm.cliente
LEFT JOIN material_master mm ON c.material = mm.material;
```

#### Esfuerzo Estimado
- **Días-persona:** 45-60
- **Duración:** 6-8 semanas
- **Equipo:** 7 personas

#### Volumen Estimado
- Registros históricos: 1M-2M partidas (24 meses)
- Crecimiento mensual: 40K-80K partidas
- Tamaño estimado: 3-6 GB

#### Riesgos
- 🔴 **ALTO:** Estructuras CO-PA varían mucho por empresa (configuración específica)
- 🟡 **MEDIO:** Requiere workshop con CO Functional para mapear campos de valor
- 🟡 **MEDIO:** Tablas dinámicas requieren mantenimiento cuando se agrega sociedad

---

### T06. FB03 - Documentos de Venta (Accounting Documents)

**Prioridad:** ⭐⭐ IMPORTANTE  
**Módulo:** FI (Financial Accounting)  
**Área:** Finanzas  
**Estado:** 📋 DOCUMENTACIÓN PENDIENTE

#### Descripción
Visualización de documentos contables (facturas, notas de crédito, pagos). Transacción de consulta para análisis de documentos individuales.

#### Tablas SAP (3-4 tablas)
1. **BKPF** - Accounting Document Header
2. **BSEG** - Accounting Document Segment
3. **BSID** - Accounting: Secondary Index for Customers (Open Items)
4. **BSAD** - Accounting: Secondary Index for Customers (Cleared Items)

#### Campos Clave
**De BKPF (cabecera):**
- Sociedad (BUKRS)
- Número documento (BELNR)
- Ejercicio (GJAHR)
- Tipo documento (BLART)
- Fecha documento (BLDAT)
- Fecha contabilización (BUDAT)
- Periodo (MONAT)
- Moneda (WAERS)
- Referencia (XBLNR)
- Usuario (USNAM)

**De BSEG (posiciones):**
- Sociedad (BUKRS)
- Documento (BELNR)
- Posición (BUZEI)
- Cuenta (HKONT)
- Cliente/Proveedor (KUNNR/LIFNR)
- Importe (DMBTR)
- Moneda (WAERS)
- Impuesto (MWSKZ)
- Texto (SGTXT)
- Centro de costo (KOSTL)
- Centro de beneficio (PRCTR)

#### Vista BigQuery Propuesta
```sql
-- view_fb03_accounting_documents.sql
CREATE OR REPLACE VIEW `elanco-power-analytics.SAP_ANALYTICS.FB03_ACCOUNTING_DOCUMENTS` AS
WITH doc_header AS (
  SELECT
    BUKRS as sociedad,
    BELNR as documento,
    GJAHR as ejercicio,
    BLART as tipo_documento,
    BLDAT as fecha_documento,
    BUDAT as fecha_contabilizacion,
    MONAT as periodo,
    WAERS as moneda,
    XBLNR as referencia,
    BKTXT as texto_cabecera,
    USNAM as usuario,
    TCODE as transaccion_origen,
    CPUDT as fecha_entrada,
    CPUTM as hora_entrada
  FROM `elanco-power-analytics.SAP_FI_REPLICAS.BKPF`
),
doc_segments AS (
  SELECT
    BUKRS as sociedad,
    BELNR as documento,
    GJAHR as ejercicio,
    BUZEI as posicion,
    BSCHL as clave_contabilizacion,
    KOART as tipo_cuenta,
    HKONT as cuenta_mayor,
    KUNNR as cliente,
    LIFNR as proveedor,
    DMBTR as importe_moneda_local,
    WRBTR as importe_moneda_documento,
    WAERS as moneda,
    MWSKZ as indicador_impuesto,
    SGTXT as texto_posicion,
    KOSTL as centro_costo,
    PRCTR as centro_beneficio,
    AUFNR as orden_interna,
    ZUONR as asignacion,
    GSBER as area_negocio,
    ZFBDT as fecha_base,
    ZBD1T as dias_descuento_1,
    ZBD1P as porcentaje_descuento_1,
    SHKZG as indicador_debe_haber
  FROM `elanco-power-analytics.SAP_FI_REPLICAS.BSEG`
)
SELECT
  -- Identificadores
  h.documento,
  h.ejercicio,
  s.posicion,
  
  -- Organización
  h.sociedad,
  
  -- Tipo de documento
  h.tipo_documento,
  CASE h.tipo_documento
    WHEN 'DR' THEN 'Factura Cliente'
    WHEN 'DZ' THEN 'Pago Cliente'
    WHEN 'DG' THEN 'Nota Crédito Cliente'
    WHEN 'KR' THEN 'Factura Proveedor'
    WHEN 'KZ' THEN 'Pago Proveedor'
    WHEN 'KG' THEN 'Nota Crédito Proveedor'
    WHEN 'SA' THEN 'Asiento Contable'
    ELSE 'Otro'
  END as tipo_documento_texto,
  
  -- Fechas
  h.fecha_documento,
  PARSE_DATE('%Y%m%d', h.fecha_documento) as fecha_documento_parsed,
  h.fecha_contabilizacion,
  PARSE_DATE('%Y%m%d', h.fecha_contabilizacion) as fecha_contable_parsed,
  h.periodo,
  
  -- Datos de la posición
  s.tipo_cuenta,
  CASE s.tipo_cuenta
    WHEN 'D' THEN 'Cliente'
    WHEN 'K' THEN 'Proveedor'
    WHEN 'S' THEN 'Cuenta Mayor'
    WHEN 'M' THEN 'Material'
    WHEN 'A' THEN 'Activo Fijo'
    ELSE 'Otro'
  END as tipo_cuenta_texto,
  
  s.cuenta_mayor,
  s.cliente,
  LTRIM(s.cliente, '0') as cliente_sin_ceros,
  s.proveedor,
  LTRIM(s.proveedor, '0') as proveedor_sin_ceros,
  
  -- Importes
  s.importe_moneda_local,
  s.importe_moneda_documento,
  s.moneda,
  s.indicador_debe_haber,
  CASE s.indicador_debe_haber
    WHEN 'S' THEN s.importe_moneda_local  -- Debe
    WHEN 'H' THEN -s.importe_moneda_local  -- Haber (negativo)
    ELSE 0
  END as importe_contable_signed,
  
  -- Dimensiones
  s.centro_costo,
  s.centro_beneficio,
  s.area_negocio,
  s.orden_interna,
  
  -- Textos
  h.texto_cabecera,
  s.texto_posicion,
  h.referencia,
  s.asignacion,
  
  -- Auditoría
  h.usuario,
  h.transaccion_origen,
  h.fecha_entrada,
  PARSE_DATE('%Y%m%d', h.fecha_entrada) as fecha_entrada_parsed,
  h.hora_entrada,
  
  -- Timestamp
  CURRENT_TIMESTAMP() as last_updated

FROM doc_header h
INNER JOIN doc_segments s 
  ON h.sociedad = s.sociedad 
  AND h.documento = s.documento 
  AND h.ejercicio = s.ejercicio;
```

#### Esfuerzo Estimado
- **Días-persona:** 50-65
- **Duración:** 7-9 semanas
- **Equipo:** 7 personas

#### Volumen Estimado
- Registros históricos: 1M-2M documentos (24 meses)
- Posiciones: 3M-6M líneas
- Crecimiento mensual: 40K-80K documentos
- Tamaño estimado: 8-12 GB

---

## FASE 3 - TRANSACCIONES COMPLEMENTARIAS

*Por razones de espacio, las siguientes 12 transacciones se documentan en formato resumido. Se expandirán en detalle en Fase 1 de implementación.*

---

### T07. ME2L - Purchase Orders by Vendor

**Prioridad:** ⏳ Pendiente de clasificar  
**Módulo:** MM  
**Tablas:** EKKO, EKPO, EKET  
**Esfuerzo:** 30-40 días-persona

---

### T08. ME23N - Display Purchase Order

**Prioridad:** ⏳ Pendiente  
**Módulo:** MM  
**Tablas:** EKKO, EKPO, EKKN, EKET  
**Esfuerzo:** 25-35 días-persona

---

### T09. MM60 - Standard Cost

**Prioridad:** ⏳ Pendiente  
**Módulo:** MM  
**Tablas:** MBEW, CKMLCR, CKMLHD  
**Esfuerzo:** 30-40 días-persona

---

### T10. MB59 - Movimientos de Material

**Prioridad:** ⏳ Pendiente  
**Módulo:** MM  
**Tablas:** MSEG, MKPF  
**Esfuerzo:** 25-35 días-persona

---

### T11. ZVEL015 - Condiciones de Precio (Custom)

**Prioridad:** ⏳ Pendiente  
**Módulo:** Z-Custom  
**Tablas:** Por analizar (ABAP)  
**Esfuerzo:** 50-70 días-persona (incluye análisis)  
**Riesgo:** 🔴 ALTO - Requiere análisis ABAP

---

### T12. FBL1N - Vendor Line Items

**Prioridad:** ⏳ Pendiente  
**Módulo:** FI  
**Tablas:** BSIK (open), BSAK (cleared)  
**Esfuerzo:** 20-30 días-persona

---

### T13. FBL5N - Customer Line Items

**Prioridad:** ⏳ Pendiente  
**Módulo:** FI  
**Tablas:** BSID (open), BSAD (cleared)  
**Esfuerzo:** 20-30 días-persona

---

### T14. MB5B - Stock for Material

**Prioridad:** ⏳ Pendiente  
**Módulo:** MM  
**Tablas:** MARD, MCHB, MSKA  
**Esfuerzo:** 20-30 días-persona

---

### T15. XK03 - Display Vendor Master

**Prioridad:** ⏳ Pendiente  
**Módulo:** MD  
**Tablas:** LFA1, LFB1, LFM1  
**Esfuerzo:** 10-15 días-persona

---

### T16. XD03 - Display Customer Master

**Prioridad:** ⏳ Pendiente  
**Módulo:** MD  
**Tablas:** KNA1, KNB1, KNVV  
**Esfuerzo:** 10-15 días-persona

---

### T17. F.08 - Balance de Comprobación

**Prioridad:** ⏳ Pendiente  
**Módulo:** FI  
**Tablas:** FAGLFLEXA, FAGLFLEXT  
**Esfuerzo:** 25-35 días-persona

---

### T18. F.01 - Estado de Situación (Balance Sheet)

**Prioridad:** ⏳ Pendiente  
**Módulo:** FI  
**Tablas:** FAGLFLEXA, SKA1  
**Esfuerzo:** 25-35 días-persona

---

## 📊 RESUMEN CONSOLIDADO

### Esfuerzo Total por Fase

| Fase | Transacciones | Esfuerzo (días-persona) | Duración | Estado |
|------|---------------|-------------------------|----------|--------|
| **Fase 0** | 1 (VA05) | 70 | 10 sem | ✅ LISTO |
| **Fase 1** | 3 (ZLEL008, KSB1, FAGLL03) | 170-225 | 23-31 sem | 📋 ESTE DOC |
| **Fase 2** | 2 (KE24, FB03) | 95-125 | 13-17 sem | 📋 ESTE DOC |
| **Fase 3** | 12 (resto) | 240-315 | 20-25 sem | 📋 RESUMIDO |
| **TOTAL** | **18** | **575-735** | **66-83 sem** | |

**Nota:** Rangos amplios reflejan incertidumbre por transacciones Z y disponibilidad de tablas.

### Inversión Total Actualizada

| Concepto | Rango Bajo | Rango Alto |
|----------|-----------|------------|
| **Esfuerzo RRHH** | 575 días-persona | 735 días-persona |
| **Consultoría Z Trans** | $2,500 | $5,000 |
| **Infraestructura (19 meses)** | $72,800 | $87,400 |
| **Contingencia RRHH (15%)** | +86 días | +110 días |
| **TOTAL DÍAS-PERSONA** | **661** | **845** |

### Timeline Maestro (Estimado)

```
Año 2026
────────────────────────────────────────────────────────────────────────

Q1 2026 (Ene-Mar):
├─► Fase 0: VA05 Piloto [10 semanas] ████████████░░░░░░░░ ✅ LISTO
└─► Fase 1 Inicio: ZLEL008 análisis [2 sem] ░░░░░░░░░░██░░░░░░░░

Q2 2026 (Abr-Jun):
├─► Fase 1: KSB1 + FAGLL03 [21 sem]     ████████████████████████
└─► Fase 2 Inicio: KE24 [6 sem]             ░░░░░░░░░░░░██████

Q3 2026 (Jul-Sep):
├─► Fase 2: FB03 [7 sem]                    ████████░░░░░░░░░░░░
└─► Fase 3 Inicio: MM Trans [10 sem]            ░░░░████████████

Q4 2026 (Oct-Dic):
└─► Fase 3: FI Trans + Maestros [10 sem]        ████████████████

Q1 2027 (Ene-Feb):
└─► UAT Final + Go-Live Completo [6 sem]        ██████░░░░░░░░░░

TOTAL: 66-83 semanas (Enero 2026 - Febrero 2027)
```

---

## 🚨 RIESGOS CONSOLIDADOS

### Riesgos Críticos (P1 - Requieren Acción Inmediata)

| ID | Riesgo | Transacciones Afectadas | Mitigación |
|----|--------|------------------------|------------|
| R01 | Tabla FAGLFLEXA no disponible | T04 (FAGLL03), T17 (F.08), T18 (F.01) | Validar en Fase 0, Plan B: SLT directo |
| R02 | Tablas Z no disponibles | T02 (ZLEL008), T11 (ZVEL015) | Análisis ABAP Fase 0, presupuesto contingencia |
| R03 | Estructuras CO-PA desconocidas | T05 (KE24) | Workshop CO Functional Fase 0 |

### Riesgos Altos (P2 - Monitorear de Cerca)

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|----|--------|--------------|---------|------------|
| R04 | Sobrecostos por transacciones Z | 60% | Alto | Buffer 15% contingencia |
| R05 | Timeline extendido por dependencies | 50% | Medio | Cronograma conservador, fases independientes |
| R06 | Recursos especializados no disponibles | 40% | Alto | Identificar y reservar recursos temprano |

---

## ✅ PRÓXIMOS PASOS RECOMENDADOS

### Semana 1 (Inmediato Post-Revisión)
1. ✅ **Revisar este documento** con Steering Committee
2. ✅ **Aprobar estrategia en fases** (0, 1, 2, 3)
3. ✅ **Validar priorización** de transacciones con Finanzas + Supply
4. ✅ **Iniciar análisis de transacciones Z** (ZLEL008, ZVEL015)

### Semana 2-4 (Fase 0 Ampliada)
1. ✅ Completar análisis ABAP de transacciones Z
2. ✅ Validar disponibilidad de TODAS las tablas en BigQuery
3. ✅ Resolver tickets BQ-7713 y BQ-7721
4. ✅ Workshop CO-PA para mapear estructura KE24
5. ✅ Actualizar estimaciones con información real

### Mes 2 (Aprobación Fase 1)
1. ✅ Presentar presupuesto detallado Fase 1 (3 trans: ZLEL008, KSB1, FAGLL03)
2. ✅ Conformar equipo ampliado (agregar CO Functional, FI Functional)
3. ✅ Aprobar inversión Fase 1
4. ✅ Kick-off Fase 1

---

## 📞 CONTACTO Y APROBACIONES

**Project Manager:**  
Email: pm@elanco.com

**Tech Lead:**  
Email: techlead@elanco.com

### Aprobaciones Requeridas

| Aprobador | Rol | Alcance a Aprobar | Firma | Fecha |
|-----------|-----|-------------------|-------|-------|
| _________ | CFO | Presupuesto completo 18 trans | _____ | _____ |
| _________ | IT Director | Arquitectura técnica expandida | _____ | _____ |
| _________ | Finance Director | Transacciones FI/CO (8 trans) | _____ | _____ |
| _________ | Supply Director | Transacciones MM/SD (7 trans) | _____ | _____ |

---

**Última actualización:** 7 de noviembre de 2025  
**Versión:** 2.0 - Solución Expandida 18 Transacciones  
**Estado:** 📋 PENDIENTE DE REVISIÓN Y APROBACIÓN
