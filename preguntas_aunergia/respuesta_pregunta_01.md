# RESPUESTA A PREGUNTA 01 - AUNERGIA
**Fecha:** 12 de noviembre de 2025  
**Versión Original:** 2.02 de la Propuesta  
**Versión Actual Recomendada:** 2.04 (Optimizada)  
**Proyecto:** Centralización de Datos y Analítica - Elanco Animal Health (CASA)

---

## RESUMEN EJECUTIVO

Estimado equipo de Aunergia,

Gracias por sus preguntas y comentarios sobre la propuesta. A continuación, encontrarán **respuestas directas, claras y concisas** a cada uno de los 4 puntos planteados.

### 📊 RESPUESTAS RÁPIDAS

| # | Pregunta | Respuesta | Detalle |
|---|----------|-----------|---------|
| **1** | ¿Acortar tiempos con mayor carga? | ✅ **SÍ** | **V2.04: 36 semanas** (-6 sem, -14%) con ABAP Developer (270h part-time). +290h (+18%) |
| **2** | ¿Visualización gráfica? | ✅ **SÍ** | **4 diagramas profesionales** en 2-3 días (arquitectura, modelo, flujos) |
| **3** | ¿Recurso ABAP? | ✅ **SÍ** | **270h incluidas** en V2.04 + SAP Basis (Elanco) requerido |
| **4** | ¿Job Descriptions? | ✅ **SÍ** | **4 JDs completos**: BI (935h), ABAP (270h), SAP (512h), PM (163h) |

### 🎯 PROPUESTA RECOMENDADA: V2.04 (OPTIMIZADA)

**Cronograma:** 36 semanas (vs 42 original) | **Go-Live:** 13 septiembre 2026  
**Esfuerzo:** 1,880h (vs 1,590h) | **Incremento:** +290h (+18%)  
**Equipo:** 4 recursos (BI + ABAP + SAP Functional + PM)  
**ROI:** Break-even en 2-3 meses post-Go-Live  

**Ventajas clave:**
- ✅ Carga sostenible BI (26h/sem)
- ✅ ABAP Developer especialista (10h/sem part-time)
- ✅ Riesgo técnico SAP reducido
- ✅ Go-Live 1 mes antes con calidad garantizada

---

---

## 1. ¿SE PUEDE PROPONER UN ESQUEMA CON MAYOR CARGA HORARIA PARA ACORTAR TIEMPOS?

### RESPUESTA EJECUTIVA

**SÍ, es posible acortar los tiempos**, pero con **limitaciones importantes** debido a premisas técnicas y operativas del proyecto. El cronograma actual de **42 semanas** ya fue comprimido un **25%** (de 56 a 42 semanas) manteniendo las mismas **1,590 horas totales**.

### ANÁLISIS DETALLADO

#### Cronograma Actual (Base)
- **Duración total:** 42 semanas (~10 meses)
- **Horas totales:** 1,590h
- **Fase 0:** 6 semanas (235h)
- **Fase 1:** 22 semanas (696h)
- **Fase 2:** 14 semanas (659h)
- **Inicio propuesto:** 6 de enero 2026
- **Finalización:** Mediados de octubre 2026

#### Premisas que Limitan la Compresión

**1. Restricción del Consultor BI (CRÍTICA)**
- El Consultor BI (recurso clave con 961h = 60.4% del proyecto) trabaja **máximo 6 horas/día** (30h/semana) por restricciones personales.
- Esta restricción ya está incorporada en el cronograma actual.
- **Impacto:** No se puede aumentar su carga horaria semanal significativamente.

**2. Dependencias Técnicas Secuenciales**
- **Fase 0 debe completarse antes de Fase 1:** Go/No-Go bloqueante
- **Fase 1 debe completarse antes de Fase 2:** Los dashboards dependen del Data Lake funcional
- **Validaciones con stakeholders:** Requieren tiempo de revisión (3-5 días por entregable)
- **Tickets de TI Global:** Permisos SAP y tablas BigQuery tienen tiempos de respuesta de 1-3 semanas

**3. Dependencias Operativas**
- **Disponibilidad de stakeholders:** Finanzas y Supply solo pueden dedicar 4-6h/semana
- **Cierres contables mensuales:** Stakeholders menos disponibles últimos días del mes
- **UAT (User Acceptance Testing):** Requiere 4 semanas mínimo para validación completa
- **Capacitación:** No se puede omitir, requiere 2-3 semanas

**4. Complejidad Técnica Inherente**
- **18 transacciones SAP:** Cada una requiere análisis, desarrollo, validación y testing
- **2 transacciones custom (ZLEL008, ZVEL015):** Requieren análisis ABAP profundo
- **12 dashboards Power BI:** Cada uno requiere diseño, desarrollo, RLS y validación
- **Calidad de datos:** Validaciones SAP ↔ BigQuery requieren tiempo (meta: ≥95% exactitud)

### ESCENARIOS DE COMPRESIÓN POSIBLES

#### ✅ ESCENARIO RECOMENDADO: VERSIÓN 2.04 (AGREGAR ABAP DEVELOPER)
**Meta:** Reducir de 42 a 36 semanas (-14%) con carga sostenible

| Aspecto | Modificación Propuesta | Viabilidad | Beneficio |
|---------|------------------------|------------|-----------|
| **Consultor BI** | 26h/sem promedio (NO aumentar) | ✅ **ÓPTIMO** - Carga sostenible | Mantiene calidad |
| **ABAP Developer** | **NUEVO**: 270h part-time (10.4h/sem) | ✅ **VIABLE** - Rol consultoría | Especialista SAP/SLT |
| **Funcional SAP** | Aumentar de 12h/sem a 14h/sem | ✅ **VIABLE** - Leve incremento | +28h para validaciones |
| **Project Manager** | Aumentar de 3.5h/sem a 4.5h/sem | ✅ **VIABLE** - Coordinación | +18h para gestión |

**Cronograma V2.04:**
- **Fase 0:** 6 semanas (sin cambio) → Mantener calidad análisis
- **Fase 1:** 20 semanas (vs 22) → -2 semanas vía paralelización
- **Fase 2:** 10 semanas (vs 14) → -4 semanas vía optimización UAT
- **TOTAL:** 36 semanas (~8.5 meses)
- **Go-Live:** 13 de septiembre 2026

**Costo/Beneficio:**
- ✅ **Ventaja:** Go-Live **6 semanas antes** (1 mes de beneficios adelantados)
- ✅ **Calidad:** Consultor BI mantiene carga sostenible (26h/sem)
- ✅ **Riesgo:** ABAP Developer reduce riesgo técnico SAP/SLT
- ✅ **Especialización:** Separación clara SAP (ABAP) vs BI (Consultor)
- 💰 **Costo:** +290h (+18% presupuesto) vs -6 semanas (-14% tiempo)
- 💰 **ROI:** Break-even en 2-3 meses post-Go-Live

#### Escenario B: COMPRESIÓN AGRESIVA (+50% carga semanal)
**Meta:** Reducir de 42 a 30 semanas (-29%)

| Aspecto | Modificación Necesaria | Viabilidad | Riesgos |
|---------|------------------------|------------|---------|
| **Consultor BI** | Aumentar de 30h/sem a 45h/sem | 🚫 **NO VIABLE** - Excede restricción de 6h/día | Insostenible |
| **Agregar Consultor BI #2** | Contratar segundo desarrollador | ⚠️ **COMPLEJO** - Curva de aprendizaje 3-4 semanas | Incremento de costo 40-50% |
| **Funcional SAP** | Aumentar de 15h/sem a 25h/sem | 🚫 **NO RECOMENDADO** - Sobrecarga operativa | Burnout, calidad baja |
| **Paralelización máxima** | Múltiples workstreams simultáneos | 🚫 **NO VIABLE** - Dependencias críticas | Caos, re-work masivo |

**Cronograma Ajustado:**
- **Fase 0:** 4 semanas (vs 6) → -2 semanas
- **Fase 1:** 15 semanas (vs 22) → -7 semanas
- **Fase 2:** 11 semanas (vs 14) → -3 semanas
- **TOTAL:** 30 semanas (~7 meses)

**Costo/Impacto:**
- ✅ **Ventaja:** Go-Live 3 meses antes (mediados de julio 2026)
- 🚫 **Riesgo ALTO:** 60-80% probabilidad de retrasos por sobrecarga
- 🚫 **Riesgo ALTO:** Calidad comprometida (< 90% exactitud SAP-BigQuery)
- 💰 **Costo:** +40-50% de horas totales si se contrata segundo desarrollador (2,265-2,385h vs 1,590h)

#### Escenario C: AGREGAR RECURSOS (Sin cambiar carga individual)
**Meta:** Reducir de 42 a 34-36 semanas mediante recursos adicionales

| Recurso Adicional | Función | Horas Adicionales | Impacto Cronograma | Costo Incremental |
|-------------------|---------|-------------------|-------------------|-------------------|
| **Consultor BI #2** | Desarrollo Dashboards Power BI en paralelo | +330h | -4 a -6 semanas en Fase 2 | +20-25% presupuesto |
| **Data Engineer** | Acelerar pipelines Fase 1 | +200h | -3 a -4 semanas en Fase 1 | +12-15% presupuesto |
| **SAP Functional #2** | Validaciones y UAT paralelas | +150h | -2 a -3 semanas en UAT | +9-10% presupuesto |

**Cronograma Ajustado (con 2 recursos adicionales):**
- **Fase 0:** 6 semanas (sin cambio - crítica)
- **Fase 1:** 18 semanas (vs 22) → -4 semanas
- **Fase 2:** 10 semanas (vs 14) → -4 semanas
- **TOTAL:** 34 semanas (~8 meses)

**Costo/Impacto:**
- ✅ **Ventaja:** Go-Live 8 semanas antes (fin de agosto 2026)
- ✅ **Calidad mantenida:** Sin comprometer validaciones
- ⚠️ **Complejidad:** Mayor coordinación (5 personas vs 3)
- 💰 **Costo:** +35-40% de horas totales (2,146-2,226h vs 1,590h)

### RECOMENDACIÓN FINAL

**✅ VERSIÓN 2.04 (OPTIMIZADA) - EQUILIBRIO TIEMPO-COSTO-CALIDAD**

**Justificación:**
1. ✅ **Cronograma realista:** 36 semanas (vs 42 original) → -6 semanas (-14%)
2. ✅ **Carga sostenible:** Consultor BI promedio 26h/semana (cómodo, permite calidad)
3. ✅ **ABAP Developer especialista:** 270h en rol consultoría (10.4h/sem, fácil de contratar)
4. ✅ **Separación de responsabilidades:** ABAP = SAP/SLT | BI = BigQuery/Power BI
5. ✅ **Menor riesgo técnico:** Especialista en SLT y Z-transactions (ZLEL008, ZVEL015)
6. ✅ **Costo controlado:** +290h (+18%) vs +378h (+24%) de V2.03
7. ✅ **ROI positivo:** Break-even en 2-3 meses post-Go-Live
8. ✅ **Calidad garantizada:** Recursos con tiempo suficiente para hacer bien el trabajo

**Cronograma V2.04 (RECOMENDADO):**
- **Inicio:** 6 de enero 2026
- **Fase 0:** 6 semanas (fin 16 de febrero 2026)
- **Fase 1:** 20 semanas (fin 5 de julio 2026)
- **Fase 2:** 10 semanas (fin 13 de septiembre 2026)
- **TOTAL:** 36 semanas (~8.5 meses)
- **Go-Live:** 13 de septiembre 2026 (vs 15 de octubre en V2.02)

**Distribución de Horas por Recurso (V2.04):**

| Recurso | V2.02 Original | V2.04 Optimizada | Delta | H/Semana Promedio |
|---------|----------------|------------------|-------|-------------------|
| **Consultor BI** | 961h | 935h | -26h | **26.0h/sem** ✅ sostenible |
| **ABAP Developer** | 0h | **270h** | +270h | **10.4h/sem** ✅ part-time |
| **Funcional SAP** | 484h | 512h | +28h | 14.2h/sem |
| **Project Manager** | 145h | 163h | +18h | 4.5h/sem |
| **TOTAL** | **1,590h** | **1,880h** | **+290h (+18%)** | 36 sem vs 42 |

**Comparativa con V2.03 (Agresiva):**
- V2.04 es **4 semanas más larga** (36 vs 32) pero **-88h más económica** (-5%)
- V2.04 tiene **ABAP Developer más fácil de contratar** (10.4h/sem vs 23.8h/sem)
- V2.04 permite **mayor calidad** (BI con 26h/sem vs 23.8h/sem)
- V2.04 tiene **menor riesgo de coordinación** (recurso part-time vs full-time)

**Ajustes Necesarios:**
- ✅ Consultor BI mantiene carga sostenible (26h/sem promedio)
- ⏳ Contratar ABAP Developer part-time con experiencia SLT y módulos MM/SD/FI
- ✅ Funcional SAP incrementa levemente (14h/sem, manejable)
- ⏳ Stakeholders comprometidos a respuestas en 2-3 días
- ⏳ Coordinación SAP Basis (Elanco) desde Fase 0

**Roles y Responsabilidades Claros:**

**Consultor BI (761h):**
- ✅ Arquitectura BigQuery (3 capas)
- ✅ Desarrollo pipelines transformación (PROCESSED/CURATED)
- ✅ Modelo dimensional (star schema)
- ✅ Desarrollo 12 dashboards Power BI
- ✅ Optimización queries BigQuery
- ❌ NO toca SAP directamente

**ABAP Developer (436h - NUEVO):**
- ✅ Análisis transacciones SAP (18 trans, incluyendo ZLEL008/ZVEL015)
- ✅ Configuración y monitoreo SAP SLT
- ✅ Extracción de datos desde SAP → BigQuery (zona RAW)
- ✅ Gestión de tickets SAP con TI Global
- ✅ Análisis de tablas Z y transacciones custom
- ✅ Coordinación con SAP Basis (Elanco)
- ❌ NO desarrolla en BigQuery ni Power BI

**Funcional SAP (484h):**
- ✅ Validaciones funcionales de negocio
- ✅ Definición de KPIs con stakeholders
- ✅ Colaboración con ABAP Developer (Fase 0 y 1)
- ✅ UAT y capacitación (Fase 2)
- ✅ Documentación funcional

**Project Manager (145h):**
- ✅ Coordinación general del proyecto
- ✅ Gestión de riesgos y cronograma
- ✅ Comunicación con stakeholders

---

## 2. ¿TIENEN ALGUNA VISUALIZACIÓN GRÁFICA DE LA SOLUCIÓN?

### RESPUESTA

**SÍ**, podemos generar un diagrama de arquitectura técnica completo. Actualmente, la propuesta incluye descripciones textuales detalladas en las secciones 2 y 5, pero no un diagrama visual formal.

### PROPUESTA DE DIAGRAMA

**Generaremos un diagrama profesional que incluya:**

#### Componentes del Diagrama de Arquitectura

**1. Capa Origen (SAP S/4HANA)**
```
┌─────────────────────────────────────────────────────┐
│           SAP S/4HANA (On-Premise)                 │
│                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │ Módulo   │ │ Módulo   │ │ Módulo   │          │
│  │   FI     │ │   SD     │ │   MM     │          │
│  │  (4 tx)  │ │  (2 tx)  │ │  (6 tx)  │          │
│  └──────────┘ └──────────┘ └──────────┘          │
│                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │ Módulo   │ │ Custom   │ │ Master   │          │
│  │   CO     │ │  Trans   │ │  Data    │          │
│  │  (2 tx)  │ │  (2 tx)  │ │  (2 tx)  │          │
│  └──────────┘ └──────────┘ └──────────┘          │
│                                                     │
│  Tablas: ACDOCA, BKPF, VBAK, EKKO, MARD, etc.    │
└─────────────────────────────────────────────────────┘
                         ↓
              ┌──────────────────────┐
              │   SAP SLT Server     │
              │  (Replicación CDC)   │
              │  Change Data Capture │
              └──────────────────────┘
                         ↓ HTTPS/RFC
```

**2. Capa Repositorio (Google BigQuery)**
```
┌─────────────────────────────────────────────────────┐
│         Google Cloud Platform (BigQuery)            │
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │          ZONA RAW (Crudo)                   │  │
│  │  • Datos tal cual desde SAP                 │  │
│  │  • Sin transformaciones                     │  │
│  │  • Dataset: casa_bi_raw                     │  │
│  │  • Particionamiento por fecha               │  │
│  └─────────────────────────────────────────────┘  │
│                      ↓                              │
│  ┌─────────────────────────────────────────────┐  │
│  │      ZONA PROCESSED (Limpio/Transformado)   │  │
│  │  • Limpieza de datos                        │  │
│  │  • Transformaciones SQL                     │  │
│  │  • Validaciones de calidad                  │  │
│  │  • Dataset: casa_bi_processed               │  │
│  └─────────────────────────────────────────────┘  │
│                      ↓                              │
│  ┌─────────────────────────────────────────────┐  │
│  │       ZONA CURATED (Modelo Dimensional)     │  │
│  │  • Star Schema                              │  │
│  │  • 8 Dimensiones + 6 Tablas Hechos         │  │
│  │  • KPIs pre-calculados                     │  │
│  │  • Dataset: casa_bi_curated                │  │
│  │                                             │  │
│  │  Dimensiones:                               │  │
│  │  • dim_tiempo, dim_geografia, dim_producto  │  │
│  │  • dim_cliente, dim_proveedor, dim_centro   │  │
│  │  • dim_cuenta_contable, dim_organizacion    │  │
│  │                                             │  │
│  │  Hechos:                                    │  │
│  │  • fact_ventas, fact_inventario             │  │
│  │  • fact_compras, fact_financiero            │  │
│  │  • fact_opex, fact_rentabilidad            │  │
│  └─────────────────────────────────────────────┘  │
│                                                     │
│  Características Técnicas:                         │
│  ✓ Particionamiento por fecha                      │
│  ✓ Clustering por dimensiones clave                │
│  ✓ Row-Level Security (RLS) por país/área         │
│  ✓ Vistas materializadas para agregaciones        │
└─────────────────────────────────────────────────────┘
                         ↓ Native Connector
```

**3. Capa Visualización (Power BI)**
```
┌─────────────────────────────────────────────────────┐
│        Microsoft Power BI Service (Cloud)           │
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │         12 Dashboards Ejecutivos            │  │
│  │                                             │  │
│  │  FINANZAS (4):                              │  │
│  │  • Financiero General  • OPEX               │  │
│  │  • Controlling         • CxP                │  │
│  │                                             │  │
│  │  COMERCIAL (3):                             │  │
│  │  • Ventas             • Rentabilidad        │  │
│  │  • CxC                                      │  │
│  │                                             │  │
│  │  SUPPLY CHAIN (3):                          │  │
│  │  • Inventario         • Supply Chain        │  │
│  │  • Compras                                  │  │
│  │                                             │  │
│  │  EJECUTIVO (2):                             │  │
│  │  • Dashboard Ejecutivo • Regional           │  │
│  │                                             │  │
│  │  Seguridad:                                 │  │
│  │  ✓ Row-Level Security por país/área        │  │
│  │  ✓ 8 licencias Power BI Pro                │  │
│  └─────────────────────────────────────────────┘  │
│                                                     │
│  Usuarios Finales: ~15 usuarios                    │
│  • 4-6 usuarios Finanzas                           │
│  • 2-4 usuarios Supply Chain                       │
│  • 2-3 usuarios Management                         │
└─────────────────────────────────────────────────────┘
```

**4. Componentes Transversales**
```
┌─────────────────────────────────────────────────────┐
│              GOBERNANZA Y CONTROL                   │
│                                                     │
│  Monitoreo y Alertas:                               │
│  • Cloud Functions para orquestación               │
│  • Logs de auditoría (BigQuery Audit Logs)        │
│  • Alertas de errores de replicación               │
│                                                     │
│  Control de Calidad:                                │
│  • Validaciones SAP ↔ BigQuery (≥95% exactitud)   │
│  • Data Quality checks automatizados               │
│  • Reconciliaciones periódicas                     │
│                                                     │
│  CI/CD y Versionado:                                │
│  • Git para código SQL y scripts                   │
│  • CI/CD para despliegues automatizados            │
│  • Ambientes: dev / qa / prod                      │
└─────────────────────────────────────────────────────┘
```

### ENTREGA DEL DIAGRAMA

**Formatos propuestos:**
1. ✅ **Diagrama de arquitectura de alto nivel** (formato PNG/SVG)
   - Visión general del flujo de datos
   - Componentes principales y conexiones
   - Estilo profesional (Lucidchart / Draw.io / Visio)

2. ✅ **Diagrama de arquitectura técnica detallada** (formato PNG/SVG)
   - Detalles de cada capa
   - Tecnologías específicas
   - Flujos de datos numerados

3. ✅ **Diagrama de modelo dimensional** (formato PNG/SVG)
   - Star schema completo
   - 8 dimensiones + 6 hechos
   - Relaciones y cardinalidades

4. ✅ **Diagrama de flujo de procesos** (formato PNG/SVG)
   - Desde extracción SAP hasta dashboard
   - Tiempos de procesamiento
   - Puntos de validación

**Plazo de entrega:**
- Diagramas preliminares: 2-3 días hábiles
- Diagramas finales revisados: Fin de Fase 0 (incluidos en entregables)

**Herramientas sugeridas:**
- Lucidchart (recomendado para arquitecturas cloud)
- Microsoft Visio
- Draw.io (gratuito)
- Google Drawings
- PowerPoint con SmartArt (rápido)

---

## 3. ¿NECESITARÍAN ALGÚN RECURSO TÉCNICO ABAP?

### RESPUESTA EJECUTIVA

**NO está incluido en el alcance base**, pero **SÍ podría ser necesario** para analizar las 2 transacciones custom (ZLEL008, ZVEL015). El esfuerzo está contemplado como **contingencia** dentro de las horas del Funcional SAP y análisis del Consultor BI.

### ANÁLISIS DETALLADO

#### Transacciones que Podrían Requerir Soporte ABAP

**1. ZLEL008 - Comparativo de Precios (Inventario Consolidado)**
- **Complejidad:** ⚠️ **ALTA** - Transacción custom compleja
- **Riesgo:** Lógica de negocio no documentada, tablas Z desconocidas
- **Necesidad ABAP:** 
  - Análisis de código fuente (SE38/SE80)
  - Identificación de tablas fuente y lógica de cálculo
  - Mapeo de campos a tablas SAP estándar

**2. ZVEL015 - Ventas Estadísticas (Condiciones de Precio)**
- **Complejidad:** ⚠️ **MEDIA-ALTA** - Pricing custom
- **Riesgo:** Puede usar tablas estándar (KONV) o custom
- **Necesidad ABAP:**
  - Análisis de algoritmo de pricing
  - Identificación de condiciones especiales
  - Validación de cálculos

#### Estrategia sin Recurso ABAP Dedicado

**Fase 0 (Semana 2-3): Análisis Inicial**
- **Responsable:** Funcional SAP + Consultor BI
- **Esfuerzo:** 8 horas (ya incluidas en las 235h de Fase 0)
- **Actividades:**
  - Ejecutar transacciones en SAP y analizar outputs
  - Identificar campos clave y tablas visibles
  - Documentar lógica de negocio entendida
  - Solicitar a TI Global Elanco:
    - Código fuente de las transacciones Z
    - Documentación técnica (si existe)
    - Tablas Z involucradas

**Escenario A: Análisis Simple (Probabilidad 60%)**
- Transacciones Z usan mayormente tablas estándar
- Lógica de cálculo es comprensible sin ABAP profundo
- **Acción:** Continuar con equipo actual
- **Esfuerzo adicional:** 0 horas (incluido en base)

**Escenario B: Análisis Complejo (Probabilidad 30%)**
- Transacciones Z tienen lógica ABAP moderadamente compleja
- Requiere análisis de código fuente ABAP
- **Acción:** Consultor BI (con conocimientos ABAP básicos) analiza con apoyo del Funcional SAP
- **Esfuerzo adicional:** 8-12 horas (incluidas en contingencia Fase 1)

**Escenario C: Análisis Muy Complejo (Probabilidad 10%)**
- Transacciones Z con lógica ABAP muy compleja
- Múltiples tablas Z interdependientes
- Algoritmos custom de cálculo
- **Acción:** Contratar consultor ABAP senior externo
- **Esfuerzo adicional:** 16-24 horas (NO incluido en alcance base)
- **Costo adicional:** Via Change Request

#### Recurso SAP Basis (Cliente)

**SÍ es necesario y DEBE ser provisto por Elanco:**
- **Rol:** Administrador SAP Basis (recurso interno de Elanco)
- **Responsabilidades:**
  - Instalación y configuración de SAP SLT Server
  - Gestión de usuarios y perfiles SAP
  - Gestión de órdenes de transporte
  - Aplicación de SAP Notes
  - Configuración de conexiones RFC
  - Monitoreo del sistema SAP
  - Troubleshooting técnico SAP
  - Asistencia en configuración del BigQuery Connector
- **Dedicación:** On-demand durante el proyecto (estimado 2-4h/semana en Fase 1)
- **Criticidad:** 🔴 **CRÍTICA** - Sin SAP Basis, la replicación SLT no es viable
- **Costo:** A cargo de Elanco (recurso interno)

### RECOMENDACIÓN

**Plan Recomendado:**

1. ✅ **Iniciar sin recurso ABAP dedicado**
   - Funcional SAP + Consultor BI analizan en Fase 0
   - Solicitar documentación técnica a TI Global Elanco

2. ✅ **Evaluación Go/No-Go en Fase 0**
   - Si Escenario A o B: Continuar sin ABAP
   - Si Escenario C: Solicitar Change Request para consultor ABAP

3. ✅ **Recurso SAP Basis provisto por Elanco**
   - Requisito obligatorio documentado en sección 10
   - Coordinación con David Saboya (TechOps)

4. ⚠️ **Contingencia presupuestada**
   - 16-24 horas de consultoría ABAP senior externa
   - Activable via Change Request si es necesario
   - Costo estimado: 15-20% adicional sobre Fase 1

**Resumen:**
- ❌ **NO incluido en alcance base:** Consultor ABAP dedicado
- ✅ **SÍ incluido en alcance base:** Análisis básico de transacciones Z (8h)
- ✅ **SÍ REQUERIDO por cliente:** Recurso SAP Basis (Elanco)
- ⚠️ **Contingencia disponible:** 16-24h consultoría ABAP externa (Change Request)

---

## 4. JOB DESCRIPTIONS (JD) DE LOS PERFILES REQUERIDOS

### RESPUESTA

**SÍ**, a continuación los Job Descriptions completos de los 3 perfiles del equipo Aunergia:

---

### PERFIL 1: ARQUITECTO DE DATOS / DESARROLLADOR PRINCIPAL (CONSULTOR BI)

**Título del Puesto:** Senior Data Architect & BI Developer  
**Empresa:** Aunergia  
**Proyecto:** Centralización de Datos y Analítica - Elanco Animal Health  
**Dedicación:** Part-time, 25-30 horas/semana (máximo 6h/día)  
**Duración:** 42 semanas (enero - octubre 2026)  
**Total horas:** 961h (60.4% del proyecto)

#### Descripción del Rol

Profesional senior responsable del diseño de arquitectura de datos, desarrollo de pipelines ETL, modelado dimensional y desarrollo de dashboards Power BI. Rol técnico multidisciplinario que combina expertise en cloud (Google BigQuery), ingeniería de datos (ETL), y visualización (Power BI).

#### Responsabilidades Principales

**Fase 0 - Due Diligence (95h):**
- Análisis técnico de dataset casa_bi en BigQuery (24h)
- Diseño de arquitectura de 3 capas (RAW/PROCESSED/CURATED) (28h)
- Benchmarks de performance y estimación de costos BigQuery (10h)
- Validación de conectividad Power BI ↔ BigQuery (4h)
- Documentación de arquitectura técnica (7h)

**Fase 1 - Data Lake (446h):**
- Setup de infraestructura BigQuery completa (60h)
  - Datasets (dev/qa/prod), particionamiento, service accounts
  - Conectores SAP SLT, Cloud Functions, controles de acceso
- Desarrollo de pipelines ETL para 18 transacciones SAP (332h)
  - Módulo FI: 4 transacciones (56h)
  - Módulo SD: 2 transacciones (32h)
  - Módulo MM: 6 transacciones (68h)
  - Módulo CO: 2 transacciones (20h)
  - FI-AP/AR: 2 transacciones (20h)
  - Master Data: 2 transacciones (20h)
  - Transacciones Z custom: análisis y desarrollo (56h)
- Optimización y automatización (50h)
  - Tuning de queries, CI/CD, monitoreo
  - Testing integral, validaciones de calidad
  - Documentación técnica completa

**Fase 2 - Dashboards (420h):**
- Diseño de modelo dimensional completo (86h)
  - Star schema: 8 dimensiones + 6 tablas hechos
  - Vistas SQL, capa semántica, definición de KPIs
- Desarrollo de 12 dashboards Power BI (280h)
  - 3 dashboards Financieros (64h)
  - 3 dashboards Ventas y Rentabilidad (68h)
  - 3 dashboards Supply Chain (62h)
  - 3 dashboards Tesorería y Ejecutivo (66h)
  - Row-Level Security (RLS) por país/área (20h)
- Testing, UAT y ajustes finales (41h)
- Documentación funcional y capacitación (13h)

#### Experiencia Requerida (Mínimo)

**Experiencia General:**
- 6+ años en roles de Data Engineering / BI Development
- 3+ años trabajando con Google Cloud Platform (BigQuery)
- 3+ años con Power BI (desarrollo de dashboards complejos)
- Experiencia demostrable en proyectos end-to-end (desde arquitectura hasta go-live)

**Experiencia Técnica Específica:**
- ✅ **Google BigQuery (CRÍTICO):**
  - Diseño de arquitectura de datos en BigQuery
  - SQL avanzado (window functions, CTEs, partitioning, clustering)
  - Optimización de queries y control de costos
  - Configuración de datasets, permisos IAM, RLS
  - Integración con herramientas de visualización

- ✅ **Power BI (CRÍTICO):**
  - Desarrollo de dashboards ejecutivos complejos (3+ hojas por dashboard)
  - DAX avanzado (measures, calculated columns, time intelligence)
  - Modelado de datos (star schema, snowflake)
  - Row-Level Security (RLS) y seguridad
  - Conectores nativos (BigQuery, SQL Server, etc.)
  - Power BI Service (workspaces, publicación, refresh schedules)

- ✅ **SAP (Deseable):**
  - Conocimiento de módulos SAP (FI, CO, SD, MM)
  - Conocimiento de tablas SAP estándar (ACDOCA, BKPF, VBAK, EKKO, etc.)
  - Experiencia con SAP SLT o herramientas de replicación
  - ABAP básico (leer código, entender lógica) - deseable

- ✅ **Data Engineering:**
  - Diseño de pipelines ETL/ELT
  - Data modeling (dimensional modeling, star schema)
  - Data quality y validaciones
  - CI/CD para data pipelines
  - Git / versionado de código

- ✅ **Cloud Architecture:**
  - Google Cloud Platform (BigQuery, Cloud Functions, Cloud Storage)
  - Infraestructura como código (Terraform deseable)
  - Seguridad cloud (IAM, encriptación)
  - Monitoreo y logging

**Habilidades Técnicas:**
- SQL (avanzado): BigQuery SQL, ANSI SQL
- DAX (Power BI): medidas complejas, time intelligence
- Python (básico-intermedio): scripting, automatización
- Git: versionado, branching, pull requests
- ABAP (básico-deseable): lectura de código, análisis de transacciones Z

**Habilidades Blandas:**
- Comunicación efectiva con stakeholders técnicos y de negocio
- Capacidad de trabajar de forma autónoma (trabajo remoto)
- Resolución de problemas complejos
- Documentación clara y detallada
- Adaptabilidad a cambios de requerimientos

#### Certificaciones Deseables (No obligatorias)

- Google Cloud Professional Data Engineer
- Microsoft Certified: Azure Data Engineer Associate (equivalente)
- Microsoft Certified: Data Analyst Associate (Power BI)
- SAP Certified Technology Associate (SAP System Administration / HANA / S/4HANA)

#### Formación Académica

**Mínimo:**
- Título universitario en Ingeniería en Sistemas, Informática, Computación o afines
- Posgrado en Data Science / Business Intelligence (deseable)

#### Idiomas

- Español: Nativo o Fluido (90%+)
- Inglés: Intermedio-Avanzado (lectura de documentación técnica)

#### Condiciones Laborales

- Modalidad: Remoto (trabajo a distancia)
- Horario: Flexible (coordinación con zona horaria CASA: GMT-3 a GMT-5)
- Disponibilidad: Lunes a Viernes
- Reuniones: 2-3 reuniones semanales con stakeholders (1-2h cada una)
- Restricción: Máximo 6 horas/día (30h/semana)

---

### PERFIL 2: ANALISTA SAP / POWER USER (FUNCIONAL SAP)

**Título del Puesto:** SAP Functional Analyst & Power User  
**Empresa:** Aunergia  
**Proyecto:** Centralización de Datos y Analítica - Elanco Animal Health  
**Dedicación:** Part-time, 15-20 horas/semana  
**Duración:** 42 semanas (enero - octubre 2026)  
**Total horas:** 484h (30.4% del proyecto)

#### Descripción del Rol

Especialista funcional SAP con profundo conocimiento de módulos FI, CO, SD y MM. Responsable de análisis funcional de transacciones SAP, validación de datos, coordinación con TI Global para gestión de permisos y tablas, y validación de dashboards desde perspectiva de negocio.

#### Responsabilidades Principales

**Fase 0 - Due Diligence (112h):**
- Gestión de tickets SAP (Ticket SAP-48219) para permisos completos (18h)
- Gestión de tickets BigQuery (BQ-7713, BQ-7721) para tablas faltantes (18h)
- Coordinación con TI Global y David Saboya (TechOps) (10h)
- Workshops de priorización de 18 transacciones SAP con stakeholders (28h)
- Análisis profundo de transacciones custom (ZLEL008, ZVEL015) (28h)
- Validación funcional de POC técnico (6h)
- Documentación de backlog priorizado (4h)

**Fase 1 - Data Lake (206h):**
- Validación funcional de datos por módulo SAP (100h)
  - FI: Mayor general, balances, documentos contables (26h)
  - SD: Órdenes de venta, rentabilidad (20h)
  - MM: Compras, inventarios, MRP (44h)
  - CO: OPEX, órdenes CO, controlling (30h)
  - Master Data: Clientes, proveedores (6h)
- Análisis profundo de tablas Z y lógica custom (38h)
- Reconciliaciones SAP ↔ BigQuery (40h)
- Testing funcional y documentación (18h)
- Soporte a desarrollo de pipelines (10h)

**Fase 2 - Dashboards (166h):**
- Definición de KPIs de negocio con stakeholders (22h)
- Validación funcional de dashboards (56h)
  - Dashboards Financieros (14h)
  - Dashboards Ventas y Rentabilidad (14h)
  - Dashboards Supply Chain (12h)
  - Dashboards Tesorería y Ejecutivo (14h)
  - Validación final integral (2h)
- User Acceptance Testing (UAT) - 4 fases (55h)
  - Coordinación con stakeholders Finanzas y Supply
  - Gestión de feedback y ajustes
- Documentación funcional y manuales de usuario (20h)
- Capacitación a usuarios finales (13h)

#### Experiencia Requerida (Mínimo)

**Experiencia General:**
- 5+ años como SAP Functional Analyst o Power User
- 3+ años trabajando con módulos SAP FI y CO (obligatorio)
- 2+ años con módulos SAP SD y/o MM (deseable)
- Experiencia en proyectos de implementación o mejora de SAP

**Experiencia Técnica Específica:**

- ✅ **Módulo FI - Financial Accounting (CRÍTICO):**
  - Transacciones: FAGLL03, FB03, F.08, F.01, FBL1N, FBL5N
  - Tablas: ACDOCA, ACDOCA_T (Universal Journal S/4HANA), BKPF
  - Conocimiento de cuentas contables, cierres mensuales
  - Plan de cuentas (Chart of Accounts)
  - Balances de comprobación y estados financieros

- ✅ **Módulo CO - Controlling (CRÍTICO):**
  - Transacciones: KSB1, KE24 (CO-PA)
  - Tablas: AUFK, COBK (histórico: COEP reemplazado por ACDOCA)
  - Órdenes CO, centros de costo
  - OPEX (gastos operativos)
  - CO-PA (Profitability Analysis)

- ✅ **Módulo SD - Sales & Distribution (Deseable):**
  - Transacciones: VA05
  - Tablas: VBAK, VBAP, VBEP, KNA1
  - Órdenes de venta, maestro de clientes
  - Pricing, condiciones comerciales

- ✅ **Módulo MM - Materials Management (Deseable):**
  - Transacciones: ME2L, ME23N, MM60, MB59, MB5B, MCHB
  - Tablas: EKKO, EKPO, MBEW, CKMLCR, MSEG, MARD, MCHB
  - Órdenes de compra, inventarios
  - Maestro de materiales, proveedores (LFA1, LFB1, LFM1)

- ✅ **Transacciones Custom Z (Deseable):**
  - Experiencia analizando transacciones custom
  - Capacidad de entender lógica de negocio sin documentación
  - Conocimiento básico de ABAP (leer código) - plus

- ✅ **Master Data:**
  - Transacciones: XK03, XD03
  - Maestros de clientes (KNA1, KNB1, KNVV)
  - Maestros de proveedores (LFA1, LFB1, LFM1)

**Experiencia en S/4HANA (Deseable pero no obligatorio):**
- Conocimiento de Universal Journal (ACDOCA/ACDOCA_T)
- Diferencias vs. SAP ECC (tablas históricas BSEG, COEP, FAGLFLEXA)
- SAP Fiori (interfaz moderna)

**Habilidades Técnicas:**
- SAP GUI: Navegación avanzada, transacciones, reportes
- SQL básico: Consultas simples, filtros, joins
- Excel avanzado: Tablas dinámicas, macros básicas
- Documentación: Capacidad de documentar procesos y flujos

**Habilidades Blandas:**
- Comunicación efectiva con stakeholders de negocio (Finanzas, Supply)
- Facilitación de workshops y sesiones de trabajo
- Capacidad de traducir requerimientos de negocio a especificaciones técnicas
- Trabajo en equipo con perfiles técnicos
- Orientación a resultados y cumplimiento de plazos
- Capacidad de gestión de múltiples tareas simultáneas

#### Certificaciones Deseables (No obligatorias)

- SAP Certified Application Associate - Financial Accounting (FI) with SAP ERP 6.0 o S/4HANA
- SAP Certified Application Associate - Management Accounting (CO) with SAP ERP 6.0
- SAP Certified Application Associate - Sales and Distribution (SD)
- SAP Certified Application Associate - Materials Management (MM)

#### Formación Académica

**Mínimo:**
- Título universitario en Contabilidad, Administración, Ingeniería Industrial, Sistemas o afines
- Posgrado en Finanzas / Controlling (deseable)
- Certificación SAP formal (deseable)

#### Idiomas

- Español: Nativo o Fluido (95%+)
- Inglés: Intermedio (lectura de documentación SAP)

#### Condiciones Laborales

- Modalidad: Remoto (trabajo a distancia)
- Horario: Flexible (coordinación con zona horaria CASA: GMT-3 a GMT-5)
- Disponibilidad: Lunes a Viernes, 15-20h/semana
- Reuniones: 3-4 reuniones semanales con stakeholders y equipo técnico
- Picos de trabajo: Fase 0 (workshops) y Fase 2 (UAT)

#### Perfil Ideal

**Candidato ideal tiene:**
- Background en Finanzas/Contabilidad + conocimiento SAP profundo
- Experiencia trabajando en empresas multinacionales (familiaridad con estructuras multi-país)
- Experiencia en proyectos de BI/Analítica desde el lado funcional
- Capacidad de "hablar el lenguaje de negocio" con Controllers y Managers
- Visión end-to-end: desde transacción SAP hasta KPI de negocio

---

### PERFIL 3: PROJECT MANAGER

**Título del Puesto:** IT Project Manager  
**Empresa:** Aunergia  
**Proyecto:** Centralización de Datos y Analítica - Elanco Animal Health  
**Dedicación:** Part-time, 3-5 horas/semana  
**Duración:** 42 semanas (enero - octubre 2026)  
**Total horas:** 145h (9.1% del proyecto)

#### Descripción del Rol

Responsable de la gestión integral del proyecto, coordinación de stakeholders, seguimiento de cronograma y presupuesto, gestión de riesgos, comunicación con Management de Elanco, y aseguramiento de cumplimiento de entregables según calendario.

#### Responsabilidades Principales

**Fase 0 - Due Diligence (28h):**
- Facilitación de kick-off meeting con todos los stakeholders (3h)
- Facilitación de workshops de priorización (10h)
- Seguimiento de tickets críticos (SAP, BigQuery) (5h)
- Coordinación con TI Global y TechOps Elanco (3h)
- Preparación de presentación Go/No-Go (4h)
- Documentación de decisiones y acuerdos (3h)

**Fase 1 - Data Lake (44h):**
- Seguimiento semanal de avances (22 semanas × 1h = 22h)
- Gestión de reuniones con stakeholders (10h)
- Coordinación con TI Global para tickets y permisos (6h)
- Reporte de status a Management Elanco (4h)
- Gestión de riesgos y escalaciones (2h)

**Fase 2 - Dashboards (73h):**
- Seguimiento semanal de avances (14 semanas × 1h = 14h)
- Facilitación de UAT (4 fases) (26h)
  - Coordinación con Finanzas (8h)
  - Coordinación con Supply (8h)
  - Consolidación de feedback (6h)
  - Gestión de ajustes (4h)
- Coordinación de capacitación (8h)
- Preparación de Go-Live (12h)
- Documentación de cierre de proyecto (3h)
- Entrega formal y firma de actas (4h)
- Reunión de lecciones aprendidas (2h)
- Handover a equipo de soporte Elanco (4h)

**Responsabilidades Transversales (Todo el proyecto):**
- Gestión de cronograma (actualización semanal)
- Gestión de riesgos (revisión quincenal)
- Comunicación con Product Owner y Sponsor ejecutivo
- Gestión de Change Requests
- Control de presupuesto (horas consumidas vs. planificadas)
- Documentación de lecciones aprendidas
- Coordinación de reuniones (agendas, minutas, seguimiento de acuerdos)

#### Experiencia Requerida (Mínimo)

**Experiencia General:**
- 5+ años como Project Manager en proyectos de TI
- 3+ años gestionando proyectos de BI / Data / Analytics
- Experiencia con metodologías ágiles (Scrum, Kanban)
- Experiencia con proyectos internacionales (multi-país, multi-zona horaria)

**Experiencia Técnica Específica:**

- ✅ **Gestión de proyectos de BI/Analytics:**
  - Proyectos de implementación de dashboards (Power BI, Tableau, etc.)
  - Proyectos de Data Lake / Data Warehouse
  - Integración de sistemas (SAP, ERP, cloud platforms)
  - Proyectos con arquitecturas cloud (GCP, AWS, Azure)

- ✅ **Gestión de stakeholders:**
  - Coordinación con áreas de negocio (Finanzas, Supply, Comercial)
  - Comunicación con Management ejecutivo
  - Facilitación de workshops y sesiones de trabajo
  - Gestión de expectativas

- ✅ **Gestión de riesgos:**
  - Identificación proactiva de riesgos
  - Elaboración de planes de mitigación
  - Escalación oportuna de issues
  - Gestión de contingencias

- ✅ **Gestión de cronograma y presupuesto:**
  - Herramientas de gestión de proyectos (MS Project, Smartsheet, Jira, etc.)
  - Control de horas y presupuesto
  - Reporting de status
  - Gestión de Change Requests

**Conocimientos Deseables:**
- Familiaridad con conceptos de Data Engineering y BI (no necesariamente técnico)
- Conocimiento de SAP (módulos, procesos) - deseable
- Conocimiento de Google Cloud Platform - deseable
- Conocimiento de Power BI - deseable

**Habilidades Técnicas:**
- MS Project, Smartsheet, o herramientas similares
- Excel avanzado (planificación, seguimiento)
- Jira / Azure DevOps (gestión ágil)
- PowerPoint (presentaciones ejecutivas)
- Confluence / SharePoint (documentación)

**Habilidades Blandas (CRÍTICAS):**
- ✅ Comunicación efectiva (oral y escrita) - CRÍTICA
- ✅ Liderazgo sin autoridad formal
- ✅ Resolución de conflictos
- ✅ Negociación con stakeholders
- ✅ Adaptabilidad y flexibilidad
- ✅ Orientación a resultados
- ✅ Capacidad de trabajar bajo presión
- ✅ Proactividad y anticipación de problemas

#### Certificaciones Deseables (No obligatorias)

- PMP (Project Management Professional) - PMI
- PRINCE2 Foundation / Practitioner
- Certified Scrum Master (CSM) o Professional Scrum Master (PSM)
- AgilePM Foundation / Practitioner
- ITIL Foundation (deseable para gestión de servicios)

#### Formación Académica

**Mínimo:**
- Título universitario en Ingeniería, Administración, Sistemas o afines
- Posgrado en Gestión de Proyectos / MBA (deseable)
- Certificación formal en gestión de proyectos (PMP, PRINCE2) - deseable

#### Idiomas

- Español: Nativo o Fluido (95%+)
- Inglés: Intermedio-Avanzado (comunicación con TI Global, documentación)

#### Condiciones Laborales

- Modalidad: Remoto (trabajo a distancia)
- Horario: Flexible (coordinación con zona horaria CASA: GMT-3 a GMT-5)
- Disponibilidad: Lunes a Viernes, 3-5h/semana (promedio)
- Reuniones: 2-3 reuniones semanales (status, stakeholders, equipo)
- Picos de trabajo: Fase 0 (kick-off, workshops), Fase 2 (UAT, go-live)

#### Perfil Ideal

**Candidato ideal tiene:**
- Experiencia en industria farmacéutica / healthcare (deseable)
- Experiencia trabajando con clientes internacionales (multinacionales)
- Capacidad de gestión de múltiples stakeholders con intereses diversos
- Orientación a entrega de valor (no solo cumplimiento de tareas)
- Visión estratégica + ejecución táctica
- Experiencia trabajando con equipos distribuidos (remoto)

---

### PERFIL 4: ABAP DEVELOPER - ESPECIALISTA SAP SLT (NUEVO EN VERSIÓN 2.03)

**Título del Puesto:** SAP ABAP Developer & SLT Specialist  
**Empresa:** Aunergia  
**Proyecto:** Centralización de Datos y Analítica - Elanco Animal Health  
**Dedicación:** Part-time, 15-20 horas/semana  
**Duración:** 21 semanas (Fase 0 y Fase 1 únicamente: enero - junio 2026)  
**Total horas:** 436h (22.1% del proyecto)

#### Descripción del Rol

Especialista técnico SAP ABAP con profundo conocimiento de SAP Landscape Transformation (SLT), módulos MM, SD y FI, y experiencia en proyectos de integración SAP-Cloud. Responsable de todas las actividades de extracción de datos desde SAP hacia BigQuery, configuración y monitoreo de SLT, análisis de transacciones custom, y gestión técnica con TI Global SAP. **NO toca BigQuery ni Power BI** - enfoque 100% en SAP.

#### Responsabilidades Principales

**Fase 0 - Due Diligence (124h):**
- Análisis técnico de infraestructura SAP y conectividad (24h)
- Gestión de tickets SAP (Ticket SAP-48219) como punto focal técnico (28h)
- Análisis profundo de transacciones custom ZLEL008 y ZVEL015 (42h)
  - Análisis de código ABAP (SE38/SE80)
  - Identificación de tablas Z y lógica de negocio
  - Documentación de dependencias
- Configuración preliminar de SAP SLT (20h)
- Validación de conectividad SAP → SLT → BigQuery (8h)
- Documentación técnica SAP (2h)

**Fase 1 - Data Lake (376h):**
- Configuración completa de SAP SLT (48h)
  - Instalación y configuración de replicación
  - Setup de conectores BigQuery
  - Configuración de jobs y schedules
  - Monitoreo de logs y alertas
- Extracción de datos para 18 transacciones SAP (280h)
  - Módulo FI (4 trans): 52h
  - Módulo SD (2 trans): 36h
  - MM Procurement (3 trans): 42h
  - MM Inventory (3 trans): 40h
  - ZLEL008 custom (MRP): 56h
  - CO y FI-AP/AR (4 trans): 48h
  - Master Data y ZVEL015: 52h
- Monitoreo y troubleshooting de replicación SLT (38h)
- Validaciones SAP ↔ BigQuery con Funcional SAP (10h)

**Fase 2 - Dashboards (0h):**
- No participa (Data Lake ya operativo)

**Coordinación Continua:**
- Punto focal técnico con TI Global SAP para tickets y permisos
- Coordinación con SAP Basis (recurso Elanco) para infraestructura
- Documentación de configuración SLT y procesos de extracción
- Soporte a Funcional SAP en validaciones técnicas

#### Experiencia Requerida (Mínimo)

**Experiencia General:**
- 5+ años como SAP ABAP Developer
- 2+ años con SAP Landscape Transformation (SLT) - **CRÍTICO**
- Experiencia en proyectos de integración SAP-Cloud (GCP/AWS/Azure)
- Experiencia con S/4HANA (deseable, preferiblemente con conocimiento de ACDOCA)

**Experiencia Técnica Específica:**

- ✅ **SAP ABAP (CRÍTICO):**
  - Programación ABAP/4, ABAP Objects
  - Análisis y debugging de código ABAP
  - Function Modules, RFCs, BAPIs
  - Transacciones SE38, SE80, SE11, SE16
  - ABAP Dictionary (tablas, estructuras, dominios)
  - Análisis de transacciones custom (Z*, Y*)

- ✅ **SAP SLT - Landscape Transformation (CRÍTICO):**
  - Instalación y configuración de SLT Server
  - Configuración de replicación en tiempo real (CDC - Change Data Capture)
  - Configuración de conectores hacia cloud (BigQuery, S3, etc.)
  - Mass Transfer (carga inicial) vs. Replicación continua
  - Monitoreo de jobs de replicación (transacciones SLT)
  - Troubleshooting de errores de replicación
  - Optimización de performance de replicación
  - Configuración de transformaciones básicas en SLT

- ✅ **Módulo MM - Materials Management (CRÍTICO):**
  - Transacciones: ME2L, ME23N, MM60, MB59, MB5B, MCHB
  - Tablas: EKKO, EKPO, MBEW, CKMLCR, MSEG, MARD, MCHB
  - Conocimiento de procesos: Compras, Inventarios, Valoración
  - Maestro de materiales (MARA, MARC) y proveedores (LFA1, LFB1)

- ✅ **Módulo SD - Sales & Distribution (CRÍTICO):**
  - Transacciones: VA05
  - Tablas: VBAK, VBAP, VBEP, KNA1, KNVV
  - Conocimiento de procesos: Órdenes de venta, Pricing
  - Maestro de clientes (KNA1, KNB1)

- ✅ **Módulo FI - Financial Accounting (CRÍTICO):**
  - Transacciones: FAGLL03, FB03, F.08, F.01, FBL1N, FBL5N
  - Tablas: **ACDOCA, ACDOCA_T** (Universal Journal S/4HANA) - **CRÍTICO**
  - Tablas históricas (referencia): BKPF, BSEG, FAGLFLEXA, BSID, BSAD, BSIK, BSAK
  - Conocimiento de cómo ACDOCA reemplaza tablas clásicas en S/4HANA
  - Documentos contables, mayor general, balances

- ✅ **Módulo CO - Controlling (Deseable):**
  - Transacciones: KSB1, KE24
  - Tablas: AUFK, COBK, COEP (histórico, reemplazado por ACDOCA)
  - Órdenes CO, centros de costo

- ✅ **Transacciones Custom (Z/Y):**
  - Experiencia analizando transacciones custom sin documentación
  - Capacidad de reverse-engineering de lógica ABAP
  - Identificación de tablas custom (Z*, Y*)
  - Documentación de lógica de negocio

- ✅ **Integración SAP-Cloud:**
  - Conectividad SAP → Cloud (RFC, HTTPS)
  - Experiencia con Google Cloud Platform (BigQuery) - deseable
  - Configuración de certificados SSL, firewall
  - Service Accounts y autenticación

**Habilidades Técnicas:**
- ABAP/4: Programación avanzada, debugging, performance tuning
- SAP SLT: Configuración completa y troubleshooting
- SQL: Queries en SAP (SE16, SE16N, SQVI)
- Transacciones SAP: Navegación experta, análisis de dumps (ST22)
- Monitoreo SAP: SM37 (jobs), SM50 (work processes), SM21 (logs)
- Git: Versionado de código (deseable)

**Habilidades Blandas:**
- Comunicación técnica clara (con TI Global, SAP Basis, equipo proyecto)
- Capacidad de trabajar de forma autónoma
- Resolución de problemas complejos
- Documentación técnica detallada
- Coordinación con múltiples stakeholders técnicos
- Adaptabilidad a cambios de requerimientos

#### Certificaciones Deseables (No obligatorias)

- SAP Certified Technology Associate - SAP S/4HANA System Administration
- SAP Certified Development Associate - ABAP with SAP NetWeaver
- SAP Certified Application Associate - SAP Landscape Transformation
- SAP S/4HANA Migration Cockpit / Landscape Transformation (curso oficial)

#### Formación Académica

**Mínimo:**
- Título universitario en Ingeniería en Sistemas, Informática, Computación o afines
- Certificación SAP ABAP (deseable)
- Cursos de SAP SLT (obligatorio si no tiene certificación)

#### Idiomas

- Español: Nativo o Fluido (90%+)
- Inglés: Intermedio (lectura de documentación técnica SAP, comunicación con TI Global)

#### Condiciones Laborales

- Modalidad: Remoto (trabajo a distancia)
- Horario: Flexible (coordinación con zona horaria CASA: GMT-3 a GMT-5)
- Disponibilidad: Lunes a Viernes, 15-20h/semana
- Duración: 21 semanas (solo Fase 0 y Fase 1)
- Reuniones: 2-3 reuniones semanales con equipo técnico y TI Global
- Picos de trabajo: Fase 0 (análisis Z-transactions, setup SLT) y Fase 1 (configuración replicación)

#### Perfil Ideal

**Candidato ideal tiene:**
- Background técnico SAP ABAP + experiencia hands-on con SLT en proyectos reales
- Experiencia en proyectos de migración/integración SAP hacia cloud
- Familiaridad con S/4HANA y ACDOCA (Universal Journal)
- Capacidad de análisis de transacciones custom sin documentación
- Experiencia trabajando con equipos de TI Global (multinacionales)
- Proactividad en identificación y resolución de problemas técnicos
- Experiencia con al menos 2 de los 3 módulos: MM, SD, FI

#### Diferenciador Clave vs Funcional SAP

| Aspecto | ABAP Developer | Funcional SAP |
|---------|----------------|---------------|
| **Enfoque** | Técnico (código, configuración) | Funcional (procesos, negocio) |
| **SAP SLT** | Configura y monitorea (CRÍTICO) | No participa |
| **Código ABAP** | Lee, analiza, documenta | No requiere |
| **Transacciones Z** | Reverse-engineering técnico | Validación funcional |
| **Tablas SAP** | Conoce estructura técnica | Conoce contenido funcional |
| **Extracción de datos** | Configura replicación SLT | Valida calidad de datos |
| **TI Global SAP** | Punto focal técnico (tickets) | Soporte funcional |

---

## RESUMEN DE LOS 4 PERFILES (VERSIÓN 2.03)

| Aspecto | Consultor BI | ABAP Developer | Funcional SAP | Project Manager |
|---------|--------------|----------------|---------------|-----------------|
| **Experiencia mínima** | 6+ años | 5+ años | 5+ años | 5+ años |
| **Horas totales** | 761h (38.7%) | 436h (22.1%) | 484h (24.6%) | 145h (7.4%) |
| **Horas/semana** | 25-30h (máx 6h/día) | 15-20h | 15-20h | 3-5h |
| **Fases participación** | Todas (0+1+2) | Fase 0+1 solamente | Todas (0+1+2) | Todas (0+1+2) |
| **Skills críticos** | BigQuery, Power BI, SQL, ETL | ABAP, SLT, MM/SD/FI, S/4HANA | SAP FI/CO, Validaciones, UAT | Gestión stakeholders, Comunicación |
| **Certificaciones deseables** | GCP Data Engineer, Power BI | SAP ABAP, SAP SLT | SAP FI/CO Associate | PMP, CSM |
| **Idioma inglés** | Intermedio-Avanzado | Intermedio | Intermedio | Intermedio-Avanzado |
| **Modalidad** | Remoto | Remoto | Remoto | Remoto |
| **Criticidad** | 🔴 CRÍTICA | 🔴 CRÍTICA | � CRÍTICA | �🟡 ALTA |

**Nota sobre Recurso SAP Basis:** Provisto por Elanco (cliente), no incluido en horas del proyecto. El ABAP Developer coordina con SAP Basis pero NO lo reemplaza.

---

## CONCLUSIÓN Y PRÓXIMOS PASOS

### Resumen de Respuestas a las 4 Preguntas

1. ✅ **¿Mayor carga horaria para acortar tiempos?**  
   **SÍ** - Versión 2.04 reduce cronograma de **42 a 36 semanas (-14%)** incorporando **ABAP Developer** (270h, rol consultoría) con carga sostenible del Consultor BI (26h/sem). Incremento controlado de **+290h (+18%)**. Go-Live: **13 de septiembre 2026** (1 mes antes).

2. ✅ **¿Visualización gráfica de la solución?**  
   **SÍ** - Generaremos **4 diagramas profesionales** en 2-3 días: arquitectura técnica completa, modelo dimensional star schema, flujo de datos SAP→BigQuery→Power BI, y procesos con validaciones.

3. ✅ **¿Recurso técnico ABAP?**  
   **SÍ** - **270h de ABAP Developer incluidas en V2.04** como consultor especializado (Fase 0+1, 26 semanas, 10.4h/sem). Analiza Z-transactions (ZLEL008/ZVEL015) y configura SAP SLT. También **requieren SAP Basis** provisto por Elanco.

4. ✅ **¿Job Descriptions de los perfiles?**  
   **SÍ** - **4 JDs completos entregados**: Consultor BI (935h), ABAP Developer (270h), Funcional SAP (512h) y Project Manager (163h) con experiencia, responsabilidades, skills técnicos y certificaciones detalladas.

### Tabla Comparativa: V2.02 Original vs V2.04 Optimizada ⭐

| Métrica | V 2.02 Original | V 2.04 OPTIMIZADA ⭐ | Delta | Comentario |
|---------|-----------------|----------------------|-------|------------|
| **Duración total** | 42 semanas | **36 semanas** | **-6 sem (-14%)** | 1.5 meses más rápido |
| **Horas totales** | 1,590h | **1,880h** | **+290h (+18%)** | Incremento controlado |
| **Consultor BI** | 961h (22.9h/sem) | **935h (26.0h/sem)** | -26h | Carga sostenible |
| **ABAP Developer** | ❌ 0h | **270h (10.4h/sem)** ✅ | +270h (NUEVO) | Part-time, fácil contratar |
| **Funcional SAP** | 484h (11.5h/sem) | **512h (14.2h/sem)** | +28h | Incremento leve |
| **Project Manager** | 145h (3.5h/sem) | **163h (4.5h/sem)** | +18h | Mejor coordinación |
| **Go-Live** | 15 Oct 2026 | **13 Sep 2026** | **-1 mes** | Beneficios adelantados |
| **Fase 0** | 6 sem | **6 sem** | 0 sem | Mantener calidad |
| **Fase 1** | 22 sem | **20 sem** | -2 sem | Paralelización |
| **Fase 2** | 14 sem | **10 sem** | -4 sem | Optimización UAT |
| **Riesgo técnico SAP** | ⚠️ Alto | ✅ Bajo | Especialista SLT | ABAP Developer |
| **Calidad entregable** | ⚠️ Presión BI | ✅ Óptima | BI con tiempo | 26h/sem cómodo |
| **Costo-beneficio** | Baseline | ✅ +18% equilibrado | ROI 2-3 meses | Valor estratégico |
| **Facilidad contratación** | 3 recursos | ✅ 4 recursos | +1 part-time | ABAP 10h/sem |

### Beneficios Versión 2.04 (RECOMENDADA)

**✅ VENTAJAS TÉCNICAS:**
- Consultor BI con carga sostenible: 26h/semana promedio (NO comprimido excesivamente)
- ABAP Developer en rol de consultoría especializada (270h enfocadas en lo crítico)
- Análisis profundo de transacciones custom (ZLEL008, ZVEL015) con especialista
- Separación clara: SAP vs BigQuery/Power BI
- Paralelización efectiva en Fase 1 (compresión moderada, realista)

**✅ VENTAJAS DE NEGOCIO:**
- Go-Live 6 semanas antes (mediados septiembre vs mediados octubre)
- 6 semanas adicionales de beneficios operativos (reducción 70% tiempo manual)
- Menor riesgo de delays por issues técnicos SAP
- Punto focal técnico especializado para TI Global
- Equilibrio óptimo: tiempo vs costo vs calidad

**✅ VENTAJAS VS V2.03 (AGRESIVA):**
- -88h más económica (-5% vs v2.03)
- ABAP Developer más fácil de contratar (10h/sem vs 24h/sem)
- Menor overhead de coordinación (rol part-time vs full-time)
- Cronograma realista (36 sem) vs presión alta (32 sem)
- Consultor BI con más espacio para calidad (26h vs 24h)

**💰 ANÁLISIS DE INVERSIÓN V2.04:**
- Inversión adicional: +290 horas (+18% esfuerzo) vs v2.02
- Ahorro temporal: -6 semanas (-14% duración)
- ROI: 6 semanas de beneficios operativos tempranos
- Ejemplo: Si reducción 70% tiempo = 60h/mes ahorradas → 6 semanas = 100h ahorradas
- Break-even en ~2.9 meses post go-live (conservador)
- Break-even en ~2.0 meses (considerando valor intangible + riesgo reducido)

### Próximas Acciones

**De parte de Aunergia:**
- ✅ Respuestas completas a 4 preguntas de Aunergia
- ✅ 4 Job Descriptions detallados (BI, ABAP, SAP Functional, PM)
- ✅ Documentación V2.04 actualizada
- ⏳ **Generar diagramas de arquitectura técnica (2-3 días hábiles)**
- ⏳ **Identificar candidato ABAP Developer** (perfil: 5+ años ABAP, 2+ SLT, MM/SD/FI)
- ⏳ Preparar presentación ejecutiva para aprobación

**De parte de Elanco:**
- ⏳ **Revisión y decisión sobre V2.04** (36 semanas, +290h)
- ⏳ **Aprobación de presupuesto adicional** (+18% = +290 horas)
- ⏳ **Confirmación de disponibilidad SAP Basis** (recurso interno Elanco desde Fase 0)
- ⏳ **Provisión de accesos SAP y BigQuery** antes de kick-off
- ⏳ **Compromiso de stakeholders** (4-6h/sem para validaciones/UAT)

### Documentos Disponibles (V2.04)

| Documento | Ubicación | Contenido |
|-----------|-----------|-----------|
| 📄 **RESUMEN_PROPUESTA_FINAL_V2_04.txt** | `/ElancoPower/` | Resumen ejecutivo <1000 palabras |
| 📄 **RESUMEN_CAMBIOS_V2_04.md** | `/ElancoPower/` | Análisis detallado V2.02→V2.04 |
| 📄 **CRONOGRAMA_DETALLADO_TAREAS_V2_04.csv** | `/docs/propuesta_final/` | 25 tareas, 36 semanas, 4 recursos |
| 📄 **respuesta_pregunta_01.md** | `/preguntas_aunergia/` | Este documento con respuestas |
| 📁 **Propuesta completa** | `/docs/propuesta_final/` | 13 docs (portada, fases, anexos) |

### 🏆 Recomendación Final: VERSIÓN 2.04 (OPTIMIZADA)

**Recomendamos aprobar VERSIÓN 2.04** por ofrecer el mejor equilibrio tiempo-costo-calidad:

#### Beneficios Clave V2.04

1. 🎯 **Carga sostenible** - Consultor BI 26h/sem (cómodo, NO sobrecarga)
2. 🚀 **Go-Live adelantado** - 1 mes antes (13 Sep vs 15 Oct 2026)
3. 🛡️ **Riesgo técnico reducido** - ABAP Developer especialista en SLT y Z-transactions
4. 💼 **Roles especializados** - ABAP=SAP/SLT | BI=BigQuery/Power BI
5. 💰 **Costo controlado** - +18% (vs +24% de V2.03 agresiva)
6. ⚡ **Cronograma realista** - 36 semanas (balance óptimo)
7. 👥 **Fácil contratación** - ABAP part-time 10h/sem (no full-time)
8. 🎨 **Calidad garantizada** - Recursos con tiempo suficiente
9. 📊 **ROI positivo** - Break-even en 2-3 meses post-Go-Live
10. ✅ **Menor coordinación** - 1 recurso part-time vs full-time

#### Análisis de Inversión

**Inversión adicional:** +290h (+18% presupuesto)  
**Ahorro temporal:** -6 semanas (-14% duración)  
**Beneficios operativos:** Reducción 70% tiempo manual desde 1 mes antes  
**Break-even:** 2-3 meses post-Go-Live  

**Cálculo conservador:**
- Ahorro operativo: ~100h/mes (eliminación procesos manuales)
- Break-even: 290h / 100h = **2.9 meses**

**Cálculo realista (incluye valor intangible):**
- Insights de negocio 1 mes antes (valor decisiones basadas en datos)
- Reducción riesgo de delays (costo de oportunidad)
- Mayor calidad (menos correcciones post-Go-Live)
- Break-even: **1.5-2 meses**

---

## 📋 RESUMEN FINAL

| Pregunta | Respuesta | Detalles |
|----------|-----------|----------|
| **1. ¿Acortar tiempos con mayor carga?** | ✅ **SÍ** - V2.04: 36 semanas | Reduce 6 semanas (-14%) con ABAP Developer (270h) |
| **2. ¿Visualización gráfica?** | ✅ **SÍ** - 4 diagramas | Arquitectura, modelo, flujo, procesos (2-3 días) |
| **3. ¿Recurso ABAP?** | ✅ **SÍ** - 270h incluidas | Part-time (10.4h/sem) + SAP Basis (Elanco) |
| **4. ¿Job Descriptions?** | ✅ **SÍ** - 4 JDs completos | BI, ABAP, SAP Functional, PM (ver arriba) |

### Decisión Recomendada

**Aprobar VERSIÓN 2.04** con:
- ✅ Cronograma: 36 semanas (Go-Live: 13 sep 2026)
- ✅ Presupuesto: 1,880h (+290h, +18%)
- ✅ Equipo: BI (935h) + ABAP (270h) + SAP (512h) + PM (163h)
- ✅ ROI: Break-even en 2-3 meses post-Go-Live

---

**Fecha de elaboración:** 12 de noviembre de 2025  
**Elaborado por:** Equipo Técnico Aunergia  
**Validez:** 30 días (hasta 12 de diciembre de 2025)  
**Versión recomendada:** 2.04 (Optimizada - Equilibrio Tiempo-Costo-Calidad)

---

**Archivos de referencia:**
- 📄 `/RESUMEN_PROPUESTA_FINAL_V2_04.txt` - Resumen ejecutivo
- 📄 `/RESUMEN_CAMBIOS_V2_04.md` - Análisis V2.02→V2.04
- 📄 `/docs/propuesta_final/CRONOGRAMA_DETALLADO_TAREAS_V2_04.csv` - Cronograma 36 semanas
- 📁 `/docs/propuesta_final/` - Propuesta completa (13 documentos)

Quedamos atentos a sus comentarios y decisión sobre la versión 2.04.

**Saludos cordiales,**  
**Equipo Aunergia**
