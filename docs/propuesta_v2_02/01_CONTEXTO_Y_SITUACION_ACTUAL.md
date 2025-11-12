# 1. CONTEXTO Y SITUACIÓN ACTUAL

## 1.1. Sobre Elanco Animal Health

**Elanco Animal Health** es una compañía global líder en salud animal, guiada por el propósito fundamental de que **los animales sanos son clave para resolver problemas relevantes del mundo**. Con presencia en más de 90 países, Elanco se dedica a desarrollar productos y servicios que mejoran la salud y el bienestar animal, contribuyendo así a la seguridad alimentaria global y al bienestar humano.

### Operación CASA (Centroamérica y Sudamérica)

La operación CASA de Elanco abarca más de 10 países en la región, incluyendo:
- Países de Centroamérica
- Brasil
- Argentina
- Chile
- Perú
- Colombia
- Uruguay
- Otros mercados sudamericanos

Esta operación regional maneja volúmenes significativos de transacciones comerciales, financieras y logísticas que requieren análisis constante para la toma de decisiones estratégicas y operativas.

---

## 1.2. Situación Actual: Problemática Identificada

### 1.2.1. Procesos Manuales de Extracción de Datos

Los equipos de **Finanzas**, **Supply Chain** y otras áreas de negocio actualmente realizan procesos manuales intensivos para obtener información de análisis:

#### Extracción Manual desde SAP S/4HANA

- Los usuarios acceden diariamente a **múltiples transacciones SAP** (VA05, ZLEL008, KSB1, FAGLL03, KE24, FB03, entre otras)
- Descargan reportes individuales de cada transacción
- El proceso se repite para cada país de la región CASA
- No existe automatización de estas extracciones
- Los usuarios requieren conocimientos avanzados de SAP para navegar el sistema

**Tiempo estimado actual:** 2-3 horas diarias por usuario

#### Consolidación Manual en Excel

- Los datos extraídos de diferentes países se combinan manualmente mediante archivos Excel
- Se realizan **"estrellados"** (cruces) de información entre múltiples hojas de cálculo
- Proceso propenso a errores humanos
- Versionado manual de archivos sin control centralizado
- Dificultad para mantener consistencia en fórmulas y cálculos

**Tiempo estimado actual:** 3-5 días por cierre mensual

#### Conectores Heterogéneos

- Se utilizan herramientas como **Business Objects** con conectividad limitada a SAP
- Múltiples herramientas sin integración entre sí
- Licencias subutilizadas por complejidad de uso
- Falta de estandarización en métodos de extracción

### 1.2.2. Centralización Fragmentada

**Problema principal:** No existe un repositorio unificado de datos que permita análisis integrado.

**Consecuencias:**
- Cada área mantiene sus propios archivos y bases de datos locales
- Información duplicada en múltiples ubicaciones
- Versiones desactualizadas o contradictorias de los mismos datos
- Imposibilidad de realizar análisis cruzados entre áreas
- Dificultad para rastrear cambios históricos

**Ejemplo:** Un analista de Supply Chain necesita datos financieros debe:
1. Solicitar archivo a Finanzas
2. Validar que sea la versión más reciente
3. Cruzar manualmente con sus propios datos
4. Total: 2-3 horas de trabajo + esperas

### 1.2.3. Reportería en Power BI Desconectada

Elanco ha adquirido **8 licencias Power BI Pro** para la región CASA:
- 4 licencias para Finanzas
- 2 licencias para Supply Chain
- 1 licencia para TechOps
- 1 licencia para TI Global

**Problema:** Estas licencias operan sobre datos **descentralizados y desactualizados**:
- Los dashboards se conectan a archivos Excel locales
- Actualización manual de datasets
- Sin conexión directa a fuentes de datos corporativas
- Reportes con información de 3-5 días de antigüedad

**Inversión subutilizada:** Licencias Pro con capacidades avanzadas (RLS, sharing, scheduled refresh) no aprovechadas por falta de infraestructura de datos.

### 1.2.4. Impacto en el Negocio

Esta situación genera múltiples problemas operativos y estratégicos:

#### Tiempo Operativo

- **Alto consumo de tiempo** en tareas repetitivas de extracción y consolidación
- Personal calificado dedicado a labores manuales en lugar de análisis de valor agregado
- Retrasos en cierre mensual y reportes financieros
- Estimación: **15-20 horas semanales** por área desperdiciadas en tareas manuales

#### Calidad de Datos

- **Riesgo de inconsistencias** por errores humanos en consolidación manual
- Dificultad para validar la exactitud de los datos
- Múltiples versiones de "la verdad" según quién haga el reporte
- Problemas de trazabilidad y auditoría

#### Capacidades Analíticas

- **Limitaciones para análisis históricos** (datos no estructurados ni archivados sistemáticamente)
- Imposibilidad de realizar análisis comparativos entre países
- Falta de capacidad para análisis de tendencias
- **Imposibilidad de realizar analítica avanzada o predictiva**

#### Toma de Decisiones

- Decisiones basadas en datos con 3-7 días de antigüedad
- Falta de visibilidad en tiempo real de indicadores clave
- Limitaciones para responder rápidamente a cambios del mercado
- Dependencia de personal específico que "conoce los datos"

---

## 1.3. Experiencia Previa con BigQuery

### 1.3.1. Implementación Corporativa

Elanco ha implementado **Google BigQuery** como plataforma de Data Lake corporativa en otras regiones operativas (principalmente América del Norte y Europa). Esta plataforma forma parte de la estrategia global de datos de la compañía.

#### Infraestructura Existente

- **Plataforma:** Google Cloud Platform (GCP)
- **Data Lake:** Google BigQuery
- **Dataset corporativo:** ERP Enterprise Data Product
- **Datos SAP:** Replicados desde SAP S/4HANA mediante conectores certificados
- **Herramientas complementarias:**
  - BigQuery Studio (entorno de desarrollo SQL)
  - ODBC Simba (conectividad con herramientas BI)
  - Gemini AI Cloud Companion (asistencia SQL - opcional)

### 1.3.2. Piloto en Sudamérica (dataset casa_bi)

Para la región de Sudamérica, TI Global inició un piloto con el **dataset casa_bi** en BigQuery (anteriormente referido como “CASA”). El objetivo era replicar el éxito de otras regiones y centralizar datos SAP de los países CASA.

#### Resultados del Piloto

El piloto encontró **obstáculos significativos** que impidieron su continuidad:

### 1.3.3. Obstáculos Identificados

Según correo de **David Saboya** (Analista IT TechOps CASA) del 9 de octubre de 2025:

> *"Específicamente se presentaron dos issues durante el desarrollo:"*

#### **Issue #1: Permisos SAP Insuficientes**

**Problema reportado:**
> *"El usuario asignado como 'power user' para hacer la integración mediante BigQuery no contaba con todos los permisos para visualizar transacciones en SAP"*

**Detalles:**
- El power user asignado no tenía acceso completo a todas las transacciones SAP necesarias
- Módulos afectados: MM (Materials Management), SD (Sales & Distribution), FI (Financial Accounting), CO (Controlling)
- Transacciones críticas bloqueadas: ZLEL008 (inventario custom), KSB1 (órdenes CO), FAGLL03 (mayor general)
- Proceso de solicitud de permisos lento (requiere tickets a TI Global)

**Estado actual:**
- Ticket SAP-48219 escalado a TI Global para solicitud de permisos completos
- Roles requeridos: MM, SD, FI, CO con autorización de exportación masiva
- Tiempo estimado de resolución: 2-4 semanas

#### **Issue #2: Tablas SAP No Disponibles en BigQuery**

**Problema reportado:**
> *"Algunas tablas [SAP] no se encuentran en el dataset de BigQuery y hay que solicitar el ingreso de estas por tickets de TI"*

**Detalles:**
- Las tablas necesarias para algunas transacciones no están replicadas en el dataset casa_bi
- Particularmente afecta a:
  - Transacciones custom (ZLEL008, ZVEL015)
  - Tablas CO-PA (CE1*, CE4* para KE24)
  - Tablas de mayor general (FAGLFLEXA para FAGLL03)
- Proceso de solicitud mediante tickets a TI Global
- No hay SLA definido para incorporación de nuevas tablas

**Estado actual:**
- Tickets BQ-7713 y BQ-7721 pendientes para incorporación de tablas
- Requiere coordinación entre TI CASA, TI Global y equipo BigQuery
- Necesidad de validar diccionario de datos SAP disponible

#### **Issue #3: Posibles Limitaciones Técnicas (A Validar)**

**Problema reportado:**
> *"El otro problema dijeron que tenía alguna limitación la herramienta. Lo que no sabemos es si la limitación es de la herramienta o desde desconocimiento de la persona que lo estaba utilizando"*

**Situación ambigua:**
- Se reportaron "limitaciones" sin especificar cuáles
- No está claro si son:
  - Limitaciones reales de BigQuery como plataforma
  - Gaps de conocimiento del power user asignado
  - Problemas de configuración o permisos
  - Restricciones impuestas por TI Global

**Requiere validación en Fase 0:**
- Análisis técnico profundo de capacidades de BigQuery
- Pruebas de performance con volúmenes reales
- Validación de funcionalidades necesarias vs. disponibles
- Documentación de limitaciones reales (si existen)

### 1.3.4. Requerimiento Crítico de TI

**David Saboya** establece como condición:

> *"Si se decide trabajar con esta herramienta debemos considerar que el 'power user' tenga cuenta de Elanco con estos skills"*

**Implicaciones:**
- El power user debe tener cuenta corporativa Elanco (no externa)
- Debe cumplir con el perfil "Power User Persona" definido por TI Global
- Requiere habilidades en SQL avanzado
- Conocimiento de procesos de negocio SAP
- Experiencia con herramientas BI (Power BI, Alteryx, etc.)

**Perfil actual:** Funcional SAP (consultoría externa) cumple con los skills técnicos pero trabaja como recurso externo. Requiere validación de accesos y formalización de accesos corporativos.

---

## 1.4. Tecnologías Confirmadas para el Proyecto

Basado en el documento **"Que_se_va_a_usar.txt"** (actualizado 10-oct-2025), alineado con Finanzas y Operaciones:

### ✅ Tecnologías Confirmadas

#### 1. **SAP S/4HANA** (Sistema Fuente)
- Versión: SAP S/4HANA 6.0 (por confirmar versión exacta)
- Power users con roles: MM, SD, FI, CO
- Módulos involucrados:
  - **MM** - Materials Management (compras, inventarios)
  - **SD** - Sales & Distribution (ventas, órdenes)
  - **FI** - Financial Accounting (contabilidad financiera)
  - **CO** - Controlling (contabilidad de costos)

#### 2. **Google BigQuery** (Data Lake)
- Dataset: **CASA** (Centroamérica y Sudamérica)
- Dataset corporativo: **ERP Enterprise Data Product**
- Características:
  - Diccionario de datos SAP mejorado
  - Nombres de tablas y columnas simplificados
  - Identificación de campos clave
  - Eliminación de columnas nulas
- Acceso: Cuenta corporativa validada (Project CASA-BI)

#### 3. **Microsoft Power BI** (Reportería y Analítica)
- Versión: Power BI Pro
- Licencias adquiridas: **8 licencias** (Orden PR-55219 cerrada 08-oct-2025)
  - 4 para Finanzas
  - 2 para Supply Chain
  - 1 para TechOps
  - 1 para TI Global
- Workspaces corporativos configurados
- Row-Level Security (RLS) por implementar

#### 4. **Herramientas de Apoyo**
- **BigQuery Studio:** Entorno de desarrollo SQL
- **ODBC Simba:** Driver para conectividad Power BI ↔ BigQuery
- **Confluence/SharePoint:** Documentación y colaboración

### ⏸️ Tecnologías Documentadas pero NO Confirmadas (Opcional)

#### 1. **Gemini AI Cloud Companion**
- Estado: Documentado como opcional
- Función: Asistencia SQL y generación de código
- Costo: Actualmente sin costo (puede cambiar)
- Decisión: Las consultas se realizarán manualmente o con GPT básico externo hasta nuevo aviso

---

## 1.5. Recursos Ya Comprometidos

### Licencias Adquiridas

✅ **Power BI Pro:**
- 8 licencias activas
- Orden de compra: PR-55219
- Fecha de adquisición: 8 de octubre de 2025
- Distribución por área confirmada

### Accesos BigQuery

✅ **Cuenta Corporativa:**
- Project: CASA-BI
- Validación: 9 de octubre de 2025
- Dataset: CASA disponible

⏳ **Permisos Pendientes:**
- Data Viewer/Data Editor para 6 integrantes (en proceso)
- Solicitudes de acceso formalizadas

### Personal

✅ **Power User Primario:**
- Funcional SAP (consultoría externa)
- Perfil: Consultoría SAP y análisis de procesos
- Skills: SQL intermedio, conocimiento módulos SAP MM/SD/FI

⏳ **Respaldos Propuestos:**
- Carolina Rondón (TI)
- Juan Sebastián Ravelo (área por confirmar)

✅ **Licencias SAP Adicionales:**
- 5 licencias para Finanzas/Supply (pruebas y validaciones)
- Acceso de solo lectura

---

## 1.6. Conclusión: Necesidad del Proyecto

### Problemas Identificados (Resumen)

1. ❌ **Procesos manuales** consumen 15-20 horas semanales por área
2. ❌ **Datos fragmentados** impiden análisis integrado
3. ❌ **Licencias Power BI subutilizadas** por falta de infraestructura
4. ❌ **Calidad de datos inconsistente** por consolidación manual
5. ❌ **Decisiones lentas** basadas en información desactualizada
6. ❌ **Piloto BigQuery inconcluso** por falta de permisos y tablas

### Oportunidades Identificadas

1. ✅ **Infraestructura BigQuery disponible** (dataset casa_bi)
2. ✅ **Licencias Power BI adquiridas** (8 licencias Pro)
3. ✅ **Experiencia corporativa** con BigQuery en otras regiones
4. ✅ **Apoyo de TI Global** para resolución de issues
5. ✅ **Equipo técnico disponible** (Aunergia + Elanco)
6. ✅ **Sponsor del negocio** (Finanzas y Supply comprometidos)

### Justificación de la Inversión

**Esfuerzo estimado:** 1,590 horas (42 semanas)

**Beneficios Proyectados:**

| Beneficio | Ahorro Anual |
|-----------|--------------|
| Reducción de horas manuales | 3,120 horas/año (3 áreas × 20h/sem × 52 sem) |
| Mejora en calidad de decisiones | Cualitativo (mejor forecasting, menos obsolescencia) |
| Optimización de licencias Power BI | Aprovechamiento completo de 8 licencias Pro |
| Reducción errores de consolidación | 500 horas/año |
| **Total Ahorro Anual** | **~3,620 horas/año** |


---

*Siguiente sección: [02_ALCANCE_GENERAL_DE_LA_PROPUESTA.md](02_ALCANCE_GENERAL_DE_LA_PROPUESTA.md)*
