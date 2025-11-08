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
│              SAP S/4HANA (Sistema Fuente)                │
│                                                      │
│  Transacción VA05  ───▶  Tablas: VBAK, VBAP, VBEP  │
│  Transacción KSB1  ───▶  Tablas: COBK, COEP, AUFK  │
│  Transacción FAGLL03 ─▶  Tabla: FAGLFLEXA          │
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
│  raw_vbak  ◀── Réplica de VBAK                      │
│  raw_vbap  ◀── Réplica de VBAP                      │
│  raw_vbep  ◀── Réplica de VBEP                      │
│  raw_cobk  ◀── Réplica de COBK                      │
│  raw_coep  ◀── Réplica de COEP                      │
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
**Tablas Requeridas (Ejemplos):**
- `COBK` (Cabecera de documentos CO)
- `COEP` (Partidas individuales CO - ¡muy grande!)
- `AUFK` (Maestro de órdenes internas)
- `CSKS` (Maestro de centros de costo)
- `CSKA` (Maestro de elementos de costo)
**Total Estimado:** ~5 tablas
**Complejidad Alta:** La tabla `COEP` es de alto volumen y el módulo CO tiene una lógica dimensional compleja.

### Ejemplo 3: FAGLL03 (Mayor General)

**Transacción:** FAGLL03
**Tablas Requeridas (Ejemplos):**
- `FAGLFLEXA` (Partidas individuales del nuevo GL - ¡volumen masivo!)
- `BKPF` (Cabecera de documentos contables)
- `BSEG` (Segmentos de documentos contables)
- `SKA1` (Plan de cuentas)
**Total Estimado:** ~4 tablas
**Complejidad Muy Alta:** `FAGLFLEXA` es una de las tablas más grandes y críticas de SAP FI, requiriendo estrategias de particionamiento y filtros eficientes.

### Estimación para el Proyecto

| Categoría | Cantidad | Tablas Estimadas | Complejidad |
|-------------------------------|----------|------------------|-----------------|
| Transacciones Prioridad 1 | 4 | ~19-21 | Alta a Muy Alta |
| Transacciones Prioridad 2 | 4 | ~11-13 | Media a Muy Alta |
| Transacciones Pendientes | 10 | ~40-50 | Baja a Compleja |
| **TOTAL ESTIMADO** | **18** | **~70-84 tablas** | **Mixta** |

---

## 5. Implicaciones para el Proyecto

### 5.1. Fase 0: Análisis Crítico

Durante Fase 0 se debe realizar un **mapeo exhaustivo**:

```
ENTRADAS (Fase 0)              PROCESO                    SALIDAS
─────────────────              ───────                    ────────
┌─────────────────┐           ┌──────────────────┐      ┌────────────────┐
│ 18 Transacciones│──────────▶│ Análisis de      │─────▶│ Lista de       │
│ SAP priorizadas │           │ Tablas           │      │ 70-90 Tablas   │
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
| Más tablas de lo estimado (>90) | Baja | Medio | Ajuste de alcance en Fase 0 |
| Tablas con volúmenes muy altos | Media | Medio | Estrategia de particionamiento |

### 5.4. Decisión Go/No-Go

**Criterio para continuar a Fase 1:**

✅ **Mínimo 80% de las tablas identificadas disponibles en BigQuery**

Por ejemplo:
- Si se identifican 80 tablas necesarias
- Mínimo 64 tablas deben estar disponibles
- Si <64 disponibles: Evaluar plan B (escalamiento a TI Global, uso de extractores RFC, etc.)

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

## 7. Configuración Típica de SLT

### 7.1. Configuración por Tabla

Para cada tabla a replicar:

```sql
-- Ejemplo conceptual de configuración SLT para tabla VBAK

SOURCE_SYSTEM: SAP_ECC_PRD
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
2. **Fase 0 mapea** transacciones → ~70-90 tablas SAP
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

**R:** SAP S/4HANA tiene >100,000 tablas. Este proyecto solo replica las ~70-90 necesarias para las 18 transacciones priorizadas.

---

## 10. Referencias

### Documentos Relacionados

- `03_TRANSACCIONES_SAP_INCLUIDAS.md` - Lista de 18 transacciones con tablas identificadas
- `05_FASE_1_CONSTRUCCION_DATA_LAKE.md` - Arquitectura de replicación
- `solucion_slt_completa/` - Documentación técnica de SLT

### Enlaces Externos

- SAP Help Portal - SAP Landscape Transformation
- SAP Community - Table Replication Best Practices
- Google Cloud - BigQuery SAP Connector Documentation

---

**Fin del Anexo Técnico**

*Versión: 1.0 - 7 de noviembre de 2025*
