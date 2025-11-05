# Propuesta de Centralización de Datos de Análisis (Versión Reducida - 50%)

---

## Introducción

### Contexto del Proyecto

**Elanco Animal Health** es una compañía global guiada por el propósito de mejorar la salud animal como clave para resolver problemas relevantes del mundo. En su operación para Centroamérica y Sudamérica (CASA), la compañía enfrenta desafíos operativos en la gestión y análisis de información empresarial que actualmente limitan la toma de decisiones ágil y basada en datos.

### Situación Actual

Actualmente, los equipos de Finanzas, Supply Chain y otras áreas de negocio realizan procesos manuales intensivos para obtener información de análisis:

- **Extracción manual desde SAP ECC**: Los usuarios acceden a múltiples transacciones SAP (VA05, ZLEL008, KSB1, FAGLL03, entre otras) y descargan reportes individualmente
- **Consolidación manual en Excel**: Los datos de diferentes países se combinan manualmente mediante archivos Excel, proceso que consume tiempo significativo y es propenso a errores
- **Conectores heterogéneos**: Se utilizan herramientas como Business Objects con conectividad limitada a SAP
- **Centralización fragmentada**: No existe un repositorio unificado de datos que permita análisis integrado
- **Reportería en Power BI desconectada**: Aunque se cuenta con 8 licencias Power BI Pro, estas operan sobre datos descentralizados

Esta situación genera:
- Alto consumo de tiempo en tareas repetitivas de extracción y consolidación
- Riesgo de inconsistencias en los datos
- Limitaciones para análisis históricos y comparativos
- Imposibilidad de realizar analítica avanzada o predictiva

### Experiencia con BigQuery

Elanco ha implementado **Google BigQuery** como plataforma de Data Lake corporativa en otras regiones. Para Sudamérica se inició un piloto con el dataset CASA, pero se encontraron obstáculos:

1. **Permisos SAP insuficientes**: El power user asignado no contaba con accesos completos a todas las transacciones necesarias
2. **Tablas faltantes en BigQuery**: Algunas tablas SAP requeridas no estaban disponibles en el dataset, requiriendo solicitudes mediante tickets a TI Global
3. **Posibles limitaciones técnicas**: Se reportaron restricciones que requieren validación para determinar si son limitaciones reales de la plataforma o desconocimiento de configuraciones

### Objetivo de Esta Propuesta

Ante este panorama, **Aunergia** (firma de consultoría especializada en optimización de procesos de negocio y consultoría TI) presenta esta propuesta preliminar reducida para:

1. **Evaluar la viabilidad técnica** de continuar con BigQuery o proponer alternativas (como Azure Data Lake)
2. **Definir el alcance preliminar** de las cuatro fases del proyecto de centralización
3. **Identificar los componentes clave** del proyecto sin entrar en estimaciones detalladas
4. **Proporcionar una base** para la toma de decisión sobre inversión completa

### Alcance de Este Documento

Esta es una **propuesta reducida (50% del alcance completo)** que incluye:

✅ Descripción conceptual de las 4 fases del proyecto  
✅ Identificación de transacciones SAP prioritarias (selección inicial)  
✅ Actividades principales por fase (listas preliminares)  
✅ Requisitos técnicos y administrativos básicos  
✅ Entregables parciales esperados  

❌ **NO incluye:**  
- Estimaciones detalladas de esfuerzo por tarea
- Cronograma semanal de actividades
- Análisis exhaustivo de riesgos
- Especificaciones técnicas detalladas
- Plan de pruebas completo

### Valor Esperado

Al implementar este proyecto completo, Elanco podrá:

- **Reducir tiempo de extracción y consolidación** de datos de días a horas (automatización)
- **Centralizar información** de 10+ países en un único repositorio confiable
- **Democratizar el acceso** a datos mediante dashboards Power BI para diferentes niveles de la organización
- **Habilitar analítica avanzada** con capacidades predictivas para forecasting de ventas, costos y demanda
- **Mejorar la calidad de datos** mediante procesos estandarizados y validaciones automatizadas
- **Optimizar inversión en licencias** Power BI aprovechando las 8 licencias Pro adquiridas
- **Crear una base escalable** para futuras necesidades de analítica empresarial

### Modelo de Colaboración

**Aunergia** propone un modelo de trabajo colaborativo con el equipo técnico de Elanco:

- **Coordinación**: Linda López (Aunergia) como punto de contacto principal
- **Consultoría SAP**: Lucía Rodríguez (Aunergia) como power user y analista de procesos
- **Soporte TI Elanco**: David Saboya (Analista IT TechOps CASA) para coordinación con TI Global
- **Desarrollo técnico**: A definir según aprobación de propuesta

### Estructura del Documento

Este documento preliminar está organizado en las siguientes secciones:

1. **Descripción General** - Visión del proyecto y fases contempladas
2. **Alcance Preliminar** - Definición inicial de objetivos y entregables
3. **Fase 0** - Revisión de alcance y factibilidad técnica
4. **Fase 1** - Automatización de transferencia de datos a Data Lake
5. **Fase 2** - Modelado dimensional y construcción de dashboards
6. **Fase 3** - Arquitectura y roadmap para modelos predictivos
7. **Requisitos** - Listado básico de necesidades técnicas y administrativas
8. **Costo y Próximos Pasos** - Inversión para elaboración de propuesta completa

---

## Descripción General de la Propuesta

Propuesta preliminar para desarrollo de proyecto de centralización de datos de análisis, cubriendo las siguientes fases:

- **Fase 0:** Revisión del alcance y factibilidad
- **Fase 1:** Construcción de repositorio (Data Lake) de datos de análisis
- **Fase 2:** Construcción de modelos y tableros de análisis
- **Fase 3:** Modelos de predicción avanzados

---

## Alcance de la Propuesta (Versión Preliminar)

### 1. Análisis de Antecedentes

Revisión inicial de la situación actual, identificando:
- Fuentes de datos principales (enfoque en SAP)
- Necesidades básicas del negocio
- Stakeholders involucrados

### 2. Documento con Propuesta Preliminar

#### 2.1. Alcances Generales

**2.1.1. Alcance de la Propuesta**
- Definición conceptual del proyecto
- Objetivos principales identificados
- Beneficios esperados (descripción general)

**2.1.2. Transacciones SAP Consideradas (Selección Inicial)**

Transacciones priorizadas para análisis inicial:
- ME2L - Compras
- MM60 - Materiales
- VA05 - Ventas
- MB59 - Movimientos
- ZLEL008 - Transacción customizada
- KSB1 - Contabilidad de costos
- KE24 - Cuenta de resultados
- FB03 - Documentos contables
- ZVEL015 - Transacción customizada
- ME23N - Pedidos de compra

*Nota: Lista preliminar sujeta a validación y ampliación*

---

## Fases del Proyecto

### Fase 0 – Revisión del Alcance y Factibilidad

**Actividades principales:**

1. **Análisis de sistemas fuente**
   - Identificación de tablas SAP relevantes
   - Evaluación de volúmenes de datos preliminares
   - Revisión de conectividad disponible

2. **Definición de requisitos iniciales**
   - Entrevistas con usuarios clave (muestra reducida)
   - Documentación de necesidades prioritarias
   - Identificación de casos de uso principales

3. **Evaluación de viabilidad técnica**
   - Revisión de infraestructura actual
   - Análisis de alternativas tecnológicas
   - Identificación de riesgos principales

**Entregables parciales:**
- Documento de alcance preliminar
- Listado de requisitos iniciales
- Evaluación de riesgos básica

---

### Fase 1 – Transferencia de Datos a Repositorio (Data Lake)

**Actividades principales:**

1. **Diseño arquitectónico**
   - Definición conceptual del Data Lake
   - Selección de tecnologías principales
   - Esquema de zonas de datos (raw, processed, curated)

2. **Configuración de conectores**
   - Setup inicial de conexiones SAP (muestra de transacciones)
   - Pruebas de conectividad básicas
   - Validación de extracción de datos

3. **Implementación de procesos ETL básicos**
   - Desarrollo de pipelines para transacciones prioritarias
   - Definición de frecuencias de carga (preliminar)
   - Establecimiento de logs y monitoreo básico

4. **Gobernanza de datos inicial**
   - Definición de nomenclaturas
   - Establecimiento de políticas de retención (borrador)
   - Configuración de seguridad básica

**Entregables parciales:**
- Arquitectura conceptual del Data Lake
- Conectores funcionales para transacciones prioritarias
- Documentación técnica inicial

---

### Fase 2 – Modelado de Datos y Generación de Tableros

**Actividades principales:**

1. **Diseño de modelo de datos**
   - Definición de modelo dimensional (esquema estrella/copo de nieve)
   - Identificación de dimensiones principales
   - Diseño de tablas de hechos prioritarias

2. **Desarrollo de capa semántica**
   - Creación de vistas de negocio
   - Definición de métricas clave (KPIs principales)
   - Establecimiento de jerarquías básicas

3. **Construcción de tableros iniciales**
   - Tableros para áreas prioritarias:
     - Compras (análisis básico)
     - Ventas (indicadores principales)
     - Inventarios (métricas clave)
   - Visualizaciones estándar
   - Filtros y controles básicos

4. **Configuración de accesos**
   - Definición de roles de usuario
   - Asignación de permisos iniciales
   - Setup de autenticación

**Entregables parciales:**
- Modelo de datos dimensional (versión 1.0)
- 3-5 tableros operativos básicos
- Documentación de usuario preliminar

---

### Fase 3 – Modelos de Predicción

**Actividades principales:**

1. **Identificación de casos de uso predictivos**
   - Análisis de oportunidades para ML/IA
   - Priorización de casos de uso
   - Definición de objetivos de predicción

2. **Exploración de datos y features**
   - Análisis exploratorio de datos históricos
   - Identificación de variables relevantes
   - Evaluación de calidad de datos para modelos

3. **Evaluación de algoritmos**
   - Revisión de técnicas aplicables:
     - Regresión (demanda, costos)
     - Clasificación (categorización)
     - Series temporales (forecasting)
     - Clustering (segmentación)
   - Selección de frameworks y herramientas

4. **Propuesta de arquitectura para ML**
   - Diseño conceptual de pipelines de entrenamiento
   - Estrategia de deployment de modelos
   - Consideraciones de monitoreo y reentrenamiento

5. **Plan de implementación futuro**
   - Roadmap de desarrollo de modelos
   - Identificación de recursos necesarios
   - Estimación de complejidad (cualitativa)

**Entregables parciales:**
- Catálogo de casos de uso predictivos
- Análisis exploratorio de datos (EDA)
- Propuesta de arquitectura ML
- Recomendaciones para siguientes pasos

---

## Requisitos Técnicos Iniciales (Listado Básico)

### Infraestructura
- Plataforma cloud o on-premise (a definir)
- Capacidad de almacenamiento (estimación preliminar requerida)
- Recursos computacionales para procesamiento

### Software y Herramientas
- Conectores SAP
- Herramientas de ETL (evaluación pendiente)
- Plataforma de BI/visualización
- Entorno para desarrollo de modelos ML

### Seguridad y Cumplimiento
- Políticas de acceso y autenticación
- Encriptación de datos (en tránsito y reposo)
- Cumplimiento normativo (a validar)

### Recursos Humanos (Perfiles)
- Arquitecto de datos
- Desarrollador ETL
- Analista de BI
- Data Scientist (para Fase 3)

---

## Requisitos Administrativos Iniciales

1. **Accesos y permisos**
   - Acceso a sistemas SAP (lectura)
   - Credenciales para ambientes de desarrollo
   - Permisos de infraestructura

2. **Coordinación**
   - Punto de contacto técnico
   - Representante de negocio
   - Comité de seguimiento

3. **Documentación base**
   - Diccionario de datos SAP
   - Manuales de procesos actuales
   - Políticas corporativas aplicables

---

## Notas Importantes

- **Esta es una propuesta preliminar - Avance del 50% para reunión del 7 de noviembre**
- Las descripciones son incompletas y requieren profundización
- No incluye estimaciones detalladas de esfuerzo ni cronograma semanal
- Los entregables son parciales y sujetos a revisión
- Se requiere completar el 50% restante después de la reunión Go/No-Go
- Este documento sirve como base para la toma de decisión sobre continuar con la propuesta completa

---

## Contexto de Este Documento

Este es un **avance del 50%** de la propuesta completa que se está elaborando para el proyecto de Centralización de Datos de Elanco. 

### Propósito del Avance:
- Proveer una visión preliminar de las 4 fases del proyecto
- Identificar transacciones SAP prioritarias (selección inicial)
- Listar actividades principales sin profundizar en detalles técnicos
- Facilitar la reunión **Go/No-Go del 7 de noviembre de 2025**
- Obtener feedback temprano antes de completar el 50% restante

### Propuesta Completa (100%):
La propuesta completa incluirá:
- ✅ Estimaciones detalladas de esfuerzo (horas por tarea y perfil técnico)
- ✅ Cronograma semanal con hitos y entregables
- ✅ Análisis exhaustivo de riesgos y mitigaciones
- ✅ Especificaciones técnicas detalladas por transacción SAP
- ✅ Plan de pruebas y criterios de aceptación
- ✅ Descripción completa de entregables por fase
- ✅ Presupuesto detallado del proyecto de implementación

---

## Costo de Elaboración

### Trabajo Realizado a la Fecha:

**Horas invertidas en este avance (50%):** 15 horas

**Actividades completadas:**
- Análisis preliminar de fuentes (audios, correos, transacciones SAP): 4h
- Investigación técnica inicial (BigQuery, Power BI): 3h
- Estructuración de contenido por las 4 fases: 4h
- Redacción de descripciones preliminares: 3h
- Revisión de consistencia: 1h

**Costo del avance (50%):** 15 horas × 25 USD/hora = **375 USD**

### Trabajo Pendiente:

**Horas estimadas para completar (50% restante):** 15 horas

**Actividades pendientes:**
- Estimaciones detalladas de esfuerzo por tarea
- Elaboración de cronograma semanal
- Análisis exhaustivo de riesgos
- Especificaciones técnicas completas
- Presupuesto detallado del proyecto

**Costo para completar (50% restante):** 15 horas × 25 USD/hora = **375 USD**

### Costo Total de la Propuesta Completa:

**30 horas × 25 USD/hora = 750 USD**

*(Costo total para elaboración de la propuesta técnica completa. No incluye implementación del proyecto)*

---

## Información del Documento

- **Tipo de documento:** Avance de Propuesta (50%)
- **Fecha de elaboración del avance:** 5 de noviembre de 2025
- **Fecha de entrega del avance:** 7 de noviembre de 2025
- **Reunión Go/No-Go:** 7 de noviembre de 2025
- **Entrega de propuesta completa (100%):** 12 de noviembre de 2025 (condicionado a aprobación)
- **Validez de la oferta:** Hasta 3 de diciembre de 2025
- **Elaborado por:** Juan Manuel Bigi (Manolo) - Arquitecto de Datos
- **Coordinación:** Linda López (Aunergia) / Lucía Rodríguez (Aunergia)
- **Cliente final:** Elanco Animal Health - Operación CASA

---

## Próximos Pasos

### Antes de la reunión del 7 de noviembre:

1. ✅ **Revisión interna Aunergia** de este documento preliminar (50%)
2. ✅ **Distribución del avance** a stakeholders de Elanco para lectura previa
3. ⏳ **Preparación de presentación** para reunión Go/No-Go

### Durante la reunión del 7 de noviembre:

4. 📊 **Presentación del avance** de propuesta (visión general de las 4 fases)
5. 💬 **Discusión de viabilidad técnica** (BigQuery vs alternativas)
6. 🎯 **Validación de transacciones SAP prioritarias** con áreas de negocio
7. ✅ **Decisión Go/No-Go** para completar la propuesta al 100%

### Después de la reunión del 7 de noviembre (si se aprueba continuar):

8. 📝 **Incorporación de feedback** recibido en la reunión
9. 🔨 **Elaboración del 50% restante** de la propuesta (estimaciones, cronograma, presupuesto)
10. 📤 **Entrega de propuesta completa** el 12 de noviembre de 2025
11. 🤝 **Reunión de presentación final** y aprobación de presupuesto

---

## Nota Final

Este documento representa un **trabajo en progreso** diseñado específicamente para facilitar la toma de decisiones en la reunión del 7 de noviembre. La propuesta completa con todas las estimaciones, cronogramas y presupuestos detallados se entregará el 12 de noviembre, una vez confirmada la continuidad del proyecto.

