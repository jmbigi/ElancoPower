# PROPUESTA DE CENTRALIZACIÓN DE DATOS DE ANÁLISIS
## ELANCO ANIMAL HEALTH - OPERACIÓN CASA

---

<div align="center">

### **PROYECTO DE IMPLEMENTACIÓN DE DATA LAKE Y ANALÍTICA EMPRESARIAL**

**Versión Final - 7 de Noviembre 2025**

---

**Elaborado por:**  
**Aunergia** - Consultoría en Optimización de Procesos y TI  
**Desarrollador Técnico:** Juan Manuel Bigi

**Para:**  
**Elanco Animal Health**  
Operación Centroamérica y Sudamérica (CASA)

---

**Fecha de Elaboración:** 7 de Noviembre 2025  
**Validez de la Oferta:** 30 días (hasta 7 de diciembre 2025)  
**Versión del Documento:** 2.0 (Revisada y ajustada a realidad del proyecto)

</div>

---

## CONTROL DE VERSIONES

| Versión | Fecha | Descripción | Autor |
|---------|-------|-------------|-------|
| 0.5 | 29-oct-2025 | Avance 50% preliminar | Juan Manuel Bigi |
| 1.0 | 5-nov-2025 | Propuesta final completa | Juan Manuel Bigi / Lucía Rodríguez |
| 2.0 | 7-nov-2025 | **Revisión realista ajustada a antecedentes** | Juan Manuel Bigi |

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

**IMPORTANTE:** Esta propuesta está basada en el presupuesto personal de Juan Manuel Bigi (USD 8,850 por 354 horas). Los costos de coordinación, Project Management y otros recursos de Aunergia se facturan por separado.

- **8 transacciones SAP prioritarias** automatizadas en MVP (VA05, ZLEL008, KSB1, FAGLL03, KE24, FB03, F.08, F.01)
- **10 transacciones adicionales** documentadas para fases futuras (ME2L, MM60, MB59, ZVEL015, ME23N, FBL1N, FBL5N, MB5B, XK03, XD03)
- **Data Lake** en Google BigQuery (dataset CASA)
- **4-6 dashboards** ejecutivos en Power BI (MVP)
- **Automatización completa** de extracción y consolidación para transacciones MVP
- **Historización** de datos (mínimo 24 meses)

### Recursos del Proyecto

**NOTA IMPORTANTE:** Este presupuesto incluye únicamente el trabajo técnico de desarrollo de Juan Manuel Bigi.

| Perfil | Horas Totales | Incluido en Presupuesto |
|--------|---------------|-------------------------|
| **Desarrollo técnico (Juan Manuel Bigi)** | 354 horas | ✅ SÍ - USD 8,850 |
| **Consultoría SAP y coordinación (Lucía Rodríguez)** | 80 horas (ref.) | ❌ NO - Factura separada Aunergia |
| **Project Management (Linda López)** | N/A | ❌ NO - Gestiona Aunergia |
| **Consultoría ABAP Especializada** | 8-16 horas (contingencia) | ⚠️ Según necesidad - USD 640-1,600 |
| **TOTAL PRESUPUESTADO (JMB)** | **354 horas** | **USD 8,850** |

### Duración

- **Tiempo total:** 13-17 semanas (~4 meses)
- **Inicio propuesto:** 14 de diciembre 2025 (tras aprobación)
- **Finalización estimada:** 9 de abril 2026
- **Disponibilidad:** Part-time 20-25 horas/semana
- **Pausa vacacional:** 1 semana durante festividades de fin de año (23-29 diciembre 2025)
- **Nota:** Cronograma condicionado a resolución de issues de permisos SAP y tablas BigQuery

### Beneficios Esperados (MVP con 8 transacciones)

✅ **Reducción del 70%** en tiempo de extracción y consolidación de datos para las transacciones prioritarias
✅ **Dashboards disponibles en 24 horas** tras cierre mensual (vs. 5-7 días actuales)  
✅ **Eliminación de procesos manuales** propensos a errores en áreas críticas (Finanzas, Ventas, Inventario, OPEX)
✅ **Democratización del acceso** a datos mediante Power BI  
✅ **Base escalable** para agregar más transacciones y analítica predictiva futura  
✅ **Ahorro estimado:** 30-40 horas/semana en procesos manuales de las áreas priorizadas
✅ **ROI estimado:** Recuperación de inversión en ~2 meses de operación

### Equipo del Proyecto

**Desarrollo Técnico (incluido en presupuesto USD 8,850):**
- **Juan Manuel Bigi** - Arquitecto de Datos y Desarrollador BigQuery/Power BI (354h)

**Coordinación y Consultoría Aunergia (facturación separada):**
- **Lucía Rodríguez** - Analista SAP Power User / Consultora de Procesos (~80h referencia)
- **Linda López** - Coordinadora General del Proyecto (según necesidad de Aunergia)

**Equipo Elanco (requerido para el proyecto):**
- **David Saboya** - Analista IT TechOps CASA (coordinación con TI Global)
- **Representantes de Finanzas** - Validación de reportes y KPIs (~20h participación)
- **Representantes de Supply Chain** - Validación de procesos logísticos (~20h participación)
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
- **08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md** - Estimación de horas detallada
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
*Información de contacto será proporcionada por Aunergia*

**Consultoría SAP:**  
Lucía Rodríguez  
*Información de contacto será proporcionada por Aunergia*

**Arquitecto de Datos:**  
Juan Manuel Bigi  
*Información de contacto será proporcionada por Aunergia*

### Elanco Animal Health

**Operación CASA:**  
*Contacto según coordinación con Aunergia*

**TI TechOps:**  
David Saboya  
Email: david.saboya@network.elancoah.com

---

## DECLARACIÓN DE CONFIDENCIALIDAD

Este documento contiene información confidencial y de propiedad exclusiva de **Aunergia** y **Elanco Animal Health**. Está destinado únicamente para uso interno y no debe ser distribuido, copiado o divulgado a terceros sin autorización previa y por escrito de ambas partes.

---

## PRÓXIMOS PASOS

1. **Revisión de la propuesta** por stakeholders de Elanco (Semana 1)
2. **Reunión de presentación** y aclaración de dudas (Semana 1-2)
3. **Decisión Go/No-Go** y aprobación de alcance (Semana 2-3)
4. **Firma de contrato** y definición de kick-off (Semana 3-4)
5. **Inicio de Fase 0** (Mes 1, Semana 1 del proyecto)

---

**Aunergia**  
*Optimización de Procesos de Negocio y Consultoría TI*  
Fundada en 2017 por ex ejecutivos de Big Four  

Clientes en: México, Centroamérica, Brasil, Chile, Perú, Uruguay, Colombia, España

---

*Documento generado: Noviembre 2025*  
*Versión 1.2 - Propuesta Final*
