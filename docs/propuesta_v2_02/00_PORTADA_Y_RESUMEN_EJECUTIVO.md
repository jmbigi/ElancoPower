# PROPUESTA DE CENTRALIZACIÓN DE DATOS DE ANÁLISIS
## ELANCO ANIMAL HEALTH - OPERACIÓN CASA

---

### **PROYECTO DE IMPLEMENTACIÓN DE DATA LAKE Y ANALÍTICA EMPRESARIAL**

**Versión Final - 8 de Noviembre 2025**

---

**Elaborado por:**  
**Aunergia** - Consultoría en Optimización de Procesos y TI  
**Consultor BI:** Consultor BI

**Para:**  
**Elanco Animal Health**  
Operación Centroamérica y Sudamérica (CASA)

---

**Fecha de Elaboración:** 8 de Noviembre 2025  
**Validez de la Oferta:** 30 días a partir de la fecha de elaboración (hasta 8 de diciembre de 2025)  
**Versión del Documento:** 3.0 (Versión Final consolidada)

</div>

---

## CONTROL DE VERSIONES

| Versión | Fecha | Descripción | Autor |
|---------|-------|-------------|-------|
| 0.5 | 29-oct-2025 | Avance 50% preliminar | Consultor BI |
| 1.0 | 5-nov-2025 | Propuesta final completa | Consultor BI / Funcional SAP |
| 2.0 | 7-nov-2025 | Revisión realista ajustada a antecedentes | Consultor BI |
| 3.0 | 8-nov-2025 | Unificación a 1,590h en 42 semanas y depuración (sin ROI/retención) | Consultor BI |

---

## RESUMEN EJECUTIVO

### FICHA TÉCNICA CANÓNICA
| Métrica | Valor |
|---------|-------|
| Transacciones SAP | 18 |
| Dashboards Power BI | 12 |
| Esfuerzo Total | 1,590 horas (42 semanas) |
| Rango Tablas SAP (MVP) | 32–38 (32 núcleo + hasta 6 condicionales) |
| Distribución Fases | F0: 235h (6 sem) · F1: 696h (22 sem) · F2: 659h (14 sem) |

Nota de canonicidad: Ante cualquier discrepancia prevalecen `03_TRANSACCIONES_SAP_INCLUIDAS.md`, `ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md`, `08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md` y `09_CRONOGRAMA_SEMANAL.md`.

### Contexto

**Elanco Animal Health** es una compañía global líder en salud animal, con operaciones en Centroamérica y Sudamérica (CASA) que abarcan más de 10 países. Actualmente, los equipos de Finanzas, Supply Chain y otras áreas de negocio enfrentan desafíos significativos en la gestión y análisis de información empresarial:

- **Procesos manuales intensivos** de extracción de datos desde SAP S/4HANA
- **Consolidación manual en Excel** de información de múltiples países
- **Falta de centralización** que impide análisis integrados y toma de decisiones ágil
- **Reportería desconectada** en Power BI sobre datos fragmentados

### Solución Propuesta

**Aunergia** propone un proyecto integral de **Centralización de Datos de Análisis** en 4 fases:

1. **Fase 0:** Revisión del alcance y factibilidad técnica (6 semanas, 235h)
2. **Fase 1:** Construcción de Data Lake con automatización SAP → BigQuery (22 semanas, 696h)
3. **Fase 2:** Modelado de datos y dashboards Power BI (14 semanas, 659h)
4. **Fase 3:** Arquitectura para modelos predictivos (descripción conceptual, sin horas incluidas)

### Alcance

- **18 transacciones SAP** completas automatizadas (FI, SD, MM, CO)
- **Data Lake** en Google BigQuery (dataset casa_bi) con arquitectura de 3 capas
- **12 dashboards** ejecutivos en Power BI con RLS
- **Automatización completa** de extracción y consolidación
- **Historización** de datos (mínimo 24 meses)

### Recursos del Proyecto

| Perfil | Horas Totales |
|--------|---------------|
| **Consultor BI** | 961 horas |
| **Funcional SAP** | 484 horas |
| **Project Manager** | 145 horas |
| **TOTAL PROYECTO** | **1,590 horas** |

**Nota:** No se incluye consultoría ABAP adicional, el Funcional SAP cuenta con el expertise SAP necesario.

### Duración Unificada

- **Tiempo total:** 42 semanas (~10 meses)
- **Inicio propuesto:** 6 de enero de 2026
- **Finalización estimada:** Mediados de octubre 2026
- **Distribución por fase consolidada:** Fase 0: 6 semanas (235h) · Fase 1: 22 semanas (696h) · Fase 2: 14 semanas (659h) = 42 semanas / 1,590h totales
- **Nota:** Consultor BI trabaja máximo 6 horas/día (30h/semana)

### Beneficios Esperados

✅ **Reducción del 70%** en tiempo de extracción y consolidación de datos para todas las áreas
✅ **Dashboards disponibles en 24 horas** tras cierre mensual (vs. 5-7 días actuales)  
✅ **Eliminación de procesos manuales** propensos a errores en áreas críticas (Finanzas, Ventas, Inventario, OPEX)
✅ **Democratización del acceso** a datos mediante 12 dashboards Power BI (promedio ~3 hojas/páginas por dashboard)  
✅ **Plataforma completa** con 18 transacciones SAP automatizadas
✅ **Ahorro estimado:** 3,620 horas/año en procesos manuales

### Equipo del Proyecto

**Equipo Aunergia:**
- **Consultor BI** - Arquitecto de Datos y Desarrollador BigQuery/Power BI (961h)
- **Funcional SAP** - Analista SAP Power User / Consultoría Funcional (484h)
- **Project Manager** - Project Manager (145h)

**Equipo Elanco (requerido para el proyecto):**
- **David Saboya** - Analista IT TechOps CASA (coordinación con TI Global)
- **Representantes de Finanzas** - Validación de reportes y KPIs
- **Representantes de Supply Chain** - Validación de procesos logísticos

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

---

## INFORMACIÓN DE CONTACTO

### Aunergia

**Coordinación de Proyecto:**  
Project Manager  
*Información de contacto será proporcionada por Aunergia*

**Consultoría SAP:**  
Funcional SAP  
*Información de contacto será proporcionada por Aunergia*

**Arquitectura de Datos / BI:**  
Consultor BI  
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

*Documento generado: 8 de Noviembre 2025*  
*Versión 3.0 - Propuesta Final*
