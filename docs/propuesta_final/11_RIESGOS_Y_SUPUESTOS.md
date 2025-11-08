# 11. RIESGOS Y SUPUESTOS

## 11.1. Matriz de Riesgos Identificados

A continuación se presenta el análisis de riesgos del proyecto con su probabilidad de ocurrencia, impacto potencial y estrategias de mitigación.

### 11.1.1. Resumen Ejecutivo de Riesgos

| Categoría | Riesgos Alto | Riesgos Medio | Riesgos Bajo | Total |
|-----------|--------------|---------------|--------------|-------|
| **Técnicos** | 3 | 4 | 2 | 9 |
| **Organizacionales** | 2 | 3 | 1 | 6 |
| **Recursos** | 1 | 2 | 2 | 5 |
| **Cronograma** | 1 | 2 | 1 | 4 |
| **Presupuesto** | 0 | 2 | 2 | 4 |
| **TOTAL** | **7** | **13** | **8** | **28** |

**Criticidad Global:** 🟡 MEDIA-ALTA (7 riesgos altos requieren atención prioritaria)

---

## 11.2. Riesgos Técnicos

### 🔴 R-T-01: Permisos SAP Insuficientes o Demorados

**Descripción:**  
Los permisos SAP solicitados (RFC, tablas, transacciones custom) no se otorgan completamente o la gestión del ticket SAP-48219 se demora más de 3 semanas.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🔴 Alta (60%) | 🔴 Crítico | 🔴 **ALTO** | Fase 0 y Fase 1 |

**Impacto Potencial:**
- ⏱️ Retraso de 2-4 semanas en inicio de Fase 1
- 💰 Posible incremento de costos por extensión de plazos
- 🚫 Imposibilidad de extraer datos de transacciones críticas (ej. ZLEL008, KE24)

**Estrategias de Mitigación:**

1. **Preventiva (ANTES del Kick-off):**
   - ✅ Solicitar permisos SAP con 3 semanas de anticipación (antes del 31-oct)
   - ✅ Designar a David Saboya (TechOps) como enlace directo con TI Global
   - ✅ Priorizar permisos de transacciones TOP 10 (ver [03_TRANSACCIONES_SAP](03_TRANSACCIONES_SAP_INCLUIDAS.md))

2. **Contingencia (SI ocurre):**
   - Plan B: Usar RFCs con usuario de servicio (Service Account)
   - Plan C: Implementar primero transacciones con acceso confirmado, postergar custom
   - Activar cláusula de extensión de plazo sin penalización si demora > 3 semanas

**Indicadores de Monitoreo:**
- 📊 Status del ticket SAP-48219 (revisión semanal)
- 📊 % de transacciones con permisos confirmados

**Responsable:** David Saboya (Elanco TI) + Project Manager

---

### 🔴 R-T-02: Tablas SAP No Disponibles en BigQuery

**Descripción:**  
Las tablas SAP necesarias (COEP, CE1*, CE4*, Z-tables) no están replicadas en BigQuery o están incompletas. Tickets BQ-7713 y BQ-7721 ya documentan esta situación.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media-Alta (50%) | 🔴 Alto | 🔴 **ALTO** | Fase 0 (bloqueante) |

**Impacto Potencial:**
- 🚫 Imposibilidad de avanzar con transacciones KE24, ZLEL008, KSB1
- 📉 Reducción del alcance funcional (de 18 a 12-14 transacciones)
- ⏱️ Retraso en cronograma si se requiere solución alternativa

**Estrategias de Mitigación:**

1. **Preventiva (Fase 0 - Semana 1):**
   - ✅ Auditoría completa de tablas disponibles en dataset casa_bi
   - ✅ Solicitar replicación de tablas faltantes (ticket TI Global)
   - ✅ Validar integridad de datos: registros, fechas, completitud

2. **Contingencia (SI ocurre):**
   - **Plan B:** Extracción directa desde SAP vía RFC/BAPI hacia BigQuery
   - **Plan C:** Priorizar transacciones con tablas completas, postergar custom
   - **Plan D:** Evaluar Azure Synapse si BigQuery no viable (costo adicional)

3. **Criterio Go/No-Go:**
   - ✅ Si ≥ 12 transacciones viables → **GO**
   - ⚠️ Si 8-11 transacciones → **GO con alcance reducido**
   - 🚫 Si < 8 transacciones → **NO-GO** (replantear)

**Responsable:** Consultor BI (Arquitecto) + TI Global Elanco

---

### 🔴 R-T-03: Complejidad Técnica de Transacciones Custom

**Descripción:**  
Las transacciones custom ZLEL008 (Comparativo de Precios) y ZVEL015 (Ventas Estadísticas) tienen lógica de negocio compleja no documentada, tablas Z desconocidas, o dependencias ocultas.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (40%) | 🟡 Medio | 🟡 **MEDIO-ALTO** | Fase 1 |

**Impacto Potencial:**
- ⏱️ Esfuerzo de análisis 2-3x mayor al estimado (de 16h a 40-50h)
- 💰 Posible sobrecosto en horas ABAP/consultoría
- 📉 Retraso en entrega de dashboards asociados

**Estrategias de Mitigación:**

1. **Preventiva (Fase 0 - Semana 2-3):**
   - ✅ Sesión de deep-dive con desarrolladores ABAP de TI Global
   - ✅ Solicitar código fuente de Z-transactions (includes, function modules)
   - ✅ Documentar lógica de cálculo y dependencias
- Asignar presupuesto de contingencia para consultoría ABAP especializada.

2. **Contingencia (SI ocurre):**
   - Contratar consultor ABAP senior por 40-60 horas (incluido en presupuesto contingencias)
   - Simplificar alcance: replicar solo outputs críticos, no toda la lógica
   - Postergar a Fase 2 si no bloquea otros dashboards

**Responsable:** Funcional SAP (SAP Analyst) + Consultor ABAP

---

### 🟡 R-T-04: Calidad de Datos en SAP

**Descripción:**  
Datos en SAP con problemas de calidad: valores nulos, duplicados, inconsistencias entre módulos, cuentas contables sin descripción, centros mal configurados.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (40%) | 🟡 Medio | 🟡 **MEDIO** | Fase 1 y Fase 2 |

**Impacto Potencial:**
- 📊 Dashboards con datos incorrectos o incompletos
- ⏱️ Tiempo adicional de limpieza de datos (10-20 horas)
- 🔄 Re-work en lógica ETL
- 📉 Desconfianza de usuarios finales en el sistema

**Estrategias de Mitigación:**

1. **Preventiva (Fase 1 - Semanas 5-6):**
   - ✅ Data Profiling exhaustivo (herramientas BigQuery Data Quality)
   - ✅ Validaciones de negocio con stakeholders
   - ✅ Catálogo de reglas de calidad (ej. cuentas contables válidas, centros activos)

2. **Contingencia (SI ocurre):**
   - Documentar excepciones y exclusiones claramente
   - Flags de calidad en tablas (campo `data_quality_flag`)
   - Comunicar limitaciones a usuarios finales
   - Plan de limpieza gradual en Fase 2

**Responsable:** Consultor BI + Funcional SAP

---

### 🟡 R-T-05: Desempeño de Consultas BigQuery

**Descripción:**  
Consultas BigQuery lentas o costosas por mal diseño de particiones, falta de clustering, o queries no optimizados.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (20%) | 🟡 Medio | 🟢 **BAJO-MEDIO** | Fase 2 |

**Impacto Potencial:**
- 💰 Costos de procesamiento BigQuery mayores a lo estimado
- ⏱️ Dashboards Power BI lentos (> 10 segundos)
- 😤 Frustración de usuarios finales

**Estrategias de Mitigación:**

1. **Preventiva (Fase 1 - Diseño):**
   - ✅ Particionamiento por fecha (columna `fecha_contable` o `created_date`)
   - ✅ Clustering por dimensiones clave (ej. `company_code`, `pais`, `material`)
   - ✅ Vistas materializadas para agregaciones frecuentes
   - ✅ Capa CURATED con datos pre-calculados

2. **Contingencia (SI ocurre):**
   - Refactorización de queries costosos (identificados con Query Plan Analyzer)
   - Implementar caché en Power BI (Import mode vs DirectQuery)
   - Optimización de tablas (re-clustering, deduplicación)

**Responsable:** Consultor BI (Arquitecto)

---

### 🟡 R-T-06: Conectividad SAP ↔ BigQuery

**Descripción:**  
Problemas de conectividad entre SAP on-premise y Google Cloud: firewall bloqueando tráfico RFC, latencia alta (> 200ms), certificados SSL expirados.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (30%) | 🟡 Medio | 🟡 **MEDIO** | Fase 1 (semanas 3-4) |

**Estrategias de Mitigación:**

1. **Preventiva (Fase 0):**
   - ✅ Prueba de conectividad en semana 2-3 de Fase 0
   - ✅ Coordinación con TI Global para abrir puertos firewall
   - ✅ Configurar VPN o Private Service Connect si es necesario

2. **Contingencia (SI ocurre):**
   - Usar extracción batch (archivos CSV vía SFTP)
   - Implementar queue de retry con backoff exponencial
   - Escalar a TI Global con prioridad P1

**Responsable:** TI Elanco + TI Global

---

### 🟡 R-T-07: Compatibilidad Power BI ↔ BigQuery

**Descripción:**  
Limitaciones del conector nativo Power BI - BigQuery: tipos de datos no soportados, funciones SQL incompatibles, rendimiento bajo en DirectQuery.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (20%) | 🟢 Bajo | 🟢 **BAJO** | Fase 2 |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Usar capa CURATED con datos pre-procesados (evitar lógica compleja en Power BI)
   - ✅ Preferir Import mode para dashboards con < 1GB datos
   - ✅ DirectQuery solo para datos near-real-time

2. **Contingencia:**
   - Implementar vistas SQL en BigQuery con transformaciones
   - Usar Power Query (M) para transformaciones cliente-side
   - Evaluar conector Simba ODBC si conector nativo insuficiente

**Responsable:** Consultor BI

---

### 🟢 R-T-08: Pérdida de Datos Durante Migración

**Descripción:**  
Pérdida accidental de datos durante desarrollo/testing en ambientes dev o qa.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (10%) | 🟡 Medio | 🟢 **BAJO** | Todas |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Backups automáticos BigQuery (7 días rolling)
   - ✅ Versionado de código SQL en Git
   - ✅ Ambientes segregados (dev/qa/prod)
   - ✅ Pruebas en dataset de desarrollo solamente

2. **Contingencia:**
   - Time-travel BigQuery (hasta 7 días atrás)
   - Rollback desde Git
   - Re-ejecución de pipelines ETL

**Responsable:** Consultor BI + TI Elanco

---

### 🟢 R-T-09: Problemas de Seguridad / Compliance

**Descripción:**  
Exposición accidental de datos sensibles (PII, financieros) por configuración incorrecta de permisos.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (10%) | 🔴 Alto | 🟡 **MEDIO** | Fase 2 y Producción |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Row-Level Security en BigQuery (filtro por país/área)
   - ✅ Auditoría de permisos antes de go-live
   - ✅ Encriptación en tránsito y en reposo (default GCP)
   - ✅ Logs de auditoría activados

2. **Contingencia:**
   - Revocar accesos inmediatamente
   - Notificar a Security Officer Elanco
   - Auditoría forense si hubo exposición

**Responsable:** TI Elanco + Aunergia

---

## 11.3. Riesgos Organizacionales

### 🔴 R-O-01: Falta de Disponibilidad de Stakeholders

**Descripción:**  
Stakeholders clave (Finanzas, Supply) no disponibles para workshops, validaciones o UAT por carga operativa (ej. cierre mensual, auditorías).

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media-Alta (50%) | 🟡 Alto | 🔴 **ALTO** | Fase 0, Fase 2 |

**Impacto Potencial:**
- ⏱️ Retraso en validaciones de requerimientos (Fase 0)
- 📉 UAT incompleto o superficial (Fase 2)
- 🚫 Go-live sin aprobación formal
- 🔄 Re-work por malentendidos de requerimientos

**Estrategias de Mitigación:**

1. **Preventiva (Antes del Kick-off):**
   - ✅ Calendario de cierres contables del 2025-2026 (evitar esas semanas)
   - ✅ Compromiso formal de disponibilidad (4-6h/semana) en kick-off
   - ✅ Designar usuarios backup por área

2. **Contingencia (SI ocurre):**
   - Grabar sesiones de workshops para revisión asíncrona
   - Extender plazos de revisión (de 3 a 5 días)
   - Aprobar por etapas parciales (no todo-o-nada)
   - Escalar a Product Owner o Management

**Responsable:** Project Manager + Product Owner

---

### 🔴 R-O-02: Cambio de Prioridades de Negocio

**Descripción:**  
Durante el proyecto, Elanco decide priorizar otras iniciativas (ej. implementación nuevo ERP, fusión/adquisición) y el proyecto de BI pierde patrocinio o presupuesto.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (15%) | 🔴 Crítico | 🟡 **MEDIO-ALTO** | Cualquier fase |

**Impacto Potencial:**
- 🚫 Cancelación del proyecto
- 💰 Pérdida de inversión parcial
- ⏱️ Pausa indefinida del proyecto

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Alinear proyecto con objetivos estratégicos de Management
   - ✅ Comunicar quick-wins tempranos (dashboards iniciales en Fase 1)
   - ✅ Mantener patrocinio activo (Product Owner + Sponsor ejecutivo)

2. **Contingencia (SI ocurre):**
   - Cláusula contractual de terminación anticipada (pago proporcional por trabajo completado)
   - Entrega de artefactos hasta el punto alcanzado
   - Opción de pausa/retoma en 6-12 meses

**Responsable:** Project Manager + Sponsor Elanco

---

### 🟡 R-O-03: Resistencia al Cambio de Usuarios

**Descripción:**  
Usuarios finales prefieren seguir usando Excel y reportes SAP tradicionales, baja adopción de dashboards Power BI.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (35%) | 🟡 Medio | 🟡 **MEDIO** | Post Go-Live |

**Impacto Potencial:**
- 📉 Bajo aprovechamiento de beneficios esperados
- 😤 Frustración del equipo y Management
- 📊 Dashboards subutilizados

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Involucrar usuarios desde Fase 0 (workshops)
   - ✅ Capacitación hands-on con casos reales
   - ✅ Dashboards intuitivos con UX/UI amigable
   - ✅ Quick-wins: reemplazar reportes más dolorosos primero

2. **Contingencia:**
   - Capacitaciones de refuerzo (incluidas)
   - Champions por área (power users evangelizadores)
   - Comunicación de éxitos tempranos (tiempo ahorrado, insights obtenidos)

**Responsable:** Project Manager + Product Owner

---

### 🟡 R-O-04: Falta de Product Owner Empoderado

**Descripción:**  
El Product Owner designado no tiene autoridad para tomar decisiones, debe escalar todo a Management, generando retrasos en aprobaciones.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (30%) | 🟡 Medio | 🟡 **MEDIO** | Fase 0 y Fase 2 |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Definir límites de autoridad del PO en kick-off
   - ✅ Escalar solo decisiones estratégicas (> 1 semana impacto o cambios de alcance significativos)
   - ✅ Designar sponsor ejecutivo para escalaciones

2. **Contingencia:**
   - Documentar decisiones pendientes y su impacto
   - Escalar a Management con opciones y recomendación
   - Buffer de tiempo para aprobaciones (3-5 días)

**Responsable:** Project Manager

---

### 🟡 R-O-05: Falta de Claridad en Requerimientos

**Descripción:**  
Requerimientos funcionales ambiguos o incompletos, descubiertos tarde en el proyecto (Fase 2), generando re-work.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (30%) | 🟡 Medio | 🟡 **MEDIO** | Fase 0 y Fase 2 |

**Estrategias de Mitigación:**

1. **Preventiva (Fase 0):**
   - ✅ Workshops de requerimientos detallados (4 sesiones de 2-3 horas)
   - ✅ Mockups de dashboards para validación temprana
   - ✅ Criterios de aceptación SMART por entregable

2. **Contingencia:**
   - Metodología ágil: iteraciones cortas con feedback continuo
   - Priorizar MVP (Minimum Viable Product) primero
   - Cambios mayores → Change Request (posible costo/tiempo adicional)

**Responsable:** Project Manager + Funcional SAP

---

### 🟢 R-O-06: Rotación de Personal Clave

**Descripción:**  
Salida de personal clave de Elanco (Product Owner, stakeholders, Funcional SAP) o del equipo (Consultor BI) durante el proyecto.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (15%) | 🟡 Medio | 🟢 **BAJO-MEDIO** | Cualquier fase |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Documentación exhaustiva (permite handover)
   - ✅ Usuarios backup identificados
   - ✅ Equipo con redundancia (Funcional SAP conoce el proyecto)

2. **Contingencia:**
   - Período de transición de 2 semanas (handover)
   - Revisión de prioridades con nuevo responsable
   - Ajuste de cronograma si necesario

**Responsable:** Project Manager + Management Elanco

---

## 11.4. Riesgos de Recursos

### 🔴 R-R-01: Sobrecarga del Funcional SAP (SAP Analyst)

**Descripción:**  
El Funcional SAP tiene demandas de su rol operativo (atención a usuarios, cierres, ad-hocs) y podría no dedicar 15-20h/semana al proyecto.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media-Alta (45%) | 🟡 Alto | 🔴 **ALTO** | Fase 1 principalmente |

**Impacto Potencial:**
- ⏱️ Retraso en análisis de transacciones SAP
- 📉 Calidad subóptima por trabajo apresurado
- 😰 Burnout del Funcional SAP

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Cronograma ajustado a 4-6h/semana (ya aplicado)
   - ✅ Priorizar semanas con baja carga operativa
   - ✅ Asistencia del Consultor BI en tareas SAP técnicas
   - ✅ Designar backup en área SAP de Elanco

2. **Contingencia:**
   - Extender plazos de Fase 1 (de 8 a 10-12 semanas)
   - Contratar SAP Analyst adicional (costo adicional)
   - Re-priorizar transacciones: hacer TOP 10 primero

**Responsable:** Project Manager + Funcional SAP

---

### 🟡 R-R-02: Dependencia del Consultor BI (Single Point of Failure)

**Descripción:**  
El Consultor BI es el único arquitecto/desarrollador; si no está disponible (enfermedad, vacaciones, otro proyecto), el proyecto se detiene.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (20%) | 🟡 Alto | 🟡 **MEDIO** | Fase 1 y Fase 2 |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Documentación técnica detallada (permite handover)
   - ✅ Code reviews con Funcional SAP (conocimiento compartido)
   - ✅ Versionado en Git (trazabilidad)
   - ✅ Coordinación de vacaciones con antelación

2. **Contingencia:**
   - Funcional SAP puede asumir tareas SQL básicas
   - Contratar desarrollador BigQuery freelance (red de Aunergia)
   - Pausar proyecto temporalmente si ausencia > 2 semanas

**Responsable:** Project Manager

---

### 🟡 R-R-03: Falta de Recursos TI Global

**Descripción:**  
TI Global de Elanco tiene baja capacidad para atender tickets (permisos SAP, tablas BigQuery, gestión de infraestructura), tiempos de respuesta > 2 semanas.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (35%) | 🟡 Medio | 🟡 **MEDIO** | Fase 0 y Fase 1 |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ David Saboya (TechOps) como enlace directo
   - ✅ Tickets con prioridad P1/P2 (justificación de negocio)
   - ✅ Solicitudes con 3-4 semanas de anticipación

2. **Contingencia:**
   - Escalar a Management Elanco
   - Implementar soluciones alternativas (ej. RFC en vez de tablas)
   - Extender plazos de Fase 0 si necesario

**Responsable:** David Saboya (TI Elanco)

---

### 🟢 R-R-04: Cambio de Prioridades de Aunergia

**Descripción:**  
Aunergia asigna al Consultor BI o al Funcional SAP a otro proyecto de mayor prioridad/rentabilidad, reduciendo su disponibilidad.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (10%) | 🟡 Medio | 🟢 **BAJO** | Cualquier fase |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Compromiso contractual de disponibilidad
   - ✅ Planificación de carga de trabajo en Aunergia

2. **Contingencia:**
   - Asignar desarrollador alternativo de Aunergia
   - Pausar proyecto con compensación si fuerza mayor

**Responsable:** Management Aunergia

---

### 🟢 R-R-05: Falta de Ambiente de Pruebas

**Descripción:**  
No hay ambiente de QA disponible, pruebas se hacen directamente en producción (alto riesgo).

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (15%) | 🟡 Medio | 🟢 **BAJO** | Fase 1 |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Requisito: 3 ambientes (dev/qa/prod) - Ver sección 10
   - ✅ Provisión en Fase 0

2. **Contingencia:**
   - Usar dataset `casa_bi_dev` como pseudo-QA
   - UAT directo en producción con datos sample

**Responsable:** TI Elanco

---

## 11.5. Riesgos de Cronograma

### 🔴 R-C-01: Retraso en Fase 0 (Due Diligence)

**Descripción:**  
La auditoría de factibilidad (Fase 0) identifica más problemas de los esperados, requiriendo más de 5 semanas para resolver.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (35%) | 🟡 Alto | 🟡 **MEDIO-ALTO** | Fase 0 |

**Impacto Potencial:**
- ⏱️ Corrimiento de todo el cronograma (2-4 semanas)
- 💰 Posible sobrecosto si se requiere consultoría adicional
- 📉 Reducción de alcance funcional

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Buffer de 1 semana incluido (4-5 semanas)
   - ✅ Criterios Go/No-Go claros (≥ 12 transacciones viables)

2. **Contingencia:**
   - Extender Fase 0 hasta 6-7 semanas máximo
   - Documentar bloqueantes y elevar a Management
   - Si > 7 semanas → Evaluar viabilidad del proyecto (posible NO-GO)

**Responsable:** Project Manager + Product Owner

---

### 🟡 R-C-02: Retrasos por Dependencias Externas

**Descripción:**  
Dependencias de TI Global (permisos, tablas, ambientes) se retrasan, impactando el camino crítico.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (40%) | 🟡 Medio | 🟡 **MEDIO** | Fase 0 y Fase 1 |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Identificar dependencias críticas en kick-off
   - ✅ Solicitar con 3-4 semanas anticipación
   - ✅ Seguimiento semanal de status

2. **Contingencia:**
   - Trabajar en paralelo en tareas no bloqueadas
   - Ajustar cronograma con aprobación de Product Owner
   - Cláusula de extensión sin penalización si retraso > 2 semanas

**Responsable:** David Saboya + Project Manager

---

### 🟡 R-C-03: Scope Creep (Aumento de Alcance)

**Descripción:**  
Stakeholders solicitan funcionalidades adicionales no contempladas (más transacciones, más dashboards, integraciones no planificadas).

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (35%) | 🟡 Medio | 🟡 **MEDIO** | Fase 2 |

**Impacto Potencial:**
- ⏱️ Retraso en go-live
- 💰 Sobrecosto si no se gestiona formalmente
- 😤 Frustración del equipo

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Alcance claramente definido en contrato (18 transacciones, 12 dashboards)
   - ✅ Proceso formal de Change Request para cambios mayores
   - ✅ Product Owner debe aprobar nuevos requerimientos

2. **Contingencia:**
   - Cambios menores: Absorber en buffer de contingencia
   - Cambios mayores: Cotización adicional + extensión de plazo
   - Priorizar: MVP en Fase 2, mejoras en Fase post-proyecto

**Responsable:** Project Manager + Product Owner

---

### 🟢 R-C-04: Feriados y Vacaciones

**Descripción:**  
Período de vacaciones (Diciembre 2025, Enero 2026) reduce disponibilidad del equipo.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Alta (80%) | 🟢 Bajo | 🟢 **BAJO** | Fase 0 y Fase 1 |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Cronograma ya considera semanas de baja actividad (Dic-Ene)
   - ✅ Buffer de 2 semanas incluido
   - ✅ Coordinar vacaciones con antelación

2. **Contingencia:**
   - Ajustar expectativas de entregables en esas semanas
   - Adelantar o postergar tareas críticas

**Responsable:** Project Manager

---

## 11.6. Riesgos de Presupuesto

### 🟡 R-P-01: Sobrecosto por Horas Extras

**Descripción:**  
El proyecto requiere más horas de las estimadas (ej. complejidad transacciones custom, re-work por calidad de datos).

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟡 Media (30%) | 🟢 Bajo-Medio | 🟡 **MEDIO** | Fase 1 y Fase 2 |

**Impacto Potencial:**
- ⏱️ Necesidad de horas adicionales (7-15% del esfuerzo estimado)
- ⚠️ Necesidad de aprobación adicional

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Estimaciones con buffer del 15-20%
   - ✅ Seguimiento semanal de horas consumidas vs. planificadas
   - ✅ Análisis detallado en Fase 0 para reducir incertidumbre

2. **Contingencia:**
   - Revisar alcance y re-priorizar transacciones
   - Solicitar aprobación formal para extensión de horas si necesario
   - Reducir alcance funcional (postergar transacciones de prioridad 3)

**Responsable:** Project Manager + Management Elanco

---

### 🟡 R-P-02: Costos de Infraestructura BigQuery Mayores

**Descripción:**  
Costos mensuales de BigQuery (almacenamiento + procesamiento) mayores a lo estimado inicialmente por Elanco.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (20%) | 🟢 Bajo | 🟢 **BAJO** | Producción |

**Impacto Potencial:**
- 💰 Costo mensual recurrente mayor para el cliente
- ⚠️ Necesidad de ajustar presupuesto operativo anual de Elanco

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Optimización de queries (ver R-T-05)
   - ✅ Particionamiento y clustering
   - ✅ Monitoreo de costos con alertas configurables

2. **Contingencia:**
   - Revisión de queries más costosos (Query Plan Analyzer)
   - Optimizar uso de almacenamiento (archival de datos muy antiguos)
   - Evaluar slots reservados si costo sostenido alto

**Responsable:** TI Elanco + Consultor BI

---

### 🟢 R-P-03: Cambios de Tarifas de Servicios

**Descripción:**  
Aumento de precios de licencias Power BI Pro o tarifas de procesamiento BigQuery durante el proyecto.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja (10%) | 🟢 Bajo | 🟢 **BAJO** | Producción |

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Licencias Power BI Pro ya adquiridas (precio fijo 2025-2026)
   - ✅ Precios BigQuery relativamente estables

2. **Contingencia:**
   - Costos asumidos por Elanco (infraestructura)
   - Ajustar presupuesto anual según necesidad

**Responsable:** Elanco Finance + TI

---

### 🟢 R-P-04: Necesidad de Recursos Adicionales No Planificados

**Descripción:**  
Se requieren recursos no planificados: consultor ABAP adicional, desarrollador BigQuery, herramientas de terceros.

| **Probabilidad** | **Impacto** | **Exposición** | **Fase Afectada** |
|------------------|-------------|----------------|-------------------|
| 🟢 Baja-Media (25%) | 🟢 Bajo-Medio | 🟢 **BAJO-MEDIO** | Fase 1 |

**Impacto Potencial:**
- 💰 Costo adicional
- ⚠️ Necesidad de aprobación formal

**Estrategias de Mitigación:**

1. **Preventiva:**
   - ✅ Horas de consultoría ABAP ya incluidas en el presupuesto (12 horas)
   - ✅ Análisis detallado en Fase 0 para identificar necesidades tempranas

2. **Contingencia:**
   - Solicitar aprobación formal para recursos adicionales si necesario
   - Re-priorizar transacciones según recursos disponibles

**Responsable:** Project Manager

---

## 11.7. Supuestos del Proyecto

Los siguientes supuestos son críticos para la viabilidad del proyecto. Si alguno NO se cumple, se debe re-evaluar alcance, cronograma o presupuesto.

### 11.7.1. Supuestos Técnicos

| # | Supuesto | Criticidad | Responsable Validación |
|---|----------|------------|------------------------|
| **S-T-01** | Google BigQuery está disponible y configurado con dataset casa_bi (dev / qa / prod) | 🔴 CRÍTICO | TI Global Elanco |
| **S-T-02** | Mínimo 12 de 18 transacciones SAP tienen tablas disponibles en BigQuery | 🔴 CRÍTICO | TI Global + Aunergia (Fase 0) |
| **S-T-03** | Permisos SAP se otorgan en máximo 3 semanas (Ticket SAP-48219) | 🔴 CRÍTICO | TI Global Elanco |
| **S-T-04** | SAP S/4HANA está estable (no hay plan de migración a S/4HANA en 2025-2026) | 🟡 ALTO | TI Elanco |
| **S-T-05** | Conectividad SAP ↔ BigQuery es técnicamente viable | 🟡 ALTO | TI Global |
| **S-T-06** | Power BI Pro puede conectarse a BigQuery vía conector nativo | 🟢 MEDIO | Aunergia |
| **S-T-07** | Datos históricos de mínimo 24 meses están disponibles en SAP | 🟢 MEDIO | Funcional SAP + Stakeholders |

### 11.7.2. Supuestos Organizacionales

| # | Supuesto | Criticidad | Responsable Validación |
|---|----------|------------|------------------------|
| **S-O-01** | Presupuesto está aprobado y disponible | 🔴 CRÍTICO | Finance Elanco |
| **S-O-02** | Product Owner está designado y tiene autoridad para tomar decisiones | 🔴 CRÍTICO | Management Elanco |
| **S-O-03** | Stakeholders (Finanzas, Supply) están disponibles 4-6h/semana | 🟡 ALTO | Product Owner |
| **S-O-04** | No hay cambios organizacionales mayores (reestructura, layoffs) durante el proyecto | 🟡 ALTO | Management Elanco |
| **S-O-05** | Existe patrocinio ejecutivo activo (sponsor de Management) | 🟡 ALTO | Management Elanco |
| **S-O-06** | Usuarios finales están motivados y dispuestos a adoptar nuevas herramientas | 🟢 MEDIO | Product Owner |

### 11.7.3. Supuestos de Recursos

| # | Supuesto | Criticidad | Responsable Validación |
|---|----------|------------|------------------------|
| **S-R-01** | Equipo Aunergia (Project Manager, Funcional SAP, Consultor BI) está disponible con la dedicación planificada | 🔴 CRÍTICO | Aunergia Management |
| **S-R-02** | Funcional SAP puede dedicar 4-6h/semana al proyecto (sin sobrecarga) | 🟡 ALTO | Funcional SAP + Project Manager |
| **S-R-03** | Consultor BI puede dedicar 15-22h/semana sin conflictos con otros proyectos | 🟡 ALTO | Aunergia Management |
| **S-R-04** | TI Global tiene capacidad para atender tickets del proyecto en SLA de 1-2 semanas | 🟡 ALTO | TI Global Elanco |
| **S-R-05** | David Saboya (TechOps) actúa como enlace efectivo con TI Global | 🟢 MEDIO | David Saboya |

### 11.7.4. Supuestos de Cronograma

| # | Supuesto | Criticidad | Responsable Validación |
|---|----------|------------|------------------------|
| **S-C-01** | Kick-off se realiza el 6 de enero de 2026 como planificado | 🟡 ALTO | Product Owner + Project Manager |
| **S-C-02** | No hay extensiones de vacaciones o feriados no planificados | 🟢 MEDIO | Todos |
| **S-C-03** | Go/No-Go se aprueba al final de Fase 0 (10-feb-2026) | 🟡 ALTO | Product Owner |
| **S-C-04** | No hay interrupciones mayores por auditorías, cierres especiales, etc. | 🟢 MEDIO | Finanzas/Supply |

### 11.7.5. Supuestos de Presupuesto

| # | Supuesto | Criticidad | Responsable Validación |
|---|----------|------------|------------------------|
| **S-P-01** | Costos de infraestructura BigQuery y licencias SLT son asumidos por Elanco (no incluidos en el esfuerzo del proyecto) | 🔴 CRÍTICO | Finance Elanco |
| **S-P-02** | Licencias Power BI Pro (8 usuarios) ya están adquiridas y disponibles | 🔴 CRÍTICO | TI Elanco |
| **S-P-03** | Recurso SAP Basis estará disponible on-demand para configuración de SLT y administración SAP | 🔴 CRÍTICO | TI Elanco |
| **S-P-04** | No se requieren herramientas de terceros adicionales (ej. Fivetran, Tableau) | 🟢 MEDIO | Aunergia |
| **S-P-05** | El esfuerzo estimado se mantiene constante durante el proyecto (42 semanas comprimidas) | 🟢 MEDIO | Aunergia Management |
| **S-P-06** | El cliente proveerá todas las herramientas de software y licencias necesarias (SLT, conectores, Power BI, BigQuery) sin costo para Aunergia | 🔴 CRÍTICO | TI Elanco + Finance |
| **S-P-07** | Costos operativos mensuales (almacenamiento, procesamiento, networking) de GCP/BigQuery no forman parte del alcance económico del servicio profesional | 🔴 CRÍTICO | Finance Elanco |

---

## 11.8. Plan de Gestión de Riesgos

### 11.8.1. Monitoreo de Riesgos

**Frecuencia:** Revisión semanal en reunión de seguimiento

**Métricas:**
- 📊 Cantidad de riesgos ALTO por categoría
- 📊 Tendencia de riesgos (nuevos, cerrados, escalados)
- 📊 % de planes de mitigación ejecutados

**Herramienta:** Planilla de seguimiento de riesgos (Excel/Google Sheets)

### 11.8.2. Responsabilidades

| Rol | Responsabilidad |
|-----|-----------------|
| **Project Manager (PM)** | Monitoreo general, actualización de registro de riesgos, escalación |
| **Product Owner** | Decisión sobre riesgos organizacionales y presupuesto |
| **Consultor BI** | Identificación y mitigación de riesgos técnicos |
| **Funcional SAP** | Identificación de riesgos SAP y datos |
| **David Saboya (TI)** | Mitigación de riesgos de infraestructura y permisos |

### 11.8.3. Escalación

**Niveles de Escalación:**

1. **Nivel 1 (Equipo):** Riesgos BAJO y MEDIO → Manejo interno
2. **Nivel 2 (Product Owner):** Riesgos ALTO → Informar y solicitar apoyo
3. **Nivel 3 (Management):** Riesgos CRÍTICOS o bloqueantes → Escalación formal

**Criterios de Escalación:**
- Riesgo materializado con impacto > 2 semanas o cambios significativos al alcance
- Supuestos críticos invalidados (ej. falta de recurso SAP Basis, tablas no disponibles en BigQuery)
- Imposibilidad de cumplir con Criterio Go/No-Go

---

## 11.9. Criterios de Go/No-Go (Resumen)

Al final de la **Fase 0** (semana 5), se evaluará si continuar con el proyecto:

### ✅ Criterios GO (Continuar)

- ✅ Mínimo **12 de 18 transacciones SAP** con tablas completas en BigQuery
- ✅ Permisos SAP **completos** otorgados
- ✅ Accesos BigQuery (Data Editor) **activos**
- ✅ Backlog priorizado y **aprobado** por Product Owner
- ✅ No más de **2 riesgos ALTO bloqueantes** sin plan de mitigación
- ✅ Estimaciones refinadas dentro de **±15% del esfuerzo original** (510-690 horas)

### 🚫 Criterios NO-GO (Detener o Re-planear)

- 🚫 Menos de **8 transacciones** viables (< 50% del alcance)
- 🚫 Permisos SAP **NO otorgados** después de 4 semanas
- 🚫 Tablas críticas en BigQuery **NO disponibles** y sin solución alternativa
- 🚫 Más de **3 riesgos CRÍTICOS** sin mitigación efectiva
- 🚫 Estimaciones superan el esfuerzo planificado en **> 25%** (750+ horas)
- 🚫 Falta de patrocinio ejecutivo o Product Owner empoderado

### ⚠️ Criterios GO CON AJUSTES

- ⚠️ 8-11 transacciones viables → Reducir alcance, ajustar esfuerzos
- ⚠️ Complejidad mayor a la esperada → Extender cronograma (hasta +10 semanas sobre 42) o ajustar recursos
- ⚠️ Riesgos ALTO manejables → Implementar planes de contingencia

---

*Siguiente sección: [12_ENTREGABLES_Y_CONDICIONES_COMERCIALES.md](12_ENTREGABLES_Y_CONDICIONES_COMERCIALES.md)*
