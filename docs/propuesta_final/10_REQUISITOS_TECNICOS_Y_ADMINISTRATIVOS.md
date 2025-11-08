# 10. REQUISITOS TÉCNICOS Y ADMINISTRATIVOS

Nota de referencia cruzada: Ver también la sección `4.6 Supuestos y Requisitos Específicos de Fase 0` para los pre-requisitos operativos y criterios de Go/No-Go asociados al patrón de integración SAP SLT → BigQuery.

## 10.1. Requisitos Previos al Inicio del Proyecto

### 10.1.1. Requisitos Administrativos CRÍTICOS

Estos requisitos **DEBEN** estar resueltos antes del kick-off:

| # | Requisito | Responsable | Fecha Límite | ¿Bloquea Inicio? |
|---|-----------|-------------|--------------|------------------|
| 1 | **Aprobación del proyecto (1,590 horas)** | Management Elanco | 03-ene-2026 | ⛔ SÍ |
| 2 | **Firma de contrato** | Legal Aunergia + Elanco | 03-ene-2026 | ⛔ SÍ |
| 3 | **Designación de Product Owner** | Management Elanco | 20-dic-2025 | ⛔ SÍ |
| 4 | **Confirmación disponibilidad stakeholders** | Finanzas/Supply | 20-dic-2025 | ⚠️ Alta |
| 5 | **Acuerdo de confidencialidad (NDA) vigente** | Legal ambas partes | 20-dic-2025 | ⛔ SÍ |

---

## 10.2. Requisitos de Accesos y Permisos

### 10.2.1. Accesos SAP S/4HANA

**Power User Primario: Funcional SAP**

| Módulo | Rol Requerido | Transacciones Clave | Status | Ticket |
|--------|---------------|---------------------|--------|--------|
| **MM** | Z_MM_POWER_USER | ME2L, MM60, MB59, MB5B, ME23N | ⏳ | SAP-48219 |
| **SD** | Z_SD_POWER_USER | VA05 | ⏳ | SAP-48219 |
| **FI** | Z_FI_POWER_USER | FAGLL03, FB03, F.08, F.01, FBL1N, FBL5N | ⏳ | SAP-48219 |
| **CO** | Z_CO_POWER_USER | KSB1, KE24 | ⏳ | SAP-48219 |
| **Custom** | Z_CUSTOM_READ | ZLEL008, ZVEL015 | ⏳ | SAP-48219 |
| **Maestros** | Z_MD_READ | XK03, XD03 | ⏳ | SAP-48219 |

**Autorizaciones Especiales Requeridas:**
- ✅ S_TABU_DIS (Autorización lectura tablas)
- ✅ S_TABU_RFC (Autorización RFC para extracción)
- ✅ Exportación masiva de datos (sin límite de registros)
- ✅ Acceso a todas las sociedades CASA (Company Codes)

**Usuarios Backup:**
- Carolina Rondón (TI) - Mismo perfil
- Juan Sebastián Ravelo - Mismo perfil

**Fecha límite resolución:** 03 de enero de 2026 (antes de kick-off)

---

### 10.2.2. Accesos Google BigQuery

**Cuenta Corporativa Elanco:**

| Usuario | Rol BigQuery | Permisos | Status |
|---------|--------------|----------|--------|
| **Funcional SAP** | BigQuery Data Editor | Read/Write dataset casa_bi | ⏳ Pendiente |
| **Consultor BI** | BigQuery Data Editor | Read/Write dataset casa_bi | ⏳ Pendiente |
| **Project Manager** | BigQuery Data Viewer | Read-only dataset casa_bi | ⏳ Pendiente |
| **David Saboya (TI)** | BigQuery Admin | Full access | ✅ OK |
| **Usuarios Finanzas (2)** | BigQuery Data Viewer | Read-only dataset casa_bi | ⏳ Pendiente |
| **Usuarios Supply (2)** | BigQuery Data Viewer | Read-only dataset casa_bi | ⏳ Pendiente |

**Proyectos y Datasets:**
- **Proyecto GCP:** `elanco-casa-bi` o `elanco-erp`
- **Dataset Desarrollo:** `casa_bi_dev`
- **Dataset QA:** `casa_bi_qa`
- **Dataset Producción:** `casa_bi_prod`

**Service Accounts:**
- `sa-bigquery-etl@elanco-casa-bi.iam.gserviceaccount.com` (para pipelines)
- Permisos: BigQuery Job User, BigQuery Data Editor

**Fecha límite resolución:** 03 de enero de 2026 (antes de inicio Fase 1)

---

### 10.2.3. Accesos Microsoft Power BI

**Licencias Ya Adquiridas (Orden PR-55219):**

| Usuario | Licencia | Workspace | Status |
|---------|----------|-----------|--------|
| **Usuarios Finanzas (4)** | Power BI Pro | CASA_Finanzas | ✅ Activas |
| **Usuarios Supply (2)** | Power BI Pro | CASA_Supply | ✅ Activas |
| **TechOps (1)** | Power BI Pro | CASA_TechOps | ✅ Activa |
| **TI Global (1)** | Power BI Pro | CASA_Admin | ✅ Activa |

**Workspaces a Crear:**
- `CASA_BI_Development` (desarrollo)
- `CASA_BI_Production` (producción)

**Permisos Requeridos:**
- Consultor BI: Power BI Pro (temporal durante proyecto) o acceso como External Guest
- Funcional SAP: Viewer en workspaces para validación

**Fecha límite configuración:** 20 de noviembre de 2025

---

### 10.2.4. Otros Accesos

| Sistema/Herramienta | Usuario | Propósito | Status |
|---------------------|---------|-----------|--------|
| **Confluence/SharePoint** | Equipo Aunergia | Documentación colaborativa | ⏳ |
| **Git Repository** | Consultor BI | Versionado código SQL | ⏳ |
| **Cloud Storage** | Equipo Aunergia | Almacenamiento artefactos | ⏳ |

---

## 10.3. Requisitos de Infraestructura

### 10.3.1. Google Cloud Platform (BigQuery)

**Recursos Requeridos:**

| Recurso | Especificación | Responsable Provisión |
|---------|----------------|---------------------|
| **BigQuery Datasets** | 3 datasets (dev/qa/prod) | TI Global Elanco |
| **Almacenamiento** | ~500GB-1TB (estimado inicial) | TI Global Elanco |
| **Procesamiento** | On-demand (sin slots reservados) | TI Global Elanco |
| **Conectores SAP** | SAP SLT (Landscape Transformation Server) | TI Global Elanco |
| **Networking** | VPN/Private Service Connect (si req.) | TI Global Elanco |

**Costos Operativos Mensuales (asumidos por Elanco):**
- Almacenamiento: ~500GB-1TB (Active storage)
- Procesamiento: Query processing on-demand
- Streaming inserts: Según volumen transaccional
- **Responsable de costos:** Cliente (Elanco)

**Fecha límite provisión:** 14 de noviembre de 2025

---

### 10.3.2. Conectividad

**Conexiones Requeridas:**

```
┌────────────┐         ┌─────────────────┐         ┌──────────────┐
│  SAP S/4HANA   │────────▶│  SAP SLT Server │────────▶│  BigQuery    │
│  (On-prem) │  RFC/   │  (Replicación   │  HTTPS  │  (GCP Cloud) │
│            │  DB Log │   en tiempo real)│        │              │
└────────────┘         └─────────────────┘         └──────────────┘
                                                            │
                                                            │ ODBC/
                                                            │ Native
                                                            ▼
                                                    ┌──────────────┐
                                                    │  Power BI    │
                                                    │  Service     │
                                                    └──────────────┘
```

**Requisitos de Red:**
- Firewall abierto para tráfico SAP → GCP (puertos RFC)
- Certificados SSL válidos
- Latencia < 100ms (SAP ↔ BigQuery)

**Responsable:** TI Elanco + TI Global

---

### 10.3.3. Ambientes

| Ambiente | Propósito | Dataset BigQuery | Workspace Power BI |
|----------|-----------|------------------|--------------------|
| **Desarrollo** | Desarrollo y pruebas | `casa_bi_dev` | `CASA_BI_Development` |
| **QA** | Validaciones pre-producción | `casa_bi_qa` | `CASA_BI_Development` |
| **Producción** | Operación real | `casa_bi_prod` | `CASA_BI_Production` |

**Estrategia de Promoción:**
- Desarrollo → QA: Validación técnica (Aunergia)
- QA → Producción: Validación negocio (Stakeholders)

---

## 10.4. Requisitos de Datos

### 10.4.1. Disponibilidad de Datos Históricos

**Requerimiento:** Mínimo 24 meses de datos históricos por transacción

| Transacción | Fecha Desde | Fecha Hasta | Status Verificación |
|-------------|-------------|-------------|---------------------|
| VA05, KE24, FAGLL03, etc. | 01-nov-2023 | 31-oct-2025 | ⏳ Validar en Fase 0 |

**Validación:**
- Verificar en Fase 0 (Semana 1-2)
- Si faltan datos: Evaluar impacto en modelos predictivos (Fase 3)

---

### 10.4.2. Tablas SAP en BigQuery

**Tablas Críticas que DEBEN estar disponibles:**

| Transacción | Tablas SAP | Status BigQuery | Ticket |
|-------------|------------|-----------------|--------|
| VA05 | VBAK, VBAP, VBEP | ⏳ Validar | - |
| ZLEL008 | Z-tables (TBD) | ❌ No disponible | BQ-7713 |
| KSB1 | COBK, COEP, AUFK | ⏳ Validar | - |
| FAGLL03 | FAGLFLEXA, BKPF, BSEG | ⚠️ Parcial | BQ-7721 |
| KE24 | CE1*, CE4* | ❌ No disponible | BQ-7713 |
| ME2L | EKKO, EKPO | ⏳ Validar | - |
| ... | ... | ... | ... |

**Criterio Go/No-Go:**
- Mínimo 12 de 18 transacciones con tablas completas disponibles
- Si <12: Evaluar plan B (Azure o extracción RFC)

---

### 10.4.3. Diccionario de Datos SAP

**Documentación Requerida:**
- Diccionario de datos (Data Dictionary) de tablas SAP
- Descripción de campos clave
- Relaciones entre tablas (foreign keys)
- Lógica de cálculo de campos derivados

**Responsable:** TI Global Elanco  
**Fecha entrega:** Disponible durante Fase 0

---

## 10.5. Requisitos de Equipo y Recursos Humanos

### 10.5.1. Equipo Aunergia (Confirmado)

| Rol | Nombre | Disponibilidad | Dedicación |
|-----|--------|----------------|------------|
| **Project Manager** | Project Manager | Part-time | 4h/semana |
| **Analista SAP / Power User** | Funcional SAP | Part-time | 15-20h/semana |
| **Arquitecto de Datos / Desarrollador** | Consultor BI | Part-time | 20-25h/semana |

**Horarios de Trabajo:**
- Zona horaria: GMT-3 (Argentina) / GMT-5 (Colombia/Perú)
- Horario hábil: Lunes a Viernes, 9:00 AM - 6:00 PM
- Flexibilidad para reuniones con stakeholders Elanco

---

### 10.5.2. Equipo Elanco (Requerido)

#### Product Owner (CRÍTICO)

| Rol | Responsabilidades | Dedicación Requerida |
|-----|-------------------|---------------------|
| **Product Owner** | - Definir prioridades<br>- Aprobar entregables<br>- Toma de decisiones | 4-6h/semana |

**Perfil ideal:**
- Controller o Gerente Finanzas con conocimiento SAP
- Visión cross-funcional (Finanzas + Supply)
- Autoridad para tomar decisiones

#### Stakeholders Clave

| Área | Rol | Participación | Dedicación |
|------|-----|---------------|------------|
| **Finanzas** | Controller / Analista Senior | Workshops, validaciones, UAT | 2-3h/semana |
| **Supply Chain** | Manager / Planeador | Workshops, validaciones, UAT | 2-3h/semana |
| **TI TechOps** | David Saboya | Coordinación TI Global, tickets | 2h/semana |
| **TI Global** | SAP Basis / BigQuery Admin | Gestión de permisos y tablas | On-demand |
| **SAP Basis (ELANCO)** | Administrador SAP | **RECURSO PROVISTO POR EL CLIENTE**<br>- Gestión de usuarios y perfiles SAP<br>- Gestión de órdenes de transporte<br>- Instalación y configuración de SLT Server<br>- Monitoreo del sistema SAP<br>- Aplicación de SAP Notes<br>- Configuración de conexiones RFC<br>- Punto de contacto para incidencias técnicas SAP | On-demand durante el proyecto |

#### Usuarios Finales (Capacitación)

- 4-6 usuarios Finanzas
- 2-4 usuarios Supply Chain
- 1-2 usuarios Management
- **Total:** ~10-15 usuarios

#### SAP Basis (Recurso del Cliente - CRÍTICO)

| Rol | Responsabilidades | Dedicación Requerida |
|-----|-------------------|---------------------|
| **SAP Basis Administrator** | **RECURSO PROVISTO POR ELANCO**<br><br>**Responsabilidades:**<br>- Instalación y configuración de SAP Landscape Transformation Server (SLT)<br>- Gestión de usuarios y perfiles SAP (creación, modificación, autorizaciones)<br>- Gestión de órdenes de transporte SAP<br>- Aplicación de SAP Notes requeridas para el proyecto<br>- Configuración de conexiones RFC (Remote Function Call)<br>- Monitoreo del sistema SAP y servidor SLT<br>- Troubleshooting de incidencias técnicas SAP<br>- Asistencia en la configuración del BigQuery Connector<br>- Punto de contacto técnico para el equipo del proyecto | **On-demand durante el proyecto**<br><br>Estimado: 2-4h/semana durante Fase 1<br><br>Picos de actividad:<br>- Fase 0: Setup inicial de permisos<br>- Fase 1: Configuración de SLT |

**Nota Importante:** La disponibilidad de un recurso SAP Basis es **CRÍTICA** para el éxito del proyecto, especialmente durante la implementación de SAP SLT (Landscape Transformation Server) en la Fase 1.

---

## 10.6. Requisitos de Documentación Base

### 10.6.1. Documentación SAP

| Documento | Descripción | Responsable | Status |
|-----------|-------------|-------------|--------|
| **Diccionario de Datos SAP** | Descripción tablas y campos | TI Global | ⏳ |
| **Transacciones SAP - Guías** | Manuales de usuario SAP | Finanzas/Supply | ⏳ |
| **Mapeo de Cuentas Contables** | Chart of Accounts por país | Finanzas | ⏳ |
| **Estructura Organizacional** | Company Codes, Centros, Almacenes | TI | ⏳ |

### 10.6.2. Documentación de Procesos

| Documento | Descripción | Responsable | Status |
|-----------|-------------|-------------|--------|
| **Procesos de Cierre** | Cómo se hace cierre mensual hoy | Finanzas | ⏳ |
| **Flujo de Consolidación** | Cómo se consolida información hoy | Finanzas/Supply | ⏳ |
| **KPIs Actuales** | Métricas y cálculos existentes | Finanzas/Supply | ⏳ |

**Fecha entrega:** Durante Fase 0 (Semanas 1-2)

---

## 10.7. Requisitos de Seguridad y Compliance

### 10.7.1. Seguridad de Datos

**Clasificación de Datos:**
- Datos financieros: **CONFIDENCIAL**
- Datos de clientes/proveedores: **CONFIDENCIAL + PII**
- Datos operativos: **INTERNO**

**Políticas a Cumplir:**
- **PII** (Personally Identifiable Information): No exponer datos personales
- **Red Data**: Datos sensibles según políticas Elanco
- **Encriptación**: En tránsito (TLS 1.2+) y en reposo (AES-256)
- **Row-Level Security**: Segregación por país/área

### 10.7.2. Auditoría y Trazabilidad

**Logs Requeridos:**
- ✅ Log de accesos a datasets BigQuery
- ✅ Log de ejecución de pipelines (quién, cuándo, qué)
- ✅ Log de accesos a dashboards Power BI
- ✅ Registro de cambios en datos (audit trail)



### 10.7.3. Backup y Disaster Recovery

| Elemento | Frecuencia Backup | RPO | RTO |
|----------|-------------------|-----|-----|
| **Datos BigQuery** | Automático (GCP) | 24h | 4h |
| **Código SQL** | Cada commit (Git) | 0 | 1h |
| **Dashboards Power BI** | Semanal | 7 días | 4h |

**Responsable:** TI Elanco (infraestructura) + Aunergia (código)

---

## 10.8. Requisitos de Comunicación

### 10.8.1. Canales de Comunicación

| Canal | Propósito | Participantes | Frecuencia |
|-------|-----------|---------------|------------|
| **Email** | Comunicación formal, entregables | Todos | Según necesidad |
| **MS Teams / Slack** | Comunicación rápida, consultas | Equipo proyecto | Diario |
| **Videollamadas** | Reuniones, workshops | Todos + Stakeholders | Según agenda |
| **Confluence/SharePoint** | Documentación compartida | Todos | Continuo |

### 10.8.2. Reuniones Establecidas

Ver sección 9.10 del documento [09_CRONOGRAMA_SEMANAL.md](09_CRONOGRAMA_SEMANAL.md)

---

## 10.9. Requisitos de Capacitación

### 10.9.1. Capacitación Pre-Proyecto (Deseable)

**Para Equipo Elanco:**
- Introducción a BigQuery (SQL básico) - 4 horas
- Introducción a Power BI (si no conocen) - 4 horas

**Responsable:** TI Elanco o Aunergia (cotización adicional si requerido)

### 10.9.2. Capacitación Durante Proyecto

**Incluida en la propuesta:**
- Power Users: 4 horas (uso avanzado dashboards)
- Usuarios Finanzas: 3 horas
- Usuarios Supply: 3 horas
- Sesión refuerzo: 2 horas

---

## 10.10. Checklist de Inicio de Proyecto

### ✅ Antes del Kick-off (6-ene-2026)

- [ ] Contrato firmado
- [ ] Proyecto aprobado (1,590 horas, 42 semanas)
- [ ] Product Owner designado
- [ ] NDA vigente
- [ ] Kick-off meeting agendado (2-3 horas)

### ✅ Durante Fase 0 (Semanas 0-6)

- [ ] Accesos SAP solicitados (Ticket SAP-48219)
- [ ] Accesos BigQuery solicitados
- [ ] Accesos Power BI configurados
- [ ] Ambientes BigQuery creados
- [ ] Documentación base entregada
- [ ] Stakeholders confirmados y disponibles

### ✅ Antes de Inicio Fase 1 (13-ene-2026)

- [ ] Permisos SAP completos confirmados ✓
- [ ] Mínimo 12 transacciones con tablas en BigQuery ✓
- [ ] Accesos Data Editor activos ✓
- [ ] Backlog priorizado y aprobado ✓
- [ ] Go/No-Go aprobado ✓

---

## 10.11. Responsabilidades de Elanco

**Responsabilidades que Elanco DEBE asumir:**

1. ✅ **SAP Landscape Transformation Server (SLT):** Instalación, configuración, licenciamiento y operación del servidor SLT
2. ✅ **Recurso SAP Basis:** Proveer administrador SAP Basis para configuración de SLT, permisos y administración del sistema SAP
3. ✅ **Infraestructura GCP:** Provisión y costos de BigQuery
4. ✅ **Licencias:** Power BI Pro (ya adquiridas), licencias SLT y BigQuery Connector
5. ✅ **Permisos y Accesos:** Gestión de tickets con TI Global
6. ✅ **Ambientes:** Provisión de ambientes dev/qa/prod
7. ✅ **Documentación Base:** Entregar documentación SAP y procesos
8. ✅ **Disponibilidad Stakeholders:** Asegurar participación en workshops/UAT
9. ✅ **Coordinación TI:** Gestión con TI Global para tickets
10. ✅ **Backup y DR:** Responsabilidad de infraestructura

**Nota:** La **operación y monitoreo continuo** de SAP SLT (jobs, colas de replicación, alerts) y conectores asociados **no están incluidos** en las horas del servicio profesional de Aunergia y son **responsabilidad de Elanco** (TI Global/SAP Basis). Aunergia puede apoyar en diagnóstico puntual dentro de las horas de proyecto o mediante cotización adicional.

---

## 10.12. Responsabilidades de Aunergia

**Responsabilidades que Aunergia asume:**

1. ✅ **Desarrollo:** Pipelines ETL, dashboards Power BI
2. ✅ **Arquitectura:** Diseño de Data Lake y modelo dimensional
3. ✅ **Testing:** Validación de calidad de datos
4. ✅ **Documentación:** Técnica, funcional y de usuario
5. ✅ **Capacitación:** Usuarios finales y power users
6. ✅ **Project Management:** Coordinación y seguimiento
7. ✅ **Periodo Post Go-Live:** Ajustes menores sujetos a evaluación (sin compromiso incluido)

---

*Siguiente sección: [11_RIESGOS_Y_SUPUESTOS.md](11_RIESGOS_Y_SUPUESTOS.md)*
