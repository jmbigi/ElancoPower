# PROPUESTA DE CENTRALIZACIÓN DE DATOS DE ANÁLISIS
## ELANCO ANIMAL HEALTH - OPERACIÓN CASA

---

<div align="center">

### **PROYECTO DE IMPLEMENTACIÓN DE DATA LAKE Y ANALÍTICA EMPRESARIAL**

**Versión Final - Noviembre 2025**

---

**Elaborado por:**  
**Aunergia** - Consultoría en Optimización de Procesos y TI

**Para:**  
**Elanco Animal Health**  
Operación Centroamérica y Sudamérica (CASA)

---

**Fecha de Elaboración:** 5 de noviembre de 2025  
**Validez de la Oferta:** 5 de diciembre de 2025  
**Versión del Documento:** 1.1 (Cronograma actualizado)

</div>

---

## CONTROL DE VERSIONES

| Versión | Fecha | Descripción | Autor |
|---------|-------|-------------|-------|
| 0.5 | 29-oct-2025 | Avance 50% preliminar | Juan Manuel Bigi |
| 1.0 | 5-nov-2025 | Propuesta final completa | Juan Manuel Bigi / Lucía Rodríguez |

---

## RESUMEN EJECUTIVO

### Contexto

**Elanco Animal Health** es una compañía global líder en salud animal, con operaciones en Centroamérica y Sudamérica (CASA) que abarcan más de 10 países. Actualmente, los equipos de Finanzas, Supply Chain y otras áreas de negocio enfrentan desafíos significativos en la gestión y análisis de información empresarial:

- **Procesos manuales intensivos** de extracción de datos desde SAP ECC
- **Consolidación manual en Excel** de información de múltiples países
- **Falta de centralización** que impide análisis integrados y toma de decisiones ágil
- **Reportería desconectada** en Power BI sobre datos fragmentados

### Solución Propuesta

**Aunergia** propone un proyecto integral de **Centralización de Datos de Análisis** en 4 fases:

1. **Fase 0:** Revisión del alcance y factibilidad técnica (3-4 semanas)
2. **Fase 1:** Construcción de Data Lake con automatización SAP → BigQuery (6-8 semanas)
3. **Fase 2:** Modelado de datos y dashboards Power BI (4-5 semanas)
4. **Fase 3:** Arquitectura para modelos predictivos (descripción conceptual)

### Alcance

- **18 transacciones SAP** automatizadas (ME2L, MM60, VA05, MB59, ZLEL008, KSB1, KE24, FB03, ZVEL015, ME23N, FAGLL03, FBL1N, F.08, F.01, XK03, XD03, FBL5N, MB5B)
- **Data Lake** en Google BigQuery (dataset CASA)
- **12 dashboards** ejecutivos en Power BI
- **Automatización completa** de extracción y consolidación
- **Historización** de datos (mínimo 24 meses)

### Recursos del Proyecto

| Perfil | Horas Totales |
|--------|---------------|
| **Desarrollo técnico (Juan Manuel Bigi)** | 478 horas |
| **Consultoría SAP y coordinación (Lucía Rodríguez)** | 145 horas |
| **Project Management (Linda López)** | 42 horas |
| **Consultoría ABAP Especializada** | 12 horas |
| **TOTAL HORAS** | **677 horas** |

### Duración

- **Tiempo total:** 24 semanas (~6 meses, incluyendo 1 semana vacacional)
- **Fecha inicio estimada:** 1 de diciembre de 2025
- **Fecha fin estimada:** 18 de mayo de 2026
- **Pausa vacacional:** 23-29 diciembre 2025 (festividades de fin de año)
- **Nota:** Ajustado por restricción de JMB (máximo 6 horas/día de trabajo)

### Beneficios Esperados

✅ **Reducción del 70%** en tiempo de extracción y consolidación de datos  
✅ **Dashboards disponibles en 24 horas** tras cierre mensual (vs. 5-7 días actuales)  
✅ **Eliminación de procesos manuales** propensos a errores  
✅ **Democratización del acceso** a datos mediante Power BI  
✅ **Base escalable** para analítica predictiva futura  
✅ **Ahorro estimado:** 50-60 horas/semana en procesos manuales

### Equipo Aunergia

- **Linda López** - Coordinadora General del Proyecto
- **Lucía Rodríguez** - Analista SAP Power User / Consultora de Procesos
- **Juan Manuel Bigi** - Arquitecto de Datos y Desarrollador BigQuery/Power BI

### Equipo Elanco (requerido)

- **David Saboya** - Analista IT TechOps CASA (coordinación con TI Global)
- **Representantes de Finanzas** - Validación de reportes y KPIs
- **Representantes de Supply Chain** - Validación de procesos logísticos
- **TI Global** - Soporte para permisos SAP y tablas BigQuery

---

## ÍNDICE DE DOCUMENTOS

Esta propuesta está organizada en los siguientes documentos:

### 📄 **Parte 1: Contexto y Antecedentes**
- **00_PORTADA_Y_RESUMEN_EJECUTIVO.md** (este documento)
- **01_CONTEXTO_Y_SITUACION_ACTUAL.md** - Análisis de la situación actual y problemática

### 📄 **Parte 2: Alcance y Transacciones**
- **02_ALCANCE_GENERAL_DE_LA_PROPUESTA.md** - Objetivos y alcance del proyecto
- **03_TRANSACCIONES_SAP_INCLUIDAS.md** - Detalle de las 18 transacciones SAP

### 📄 **Parte 3: Descripción de Fases**
- **04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD.md** - Due diligence técnico
- **05_FASE_1_CONSTRUCCION_DATA_LAKE.md** - Automatización SAP → BigQuery
- **06_FASE_2_MODELADO_Y_DASHBOARDS.md** - Power BI y reportería
- **07_FASE_3_MODELOS_PREDICTIVOS.md** - Arquitectura de analítica avanzada

### 📄 **Parte 4: Estimaciones y Planificación**
- **08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md** - Horas y presupuesto detallado
- **09_CRONOGRAMA_SEMANAL.md** - Planificación temporal del proyecto

### 📄 **Parte 5: Requisitos y Cierre**
- **10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md** - Prerrequisitos del proyecto
- **11_RIESGOS_Y_SUPUESTOS.md** - Análisis de riesgos y mitigaciones
- **12_ENTREGABLES_Y_CONDICIONES_COMERCIALES.md** - Productos y términos contractuales

### 📄 **Anexos**
- **ANEXO_A_METODOLOGIA_DE_TRABAJO.md** - Enfoque y prácticas de desarrollo
- **ANEXO_B_PERFILES_TECNICOS.md** - CVs y experiencia del equipo
- **ANEXO_C_CASOS_DE_EXITO.md** - Referencias de proyectos similares

---

## INFORMACIÓN DE CONTACTO

### Aunergia

**Coordinadora del Proyecto:**  
Linda López  
Email: linda.lopez@aunergia.com.ar  
Teléfono: [Por confirmar]

**Consultoría SAP:**  
Lucía Rodríguez  
Email: lucia.rodriguez@aunergia.com.ar  
Teléfono: [Por confirmar]

**Arquitecto de Datos:**  
Juan Manuel Bigi  
Email: [Por confirmar]  
Teléfono: [Por confirmar]

**Oficinas:**
- **Argentina (Sede Principal):** Buenos Aires
- **Estados Unidos:** [Ciudad]
- **España:** [Ciudad]

### Elanco Animal Health

**Operación CASA:**  
[Contacto principal por confirmar]

**TI TechOps:**  
David Saboya  
Email: david.saboya@network.elancoah.com

---

## DECLARACIÓN DE CONFIDENCIALIDAD

Este documento contiene información confidencial y de propiedad exclusiva de **Aunergia** y **Elanco Animal Health**. Está destinado únicamente para uso interno y no debe ser distribuido, copiado o divulgado a terceros sin autorización previa y por escrito de ambas partes.

---

## PRÓXIMOS PASOS

1. **Revisión de la propuesta** por stakeholders de Elanco (6-10 nov 2025)
2. **Reunión de presentación** y aclaración de dudas (11-15 nov 2025)
3. **Decisión Go/No-Go** y aprobación de presupuesto (18-22 nov 2025)
4. **Firma de contrato** y definición de kick-off (25-29 nov 2025)
5. **Inicio de Fase 0** (1 diciembre 2025)

---

**Aunergia**  
*Optimización de Procesos de Negocio y Consultoría TI*  
Fundada en 2017 por ex ejecutivos de Big Four  

Clientes en: México, Centroamérica, Brasil, Chile, Perú, Uruguay, Colombia, España

---

*Documento generado el 5 de noviembre de 2025*  
*Versión 1.0 - Propuesta Final*
