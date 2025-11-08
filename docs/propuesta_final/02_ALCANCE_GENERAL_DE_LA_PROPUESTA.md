# 2. ALCANCE GENERAL DE LA PROPUESTA

## 2.1. Visión del Proyecto

### 2.1.1. Objetivo General

Implementar una **solución integral de centralización de datos de análisis** que permita a Elanco Animal Health (Operación CASA) automatizar la extracción, consolidación y análisis de información empresarial desde SAP S/4HANA, utilizando Google BigQuery como Data Lake central y Microsoft Power BI como plataforma de reportería y analítica.

### 2.1.2. Objetivos Específicos

1. **Automatizar extracción de datos SAP**
   - Eliminar procesos manuales de descarga de reportes
   - Implementar pipelines automatizados para 18 transacciones SAP
   - Establecer frecuencias de sincronización óptimas por transacción

2. **Centralizar información de países CASA**
   - Crear repositorio único en BigQuery para datos de todos los países
   - Estandarizar estructuras de datos entre países
   - Implementar historización de datos (mínimo 24 meses)

3. **Democratizar el acceso a datos**
   - Desarrollar dashboards Power BI para diferentes niveles organizacionales
   - Implementar Row-Level Security (RLS) por país y área
   - Capacitar usuarios en autoservicio de reportes

4. **Mejorar calidad y confiabilidad de datos**
   - Establecer procesos de validación automatizados
   - Implementar controles de calidad SAP ↔ BigQuery
   - Documentar diccionario de datos unificado

5. **Habilitar capacidades analíticas avanzadas**
   - Crear base técnica para modelos predictivos futuros
   - Establecer arquitectura escalable para Machine Learning
   - Diseñar roadmap de analítica avanzada

---

## 2.2. Alcance del Proyecto

### 2.2.1. Incluido en el Alcance

#### ✅ Sistemas Fuente
- **SAP S/4HANA:** Datos de 18 transacciones priorizadas (ver sección 3)
  - *Nota técnica:* Se replicarán las **tablas SAP subyacentes** (estimado 70-90 tablas) asociadas a estas transacciones
  - Las transacciones SAP son interfaces de usuario; lo que se replica mediante SLT son las tablas de base de datos
- **Módulos SAP:** MM, SD, FI, CO
- **Países:** Todos los países de la operación CASA (~10 países)
- **Historización:** Mínimo 24 meses de datos históricos
- **Volumen de Tablas:** Estimación de **70-90 tablas SAP** a replicar.

#### ✅ Infraestructura de Datos
- **Data Lake:** Google BigQuery (dataset casa_bi: entornos dev / qa / prod)
- **Arquitectura:** Zonas RAW → PROCESSED → CURATED
- **Conectores:** **SAP SLT (Landscape Transformation Server)** para replicación en tiempo real SAP S/4HANA ↔ BigQuery
  - *Nota: La instalación y configuración de SLT es responsabilidad del cliente (Elanco) con soporte del equipo SAP Basis*
- **Procesamiento:** Pipelines ETL/ELT con BigQuery SQL
- **Monitoreo:** Logs de ejecución, alertas de errores, dashboards operativos

#### ✅ Capa Semántica y Modelado
- **Modelo dimensional:** Esquema estrella/copo de nieve
- **Dimensiones principales:** Tiempo, Geografía (país), Producto, Cliente, Proveedor, Centro, Cuenta Contable
- **Tablas de hechos:** Ventas, Compras, Inventarios, Movimientos, Transacciones Financieras, OPEX
- **Métricas (KPIs):** ~30-40 métricas clave definidas con el negocio

#### ✅ Reportería y Visualización
- **Plataforma:** Microsoft Power BI Pro
- **Dashboards:** 12 dashboards ejecutivos (ver detalle en Fase 2)
- **Conexión:** Nativa Power BI ↔ BigQuery (o ODBC Simba)
- **Seguridad:** Row-Level Security (RLS) por país/área/usuario
- **Actualización:** Programada (diaria/semanal según dashboard)
- **Capacitación:** Usuarios finales en uso de dashboards

#### ✅ Documentación
- **Documentación técnica:**
  - Arquitectura de datos completa
  - Diccionario de datos SAP → BigQuery
  - Código SQL de pipelines (versionado en Git)
  - Mapeos de transacciones SAP a tablas BigQuery
  - Guías de troubleshooting
  
- **Documentación funcional:**
  - Catálogo de dashboards y métricas
  - Manual de usuario Power BI
  - Procedimientos operativos (runbooks)
  - Plan de contingencia

- **Documentación de gobierno:**
  - Políticas de acceso y seguridad
  - Estándares de nomenclatura
  - Procesos de cambio
  - SLAs y métricas de calidad

#### ✅ Capacitación y Transferencia de Conocimiento
- **Power users:** 3 sesiones de capacitación técnica (Funcional SAP + 2 backups)
- **Usuarios finales:** 2 sesiones por área (Finanzas, Supply Chain)
- **TI:** 1 sesión de handover técnico (David Saboya y equipo)
- **Materiales:** Videos tutoriales, guías paso a paso

#### ✅ Fase 3: Descripción Conceptual de Analítica Predictiva
- Catálogo de casos de uso de Machine Learning
- Análisis exploratorio de datos (EDA) para modelos predictivos
- Propuesta de arquitectura ML (sin implementación)
- Roadmap de desarrollo de modelos (sin estimación de esfuerzo)
- Recomendaciones para siguientes pasos

### 2.2.2. Excluido del Alcance

#### ❌ Sistemas Adicionales (Fuera del Alcance Inicial)
- Datos de sistemas diferentes a SAP S/4HANA
- Integración con CRM, HRIS u otros sistemas transaccionales
- Datos de redes sociales o fuentes externas
- Datos de sensores IoT o dispositivos móviles

#### ❌ Módulos SAP No Incluidos
- Módulos de producción (PP - Production Planning)
- Módulos de proyectos (PS - Project Systems)
- Módulos de recursos humanos (HCM - Human Capital Management)
- Módulos de mantenimiento (PM - Plant Maintenance)

#### ❌ Tablas/Transacciones SAP Adicionales
- Solo se incluyen las **tablas SAP asociadas a las 18 transacciones priorizadas** (ver sección 3)
- Tablas o transacciones adicionales requerirán cotización separada
- Si durante Fase 0 se identifican tablas adicionales necesarias, se evaluará el impacto en esfuerzo

#### ❌ Desarrollo de Modelos Predictivos (Fase 3)
- **Solo se entrega descripción conceptual** en Fase 3
- La **implementación de modelos ML** se cotiza en proyecto separado
- Estimación preliminar para implementación: 8-10 semanas
- Incluye: Data Science, MLOps, entrenamiento, deployment, monitoreo

#### ❌ Infraestructura y Licencias (Responsabilidad del Cliente)
- **SAP Landscape Transformation Server (SLT):** Instalación, configuración y licenciamiento - provisto y configurado por Elanco con su equipo SAP Basis
- Licencias de Google Cloud Platform (BigQuery) - costo asumido por Elanco
- Licencias Power BI Pro - ya adquiridas por Elanco
- Infraestructura de red y seguridad - gestionada por TI Elanco
- Ambientes de desarrollo/QA/producción - provisionados por TI Global
- **Recurso SAP Basis:** Provisto por Elanco para tareas de administración SAP y configuración de SLT

#### ❌ Soporte Post-Implementación
- Mantenimiento evolutivo continuo - se cotiza por separado
- Desarrollo de nuevos dashboards - se cotiza por separado

#### ❌ Rollout a Nuevas Regiones
- Alcance limitado a **operación CASA** (Centroamérica y Sudamérica)
- Rollout a otras regiones (EMEA, APAC, NA) se cotiza por separado

#### ❌ Integración con Herramientas Legacy
- Migración de reportes Business Objects - no incluida
- Conversión de macros Excel existentes - no incluida
- Integración con herramientas de terceros - no incluida

---

## 2.3. Enfoque Metodológico

### 2.3.1. Metodología Ágil Adaptada

El proyecto se ejecutará siguiendo principios de **metodología ágil** adaptados a la naturaleza de implementación de infraestructura de datos:

#### Sprints de 2 Semanas
- Planificación de sprint (1-2 horas)
- Desarrollo y testing (8-9 días)
- Demo y retrospectiva (1-2 horas)
- Total: ~10 días hábiles por sprint

#### Entregables Incrementales
- Cada fase entrega valor funcional
- Validaciones con usuarios al finalizar cada sprint
- Feedback continuo incorporado en siguientes iteraciones

#### Roles y Responsabilidades Claras
- **Product Owner:** Representante de Finanzas/Supply (Elanco)
- **Scrum Master:** Project Manager (Aunergia) - facilita, no controla
- **Development Team:** Funcional SAP + Consultor BI
- **Stakeholders:** TI Global, áreas de negocio

### 2.3.2. Fases del Proyecto

El proyecto se divide en **4 fases** con objetivos específicos:

```
┌──────────────────────────────────────────────────────────────────────────┐
│                             ROADMAP CONSOLIDADO                           │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  FASE 0 (6 sem / 235h)   FASE 1 (22 sem / 696h)   FASE 2 (14 sem / 659h)  │
│  ────────────────────    ──────────────────────   ─────────────────────   │
│  Due Diligence           Data Lake Construction   Dashboards Power BI     │
│                                                                          │
│  FASE 3 (Roadmap ML conceptual, sin horas incluidas en total 1,590h)      │
│                                                                          │
│  Duración total proyecto (Fases 0-2): 42 semanas / 1,590h                │
│                                                                          │
│  └─ Go/No-Go                                                             │
│     Decision al cierre de Fase 0                                         │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

#### **Fase 0: Revisión del Alcance y Factibilidad** (6 semanas, 235h consolidado)
- **Objetivo:** Validar viabilidad técnica, resolver issues de permisos, definir backlog
- **Entregables:** Plan técnico, backlog priorizado, Go/No-Go documentado
- **Decisión crítica:** ¿Continuar con Fase 1 o replantear enfoque?

#### **Fase 1: Construcción de Data Lake** (22 semanas, 696h consolidado)
- **Objetivo:** Automatizar extracción SAP → BigQuery para 18 transacciones
- **Entregables:** Pipelines funcionales, datos centralizados, validaciones de calidad
- **Hito:** Primer dashboard operativo con datos reales

#### **Fase 2: Modelado y Dashboards Power BI** (14 semanas, 659h consolidado)
- **Objetivo:** Crear capa semántica y dashboards ejecutivos
- **Entregables:** 12 dashboards, RLS configurado, usuarios capacitados
- **Hito:** Go-live de reportería centralizada

#### **Fase 3: Arquitectura de Analítica Predictiva** (descripción)
- **Objetivo:** Diseñar roadmap de modelos ML sin implementar
- **Entregables:** Catálogo casos de uso, EDA, arquitectura propuesta
- **Nota:** Implementación se cotiza en proyecto separado

---

## 2.4. Criterios de Éxito

### 2.4.1. Criterios Cuantitativos

| Métrica | Objetivo |
|---------|----------|
| **Tablas SAP replicadas** | 100% de las tablas identificadas para las 18 transacciones (~70-90 tablas) |
| **Transacciones SAP con datos disponibles** | 18 de 18 (100%) |
| **Reducción tiempo de consolidación** | ≥ 70% (de 3-5 días a < 1 día) |
| **Tiempo de actualización de dashboards** | ≤ 24 horas desde cierre de periodo |
| **Exactitud de datos (SAP vs BigQuery)** | ≥ 99.5% |
| **Disponibilidad del sistema** | ≥ 99% (horario hábil) |
| **Usuarios capacitados** | ≥ 15 usuarios (power users + finales) |
| **Adopción de dashboards** | ≥ 80% de usuarios activos a 30 días post go-live |
| **Satisfacción de usuarios** | ≥ 4.0/5.0 en encuesta post-implementación |

### 2.4.2. Criterios Cualitativos

✅ **Eliminación de procesos manuales críticos**
- Los usuarios no deben descargar manualmente reportes SAP para análisis rutinarios
- La consolidación entre países debe ser automática

✅ **Versión única de la verdad**
- Una sola fuente de datos confiable para todos los usuarios
- Trazabilidad completa de cambios y actualizaciones

✅ **Autoservicio de reportes**
- Los usuarios finales pueden crear sus propios análisis sin depender de TI
- Reducción de solicitudes de reportes ad-hoc a TI

✅ **Fundamento para analítica avanzada**
- Infraestructura escalable lista para modelos predictivos
- Datos históricos completos y de calidad disponibles

✅ **Transferencia de conocimiento efectiva**
- Equipo Elanco (TI + negocio) puede mantener y evolucionar la solución
- Documentación completa y accesible

---

## 2.5. Supuestos Clave

### 2.5.1. Supuestos Técnicos

| # | Supuesto | Validación Requerida |
|---|----------|---------------------|
| 1 | BigQuery será la plataforma definitiva (o se evalúa Azure en Fase 0) | Fase 0: Semana 1 |
| 2 | Las 18 transacciones SAP son suficientes para MVP | Fase 0: Workshop |
| 3 | Los datos históricos están disponibles en SAP (mínimo 24 meses) | Fase 0: Semana 2 |
| 4 | Power BI puede conectarse nativamente a BigQuery | Fase 0: Semana 1 |
| 5 | No se requieren interfaces en tiempo real (batch nocturno es aceptable) | Fase 0: Workshop |
| 6 | Las tablas SAP necesarias estarán disponibles en BigQuery (post-tickets) | Fase 0: Semana 3-4 |
| 7 | No hay restricciones de compliance que bloqueen centralización de datos | Fase 0: Semana 1 |

### 2.5.2. Supuestos de Recursos

| # | Supuesto | Responsable Validación |
|---|----------|----------------------|
| 1 | Funcional SAP tendrá permisos SAP completos al iniciar Fase 1 | TI Global / David Saboya |
| 2 | El equipo de Finanzas/Supply estará disponible para validaciones (~4h/semana) | Sponsor del proyecto |
| 3 | TI Global dará soporte para tickets de tablas BigQuery (respuesta < 1 semana) | David Saboya |
| 4 | Los 8 usuarios Power BI Pro tienen sus licencias activas | TI Elanco |
| 5 | Existe acuerdo de confidencialidad vigente Aunergia-Elanco | Legal |
| 6 | Ambiente de desarrollo/QA en BigQuery estará disponible | TI Global |
| 7 | Cuentas y credenciales corporativas estarán listas al inicio del proyecto | TI Elanco |

### 2.5.3. Supuestos de Tiempo

| # | Supuesto | Implicación |
|---|----------|-------------|
| 1 | Disponibilidad part-time: 20-25h/semana Consultor BI | Duración: 13-17 semanas |
| 2 | Disponibilidad de Funcional SAP según gestión de Aunergia (~15-20h/semana) | Sin impacto |
| 3 | Respuestas de TI Global en máximo 1 semana para tickets críticos | Holguras en cronograma |
| 4 | Validaciones con usuarios en máximo 3 días hábiles | Planificado en sprints |
| 5 | No hay periodos de bloqueo (vacaciones, cierre de año) | Ajustar cronograma |

---

## 2.6. Restricciones del Proyecto

### 2.6.1. Restricciones de Esfuerzo

- **Esfuerzo total estimado:** 1,590 horas (42 semanas)
- **No se admiten incrementos de esfuerzo** sin aprobación previa por cambios de alcance
- **Equipo completo:** Consultor BI (961h), Funcional SAP (484h), Project Manager (145h)

### 2.6.2. Restricciones Temporales

- **Duración total:** 42 semanas (~10 meses)
- **Fecha inicio deseada:** 6 de enero de 2026
- **Fecha límite para Fase 2:** 20 de septiembre de 2026
- **Consideraciones:** Consultor BI trabaja máximo 6h/día (30h/semana)

### 2.6.3. Restricciones Tecnológicas

- **Plataformas mandatorias:** SAP S/4HANA, BigQuery, Power BI (definidas por Elanco)
- **No se pueden usar herramientas de terceros** sin aprobación de TI Global
- **Cumplimiento de políticas corporativas** de seguridad y privacidad de datos
- **Restricciones de red:** Acceso a BigQuery desde red corporativa Elanco

### 2.6.4. Restricciones de Recursos

- **Personal Aunergia:** 2-3 personas (Project Manager, Funcional SAP, Consultor BI)
- **Disponibilidad part-time:** No hay dedicación full-time
- **Soporte TI Global:** Limitado a tickets (no desarrollo)
- **Power users Elanco:** Disponibilidad limitada por tareas operativas

---

## 2.7. Dependencias Críticas

### 2.7.1. Dependencias Externas (Bloqueantes)

| Dependencia | Responsable | Fecha Límite | Impacto si No se Cumple |
|-------------|-------------|--------------|-------------------------|
| **Permisos SAP completos** (Ticket SAP-48219) | TI Global | 10-nov-2025 | ⛔ Bloquea inicio Fase 1 |
| **Tablas BigQuery disponibles** (Tickets BQ-7713, BQ-7721) | TI Global | 17-nov-2025 | ⚠️ Retrasa Fase 1 (~2 semanas) |
| **Accesos Data Editor BigQuery** (6 usuarios) | TI Elanco | 14-nov-2025 | ⚠️ Retrasa inicio desarrollo |
| **Aprobación presupuesto** | Finanzas Elanco | 10-nov-2025 | ⛔ Bloquea proyecto completo |
| **Definición de Product Owner** | Management Elanco | 11-nov-2025 | ⚠️ Retrasa decisiones |

### 2.7.2. Dependencias Internas (Gestionables)

| Dependencia | Responsable | Fecha Límite | Mitigación |
|-------------|-------------|--------------|------------|
| **Workshop priorización transacciones** | Funcional SAP + Áreas negocio | 18-nov-2025 | Sesiones virtuales asíncronas |
| **Validación arquitectura BigQuery** | Consultor BI | 15-nov-2025 | Iniciar análisis antes de kick-off |
| **Definición de KPIs** | Finanzas + Supply | 25-nov-2025 | Usar KPIs estándar como base |
| **Ambiente desarrollo BigQuery** | TI Elanco | 14-nov-2025 | Usar ambiente compartido temporalmente |

---

## 2.8. Entregables Generales del Proyecto

### 2.8.1. Por Fase

#### **Fase 0: Due Diligence**
1. Plan técnico detallado de implementación
2. Backlog definitivo de transacciones SAP priorizado
3. Arquitectura SAP → BigQuery → Power BI aprobada
4. Checklist de permisos completo (SAP + BigQuery)
5. Plan de extracción por módulo (MM, SD, FI, CO)
6. Matriz de riesgos actualizada
7. Criterios de calidad de datos definidos
8. Documento Go/No-Go para Fase 1

#### **Fase 1: Data Lake**
1. Pipelines automatizados para 18 transacciones SAP
2. Dataset BigQuery estructurado (zonas RAW, PROCESSED, CURATED)
3. Historización de datos implementada (24 meses)
4. Diccionarios de datos documentados (SAP ↔ BigQuery)
5. Reportes de validación de calidad de datos
6. Monitoreo de costos BigQuery implementado
7. Código versionado en repositorio Git
8. Documentación técnica completa
9. Scripts de contingencia y rollback

#### **Fase 2: Dashboards**
1. Modelo de datos Power BI certificado
2. 12 dashboards productivos (Financiero General, Ventas, Inventario, OPEX, Ejecutivo, Supply Chain, Compras, Rentabilidad, Cuentas por Pagar, Cuentas por Cobrar, Controlling, Estadístico Regional)
3. Row-Level Security configurado por país/área
4. Conexión Power BI ↔ BigQuery validada
5. Manual de usuario Power BI (español)
6. Videos tutoriales (<5 min por dashboard)
7. Capacitación usuarios finales completada (registro de asistencia)
8. Plan de soporte y mantenimiento
9. UAT firmado por stakeholders

#### **Fase 3: ML Roadmap** (Solo Descripción)
1. Catálogo de casos de uso de Machine Learning
2. Análisis exploratorio de datos (EDA) con visualizaciones
3. Propuesta de arquitectura ML (diagramas)
4. Roadmap de desarrollo de modelos (sin estimaciones)
5. Recomendaciones para siguiente proyecto

### 2.8.2. Documentación Transversal

📋 **Al finalizar el proyecto se entregará:**

1. **Arquitectura Completa**
   - Diagramas de arquitectura técnica (Visio/Draw.io)
   - Diagrama de flujo de datos end-to-end
   - Documentación de decisiones arquitectónicas (ADRs)

2. **Documentación Técnica**
   - Código SQL comentado (BigQuery)
   - Modelos de datos (ERD)
   - Mapeos de campos SAP → BigQuery (Excel/CSV)
   - Guías de troubleshooting

3. **Documentación Funcional**
   - Catálogo de dashboards y métricas
   - Glosario de términos de negocio
   - Procedimientos operativos (SOPs)
   - FAQs para usuarios

4. **Documentación de Gobierno**
   - Políticas de acceso y seguridad
   - Estándares de nomenclatura
   - Procesos de gestión de cambios
   - SLAs y métricas de calidad

5. **Materiales de Capacitación**
   - Presentaciones PowerPoint
   - Videos tutoriales grabados
   - Ejercicios prácticos
   - Evaluaciones de conocimiento

---

*Siguiente sección: [03_TRANSACCIONES_SAP_INCLUIDAS.md](03_TRANSACCIONES_SAP_INCLUIDAS.md)*
