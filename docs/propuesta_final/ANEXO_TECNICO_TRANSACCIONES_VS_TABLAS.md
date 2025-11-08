# ANEXO TÉCNICO: TRANSACCIONES SAP vs. TABLAS SAP

## Propósito de este Documento

Este anexo técnico tiene como objetivo aclarar la diferencia fundamental entre:
- **Transacciones SAP** (códigos de transacción como VA05, KSB1, etc.)
- **Tablas SAP** (estructuras de base de datos como VBAK, COEP, etc.)

Y explicar **qué se replica realmente** en el proyecto.

---

## 1. ¿Qué es una Transacción SAP?

### Definición

Una **transacción SAP** es un **código de programa** (típicamente de 4 caracteres) que ejecuta una función específica en el sistema SAP. Es esencialmente una **interfaz de usuario** que permite:
- Consultar datos
- Crear/modificar registros
- Generar reportes
- Ejecutar procesos de negocio

### Ejemplos Comunes

| Código | Nombre | Función |
|--------|--------|---------|
| **VA05** | Lista de órdenes de venta | Muestra órdenes de venta abiertas |
| **KSB1** | Partidas reales por CE | Muestra movimientos de controlling |
| **FAGLL03** | Visualizar partidas GL | Muestra movimientos contables |
| **ME2L** | PO por proveedor | Lista pedidos de compra |

### Arquitectura de una Transacción

```
┌─────────────────────────────────────────────────┐
│         TRANSACCIÓN SAP (VA05)                  │
│                                                 │
│  ┌───────────────────────────────────┐         │
│  │   INTERFAZ DE USUARIO (PANTALLA)  │         │
│  │   - Campos de entrada              │         │
│  │   - Botones                        │         │
│  │   - Resultados visuales            │         │
│  └──────────────┬────────────────────┘         │
│                 │                               │
│                 ▼                               │
│  ┌───────────────────────────────────┐         │
│  │   LÓGICA DE PROGRAMA ABAP         │         │
│  │   - Validaciones                   │         │
│  │   - Cálculos                       │         │
│  │   - Formateo                       │         │
│  └──────────────┬────────────────────┘         │
│                 │                               │
│                 ▼                               │
│  ┌───────────────────────────────────┐         │
│  │   CONSULTAS A BASE DE DATOS       │         │
│  │   SELECT FROM VBAK, VBAP, VBEP    │         │
│  └──────────────┬────────────────────┘         │
└─────────────────┼───────────────────────────────┘
                  │
                  ▼
        ┌──────────────────┐
        │   TABLAS SAP     │
        │   - VBAK         │
        │   - VBAP         │
        │   - VBEP         │
        └──────────────────┘
```

**Punto clave:** La transacción es solo la "ventana" para acceder a los datos. Los datos reales están en **tablas de base de datos**.

---

## 2. ¿Qué es una Tabla SAP?

### Definición

Una **tabla SAP** es una **estructura de base de datos** que almacena información de manera persistente. Es donde realmente residen los datos del sistema SAP.

### Características

- Nombre técnico (ej. VBAK, BSEG, MARA)
- Campos con tipos de datos definidos
- Claves primarias y foráneas
- Índices para optimizar consultas
- Millones de registros (en sistemas productivos)

### Ejemplo: Tabla VBAK (Cabecera de Órdenes de Venta)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| VBELN | CHAR(10) | Número de orden de venta |
| ERDAT | DATS(8) | Fecha de creación |
| KUNNR | CHAR(10) | Número de cliente |
| NETWR | CURR(15) | Valor neto |
| WAERK | CUKY(5) | Moneda |

### Relaciones entre Tablas

Las tablas SAP están relacionadas entre sí:

```
VBAK (Cabecera Orden)
  │
  ├─ 1:N ──▶ VBAP (Posiciones)
  │             │
  │             ├─ 1:N ──▶ VBEP (Schedule Lines)
  │             │
  │             └─ N:1 ──▶ MARA (Maestro Materiales)
  │
  └─ N:1 ──▶ KNA1 (Maestro Clientes)
```

---

## 3. ¿Qué se Replica Realmente?

### Respuesta: LAS TABLAS, NO LAS TRANSACCIONES

**SAP SLT (Landscape Transformation Server)** replica **tablas de base de datos**, no transacciones.

### Proceso de Replicación

```
┌──────────────────────────────────────────────────────┐
│              SAP S/4HANA (Sistema Fuente)            │
│                                                      │
│  Transacción VA05  ───▶  Tablas: VBAK, VBAP, VBUK, VBUP  │
│  Transacción KSB1  ───▶  Tablas: ACDOCA, AUFK, CSKS      │
│  Transacción FAGLL03 ─▶  Tablas: ACDOCA, BKPF            │
│                                                      │
└──────────────────────┬───────────────────────────────┘
                       │
                       │ SLT Replicación
                       │ (Tabla por tabla)
                       │
                       ▼
┌──────────────────────────────────────────────────────┐
│           Google BigQuery (Destino)                  │
│                                                      │
│  raw_vbak  ◀── Réplica de VBAK                       │
│  raw_vbap  ◀── Réplica de VBAP                       │
│  raw_vbuk  ◀── Réplica de VBUK                       │
│  raw_vbup  ◀── Réplica de VBUP                       │
│  raw_acdoca◀── Réplica de ACDOCA                     │
│  raw_bkpf  ◀── Réplica de BKPF                       │
│  ...                                                 │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Configuración de SLT

En SLT se configura:
- ✅ Nombre de la tabla SAP a replicar (ej. VBAK)
- ✅ Campos a incluir (puede ser todos o un subconjunto)
- ✅ Filtros (ej. solo datos de ciertos países)
- ✅ Frecuencia de replicación (tiempo real o batch)
- ✅ Destino (BigQuery)

**NO se configura "replicar transacción VA05"**, porque la transacción es solo código de programa.

---

## 4. Mapeo: Transacciones → Tablas

### Ejemplo 1: VA05 (Órdenes de Venta)

**Transacción:** VA05
**Tablas Requeridas (Ejemplos):**
- `VBAK` (Cabecera de orden de venta)
- `VBAP` (Posiciones de la orden)
- `VBEP` (Fechas de entrega programadas)
- `KNA1` (Maestro de clientes)
- `MARA` (Maestro de materiales)
**Total Estimado:** ~5 tablas
**Complejidad Media:** Implica joins entre tablas transaccionales y maestras.

### Ejemplo 2: KSB1 (OPEX / Controlling)

**Transacción:** KSB1
**Tablas Requeridas (Ejemplos en S/4HANA):**
- `ACDOCA` (Universal Journal: reemplaza COEP/FAGLFLEXA/BSEG)
- `AUFK` (Maestro de órdenes internas)
- `CSKS` (Maestro de centros de costo)
- `CSKA` (Maestro de elementos de costo)
**Total Estimado:** ~5 tablas
**Complejidad Alta:** La tabla `COEP` es de alto volumen y el módulo CO tiene una lógica dimensional compleja.

### Ejemplo 3: FAGLL03 (Mayor General)

**Transacción:** FAGLL03
**Tablas Requeridas (Ejemplos en S/4HANA):**
- `ACDOCA` (Partidas individuales del Universal Journal)
- `BKPF` (Cabecera de documentos contables)
- `SKA1` (Plan de cuentas)
**Total Estimado:** ~4 tablas
**Complejidad Muy Alta:** `ACDOCA` es una de las tablas más grandes y críticas en S/4HANA FI/CO, requiriendo estrategias de particionamiento y filtros eficientes.

### Estimación para el Proyecto

| Categoría | Cantidad | Tablas Estimadas | Complejidad |
|-------------------------------|----------|------------------|-----------------|
| Transacciones Prioridad 1 | 4 | ~12-18 | Media a Alta |
| Transacciones Prioridad 2 | 4 | ~8-12 | Media |
| Transacciones Pendientes | 10 | ~15-35 | Baja a Media |
| **TOTAL ESTIMADO** | **18** | **~35-65 tablas** | **Mixta (optimizada por S/4)** |

---

## 5. Implicaciones para el Proyecto

### 5.1. Fase 0: Análisis Crítico

Durante Fase 0 se debe realizar un **mapeo exhaustivo**:

```
ENTRADAS (Fase 0)              PROCESO                    SALIDAS
─────────────────              ───────                    ────────
┌─────────────────┐           ┌──────────────────┐      ┌────────────────┐
│ 18 Transacciones│──────────▶│ Análisis de      │─────▶│ Lista de       │
│ SAP priorizadas │           │ Tablas           │      │ 35-65 Tablas   │
└─────────────────┘           │ Subyacentes      │      │ SAP a Replicar │
                              └──────────────────┘      └────────────────┘
                                       │
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ Validación con   │
                              │ TI Global:       │
                              │ ¿Tablas          │
                              │ disponibles en   │
                              │ BigQuery?        │
                              └──────────────────┘
```

### 5.2. Actividades Clave de Fase 0

| # | Actividad | Responsable | Horas |
|---|-----------|-------------|-------|
| 1 | Análisis de cada transacción para identificar tablas | Funcional SAP + Consultor BI | 16h |
| 2 | Análisis de transacciones custom (Z) con código ABAP | Consultor ABAP | 12h |
| 3 | Validación de disponibilidad de tablas en BigQuery | TI Global | (no factura) |
| 4 | Análisis de relaciones entre tablas (joins) | Consultor BI | 8h |
| 5 | Estimación de volúmenes por tabla | Funcional SAP + Consultor BI | 4h |
| 6 | Documentación de mapeo completo | Consultor BI | 8h |

### 5.3. Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Tablas no disponibles en BigQuery | Media | Alto | Ticket a TI Global en Fase 0 |
| Transacciones Z con tablas desconocidas | Media | Medio | Análisis ABAP (12h incluidas) |
| Más tablas de lo estimado (>65) | Baja | Medio | Ajuste de alcance en Fase 0 |
| Tablas con volúmenes muy altos (ACDOCA) | Media | Medio | Estrategia de particionamiento y filtros |

### 5.4. Decisión Go/No-Go

**Criterio para continuar a Fase 1:**

✅ **Mínimo 80% de las tablas identificadas disponibles en BigQuery**

Por ejemplo:
- Si se identifican 50 tablas necesarias (S/4 optimizado)
- Mínimo 40 tablas deben estar disponibles
- Si <40 disponibles: Evaluar plan B (escalamiento a TI Global, uso de extractores RFC, etc.)

---

## 6. Ventajas de Replicar Tablas vs. Ejecutar Transacciones

### Enfoque 1: Ejecutar Transacciones (NO RECOMENDADO)

```
❌ Cada vez que se necesita un reporte:
   1. Ejecutar transacción SAP manualmente o vía RFC
   2. Descargar archivo
   3. Procesar archivo
   
   Problemas:
   - Lento (minutos por ejecución)
   - Carga en el sistema SAP
   - No escalable
   - Depende de disponibilidad de SAP
```

### Enfoque 2: Replicar Tablas (RECOMENDADO - Este Proyecto)

```
✅ Una vez configurado SLT:
   1. Tablas se replican automáticamente (tiempo real o batch)
   2. Datos siempre disponibles en BigQuery
   3. Consultas ilimitadas sin impactar SAP
   
   Ventajas:
   - Rápido (segundos por query)
   - Sin carga en SAP productivo
   - Escalable infinitamente
   - Independiente de disponibilidad de SAP
   - Histórico completo siempre accesible
```

---

## 7. Configuración Típica de SLT y Optimización BigQuery (S/4HANA)

### 7.1. Configuración por Tabla

Para cada tabla a replicar:

```sql
-- Ejemplo conceptual de configuración SLT para tabla VBAK

SOURCE_SYSTEM: SAP_S4_PRD
SOURCE_TABLE: VBAK
TARGET_SYSTEM: BIGQUERY
TARGET_TABLE: casa_bi_prod.raw_vbak

REPLICATION_MODE: REAL_TIME  -- o BATCH
INITIAL_LOAD: TRUE           -- Carga histórica
DELTA_LOAD: TRUE             -- Actualizaciones incrementales

FIELD_MAPPING:
  VBELN → vbeln (Primary Key)
  ERDAT → creation_date
  KUNNR → customer_number
  NETWR → net_value
  WAERK → currency
  ...

FILTERS:
  -- Opcional: Replicar solo ciertos países
  WHERE VKORG IN ('CASA', 'BR01', 'CL01', ...)
```

### 7.2. Monitoreo de Replicación

SLT proporciona:
- Estado de replicación por tabla (OK / ERROR)
- Lag de replicación (¿cuánto retraso tiene?)
- Número de registros replicados
- Errores y advertencias

### 7.3. Recomendaciones BigQuery para ACDOCA (Universal Journal)

Objetivo: rendimiento consistente y costos controlados en consultas contables y de controlling.

- Modelo por capas (nombres referenciales):
  - raw_acdoca: réplica 1:1 desde SLT (columnas técnicas incluidas)
  - stg_acdoca: tipado y normalización (conversiones de fecha/moneda)
  - fact_acdoca: tabla de hechos optimizada para analítica
  - mv_acdoca_totales: vista/materialización de totales mensuales (uso de ACDOCA_T cuando aplique)

- Particionamiento recomendado:
  - Por fecha de contabilización: BUDAT_DATE (DATE) derivado de BUDAT
  - Alternativa: partición por entero de periodo fiscal (INT RANGE sobre GJAHR_POPER = GJAHR*100 + POPER)
  - Retención: histórico de 24-36 meses particionado; particiones antiguas opcionalmente archivadas

- Clustering recomendado (hasta 4 columnas por tabla, ajustable por caso de uso):
  - FI/CO general: BUKRS, RLDNR, RACCT, KOSTL
  - Opcional según uso: PRCTR, AUFNR, SEGMENT
  - Para análisis SD en ACDOCA: KUNNR, MATNR (si están pobladas)

- Clave técnica y unicidad:
  - Componer doc_key = CONCAT_WS('|', RLDNR, BUKRS, GJAHR, BELNR, DOCLN)
  - Mantener columnas de operación CDC del conector (op_type I/U/D o _CHANGE_TYPE) y un flag _is_deleted

- Tipos de datos y normalización:
  - Importes (CURR/DEC): BigQuery NUMERIC/ BIGNUMERIC según precisión
  - Fechas: convertir DATS (YYYYMMDD) a DATE; tiempos a DATETIME/TIMESTAMP con TZ definida
  - Monedas: mantener CUKY (WAERS) y considerar tablas TCUR* si se requieren conversiones

- Seguridad y gobierno:
  - Row-level security por BUKRS y/o RLDNR cuando aplique
  - Etiquetas/tags: sistema=SAP, dominio=FI, criticidad=alta, retencion=36m

- Optimización de consultas típicas:
  - Trial Balance: preferir ACDOCA_T o materializar totales por BUKRS/RLDNR/RACCT/GJAHR/POPER
  - Conciliaciones: filtrar por periodo y sociedad; evitar scans cross-ledger innecesarios

- Costos y mantenimiento:
  - Programar vaciado de particiones históricas si no se requiere >36m
  - Auditoría de bytes escaneados por dashboard para ajustar clustering

### 7.4. Checklist de Validación con TI Global (S/4HANA → BigQuery)

1) Disponibilidad ACDOCA y ACDOCA_T
   - Profundidad histórica (meses) y cobertura delta
   - Frecuencia y latencia objetivo (diaria o near-real-time)

2) Configuración SLT / Conector
   - Modo de replicación (RT vs batch) y colas
   - Marcadores de operación (I/U/D) y manejo de borrados

3) Integridad y llaves
   - Conformidad de clave (RLDNR, BUKRS, GJAHR, BELNR, DOCLN)
   - Join con BKPF validado (BELNR/BUKRS/GJAHR)

4) Tablas complementarias críticas
   - SD: VBUK/VBUP para estatus; VBAK/VBAP para cabecera/posiciones
   - MM: MBEW (valoración), MARD/MCHB (stock), MKPF/MSEG (movimientos)
   - Textos: STXL declustering si se requieren textos

5) Estándares de datos
   - Mapeo de tipos SAP → BigQuery (DEC→NUMERIC, DATS→DATE)
   - Zona horaria y calendario fiscal (períodos POPER)

6) Seguridad y cumplimiento
   - RLS por sociedad (BUKRS)
   - Encriptación y etiquetado de datasets/tablas

7) Operación y monitoreo
   - Dashboards de replicación (lag, errores)
   - Procedimiento de re-procesamiento inicial y reintentos

---

## 8. Resumen Ejecutivo

### Para Stakeholders de Negocio

**Pregunta:** ¿Por qué hablamos de transacciones si replicamos tablas?

**Respuesta:**
- Las **transacciones** (VA05, KSB1, etc.) son el **lenguaje de negocio** que todos entienden
- Las **tablas** (VBAK, COEP, etc.) son el **lenguaje técnico** donde están los datos
- Usamos las transacciones como **punto de partida** para identificar qué datos necesita el negocio
- Luego **traducimos** esas necesidades a las tablas SAP específicas que se deben replicar

**Analogía:**
```
Transacción SAP = "Informe de Ventas Mensuales" (lo que pides)
Tablas SAP      = Base de datos de ventas (de donde viene la info)

No envías el informe a BigQuery, envías la base de datos.
Luego recreas el informe en Power BI usando esos datos.
```

### Para Stakeholders Técnicos

**Proceso Completo:**

1. **Negocio identifica** 18 transacciones críticas
2. **Fase 0 mapea** transacciones → ~35-65 tablas SAP (optimizado por ACDOCA)
3. **TI Global confirma** disponibilidad de tablas en BigQuery
4. **SLT replica** tablas configuradas a BigQuery
5. **BigQuery procesa** datos (limpieza, transformaciones)
6. **Power BI consulta** datos procesados para dashboards

**Resultado Final:**
- Usuarios ven en Power BI la **misma información** que verían en la transacción SAP
- Pero con la ventaja de centralización, historización y análisis flexible

---

## 9. Preguntas Frecuentes

### P1: ¿Por qué no replicar directamente las transacciones?

**R:** Porque las transacciones son programas, no datos. Solo las tablas contienen datos persistentes.

### P2: ¿Todas las tablas SAP se replican completas?

**R:** No necesariamente. Se pueden:
- Replicar solo ciertos campos (por performance)
- Aplicar filtros (ej. solo últimos 24 meses, solo ciertos países)
- Replicar en modo incremental (solo cambios)

### P3: ¿Qué pasa si una transacción requiere 10 tablas pero solo 8 están disponibles?

**R:** Se evalúa en Fase 0:
- Si las 2 faltantes son críticas: Escalamiento a TI Global
- Si son complementarias: Se implementa con 8 tablas, con limitaciones documentadas

### P4: ¿Las transacciones custom (Z) son más complejas?

**R:** Sí, porque:
- Pueden usar tablas custom (Z-tables) no estándar
- La lógica de negocio puede estar en código ABAP, no en las tablas
- Requieren análisis de código para entender qué hacen

### P5: ¿Cuántas tablas SAP existen en total?

**R:** SAP S/4HANA tiene >100,000 tablas. Este proyecto replica aproximadamente **~35-65** tablas, optimizado por el uso de **ACDOCA** (Universal Journal) que reemplaza múltiples tablas históricas.

---

## 10. Referencias

### Documentos Relacionados

- `03_TRANSACCIONES_SAP_INCLUIDAS.md` - Lista de 18 transacciones con tablas identificadas
- `05_FASE_1_CONSTRUCCION_DATA_LAKE.md` - Arquitectura de replicación
- (Referencia histórica eliminada) La documentación técnica específica de SLT antes listada en `solucion_slt_completa/` fue absorbida en este anexo y en `05_FASE_1_CONSTRUCCION_DATA_LAKE.md`.

### Enlaces Externos

- SAP Help Portal - SAP Landscape Transformation
- SAP Community - Table Replication Best Practices
- Google Cloud - BigQuery SAP Connector Documentation

---

**Fin del Anexo Técnico**

---

## 11. Plan de Optimización del Rango de Tablas (Poda Controlada)

Esta sección documenta el proceso propuesto para reducir el rango operativo de tablas replicadas manteniendo cobertura de KPIs y evitando regresiones de calidad.

### 11.1. Estado Actual vs. Objetivo
| Concepto | Valor Vigente (Canónico) | Objetivo Tentativo (Exploratorio) | Condición de Cambio |
|----------|---------------------------|-----------------------------------|---------------------|
| Rango de Tablas | ~76–85 | ~35–65 | Validación completa de poda y no-impacto en KPIs |
| Tablas Obsoletas Excluidas | BSEG, COEP, FAGLFLEXA | (sin cambios) | Confirmado por uso de ACDOCA |
| Tablas Condicionales | STXL, KONV, KONP, MCHB, MAKT | Incluir solo si caso de uso confirmado | Aprobación Funcional + BI |

Mientras no se complete la validación formal, el rango ~76–85 continúa siendo el único valor canónico.

### 11.2. Clasificación de Tablas
Categorías utilizadas en `docs/internos/mapeo_transacciones_tablas_detallado.csv`:
- core: Imprescindible para KPIs de los 12 dashboards.
- derivada: Puede reconstruirse mediante joins / vistas; aporta comodidad o performance.
- condicional: Depende de un caso de uso específico (textos, pricing detallado, lote, etc.).
- obsoleta: Sustituida por estructura consolidada (ej. ACDOCA).

### 11.3. Criterios de Exclusión
1. Sustituida completamente por ACDOCA/ACDOCA_T.
2. Aporta solo descripciones no críticas (etiquetas) y puede diferirse (ej. MAKT si se tolera código de material inicialmente).
3. Uso eventual que puede resolverse on-demand (pricing histórico detallado).
4. Alto costo de replicación vs. bajo aporte analítico incremental.

### 11.4. Metodología de Validación
1. Trazar cada KPI de los 12 dashboards → campos → tabla origen.
2. Marcar tablas sin KPIs dependientes: candidatas a exclusión.
3. Simular (en análisis) dataset sin derivadas y confirmar que ningún dashboard pierde métrica / dimensión.
4. Documentar en informe de poda (internos) impacto y ahorro estimado (almacenamiento + bytes escaneados).
5. Someter a aprobación conjunta (Funcional SAP + Consultor BI + PM).

### 11.5. Riesgos y Mitigaciones
| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| Exclusión prematura rompe un KPI | Alto | Validación sistemática KPI→Tabla antes de excluir |
| Reincorporación tardía añade reprocesos | Medio | Mantener checklist de reversión rápida |
| Subestimación de necesidad de textos | Bajo | Implementar fallback: vista sintética de descripciones externas |

### 11.6. Próximos Entregables
- Checklist KPI→Tabla.
- Informe de poda (v1) con conteo por categoría.
- Actualización opcional de este anexo elevando nuevo rango (si aprobado).

### 11.7. Nota de Transparencia
Las menciones a "~35–65" en documentos de entregables se consideran EXPLORATORIAS hasta que este anexo se actualice elevando el nuevo rango y `estado_documentos.md` refleje el cambio.

---

*Versión: 1.3 - 8 de noviembre de 2025 (añadida sección 11)*
