# 6. FASE 2 - MODELADO DE DATOS Y GENERACIÓN DE DASHBOARDS

## 6.1. Objetivo de la Fase

**Crear la capa semántica de datos** y desarrollar dashboards ejecutivos en Power BI que permitan a los usuarios de negocio realizar análisis autoservicio sobre los datos centralizados en BigQuery.

### Objetivos Específicos

1. ✅ Diseñar modelo dimensional optimizado para analítica
2. ✅ Desarrollar 12 dashboards ejecutivos en Power BI (promedio ~3 hojas cada uno)
3. ✅ Implementar Row-Level Security (RLS) por país/área
4. ✅ Capacitar usuarios finales en uso de dashboards
5. ✅ Establecer proceso de actualización programada

---

## 6.2. Duración y Recursos

| Parámetro | Valor |
|-----------|-------|
| **Duración estimada** | 8 semanas (ajustado por restricción 6h/día JMB) |
| **Fase del proyecto** | Mes 4-5, Semanas 16-23 |
| **Horas totales** | 294 horas |
| **Equipo** | Juan Manuel Bigi (240h) + Lucía Rodríguez (37h) + Linda López (17h) |
| **Restricción** | JMB trabaja máximo 6h/día = 30h/semana |

---

## 6.3. Actividades Detalladas

### 6.3.1. Diseño de Modelo Dimensional

**Responsable:** Juan Manuel Bigi  
**Duración:** 32 horas  
**Semanas:** 1-2

#### Modelo Estrella/Copo de Nieve

**Dimensiones Principales:**

| Dimensión | Fuente SAP | Campos Clave | Granularidad |
|-----------|------------|--------------|--------------|
| **dim_tiempo** | Sistema | Fecha, Año, Mes, Trimestre, Semana | Día |
| **dim_geografia** | T001 (Sociedades) | País, Región, Sociedad | País |
| **dim_producto** | MARA, MAKT | Material, Descripción, Categoría, Línea | Material |
| **dim_cliente** | KNA1, KNVV | Cliente, Nombre, Canal, Segmento | Cliente |
| **dim_proveedor** | LFA1, LFB1 | Proveedor, Nombre, País | Proveedor |
| **dim_centro** | T001W | Centro, Planta, Almacén | Centro |
| **dim_cuenta_contable** | SKA1, SKAT | Cuenta, Descripción, Tipo, Grupo | Cuenta GL |
| **dim_centro_costo** | CSKS | Centro Costo, Descripción, Jerarquía | Centro Costo |

**Tablas de Hechos:**

| Tabla Hechos | Fuente | Métricas Principales | Granularidad |
|--------------|--------|----------------------|--------------|
| **fact_ventas** | VA05, KE24 | Cantidad, Valor Neto, Costo, Margen | Línea orden |
| **fact_compras** | ME2L | Cantidad, Valor, Precio Unitario | Línea OC |
| **fact_inventario** | ZLEL008, MB5B | Stock Disponible, En Tránsito, Valorización | Material-Centro-Día |
| **fact_movimientos** | MB59 | Entradas, Salidas, Transferencias | Movimiento |
| **fact_gl** | FAGLL03 | Debe, Haber, Saldo | Partida GL |
| **fact_opex** | KSB1 | Importe Real, Importe Plan, Variación | Partida CO |

#### Tareas de Modelado

| # | Actividad | Horas | Entregable |
|---|-----------|-------|------------|
| 1 | Diseño de dimensiones (8 dimensiones) | 12h | ERD de dimensiones |
| 2 | Diseño de tablas de hechos (6 hechos) | 12h | ERD de hechos |
| 3 | Definición de relaciones y cardinalidades | 4h | Diagrama de relaciones |
| 4 | Optimización y clustering | 2h | Índices definidos |
| 5 | Documentación del modelo | 2h | Diccionario de modelo |

#### Ejemplo: Modelo Ventas

```
┌─────────────────┐       ┌──────────────────┐       ┌─────────────────┐
│   dim_tiempo    │       │   fact_ventas    │       │  dim_producto   │
├─────────────────┤       ├──────────────────┤       ├─────────────────┤
│ fecha_key (PK)  │──────→│ fecha_key (FK)   │←──────│ producto_key(PK)│
│ fecha           │       │ producto_key(FK) │       │ material        │
│ año             │       │ cliente_key (FK) │       │ descripcion     │
│ mes             │       │ pais_key (FK)    │       │ categoria       │
│ trimestre       │       │ cantidad         │       │ linea_negocio   │
│ semana          │       │ valor_neto       │       └─────────────────┘
└─────────────────┘       │ costo_ventas     │
                          │ margen_bruto     │
┌─────────────────┐       │ moneda           │       ┌─────────────────┐
│  dim_cliente    │       └──────────────────┘       │  dim_geografia  │
├─────────────────┤              │                   ├─────────────────┤
│ cliente_key(PK) │──────────────┘                   │ pais_key (PK)   │
│ cliente_id      │                        ┌─────────│ pais            │
│ nombre          │                        │         │ region          │
│ canal           │                        │         │ sociedad        │
│ segmento        │                        │         └─────────────────┘
└─────────────────┘                        │
```

---

### 6.3.2. Desarrollo de Capa Semántica en BigQuery

**Responsable:** Juan Manuel Bigi  
**Duración:** 20 horas  
**Semanas:** 2-3

#### Vistas de Negocio

Crear vistas SQL que abstraigan la complejidad técnica:

**Vista: vw_ventas_por_producto_pais**
```sql
CREATE OR REPLACE VIEW `casa_bi.vw_ventas_por_producto_pais` AS
SELECT
    t.año,
    t.mes,
    t.trimestre,
    g.pais,
    g.region,
    p.categoria AS categoria_producto,
    p.linea_negocio,
    SUM(fv.cantidad) AS cantidad_total,
    SUM(fv.valor_neto) AS ventas_netas,
    SUM(fv.costo_ventas) AS costo_total,
    SUM(fv.margen_bruto) AS margen_total,
    SAFE_DIVIDE(SUM(fv.margen_bruto), SUM(fv.valor_neto)) AS margen_porcentual
FROM `casa_bi.fact_ventas` fv
INNER JOIN `casa_bi.dim_tiempo` t ON fv.fecha_key = t.fecha_key
INNER JOIN `casa_bi.dim_geografia` g ON fv.pais_key = g.pais_key
INNER JOIN `casa_bi.dim_producto` p ON fv.producto_key = p.producto_key
GROUP BY 1,2,3,4,5,6,7;
```

#### KPIs Principales (30-40 métricas)

**Ventas:**
- Ventas Netas
- Crecimiento YoY
- Margen Bruto %
- Ticket Promedio
- Órdenes Abiertas (Backlog)

**Inventario:**
- Stock Disponible
- Días de Inventario (DOI)
- Rotación de Inventario
- Stock en Tránsito
- Valorización Total

**Financiero:**
- Balance por Cuenta
- OPEX vs Budget
- Cuentas por Cobrar
- Cuentas por Pagar
- Flujo de Efectivo

**Supply Chain:**
- On-Time Delivery %
- Órdenes Completadas
- Lead Time Promedio
- Fill Rate %

---

### 6.3.3. Desarrollo de Dashboards Power BI

**Responsable:** Juan Manuel Bigi  
**Duración:** 60 horas  
**Semanas:** 3-5

#### Dashboard 1: Dashboard Financiero (10h)

**Audiencia:** Controller, Analistas Finanzas  
**Fuentes:** FAGLL03, F.08, F.01, FB03

**Páginas:**
1. **Overview Financiero**
   - Balance General (activos, pasivos, patrimonio)
   - P&L resumido (ingresos, costos, gastos, resultado)
   - KPIs principales (EBITDA, margen neto, ROE)
   - Gráficos de tendencia mensual

2. **Análisis de Mayor General**
   - Saldos por cuenta contable
   - Drill-down a partidas individuales
   - Filtros: Sociedad, Periodo, Cuenta

3. **Cuentas por Cobrar/Pagar**
   - Aging de CxC y CxP
   - Top 10 clientes/proveedores
   - Análisis de morosidad

**Visualizaciones:**
- Tarjetas de KPIs
- Gráficos de barras (comparativo)
- Gráficos de líneas (tendencias)
- Tablas con drill-through
- Matriz de aging

---

#### Dashboard 2: Dashboard de Ventas (10h)

**Audiencia:** Gerente Comercial, Vendedores  
**Fuentes:** VA05, KE24

**Páginas:**
1. **Overview de Ventas**
   - Ventas del mes vs. target
   - Crecimiento YoY
   - Top 10 productos
   - Top 10 clientes
   - Mapa de ventas por país

2. **Análisis de Backlog**
   - Órdenes abiertas por valor
   - Antigüedad de órdenes
   - Proyección de cierre

3. **Rentabilidad**
   - Margen bruto por producto/cliente
   - Análisis de pricing
   - Contribución por línea de negocio

**Visualizaciones:**
- KPIs con variación % vs. periodo anterior
- Mapa coroplético (ventas por geografía)
- Gráfico de cascada (waterfall) para análisis de variación
- Scatter plot (precio vs. volumen)

---

#### Dashboard 3: Dashboard de Inventario (10h)

**Audiencia:** Supply Chain Manager, Planeadores  
**Fuentes:** ZLEL008, MB5B, MB59

**Páginas:**
1. **Overview de Inventario**
   - Stock disponible por categoría
   - Valorización total
   - DOI (Days of Inventory) por producto
   - Alertas de stock bajo/excesivo

2. **Análisis de Movimientos**
   - Entradas y salidas del mes
   - Transferencias entre centros
   - Ajustes de inventario

3. **Rotación y Obsolescencia**
   - Productos de baja rotación
   - Inventario obsoleto (>365 días)
   - Valorización de riesgo

**Visualizaciones:**
- Gráfico de Pareto (ABC de inventario)
- Heatmap (rotación por categoría/centro)
- Tabla con alertas condicionales

---

#### Dashboard 4: Dashboard de OPEX (10h)

**Audiencia:** Controllers, Gerentes de Área  
**Fuentes:** KSB1

**Páginas:**
1. **Control Presupuestario**
   - OPEX real vs. budget por centro de costo
   - Variaciones ($  y %)
   - Tendencia mensual
   - Forecast de cierre

2. **Análisis por Naturaleza**
   - Gastos por elemento de costo
   - Drill-down a órdenes CO
   - Comparativo YoY

3. **Detalle por Centro de Costo**
   - Top gastos del periodo
   - Análisis de justificaciones
   - Histórico 12 meses

**Visualizaciones:**
- Gauge charts (% ejecución presupuesto)
- Gráficos de varianza
- Tabla de detalle con alertas

---

#### Dashboard 5: Dashboard Ejecutivo (10h)

**Audiencia:** Dirección, Management  
**Fuentes:** Consolidado de todos

**Páginas:**
1. **KPIs Corporativos**
   - Ventas, Margen, OPEX, Inventario
   - Semáforos de cumplimiento
   - Tendencias clave
   - Alertas críticas

2. **Análisis por País**
   - Performance por geografía
   - Comparativo entre países
   - Drill-down a dashboards específicos

**Visualizaciones:**
- Tarjetas grandes con variación
- Sparklines (mini gráficos de tendencia)
- Tabla resumen con alertas

---

#### Dashboard 6: Dashboard de Supply Chain (10h)

**Audiencia:** Supply Chain Manager  
**Fuentes:** VA05, ME2L, ZLEL008

**Páginas:**
1. **Órdenes y Entregas**
   - On-Time Delivery %
   - Órdenes pendientes
   - Análisis de lead times

2. **Compras**
   - Órdenes de compra abiertas
   - Análisis de proveedores
   - Cumplimiento de entregas

---

#### Dashboard 7: Dashboard de Compras (Procurement) (10h)

**Audiencia:** Jefe de Compras, Analistas de Compras  
**Fuentes:** ME2L, ME23N, LFA1

**Páginas:**
1. **Overview de Compras**
   - Valor de compras del periodo
   - Órdenes de compra abiertas vs. cerradas
   - Top proveedores por volumen
   - Análisis de precio promedio

2. **Performance de Proveedores**
   - Cumplimiento de entregas
   - Calidad de producto
   - Lead time promedio por proveedor

3. **Análisis de Categorías**
   - Gasto por categoría de compra
   - Oportunidades de consolidación
   - Tendencias de precios

**Visualizaciones:**
- Treemap (proveedores por valor)
- Gráficos de línea (tendencias de precio)
- Tabla con ranking de proveedores

---

#### Dashboard 8: Dashboard de Rentabilidad por Producto (10h)

**Audiencia:** Product Managers, Gerencia Comercial  
**Fuentes:** KE24, VA05, FAGLL03

**Páginas:**
1. **Análisis de Márgenes**
   - Margen bruto por producto
   - Contribución por línea de negocio
   - Matriz precio-volumen
   - Productos más/menos rentables

2. **Análisis de Costos**
   - Desglose de costo por componente
   - Variaciones de costo
   - Análisis de pricing

3. **Análisis de Portafolio**
   - Matriz BCG (Boston Consulting Group)
   - Productos estrella vs. perros
   - Recomendaciones de optimización

**Visualizaciones:**
- Scatter plot (margen vs. volumen)
- Matriz BCG
- Gráficos de cascada (waterfall)

---

#### Dashboard 9: Dashboard de Cuentas por Pagar (10h)

**Audiencia:** Finanzas, Tesorería  
**Fuentes:** FBL1N, F.08

**Páginas:**
1. **Overview de Payables**
   - Saldo total por pagar
   - Aging de facturas (0-30, 31-60, 61-90, >90 días)
   - Top proveedores por saldo
   - Vencimientos próximos

2. **Análisis de Flujo de Caja**
   - Proyección de pagos 90 días
   - Pagos realizados vs. planificados
   - Descuentos por pronto pago disponibles

3. **Análisis por Proveedor**
   - Detalle de facturas pendientes
   - Histórico de pagos
   - Términos de pago

**Visualizaciones:**
- Gráfico de aging (barras apiladas)
- Timeline de vencimientos
- Tabla con alertas de vencimiento

---

#### Dashboard 10: Dashboard de Cuentas por Cobrar (10h)

**Audiencia:** Finanzas, Créditos y Cobranzas  
**Fuentes:** FBL5N, F.01

**Páginas:**
1. **Overview de Receivables**
   - Saldo total por cobrar
   - Aging de facturas (0-30, 31-60, 61-90, >90 días)
   - Top clientes por saldo
   - DSO (Days Sales Outstanding)

2. **Análisis de Cobranza**
   - Efectividad de cobranza
   - Facturas vencidas
   - Riesgo de incobrabilidad
   - Proyección de cobros

3. **Análisis por Cliente**
   - Detalle de facturas pendientes
   - Histórico de pagos
   - Límite de crédito vs. utilizado

**Visualizaciones:**
- Gráfico de aging (barras apiladas)
- Heatmap (riesgo por cliente)
- Tabla con alertas de morosidad

---

#### Dashboard 11: Dashboard de Controlling (CO) (10h)

**Audiencia:** Controllers, Analistas Financieros  
**Fuentes:** KSB1, COEP, AUFK

**Páginas:**
1. **Overview de Centros de Costo**
   - Ejecución presupuestaria por centro
   - Variaciones significativas
   - Distribuciones y asignaciones
   - Análisis de órdenes internas

2. **Análisis de Elementos de Costo**
   - Gasto por naturaleza
   - Comparativo real vs. plan
   - Tendencias y forecast

3. **Reporting Corporativo**
   - Consolidado por área
   - Drill-down jerárquico
   - Análisis de desviaciones

**Visualizaciones:**
- Gráficos de varianza
- Sunburst (jerarquía de centros de costo)
- Tabla de detalle con drill-through

---

#### Dashboard 12: Dashboard Estadístico Regional (10h)

**Audiencia:** Dirección Regional, Strategic Planning  
**Fuentes:** Consolidado de todas las fuentes

**Páginas:**
1. **Comparativo Regional**
   - KPIs por país (ventas, margen, OPEX, inventario)
   - Ranking de países por performance
   - Share de mercado por región
   - Análisis de crecimiento

2. **Análisis de Tendencias**
   - Evolución histórica 24 meses
   - Estacionalidad por país
   - Proyecciones y forecast
   - Análisis de correlaciones

3. **Benchmarking**
   - Best practices por país
   - Oportunidades de mejora
   - Análisis de eficiencia operativa

**Visualizaciones:**
- Mapas geográficos interactivos
- Small multiples (paneles comparativos)
- Gráficos de radar (spider charts)
- Líneas de tendencia con forecast

---

### 6.3.4. Configuración de Row-Level Security (RLS)

**Responsable:** Juan Manuel Bigi  
**Duración:** 18 horas  
**Semana:** 5

#### Estrategia de Seguridad

**Reglas RLS por Rol:**

| Rol | Acceso | Filtro Aplicado |
|-----|--------|-----------------|
| **Director Regional** | Todos los países | Sin filtro |
| **Country Manager** | Su país | `dim_geografia[pais] = USERPRINCIPALNAME()` |
| **Gerente Finanzas** | Todos los países | Sin filtro |
| **Analista Finanzas** | Su país | País asignado |
| **Gerente Supply** | Todos los países | Sin filtro |
| **Planeador** | Su país + centros asignados | País + Centro |

#### Implementación

1. **Tabla de seguridad** (BigQuery):
```sql
CREATE TABLE casa_bi.security_users (
    email STRING,
    rol STRING,
    pais STRING,
    centros ARRAY<STRING>
);
```

2. **Configuración RLS en Power BI:**
```DAX
[RLS_Filter] = 
VAR UserEmail = USERPRINCIPALNAME()
VAR UserCountry = LOOKUPVALUE(security_users[pais], security_users[email], UserEmail)
RETURN
    IF(
        UserCountry = "ALL",
        TRUE(),
        dim_geografia[pais] = UserCountry
    )
```

---

### 6.3.5. Testing con Usuarios (UAT)

**Responsables:** Juan Manuel Bigi + Lucía Rodríguez + Stakeholders  
**Duración:** 30 horas equipo técnico + 12 horas stakeholders  
**Semanas:** 6-7

#### Proceso de UAT

**Sesión 1: Finanzas - Core (6h)**
- Validación Dashboard Financiero General
- Validación Dashboard OPEX
- Validación Dashboard Cuentas por Pagar
- Validación Dashboard Cuentas por Cobrar
- Validación Dashboard Controlling
- Pruebas de RLS
- Recopilación de feedback

**Sesión 2: Supply Chain y Ventas (6h)**
- Validación Dashboard Ventas
- Validación Dashboard Inventario
- Validación Dashboard Supply Chain
- Validación Dashboard Compras
- Validación Dashboard Rentabilidad por Producto
- Recopilación de feedback

**Sesión 3: Ejecutivos y Regional (4h)**
- Validación Dashboard Ejecutivo
- Validación Dashboard Estadístico Regional
- Pruebas de drill-down y navegación
- Aprobación final

**Sesión 4: Ajustes y Re-testing (6h)**
- Correcciones basadas en feedback
- Re-validación de cambios críticos
- Sign-off final
- Recopilación de feedback

**Sesión 3: Management (2h)**
- Validación Dashboard Ejecutivo
- Aprobación general
- Solicitud de ajustes menores

#### Checklist UAT

- [ ] Datos correctos vs. SAP (reconciliación)
- [ ] Visualizaciones claras y comprensibles
- [ ] RLS funciona correctamente por usuario
- [ ] Performance aceptable (<3 seg carga inicial)
- [ ] Filtros y slicers funcionan correctamente
- [ ] Drill-through y drill-down operativos
- [ ] Exportación a Excel funcional
- [ ] Dashboards responsive (web y móvil)

---

### 6.3.6. Documentación y Capacitación

**Responsables:** Juan Manuel Bigi + Lucía Rodríguez  
**Duración:** 24 horas (12h cada uno)  
**Semana:** 6

#### Documentación de Usuario

| Documento | Páginas | Contenido |
|-----------|---------|-----------|
| **Manual de Usuario Power BI** | 30-40 | Guía paso a paso para cada dashboard |
| **Catálogo de Dashboards** | 10-15 | Descripción, audiencia, KPIs |
| **Glosario de Términos** | 8-10 | Definiciones de métricas y dimensiones |
| **FAQs** | 5-8 | Preguntas frecuentes y soluciones |
| **Quick Reference Guide** | 2 | Tarjeta de referencia rápida |

#### Videos Tutoriales

6 videos cortos (3-5 min cada uno):
1. Introducción a Power BI y navegación
2. Dashboard Financiero - Tour guiado
3. Dashboard de Ventas - Casos de uso
4. Dashboard de Inventario - Análisis práctico
5. Uso de filtros y slicers
6. Exportación y compartición de reportes

#### Sesiones de Capacitación

**Capacitación Power Users (4h)**
- Participantes: Lucía + 2 backups
- Contenido:
  - Uso avanzado de dashboards
  - Creación de bookmarks
  - Configuración de alertas
  - Troubleshooting básico

**Capacitación Usuarios Finales - Finanzas (3h)**
- Participantes: 6-8 usuarios
- Dashboards: Financiero, OPEX, Ejecutivo

**Capacitación Usuarios Finales - Supply (3h)**
- Participantes: 4-6 usuarios
- Dashboards: Ventas, Inventario, Supply

**Sesión de Refuerzo (2h)**
- Todos los usuarios
- Resolución de dudas
- Mejores prácticas

---

### 6.3.7. Ajustes Post-UAT

**Responsable:** Juan Manuel Bigi  
**Duración:** 16 horas  
**Semana:** 6

#### Tipos de Ajustes

**Ajustes Menores (incluidos):**
- Cambios de colores/formato
- Ajustes de etiquetas
- Reordenamiento de visualizaciones
- Modificación de filtros

**Ajustes Mayores (evaluación):**
- Nuevas páginas/dashboards
- Nuevas métricas no contempladas
- Cambios estructurales del modelo

**Criterio:** Ajustes que consuman >8h requieren aprobación y cotización adicional.

---

## 6.4. Entregables de Fase 2

### 6.4.1. Modelo de Datos

✅ Modelo dimensional completo (8 dimensiones + 6 hechos)  
✅ ERD documentado  
✅ Diccionario de datos del modelo  
✅ Vistas de negocio en BigQuery (15-20 vistas)

### 6.4.2. Dashboards Power BI

✅ 12 dashboards productivos:
1. Dashboard Financiero General
2. Dashboard de Ventas (Sales)
3. Dashboard de Inventario
4. Dashboard OPEX
5. Dashboard Ejecutivo
6. Dashboard Supply Chain
7. Dashboard de Compras (Procurement)
8. Dashboard de Rentabilidad por Producto
9. Dashboard de Cuentas por Pagar
10. Dashboard de Cuentas por Cobrar
11. Dashboard de Controlling (CO)
12. Dashboard Estadístico Regional
6. Dashboard Supply Chain (opcional)

✅ Row-Level Security configurado  
✅ Scheduled refresh programado (diario/semanal)

### 6.4.3. Documentación

✅ Manual de Usuario Power BI (30-40 págs)  
✅ Catálogo de Dashboards  
✅ Glosario de Términos  
✅ FAQs  
✅ 6 videos tutoriales  

### 6.4.4. Capacitación

✅ Capacitación power users completada (registro)  
✅ Capacitación usuarios finales completada (2 sesiones)  
✅ Materiales de capacitación entregados

### 6.4.5. Validación

✅ UAT firmado por stakeholders  
✅ Matriz de validación (datos SAP vs. Power BI)  
✅ Registro de ajustes realizados

---

## 6.5. Cronograma Semanal Fase 2

### Semana 1-2 (24 feb - 9 mar): Modelado

| Actividad | Responsable | Horas |
|-----------|-------------|-------|
| Diseño dimensiones y hechos | JMB | 24h |
| Desarrollo vistas BigQuery | JMB | 16h |
| Revisión con stakeholders | Todos | 4h |

**Hito:** Modelo dimensional aprobado

---

### Semana 3-4 (10-23 mar): Desarrollo Dashboards (Parte 1)

| Actividad | Responsable | Horas |
|-----------|-------------|-------|
| Dashboard Financiero | JMB | 10h |
| Dashboard Ventas | JMB | 10h |
| Dashboard Inventario | JMB | 10h |
| Revisiones iterativas | Todos | 6h |

**Hito:** 3 dashboards funcionales

---

### Semana 5 (21-27 abr): Dashboards Finales + RLS

| Actividad | Responsable | Horas |
|-----------|-------------|-------|
| Dashboard OPEX | JMB | 10h |
| Dashboard Ejecutivo | JMB | 10h |
| Dashboards adicionales (Supply, Compras, etc.) | JMB | 10h |

**Hito:** Todos los dashboards base completos

---

### Semana 6 (28 abr - 4 may): RLS y UAT Inicio

| Actividad | Responsable | Horas |
|-----------|-------------|-------|
| Configuración RLS (12 dashboards) | JMB | 18h |
| UAT con Finanzas | Todos + Stakeholders | 6h |
| Ajustes UAT iniciales | JMB | 8h |

**Hito:** RLS configurado, UAT Finanzas iniciado

---

### Semana 7 (5-11 may): UAT y Ajustes

| Actividad | Responsable | Horas |
|-----------|-------------|-------|
| UAT con Supply | Todos + Stakeholders | 6h |
| Ajustes post-UAT | JMB | 16h |
| Documentación | JMB + Lucía | 8h |

**Hito:** UAT completo, ajustes implementados

---

### Semana 8 (12-18 may): Capacitación y Go-Live

| Actividad | Responsable | Horas |
|-----------|-------------|-------|
| Capacitación usuarios | Lucía + JMB | 12h |
| Testing final | JMB | 4h |
| **Go-Live Power BI** 🎉 | Todos | 2h |
| Cierre Fase 2 | Todos | 4h |

**Hito:** Go-live exitoso de Power BI

---

## 6.6. Esfuerzo de Fase 2

| Recurso | Horas |
|---------|-------|
| **Juan Manuel Bigi** | 240h |
| **Lucía Rodríguez** | 37h |
| **Linda López (PM)** | 17h |
| **Stakeholders Elanco** | 54h (sin costo) |
| **TOTAL FASE 2** | **294h** |

---

## 6.7. Criterios de Éxito de Fase 2

✅ **Fase 2 se considera exitosa si:**

1. ✅ 12 dashboards productivos y validados
2. ✅ RLS configurado y probado por rol
3. ✅ UAT aprobado por stakeholders de Finanzas y Supply
4. ✅ Usuarios capacitados (mínimo 15 usuarios)
5. ✅ Documentación completa entregada
6. ✅ Actualización programada funcionando (scheduled refresh)
7. ✅ Performance aceptable (<3 segundos carga inicial)
8. ✅ Adopción: ≥70% de usuarios activos a 15 días post go-live

---

### 6.3.8. Post Go-Live

Periodo posterior a la puesta en producción sin compromisos operativos incluidos: cualquier ajuste o evolución se evalúa y cotiza aparte. No se contemplan actividades de operación continua en este documento.

---

*Siguiente sección: [07_FASE_3_MODELOS_PREDICTIVOS.md](07_FASE_3_MODELOS_PREDICTIVOS.md)*
