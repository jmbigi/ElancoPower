# 5. FASE 1 | **Duración:** | 10 semanas (sprints de 2 semanas, con holguras para ajustes) |
| **Fecha inicio** | 13 de enero de 2026 |
| **Fecha fin** | 23 de marzo de 2026 |ONSTRUCCIÓN DE DATA LAKE

## 5.1. Objetivo de la Fase

**Automatizar la extracción de datos desde SAP ECC hacia BigQuery**, creando un repositorio centralizado (Data Lake) con datos históricos de las 18 transacciones priorizadas, implementando controles de calidad y estableciendo procesos de sincronización periódica.

---

## 5.2. Duración y Recursos

| Parámetro | Valor |
|-----------|-------|
| **Duración estimada** | 10 semanas (sprints de 2 semanas, con holguras para ajustes) |
| **Fase del proyecto** | Mes 2-3, Semanas 6-15 |
| **Horas totales** | 267 horas |
| **Equipo** | Juan Manuel Bigi (180h) + Lucía Rodríguez (60h) + Linda López (15h) + Consultor ABAP (12h contingencia) |

---

## 5.3. Arquitectura del Data Lake

### 5.3.1. Modelo de Zonas (Layers)

```
SAP ECC                    BIGQUERY DATASET: CASA
┌──────────────┐          ┌─────────────────────────────────────┐
│              │          │                                     │
│  Módulos:    │  Extract │  ┌────────────────────────────┐    │
│  - MM        │─────────▶│  │  RAW LAYER                 │    │
│  - SD        │          │  │  (Datos tal cual de SAP)   │    │
│  - FI        │          │  │  Tablas: raw_vbak,         │    │
│  - CO        │          │  │          raw_ekko, ...     │    │
│              │          │  └────────────────────────────┘    │
│  18 Trans.   │          │           │                        │
│              │          │           │ Transform              │
│              │          │           ▼                        │
│              │          │  ┌────────────────────────────┐    │
│              │          │  │  PROCESSED LAYER           │    │
│              │          │  │  (Limpieza, validación)    │    │
│              │          │  │  Tablas: prc_sales_orders, │    │
│              │          │  │          prc_inventory,... │    │
│              │          │  └────────────────────────────┘    │
│              │          │           │                        │
│              │          │           │ Load                   │
│              │          │           ▼                        │
│              │          │  ┌────────────────────────────┐    │
│              │          │  │  CURATED LAYER             │    │
│              │          │  │  (Business-ready)          │    │
│              │          │  │  Tablas: cur_ventas,       │    │
│              │          │  │          cur_inventario,.. │    │
│              │          │  └────────────────────────────┘    │
│              │          │           │                        │
└──────────────┘          └───────────┼────────────────────────┘
                                      │
                                      ▼
                          ┌──────────────────────┐
                          │   POWER BI           │
                          │   (Dashboards)       │
                          └──────────────────────┘
```

### 5.3.2. Descripción de Capas

#### **RAW LAYER (Zona Bronce)**

**Propósito:** Almacenar datos tal cual vienen de SAP, sin transformaciones.

**Características:**
- Esquema idéntico a tablas SAP
- Sin limpieza ni validación
- Historización completa (append-only)
- Particionado por fecha de carga
- Compresión GZIP activada

**Nomenclatura:** `raw_<nombre_tabla_sap>`
- Ejemplo: `raw_vbak`, `raw_ekko`, `raw_bkpf`

**Retención:** 36 meses (3 años)

---

#### **PROCESSED LAYER (Zona Plata)**

**Propósito:** Datos limpios, validados y estandarizados.

**Transformaciones aplicadas:**
- Limpieza de valores nulos/vacíos
- Normalización de fechas y números
- Validación de claves foráneas
- Deduplicación de registros
- Casteo de tipos de datos
- Agregación de flags de calidad

**Nomenclatura:** `prc_<concepto_negocio>`
- Ejemplo: `prc_sales_orders`, `prc_purchase_orders`, `prc_gl_items`

**Retención:** 24 meses (2 años)

---

#### **CURATED LAYER (Zona Oro)**

**Propósito:** Datos listos para consumo por usuarios de negocio y herramientas BI.

**Características:**
- Modelo dimensional (facts + dimensions)
- Nombres de columnas en español/inglés de negocio
- Métricas pre-calculadas
- Joins pre-ejecutados (desnormalización controlada)
- Optimización para queries analíticos
- Clustering por campos de filtrado común

**Nomenclatura:** `cur_<concepto_negocio>`
- Ejemplo: `cur_ventas`, `cur_inventario`, `cur_gl_balance`

**Retención:** 24 meses (2 años)

---

## 5.4. Actividades Detalladas

### 5.4.1. Configuración de Infraestructura BigQuery

**Responsable:** Juan Manuel Bigi  
**Duración:** 16 horas  
**Semana:** 1 (Fase 1)

#### Tareas

| # | Actividad | Horas | Entregable |
|---|-----------|-------|------------|
| 1 | Creación de datasets por zona (RAW, PROCESSED, CURATED) | 2h | Datasets configurados |
| 2 | Definición de políticas de retención | 2h | Políticas documentadas |
| 3 | Configuración de particionamiento y clustering | 4h | Tablas optimizadas |
| 4 | Setup de conectores SAP ECC ↔ BigQuery | 4h | Conectores funcionales |
| 5 | Configuración de service accounts y permisos | 2h | IAM roles asignados |
| 6 | Setup de monitoreo de costos | 2h | Dashboard de costos activo |

#### Conectores SAP ↔ BigQuery

**Método de Replicación:**
- **SAP SLT (Landscape Transformation Server):** Se utilizará como la solución principal para la replicación de datos en tiempo real desde SAP ECC a Google BigQuery. SLT captura los cambios en las tablas de origen de SAP a nivel de base de datos y los replica de manera eficiente en el destino.

**Ventajas de SLT:**
- **Replicación en Tiempo Real:** Permite tener datos actualizados en BigQuery con una latencia mínima.
- **Bajo Impacto:** Minimiza la carga en el sistema SAP de origen.
- **Confiabilidad:** Es una solución robusta y certificada por SAP para este tipo de escenarios.

**Decisión:** El uso de SAP SLT es una decisión de arquitectura clave para garantizar la frescura y consistencia de los datos en el Data Lake.

---

### 5.4.2. Desarrollo de Pipelines ETL - Módulo FI

**Responsable:** Juan Manuel Bigi  
**Duración:** 40 horas  
**Semanas:** 2-4 (Sprint 1-2)

#### Transacciones Módulo FI

| Transacción | Tablas SAP | Complejidad | Horas |
|-------------|------------|-------------|-------|
| **FAGLL03** | FAGLFLEXA, BKPF, BSEG | Alta | 12h |
| **FB03** | BKPF, BSEG, BSID/BSAD | Media | 10h |
| **F.08** | FAGLFLEXT (totales), FAGLFLEXA | Media | 10h |
| **F.01** | FAGLFLEXT, SKA1 | Media | 8h |

#### Pipeline Tipo (Ejemplo: FAGLL03)

**Paso 1: Extracción (RAW)**
```sql
-- Crear tabla RAW con datos de FAGLFLEXA
CREATE OR REPLACE TABLE `casa_bi.raw_faglflexa`
PARTITION BY DATE(load_timestamp)
AS
SELECT 
    *,
    CURRENT_TIMESTAMP() as load_timestamp,
    'fagll03' as source_transaction
FROM `elanco_erp.faglflexa`
WHERE budat >= DATE_SUB(CURRENT_DATE(), INTERVAL 24 MONTH);
```

**Paso 2: Procesamiento (PROCESSED)**
```sql
-- Limpieza y validación
CREATE OR REPLACE TABLE `casa_bi.prc_gl_items` AS
SELECT
    ryear,
    rbukrs as company_code,
    racct as gl_account,
    poper as period,
    SAFE_CAST(hsl AS NUMERIC) as amount_local,
    SAFE_CAST(ksl AS NUMERIC) as amount_group,
    -- Validaciones
    CASE 
        WHEN racct IS NULL THEN 'INVALID_ACCOUNT'
        WHEN hsl IS NULL THEN 'MISSING_AMOUNT'
        ELSE 'VALID'
    END as quality_flag,
    load_timestamp
FROM `casa_bi.raw_faglflexa`
WHERE quality_flag = 'VALID';
```

**Paso 3: Curación (CURATED)**
```sql
-- Modelo de negocio con joins
CREATE OR REPLACE TABLE `casa_bi.cur_gl_balance` AS
SELECT
    gl.company_code,
    gl.gl_account,
    coa.account_name, -- Join con maestro
    gl.period,
    SUM(gl.amount_local) as balance_local,
    SUM(gl.amount_group) as balance_group
FROM `casa_bi.prc_gl_items` gl
LEFT JOIN `casa_bi.dim_chart_of_accounts` coa
    ON gl.gl_account = coa.gl_account
GROUP BY 1,2,3,4;
```

---

### 5.4.3. Desarrollo de Pipelines ETL - Módulo SD

**Responsable:** Juan Manuel Bigi  
**Duración:** 16 horas  
**Semanas:** 5-6 (Sprint 3)

#### Transacciones Módulo SD

| Transacción | Tablas SAP | Complejidad | Horas |
|-------------|------------|-------------|-------|
| **VA05** | VBAK, VBAP, VBEP, KNA1 | Media-Alta | 16h |

**Particularidades:**
- Múltiples joins (cabecera + posiciones + schedule lines)
- Cálculo de backlog (órdenes abiertas)
- Integración con maestro de clientes

---

### 5.4.4. Desarrollo de Pipelines ETL - Módulo MM

**Responsable:** Juan Manuel Bigi + Lucía Rodríguez  
**Duración:** 48 horas (40h JMB + 8h Lucía)  
**Semanas:** 7-10 (Sprint 4-5)

#### Transacciones Módulo MM

| Transacción | Tablas SAP | Complejidad | Horas | Observaciones |
|-------------|------------|-------------|-------|---------------|
| **ZLEL008** | Z-tables (TBD) | **MUY ALTA** | 24h | Custom, requiere análisis ABAP |
| **ME2L** | EKKO, EKPO | Media | 12h | Purchase orders estándar |
| **MB5B** | MARD, MCHB | Media | 12h | Stock por material |

**ZLEL008 - Plan de Acción:**
1. Análisis de código ABAP (Fase 0 completada)
2. Identificación de tablas fuente
3. Replicación de lógica en SQL BigQuery
4. Validación exhaustiva con power user
5. Consultoría ABAP si es necesaria (8h contingencia)

---

### 5.4.5. Desarrollo de Pipelines ETL - Módulo CO

**Responsable:** Juan Manuel Bigi  
**Duración:** 28 horas  
**Semanas:** 11-12 (Sprint 6)

#### Transacciones Módulo CO

| Transacción | Tablas SAP | Complejidad | Horas |
|-------------|------------|-------------|-------|
| **KSB1** | COBK, COEP, AUFK | Alta | 16h |
| **KE24** | CE1xxxx, CE4xxxx | Alta | 12h |

**Complejidad CO:**
- Múltiples dimensiones (cost center, order, WBS element)
- Jerarquías de controlling
- Lógica de agregación compleja

---

### 5.4.6. Testing y Validación de Calidad

**Responsables:** Juan Manuel Bigi + Lucía Rodríguez  
**Duración:** 24 horas (16h JMB + 8h Lucía)  
**Semanas:** 13-14 (continuo durante desarrollo)

#### Tipos de Validación

**1. Validación de Volumen (Reconciliación SAP ↔ BigQuery)**

Para cada transacción:
```sql
-- Query de validación
SELECT 
    'SAP' as source,
    COUNT(*) as record_count,
    SUM(amount) as total_amount
FROM sap_source_table
UNION ALL
SELECT 
    'BigQuery' as source,
    COUNT(*) as record_count,
    SUM(amount) as total_amount
FROM bigquery_target_table;
```

**Criterio:** Diferencia < 0.5%

**2. Validación de Claves (Integridad Referencial)**

- Verificar que todas las foreign keys existan
- Validar maestros de datos completos
- Detectar registros huérfanos

**3. Validación de Cálculos**

- Comparar totales calculados vs. SAP
- Validar agregaciones (SUM, AVG, COUNT)
- Verificar fórmulas de negocio (márgenes, ratios)

**4. Validación de Fechas**

- Verificar que datos históricos estén completos (24 meses)
- Validar que no haya gaps en series temporales
- Comprobar sincronización diaria/semanal

#### Matriz de Validación

| Transacción | Vol (SAP vs BQ) | Claves | Cálculos | Fechas | Status |
|-------------|-----------------|--------|----------|--------|--------|
| FAGLL03 | ✅ 99.8% | ✅ OK | ✅ OK | ✅ OK | ✅ PASS |
| VA05 | ⚠️ 98.2% | ✅ OK | ✅ OK | ✅ OK | ⚠️ REVIEW |
| ZLEL008 | ❌ 85.3% | ❌ Issues | ⏳ Pending | ✅ OK | ❌ FAIL |

---

### 5.4.7. Documentación Técnica

**Responsable:** Juan Manuel Bigi  
**Duración:** 12 horas  
**Semanas:** 13-14 (final de Fase 1)

#### Documentos a Generar

1. **Diccionarios de Datos (18 documentos)**
   - Por cada transacción SAP
   - Mapeo campo SAP → campo BigQuery
   - Descripción de transformaciones aplicadas
   - Reglas de negocio implementadas

2. **Guía de Arquitectura Técnica**
   - Diagramas de flujo de datos
   - Decisiones arquitectónicas (ADRs)
   - Configuración de infraestructura

3. **Scripts SQL Documentados**
   - Código versionado en Git
   - Comentarios en línea
   - README por módulo

4. **Runbooks Operativos**
   - Procedimientos de monitoreo
   - Troubleshooting común
   - Procedimientos de contingencia

---

### 5.4.8. Ajustes y Gestión de Issues

**Responsable:** Lucía Rodríguez  
**Duración:** 16 horas  
**Semanas:** 1-14 (continuo)

#### Actividades

- Coordinación con TI Global para resolver tickets
- Seguimiento de issues de permisos/accesos
- Validación funcional con usuarios de negocio
- Gestión de cambios de alcance
- Comunicación con stakeholders

---

## 5.5. Cronograma Semanal Fase 1

### Sprint 1-2: Módulo FI (Semanas 1-4)

| Semana | Actividades Principales | Horas | Hitos |
|--------|------------------------|-------|-------|
| 1 | Setup infraestructura + FAGLL03 | 20h | Infraestructura lista |
| 2 | FAGLL03 (cont.) + FB03 | 20h | FAGLL03 completo |
| 3 | F.08 + F.01 | 18h | Módulo FI completo |
| 4 | Testing FI + documentación | 12h | Validación FI OK |

---

### Sprint 3: Módulo SD (Semanas 5-6)

| Semana | Actividades Principales | Horas | Hitos |
|--------|------------------------|-------|-------|
| 5 | VA05 desarrollo | 20h | VA05 en RAW/PROCESSED |
| 6 | VA05 CURATED + testing | 16h | VA05 completo |

---

### Sprint 4-5: Módulo MM (Semanas 7-10)

| Semana | Actividades Principales | Horas | Hitos |
|--------|------------------------|-------|-------|
| 7 | ME2L desarrollo | 12h | ME2L completo |
| 8 | MB5B desarrollo | 12h | MB5B completo |
| 9 | ZLEL008 análisis + desarrollo (parte 1) | 20h | ZLEL008 50% |
| 10 | ZLEL008 desarrollo (parte 2) + testing | 20h | ZLEL008 completo |

---

### Sprint 6: Módulo CO (Semanas 11-12)

| Semana | Actividades Principales | Horas | Hitos |
|--------|------------------------|-------|-------|
| 11 | KSB1 desarrollo | 16h | KSB1 completo |
| 12 | KE24 desarrollo | 12h | KE24 completo |

---

### Sprint 7-8: Cierre y Ajustes (Semanas 13-14)

| Semana | Actividades Principales | Horas | Hitos |
|--------|------------------------|-------|-------|
| 13 | Testing integral + validaciones | 16h | Todas las transacciones validadas |
| 14 | Documentación + ajustes finales | 12h | Fase 1 completa |

---

## 5.6. Entregables de Fase 1

### 5.6.1. Infraestructura

✅ Dataset BigQuery `casa_bi` con 3 zonas (RAW, PROCESSED, CURATED)  
✅ 18 pipelines ETL funcionales y automatizados  
✅ Conectores SAP ↔ BigQuery configurados  
✅ Monitoreo de costos y performance implementado  

### 5.6.2. Datos

✅ Historización de 24 meses de datos para 18 transacciones  
✅ Datos validados (reconciliación SAP ↔ BigQuery > 99%)  
✅ Calidad de datos documentada (matriz de validación)  

### 5.6.3. Documentación

✅ 18 diccionarios de datos (mapeo SAP ↔ BigQuery)  
✅ Guía de arquitectura técnica  
✅ Scripts SQL versionados en Git  
✅ Runbooks operativos (monitoreo, troubleshooting)  

### 5.6.4. Código

✅ Repositorio Git con todo el código SQL  
✅ Scripts de despliegue (deployment)  
✅ Scripts de rollback (contingencia)  

---

## 5.7. Esfuerzo de Fase 1

| Recurso | Horas |
|---------|-------|
| **Juan Manuel Bigi** | 180h |
| **Lucía Rodríguez** | 60h |
| **Linda López (PM)** | 15h |
| **Consultor ABAP** (contingencia) | 12h |
| **TOTAL FASE 1** | **267h** |

---

## 5.8. Criterios de Éxito de Fase 1

✅ **Fase 1 se considera exitosa si:**

1. ✅ 18 transacciones SAP automatizadas (o mínimo 16 si hubo issues técnicos)
2. ✅ Datos históricos completos (24 meses) disponibles en BigQuery
3. ✅ Validación SAP ↔ BigQuery > 99% de exactitud
4. ✅ Pipelines ejecutándose automáticamente (diario/semanal según transacción)
5. ✅ Documentación técnica completa entregada
6. ✅ Primer dashboard operativo funcional con datos reales (adelanto de Fase 2)

---

*Siguiente sección: [06_FASE_2_MODELADO_Y_DASHBOARDS.md](06_FASE_2_MODELADO_Y_DASHBOARDS.md)*
