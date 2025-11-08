# 12. ENTREGABLES Y CONDICIONES COMERCIALES

## 12.1. Catálogo Completo de Entregables

A continuación se detalla la lista exhaustiva de todos los entregables del proyecto, organizados por fase.

---

## 12.2. Entregables por Fase

### 📋 FASE 0: Revisión de Alcance y Factibilidad (Semanas 1-5)

#### Documento 1: Reporte de Auditoría Técnica
**Descripción:** Análisis exhaustivo de la disponibilidad y calidad de datos en BigQuery y SAP.

**Contenido:**
- ✅ Inventario de tablas SAP en BigQuery (18 transacciones evaluadas)
- ✅ Diccionario de datos completo (campos, tipos, relaciones)
- ✅ Análisis de calidad de datos (completitud, consistencia, duplicados)
- ✅ Datos históricos disponibles (fecha desde/hasta por transacción)
- ✅ Identificación de tablas faltantes o incompletas
- ✅ Validación de conectividad SAP ↔ BigQuery
- ✅ Recomendaciones técnicas

**Formato:** Documento PDF/DOCX (30-40 páginas)  
**Fecha Entrega:** Semana 3 (27-ene-2026)  
**Aprobador:** Product Owner + TI Elanco

---

#### Documento 2: Backlog Priorizado del Proyecto
**Descripción:** Lista priorizada de transacciones SAP a implementar con estimaciones refinadas.

**Contenido:**
- ✅ 18 transacciones clasificadas por prioridad (1-Alta, 2-Media, 3-Baja)
- ✅ User Stories por transacción (formato: "Como [usuario], quiero [funcionalidad], para [beneficio]")
- ✅ Criterios de aceptación SMART por user story
- ✅ Estimaciones refinadas de esfuerzo (horas por transacción)
- ✅ Dependencias técnicas identificadas
- ✅ Propuesta de MVP (Minimum Viable Product) para Fase 1

**Formato:** Excel/Google Sheets + Documento PDF  
**Fecha Entrega:** Semana 4 (03-feb-2026)  
**Aprobador:** Product Owner + Stakeholders

---

#### Documento 3: Arquitectura Detallada del Data Lake
**Descripción:** Diseño técnico completo de la solución de datos en BigQuery.

**Contenido:**
- ✅ Diagrama de arquitectura (RAW → PROCESSED → CURATED)
- ✅ Modelo de datos dimensional (star schema o snowflake)
- ✅ Diseño de tablas (DDL scripts)
- ✅ Estrategia de particionamiento y clustering
- ✅ Nomenclatura de tablas y campos (convenciones)
- ✅ Política de retención de datos
- ✅ Estrategia de seguridad (Row-Level Security, permisos)
- ✅ Documentación de flujos de datos (ETL pipelines)

**Formato:** Documento PDF + Archivos SQL  
**Fecha Entrega:** Semana 4 (03-feb-2026)  
**Aprobador:** TI Elanco + Arquitecto Aunergia

---

#### Documento 4: Plan de Proyecto Actualizado
**Descripción:** Cronograma detallado y plan de ejecución de Fases 1 y 2.

**Contenido:**
- ✅ Cronograma semanal (Gantt chart)
- ✅ Hitos y entregables por semana
- ✅ Asignación de recursos (quién hace qué)
- ✅ Plan de comunicación (reuniones, reportes)
- ✅ Identificación de riesgos específicos
- ✅ Métricas de éxito (KPIs del proyecto)

**Formato:** MS Project / Smartsheet / Excel + PDF  
**Fecha Entrega:** Semana 5 (10-feb-2026)  
**Aprobador:** Product Owner + Linda López (PM)

---

#### Entregable 5: Decisión Go/No-Go (CRÍTICO)
**Descripción:** Reporte ejecutivo con recomendación de continuar, ajustar o detener el proyecto.

**Contenido:**
- ✅ Resumen de hallazgos de la auditoría
- ✅ Evaluación de criterios Go/No-Go (ver sección 11.9)
- ✅ Riesgos identificados y planes de mitigación
- ✅ Recomendación justificada (GO / NO-GO / GO CON AJUSTES)
- ✅ Si GO: Plan de acción para Fase 1
- ✅ Si NO-GO: Alternativas y próximos pasos

**Formato:** Presentación PowerPoint (15-20 slides) + Documento ejecutivo (5-7 páginas)  
**Fecha Entrega:** 10-feb-2026 (Workshop con Product Owner y Stakeholders)  
**Aprobador:** Product Owner + Management Elanco

**Criterio:** Si NO-GO → Proyecto se detiene. Aunergia cobra solo Fase 0 (116 horas).

---

### 🏗️ FASE 1: Construcción del Repositorio (Data Lake) (Semanas 6-15)

#### Entregable 6: Base de Datos BigQuery en Producción
**Descripción:** Data Lake operativo en BigQuery con datos de las transacciones SAP priorizadas.

**Contenido Técnico:**
- ✅ **Capa RAW:** Tablas con datos crudos de SAP (replicación 1:1)
  - Nomenclatura: `raw_sap_<tabla>` (ej. `raw_sap_ekko`, `raw_sap_vbak`)
  - Particionamiento por fecha de carga (`_load_date`)
  - Datos históricos: mínimo 24 meses

- ✅ **Capa PROCESSED:** Tablas con transformaciones y limpieza
  - Nomenclatura: `processed_<módulo>_<entidad>` (ej. `processed_mm_compras`)
  - Limpieza de datos: eliminación de duplicados, corrección de tipos
  - Aplicación de reglas de negocio
  - Particionamiento por fecha transaccional

- ✅ **Capa CURATED:** Modelo dimensional (Star Schema)
  - Tablas de hechos (Facts): `fact_<proceso>` (ej. `fact_ventas`, `fact_compras`)
  - Tablas de dimensiones (Dims): `dim_<entidad>` (ej. `dim_producto`, `dim_cliente`)
  - Agregaciones pre-calculadas
  - Row-Level Security configurado (filtro por país/área)

**Cobertura Mínima:**
- ✅ Mínimo **12 de 18 transacciones** implementadas
- ✅ Prioridad 1 (TOP 6): 100% completadas
- ✅ Prioridad 2 (MID 6): 80% completadas
- ✅ Prioridad 3 (LOW 6): Best-effort

**Calidad de Datos:**
- ✅ Data Quality checks automáticos (validaciones SQL)
- ✅ Completitud > 95% en campos críticos
- ✅ Trazabilidad: metadata de carga (fecha, fuente, usuario)

**Formato:** Dataset BigQuery `casa_bi_prod` con tablas pobladas  
**Fecha Entrega:** Semana 15 (2-mar-2026)  
**Aprobador:** Lucía Rodríguez + TI Elanco (Validación técnica)

---

#### Entregable 7: Pipelines ETL Operativos
**Descripción:** Pipelines automatizados para extracción, transformación y carga de datos SAP → BigQuery.

**Contenido:**
- ✅ Scripts SQL o Python para extracción desde SAP (vía RFC/tablas)
- ✅ Scripts de transformación (limpieza, enriquecimiento, cálculos)
- ✅ Scripts de carga a BigQuery (capa RAW, PROCESSED, CURATED)
- ✅ Orquestación (Airflow, Cloud Composer, o scripts bash con cron)
- ✅ Logs de ejecución y notificaciones de errores
- ✅ Política de carga: inicial (full load) + incremental (delta)

**Frecuencia de Carga:**
- Datos transaccionales: Diario (overnight, 2:00 AM)
- Datos maestros: Semanal (domingos)
- Dashboards: Refresh automático (según Power BI)

**Formato:** Código versionado en Git + Documentación técnica  
**Fecha Entrega:** Semana 15 (2-mar-2026)  
**Aprobador:** Juan Manuel Bigi + TI Elanco

---

#### Entregable 8: Documentación Técnica del Data Lake
**Descripción:** Documentación exhaustiva para TI Elanco y futuros mantenedores.

**Contenido:**
- ✅ **Data Dictionary:** Descripción de todas las tablas y campos
- ✅ **Diagramas de Flujo (Data Flow Diagrams):** Origen → Transformación → Destino
- ✅ **Modelo Dimensional:** Diagramas ER (Entity-Relationship)
- ✅ **Manual de Operación:** Cómo ejecutar pipelines, monitorear errores, troubleshooting
- ✅ **Guía de Desarrollo:** Convenciones de código, cómo agregar nuevas transacciones
- ✅ **Anexo:** Scripts SQL de ejemplo, queries útiles

**Formato:** Documento PDF/DOCX (60-80 páginas) + Wiki/Confluence  
**Fecha Entrega:** Semana 15 (2-mar-2026)  
**Aprobador:** TI Elanco

---

#### Entregable 9: Reporte de Validación de Datos
**Descripción:** Validación cruzada de datos BigQuery vs. SAP para asegurar consistencia.

**Contenido:**
- ✅ Comparaciones de totales (sumas, conteos) por transacción
- ✅ Muestreo de registros individuales (validación 1:1)
- ✅ Identificación de discrepancias y su causa raíz
- ✅ % de completitud de datos por transacción
- ✅ Casos de borde o excepciones documentadas

**Formato:** Documento Excel/PDF (20-30 páginas)  
**Fecha Entrega:** Semana 15 (2-mar-2026)  
**Aprobador:** Lucía Rodríguez + Stakeholders

---

### 📊 FASE 2: Modelado y Construcción de Dashboards (Semanas 16-22)

#### Entregable 10: Dashboards Operativos en Power BI (12 dashboards)
**Descripción:** Dashboards interactivos publicados en Power BI Service para usuarios finales.

**Dashboards Incluidos:**

1. **Dashboard Financiero General (FAGLL03, FB03)**
   - KPIs: Balance por cuenta, saldos deudores/acreedores, variaciones mensuales
   - Filtros: Fecha, país, sociedad, cuenta contable
   - Visualizaciones: Gráfico de barras (balance), tabla detalle, tarjetas KPI

2. **Dashboard de Ventas - Sales (VA05, KE24, XD03)**
   - KPIs: Ventas brutas/netas, órdenes abiertas/cerradas, clientes activos, productos TOP 10
   - Filtros: Fecha, país, canal de distribución, cliente, material
   - Visualizaciones: Gráfico de columnas (ventas mensuales), mapa, tabla detalle

3. **Dashboard de Inventario (ZLEL008, MB5B, MB59)**
   - KPIs: Valor de inventario, rotación, stock obsoleto, días de cobertura, stock en tránsito
   - Filtros: Centro, almacén, material, país
   - Visualizaciones: Treemap (valor por categoría), tabla con semáforo (stock crítico), heatmap

4. **Dashboard de OPEX (KSB1)**
   - KPIs: OPEX real vs. budget, variaciones, forecast de cierre
   - Filtros: Fecha, centro de costo, país, elemento de costo
   - Visualizaciones: Gauge charts, gráficos de varianza, tabla de detalle

5. **Dashboard Ejecutivo (Consolidado)**
   - KPIs: Ventas, Margen, OPEX, Inventario, semáforos de cumplimiento
   - Filtros: Fecha, país, línea de negocio
   - Visualizaciones: Tarjetas grandes, sparklines, tabla resumen

6. **Dashboard Supply Chain (VA05, ME2L, ZLEL008)**
   - KPIs: On-Time Delivery %, órdenes pendientes, lead times, análisis de compras
   - Filtros: Fecha, proveedor, material, centro
   - Visualizaciones: Timeline, gráficos de tendencia, tabla de órdenes

7. **Dashboard de Compras - Procurement (ME2L, ME23N, XK03)**
   - KPIs: Órdenes abiertas, recepciones pendientes, valor total compras, lead time promedio
   - Filtros: Fecha, material, proveedor, centro, organización de compras
   - Visualizaciones: Treemap (proveedores), gráficos de tendencia, tabla de órdenes

8. **Dashboard de Rentabilidad por Producto (KE24, VA05, FAGLL03)**
   - KPIs: Margen bruto por producto, contribución por línea, matriz precio-volumen
   - Filtros: Fecha, producto, línea de negocio, país
   - Visualizaciones: Scatter plot, matriz BCG, gráficos de cascada

9. **Dashboard de Cuentas por Pagar (FBL1N, F.08, XK03)**
   - KPIs: Saldo total AP, aging (0-30, 31-60, 61-90, >90 días), proveedores TOP 10
   - Filtros: Fecha, país, sociedad, proveedor, moneda
   - Visualizaciones: Gráfico de aging, timeline de vencimientos, tabla detalle

10. **Dashboard de Cuentas por Cobrar (FBL5N, F.01, XD03)**
    - KPIs: Saldo total AR, aging, clientes TOP 10, DSO, % morosidad
    - Filtros: Fecha, país, cliente, sociedad
    - Visualizaciones: Gráfico de aging, heatmap de riesgo, tabla detalle

11. **Dashboard de Controlling - CO (KSB1, COEP, AUFK)**
    - KPIs: Ejecución presupuestaria por centro de costo, variaciones, distribuciones
    - Filtros: Fecha, centro de costo, área, orden interna
    - Visualizaciones: Gráficos de varianza, sunburst, tabla con drill-through

12. **Dashboard Estadístico Regional (Consolidado)**
    - KPIs: Comparativo de KPIs por país, ranking de performance, share regional
    - Filtros: Fecha, país, métrica
    - Visualizaciones: Mapas geográficos, small multiples, spider charts, líneas de tendencia

**Calidad de Dashboards:**
- ✅ Diseño responsive (Desktop y Mobile)
- ✅ Tiempos de carga < 10 segundos
- ✅ Colores corporativos Elanco
- ✅ Tooltips explicativos en cada visual
- ✅ Botones de navegación intuitivos
- ✅ Drill-down en gráficos clave

**Formato:** Archivos .pbix + Publicados en Power BI Service (Workspace `CASA_BI_Production`)  
**Fecha Entrega:** Semana 20 (13-abr-2026)  
**Aprobador:** Stakeholders (UAT) + Product Owner

---

#### Entregable 11: Documentación Funcional de Dashboards
**Descripción:** Guía de usuario para entender y utilizar los dashboards.

**Contenido:**
- ✅ Propósito de cada dashboard (¿Para qué sirve?)
- ✅ KPIs incluidos y su cálculo (fórmulas)
- ✅ Filtros disponibles y su uso
- ✅ Casos de uso por tipo de usuario (Finanzas, Supply, Management)
- ✅ Preguntas frecuentes (FAQs)
- ✅ Troubleshooting (¿Qué hacer si no veo datos?)

**Formato:** Documento PDF/DOCX (30-40 páginas) con screenshots  
**Fecha Entrega:** Semana 20 (13-abr-2026)  
**Aprobador:** Product Owner

---

#### Entregable 12: Manuales de Capacitación
**Descripción:** Material didáctico para capacitación de usuarios finales y power users.

**Contenido:**
- ✅ **Manual de Usuario Final (Finanzas/Supply):**
  - Cómo acceder a Power BI Service
  - Navegación básica en dashboards
  - Uso de filtros y slicers
  - Exportación a Excel/PDF
  - Best practices

- ✅ **Manual de Power User:**
  - Conceptos avanzados (drill-down, bookmarks)
  - Creación de reportes personalizados (si aplica)
  - Interpretación de KPIs complejos
  - Validación de datos (cómo verificar si los números son correctos)

- ✅ **Presentación de Capacitación:**
  - Slides para sesiones de training
  - Ejercicios prácticos con datos reales

**Formato:** Documentos PDF + Presentación PowerPoint  
**Fecha Entrega:** Semana 20 (13-abr-2026)  
**Aprobador:** Product Owner + Lucía Rodríguez

---

#### Entregable 13: Reporte de Pruebas de Aceptación de Usuario (UAT)
**Descripción:** Documentación de las pruebas realizadas por usuarios finales y su aprobación.

**Contenido:**
- ✅ Casos de prueba ejecutados (por dashboard)
- ✅ Resultados: Aprobado / No Aprobado / Con observaciones
- ✅ Bugs identificados y su resolución
- ✅ Feedback de usuarios (sugerencias de mejora)
- ✅ Acta de aceptación firmada por stakeholders

**Formato:** Documento Excel + Acta de Aceptación PDF  
**Fecha Entrega:** Semana 21 (20-abr-2026)  
**Aprobador:** Stakeholders + Product Owner (FIRMA)

---

#### Entregable 14: Go-Live (Puesta en Producción)
**Descripción:** Dashboards activos y accesibles para todos los usuarios finales.

**Contenido:**
- ✅ Dashboards publicados en `CASA_BI_Production` workspace
- ✅ Permisos configurados (8 usuarios con licencias Power BI Pro)
- ✅ Datos actualizados y validados
- ✅ Pipelines ETL corriendo en modo automático
- ✅ Monitoreo de errores activo (alertas)
- ✅ Comunicación a usuarios (email con enlaces y guías)

**Fecha Go-Live:** 20-abr-2026 (Lunes - Inicio de semana laboral)  
**Aprobador:** Product Owner + TI Elanco

---

#### Entregable 15: Sesiones de Capacitación (Incluidas)
**Descripción:** Sesiones presenciales o virtuales para entrenar usuarios finales y power users.

**Sesiones:**

| Audiencia | Duración | Contenido | Fecha |
|-----------|----------|-----------|-------|
| **Power Users (2 personas)** | 4 horas | Uso avanzado dashboards, troubleshooting, validación datos | Semana 19 |
| **Usuarios Finanzas (4-6 personas)** | 3 horas | Navegación básica, dashboards financieros, exportación | Semana 20 |
| **Usuarios Supply (2-4 personas)** | 3 horas | Navegación básica, dashboards supply/inventarios | Semana 20 |
| **Sesión de Refuerzo (todos)** | 2 horas | Q&A, casos avanzados, tips & tricks | Semana 21 |

**Total:** 12 horas de capacitación incluidas en el proyecto

**Formato:** Sesiones virtuales (Zoom/Teams) con grabación  
**Fecha Entrega:** Semanas 19-21  
**Responsable:** Juan Manuel Bigi + Lucía Rodríguez

---

### 📖 FASE 3: Modelos de Predicción (Solo Descripción - NO Implementación)

#### Entregable 16: Documento de Propuesta de Modelos Predictivos
**Descripción:** Análisis conceptual y propuesta de modelos de Machine Learning / Forecasting para futura implementación.

**Contenido:**
- ✅ Identificación de 8 casos de uso potenciales:
  1. Pronóstico de Ventas (Forecasting)
  2. Optimización de Inventarios (Stock Safety)
  3. Predicción de Morosidad (Credit Scoring)
  4. Detección de Fraudes/Anomalías
  5. Segmentación de Clientes (Clustering)
  6. Precios Dinámicos (Price Optimization)
  7. Predicción de Churn (Client Retention)
  8. Optimización de Rutas de Distribución

- ✅ Por cada caso de uso:
  - Descripción del problema y beneficio esperado
  - Datos requeridos (fuentes, volumen, calidad)
  - Técnicas de ML aplicables (regresión, clasificación, clustering, time series)
  - Estimación de esfuerzo (horas) y complejidad (baja/media/alta)
  - ROI estimado (cualitativo)

- ✅ Recomendación de priorización (Quick-wins vs. Long-term)
- ✅ Roadmap sugerido para implementación (Fase 3 futura)

**IMPORTANTE:** Este entregable es **descriptivo/conceptual solamente**. NO incluye implementación de código, modelos entrenados, ni despliegue en producción.

**Formato:** Documento PDF/DOCX (40-50 páginas)  
**Fecha Entrega:** Semana 21 (20-abr-2026)  
**Aprobador:** Product Owner + Stakeholders

---

### 🎯 Entregables Transversales (Todas las Fases)

#### Entregable 17: Reportes de Avance Semanales
**Descripción:** Reporte ejecutivo de progreso del proyecto.

**Contenido:**
- ✅ Actividades completadas en la semana
- ✅ Actividades planificadas para próxima semana
- ✅ % de avance general del proyecto
- ✅ Riesgos/bloqueantes identificados
- ✅ Decisiones requeridas
- ✅ Consumo de horas vs. planificado

**Formato:** Email + Documento PDF (2-3 páginas)  
**Frecuencia:** Semanal (viernes EOD)  
**Destinatarios:** Product Owner + Stakeholders clave

---

#### Entregable 18: Minutas de Reuniones
**Descripción:** Registro de todas las reuniones del proyecto.

**Contenido:**
- ✅ Fecha, participantes, duración
- ✅ Temas discutidos
- ✅ Decisiones tomadas
- ✅ Acción items (responsable, fecha compromiso)
- ✅ Próximos pasos

**Formato:** Documento Word/Google Doc  
**Frecuencia:** Después de cada reunión (24h)  
**Responsable:** Linda López (PM)

---

#### Entregable 19: Código Fuente en Repositorio Git
**Descripción:** Todo el código del proyecto versionado y accesible.

**Contenido:**
- ✅ Scripts SQL (ETL, transformaciones, vistas)
- ✅ Scripts Python (si aplicables para extracción)
- ✅ Archivos .pbix de Power BI
- ✅ Archivos de configuración (YAML, JSON)
- ✅ README.md con instrucciones de ejecución

**Formato:** Repositorio Git (GitHub, GitLab, o Bitbucket)  
**Acceso:** TI Elanco (permisos de lectura/escritura)  
**Fecha Entrega:** Continuo (commits semanales)

---

#### Entregable 20: Documento de Cierre de Proyecto
**Descripción:** Reporte final al completar el proyecto.

**Contenido:**
- ✅ Resumen ejecutivo del proyecto
- ✅ Objetivos alcanzados vs. planificados
- ✅ Entregables completados (checklist)
- ✅ Métricas finales (horas consumidas, presupuesto, cronograma)
- ✅ Lecciones aprendidas
- ✅ Recomendaciones para futuras fases
- ✅ Plan de soporte post go-live (30 días)

**Formato:** Documento PDF (15-20 páginas) + Presentación ejecutiva (10 slides)  
**Fecha Entrega:** 27-abr-2026 (1 semana post go-live)  
**Aprobador:** Product Owner + Management Elanco

---

## 12.3. Resumen de Entregables

| Fase | # Entregables | Entregables Clave |
|------|---------------|-------------------|
| **Fase 0** | 5 | Auditoría técnica, Backlog, Arquitectura, Plan, Go/No-Go |
| **Fase 1** | 4 | Data Lake BigQuery, Pipelines ETL, Documentación técnica, Validación |
| **Fase 2** | 6 | 12 Dashboards Power BI, Documentación funcional, Capacitaciones, Go-Live |
| **Fase 3** | 1 | Propuesta de modelos predictivos (solo descripción) |
| **Transversal** | 4 | Reportes semanales, Minutas, Código Git, Cierre |
| **TOTAL** | **20** | **20 entregables formales** |

---

## 12.4. Condiciones Comerciales

### 12.4.1. Esfuerzo Total del Proyecto

**Desglose por Fase:**

| Fase | Descripción | Horas |
|------|-------------|-------|
| **Fase 0** | Revisión de Alcance y Factibilidad (4-5 semanas) | 116h |
| **Fase 1** | Construcción de Data Lake (22 semanas) | 696h |
| **Fase 2** | Modelado y Dashboards (14 semanas) | 659h |
| **Fase 3** | Modelos Predictivos (solo descripción) | Incluido en Fase 2 |
| **TOTAL** | **42 semanas** | **1,590h** |

---

### 12.4.2. Hitos del Proyecto

**Estructura de Entrega:** Por hitos (Milestone-based)

| Hito | Fecha Estimada | % del Esfuerzo | Horas | Condición de Aceptación |
|------|----------------|----------------|-------|-------------------------|
| **Hito 1: Inicio del Proyecto** | 6-ene-2026 | - | - | Contrato firmado, Kick-off realizado |
| **Hito 2: Entrega Go/No-Go (Fase 0)** | 12-ene-2026 | 15% | 235h | Aprobación de Go/No-Go |
| **Hito 3: Data Lake Completado (Fase 1)** | 14-jun-2026 | 44% | 696h | Aprobación técnica Data Lake |
| **Hito 4: 12 Dashboards UAT (Fase 2)** | 20-sep-2026 | 41% | 659h | Aprobación UAT por stakeholders |
| **Hito 5: Go-Live y Cierre** | 20-sep-2026 | - | - | Go-Live exitoso + Cierre |
| **TOTAL** | | **100%** | **1,590h** | |

**Nota sobre Condiciones Comerciales:**
- Las condiciones comerciales y esquema de facturación serán definidas en acuerdo separado
- Esfuerzo total del proyecto: 1,590 horas distribuidas en 42 semanas
- Si el proyecto se detiene en Fase 0 (NO-GO), se factura solo el esfuerzo de Fase 0 (235 horas)

---

### 12.4.3. Alcance Incluido

**✅ Incluido en el Alcance del Proyecto:**

1. **Recursos Humanos:**
   - Linda López (Project Manager): 145 horas
   - Lucía Rodríguez (SAP Analyst / Data Analyst): 484 horas
   - Juan Manuel Bigi (Data Architect / Developer): 961 horas
   - **Total Esfuerzo:** 1,590 horas

2. **Entregables:**
   - Los 20 entregables listados en sección 12.2

3. **Actividades:**
   - Análisis de requerimientos (workshops)
   - Diseño de arquitectura
   - Desarrollo de pipelines ETL
   - Desarrollo de 12 dashboards Power BI (promedio ~3 hojas por dashboard)
   - Documentación técnica y funcional
   - Capacitaciones (12 horas totales)
   - UAT y validaciones
   - Post go-live: coordinación de ajustes menores si corresponde (sin compromisos de operación continua incluidos)

4. **Reuniones:**
   - Kick-off
   - Workshops (4 sesiones de 2-3 horas)
   - Reuniones de seguimiento semanales
   - Presentación Go/No-Go
   - UAT con stakeholders
   - Go-Live

5. **Soporte Post Go-Live:**
   - 30 días de soporte incluido (desde 20-abr-2026 hasta 20-may-2026)
   - Atención a incidencias (L-V, 9 AM - 6 PM GMT-3/GMT-5)
   - Correcciones de bugs identificados en UAT o post go-live
   - Ajustes menores a dashboards (sin cambio de alcance)
   - Capacitaciones de refuerzo (si necesarias)

---

### 12.4.4. Alcance NO Incluido (Exclusiones)

**❌ NO Incluido en el Presupuesto (requiere cotización adicional):**

1. **Infraestructura:**
   - Costos de Google Cloud Platform (BigQuery storage, processing)
   - Licencias Microsoft Power BI Pro (ya adquiridas por Elanco)
   - Costos de conectividad (VPN, Private Service Connect)

2. **Herramientas de Terceros:**
   - Fivetran, Airbyte, Stitch (herramientas ETL de pago)
   - dbt Cloud, Matillion (herramientas de transformación)
   - Tableau, Looker (herramientas BI alternativas)

3. **Desarrollo Adicional:**
   - Transacciones SAP adicionales (más de las 18 planificadas)
   - Dashboards adicionales (más de los 6 incluidos)
   - Integraciones con otros sistemas (ej. CRM, HR, WMS)
   - Implementación de modelos predictivos (Fase 3 es solo descripción)

4. **Consultoría Especializada:**
   - Auditoría de seguridad externa
   - Consultoría de arquitectura de datos avanzada (Data Mesh, etc.)
   - Consultoría de Machine Learning / Data Science (para Fase 3 futura)

5. **Servicios post go-live (opcionales):**
   - Evolutivos o nuevos requerimientos posteriores al proyecto
   - Monitoreo y operación a demanda
   - Mantenimiento evolutivo (nuevas funcionalidades post-proyecto)

6. **Cambios de Alcance Mayores:**
   - Cambios que requieran > 10 horas adicionales de desarrollo
   - Rediseño de arquitectura por cambios en requerimientos

**Proceso para Cotización Adicional:**
- Solicitud formal por escrito (email o Change Request)
- Aunergia evaluará esfuerzo y entregará cotización en 5 días hábiles
- Requiere aprobación de Product Owner antes de iniciar

---

### 12.4.5. Garantías y Compromisos

#### Garantías de Aunergia:

✅ **Calidad de Entregables:**
- Dashboards funcionales y sin errores críticos (bloqueantes)
- Datos validados con precisión > 95% vs. SAP
- Documentación completa y comprensible
- Código limpio y documentado (buenas prácticas)

✅ **Cumplimiento de Cronograma:**
- Esfuerzo razonable para cumplir plazos estimados
- Si retrasos por causa de Aunergia > 2 semanas: Sin costo adicional de horas extras
- Si retrasos por causa de Elanco (ej. permisos): Extensión de plazo sin penalización

✅ **Post Go-Live:**
- Ajustes menores y corrección de bugs evaluados y planificados caso a caso

✅ **Confidencialidad:**
- NDA (Non-Disclosure Agreement) vigente
- Datos de Elanco tratados con confidencialidad
- No compartir información con terceros sin autorización

#### Responsabilidades de Elanco:

✅ **Provisión de Accesos:**
- Permisos SAP, BigQuery, Power BI en plazos acordados (ver sección 10)

✅ **Disponibilidad de Stakeholders:**
- Participación en workshops, validaciones, UAT (4-6h/semana)

✅ **Infraestructura:**
- Provisión de BigQuery datasets, ambientes, conectividad

✅ **Pagos:**
- Pagos en plazo según esquema de hitos (15 días hábiles)

✅ **Documentación Base:**
- Entregar documentación SAP, procesos, diccionario de datos (Fase 0)

---

### 12.4.6. Política de Cambios (Change Management)

**Cambios Menores (< 10 horas esfuerzo):**
- Se evalúan dentro del buffer de proyecto
- Requieren aprobación de PM (Linda López)
- Se documentan en minutas

**Cambios Mayores (> 10 horas esfuerzo):**
- Requieren Change Request formal
- Aunergia evalúa impacto en esfuerzo adicional y extensión de plazo
- Requieren aprobación escrita de Product Owner
- Se negocian comercialmente por separado

**Procedimiento de Change Request:**
1. Stakeholder solicita cambio (por escrito)
2. Linda López evalúa impacto (horas, costo, plazo)
3. Aunergia emite cotización (dentro de 5 días hábiles)
4. Product Owner aprueba o rechaza
5. Si aprueba: Se actualiza contrato/cronograma
6. Se ejecuta cambio

---

### 12.4.7. Criterios de Aceptación

**Criterios para Aprobar Entregables:**

✅ **Fase 0 (Go/No-Go):**
- Mínimo 12 transacciones viables identificadas
- Arquitectura técnicamente factible
- Riesgos ALTO mitigables
- Backlog priorizado y aceptado por Product Owner

✅ **Fase 1 (Data Lake):**
- Datos cargados en BigQuery con completitud > 95%
- Validación cruzada con SAP aprobada por Lucía
- Pipelines ETL corriendo automáticamente sin errores críticos
- Documentación técnica completa

✅ **Fase 2 (Dashboards):**
- 12 dashboards publicados y funcionales
- UAT aprobado por stakeholders (firmado)
- Capacitaciones completadas (mínimo 12 usuarios capacitados)
- Tiempos de carga < 10 segundos

✅ **Fase 3 (Propuesta Predictiva):**
- Documento con 8 casos de uso descritos
- Estimaciones de esfuerzo por caso de uso
- Aprobado por Product Owner

**Proceso de Aceptación:**
1. Aunergia entrega entregable
2. Elanco tiene 5 días hábiles para revisar y aprobar/rechazar
3. Si rechazado: Aunergia corrige en 3-5 días hábiles
4. Máximo 2 rondas de correcciones sin costo
5. Una vez aprobado: Se emite factura (si corresponde a hito)

---

### 12.4.8. Cláusulas de Terminación Anticipada

**Terminación por Elanco:**
- Elanco puede terminar el contrato en cualquier momento con notificación de 2 semanas
- Se paga por trabajo completado hasta la fecha (proporcional)
- Aunergia entrega todos los artefactos desarrollados hasta ese momento

**Terminación por Aunergia:**
- Solo por incumplimiento de Elanco (ej. falta de pago > 60 días, falta de accesos > 4 semanas)
- Notificación formal con 2 semanas de antelación
- Se factura trabajo completado

**Terminación por NO-GO (Fase 0):**
- Si al final de Fase 0 se decide NO-GO, el proyecto se detiene
- Se factura solo el esfuerzo de Fase 0 (116 horas)
- No hay penalizaciones para ninguna parte

---

### 12.4.9. Propiedad Intelectual

**Código y Artefactos Desarrollados:**
- Propiedad de **Elanco Animal Health** al completar el pago del 100%
- Aunergia transfiere todos los derechos de uso, modificación, distribución

**Conocimiento y Metodologías:**
- Aunergia retiene derechos sobre metodologías propias, frameworks, templates genéricos
- Aunergia puede usar conocimiento general adquirido en futuros proyectos (sin revelar datos confidenciales de Elanco)

**Código Open Source:**
- Si se utiliza código open source, se respetan sus licencias (MIT, Apache, etc.)
- Se documenta en repositorio Git

---

### 12.4.10. Ley Aplicable y Resolución de Conflictos

**Ley Aplicable:**
- Contrato regido por leyes de [PAÍS - A definir según ubicación de Elanco CASA]

**Resolución de Conflictos:**
- Primera instancia: Negociación directa entre Linda López (PM) y Product Owner
- Segunda instancia: Mediación entre Management de ambas partes
- Tercera instancia: Arbitraje según leyes locales

---

### 12.4.11. Contactos del Proyecto

**Por Aunergia:**
- **Project Manager:** Linda López  
  Email: linda.lopez@aunergia.com | Tel: [TBD]

- **Technical Lead:** Juan Manuel Bigi  
  Email: jmbigi@aunergia.com | Tel: [TBD]

**Por Elanco:**
- **Product Owner:** [A DESIGNAR]  
  Email: [TBD] | Tel: [TBD]

- **TI TechOps:** David Saboya  
  Email: david.saboya@network.elancoah.com | Tel: [TBD]

---

### 12.4.12. Anexos Contractuales

Los siguientes documentos forman parte integral del contrato:

1. ✅ Esta propuesta completa (Documentos 00-12)
2. ✅ Cronograma semanal detallado (Documento 09)
3. ✅ Estimación de esfuerzos y costos (Documento 08)
4. ✅ NDA (Non-Disclosure Agreement) - Si no existe, a firmar
5. ✅ Orden de Compra de Elanco o Carta de Intención
6. ✅ Anexo de licencias Power BI (Orden PR-55219)

---

## 12.5. Términos de Soporte Post Go-Live

### 12.5.1. Soporte Incluido (Primeros 30 Días)

**Período:** 20-abr-2026 al 20-may-2026

**Alcance del Soporte:**
- ✅ Corrección de bugs identificados en go-live o durante uso
- ✅ Ajustes menores a dashboards (sin cambio de alcance)
- ✅ Troubleshooting de errores en pipelines ETL
- ✅ Soporte a usuarios (consultas sobre uso de dashboards)
- ✅ Sesiones de capacitación de refuerzo (si necesarias)

**SLA (Service Level Agreement):**
- **Horario:** Lunes a Viernes, 9:00 AM - 6:00 PM (GMT-3 o GMT-5)
- **Tiempo de Respuesta:** 24-48 horas para consultas
- **Tiempo de Resolución:**
  - Bugs críticos (bloqueantes): 48 horas
  - Bugs no críticos: 5 días hábiles
  - Consultas: Respuesta en 24-48 horas

**Canales de Soporte:**
- Email: soporte-elanco@aunergia.com
- MS Teams / Slack (si canal habilitado)
- Reunión semanal de seguimiento (1 hora)

**Exclusiones:**
- Nuevas funcionalidades (requieren cotización)
- Cambios de alcance mayores (requieren Change Request)
- Soporte fuera de horario laboral (24/7)

---

### 12.5.2. Soporte Extendido (Opcional - Post 30 Días)

**Modalidad 1: Soporte On-Demand (Pay-per-Use)**
- A cotizar según necesidad
- Sin compromiso mínimo
- Facturación mensual por horas consumidas
- Ideal para: Soporte esporádico, pequeños ajustes

**Modalidad 2: Retainer Mensual**
- Paquete: Horas mensuales acordadas
- Incluye: Soporte continuo, pequeñas mejoras, monitoreo
- Ideal para: Mantenimiento evolutivo, nuevas transacciones

**Modalidad 3: Proyecto de Fase 3 (Modelos Predictivos)**
- Implementación completa de modelos de ML
- Cotización por separado según alcance específico
- Duración estimada: 12-16 semanas

---

## 12.6. Firma y Aceptación

**PROPUESTA VÁLIDA POR:** 30 días desde la fecha de emisión (hasta 10-dic-2025)

**EMISIÓN DE PROPUESTA:**
- **Fecha:** [Fecha actual]
- **Versión:** 1.0 - Propuesta Final

**PREPARADO POR:**

---

**Linda López**  
Project Manager  
Aunergia S.A.  
Email: linda.lopez@aunergia.com

---

**ACEPTACIÓN POR ELANCO:**

Al firmar abajo, Elanco Animal Health acepta los términos y condiciones de esta propuesta y autoriza a Aunergia a iniciar el proyecto.

---

**Firma:** ________________________________  
**Nombre:** ________________________________  
**Cargo:** ________________________________  
**Fecha:** ________________________________

---

## 12.7. Próximos Pasos

Una vez aceptada esta propuesta:

1. ✅ **Firma de Contrato:** Aunergia preparará contrato formal (3-5 días hábiles)
2. ✅ **Acuerdo Comercial:** Definir términos de facturación basados en 1,590 horas de esfuerzo
3. ✅ **Kick-off Meeting:** Programar para 1-dic-2025 (2-3 horas)
4. ✅ **Solicitud de Accesos:** Iniciar trámites de permisos SAP, BigQuery, Power BI
5. ✅ **Inicio Fase 0:** 1-dic-2025 (Semana 0)

---

**¡Gracias por confiar en Aunergia para este proyecto estratégico!**

Estamos entusiasmados de trabajar junto a Elanco en la transformación digital de sus procesos de análisis de datos.

---

*Fin del documento. [Volver al índice](README.md)*
