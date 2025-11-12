# PROPUESTA DE CENTRALIZACIÓN DE DATOS DE ANÁLISIS
## ELANCO ANIMAL HEALTH - OPERACIÓN CASA

---

### **PROYECTO DE IMPLEMENTACIÓN DE DATA LAKE Y ANALÍTICA EMPRESARIAL**

**Versión 2.04 - 10 de Noviembre 2025**

---

**Elaborado por:**  
**Aunergia** - Consultoría en Optimización de Procesos y TI  
**Consultor BI:** Consultor BI

**Para:**  
**Elanco Animal Health**  
Operación Centroamérica y Sudamérica (CASA)

---

**Fecha de Elaboración:** 10 de Noviembre 2025  
**Validez de la Oferta:** 30 días a partir de la fecha de elaboración (hasta 10 de diciembre de 2025)  
**Versión del Documento:** 2.04 (Con ABAP Developer - Cronograma Moderado)

</div>

---

## CONTROL DE VERSIONES

| Versión | Fecha | Descripción | Autor |
|---------|-------|-------------|-------|
| 0.5 | 29-oct-2025 | Avance 50% preliminar | Consultor BI |
| 1.0 | 5-nov-2025 | Propuesta final completa | Consultor BI / Funcional SAP |
| 2.0 | 7-nov-2025 | Revisión realista ajustada a antecedentes | Consultor BI |
| 3.0 | 8-nov-2025 | Unificación a 1,590h en 42 semanas (V2.02) | Consultor BI |
| 2.04 | 10-nov-2025 | Optimización con ABAP Developer: 1,880h en 36 semanas | Consultor BI |

---

## RESUMEN EJECUTIVO

### FICHA TÉCNICA CANÓNICA V2.04
| Métrica | Valor |
|---------|-------|
| Transacciones SAP | 18 |
| Dashboards Power BI | 12 |
| Esfuerzo Total | **1,880 horas (36 semanas)** |
| Recursos | **4 (BI, ABAP Developer, SAP Functional, PM)** |
| Rango Tablas SAP (MVP) | 32–38 (32 núcleo + hasta 6 condicionales) |
| Distribución Fases | F0: 328h (6 sem) · F1: 852h (20 sem) · F2: 700h (10 sem) |
| Go-Live | **13 de septiembre de 2026** |

**Cambios vs V2.02:** +290h esfuerzo (+18%), -6 semanas duración (-14%), +1 recurso ABAP Developer, Go-Live 1 mes antes.

Nota de canonicidad: Ante cualquier discrepancia prevalecen `03_TRANSACCIONES_SAP_INCLUIDAS.md`, `ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md`, `08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS_V2_04.md` y `09_CRONOGRAMA_SEMANAL_V2_04.md`.

### Contexto

**Elanco Animal Health** es una compañía global líder en salud animal, con operaciones en Centroamérica y Sudamérica (CASA) que abarcan más de 10 países. Actualmente, los equipos de Finanzas, Supply Chain y otras áreas de negocio enfrentan desafíos significativos en la gestión y análisis de información empresarial:

- **Procesos manuales intensivos** de extracción de datos desde SAP S/4HANA
- **Consolidación manual en Excel** de información de múltiples países
- **Falta de centralización** que impide análisis integrados y toma de decisiones ágil
- **Reportería desconectada** en Power BI sobre datos fragmentados

### Solución Propuesta V2.04

**Aunergia** propone un proyecto integral de **Centralización de Datos de Análisis** en 3 fases con **4 recursos especializados**:

1. **Fase 0:** Revisión del alcance y factibilidad técnica (6 semanas, 328h)
2. **Fase 1:** Construcción de Data Lake con automatización SAP → BigQuery (20 semanas, 852h)
3. **Fase 2:** Modelado de datos y dashboards Power BI (10 semanas, 700h)

**Novedad V2.04:** Incorporación de **ABAP Developer especialista** para:
- Configuración y monitoreo SAP SLT
- Análisis de transacciones custom (ZLEL008, ZVEL015)
- Extracción de datos SAP → BigQuery (capa RAW)
- Gestión de tickets SAP con TI Global

### Alcance

- **18 transacciones SAP** completas automatizadas (FI, SD, MM, CO)
- **Data Lake** en Google BigQuery (dataset casa_bi) con arquitectura de 3 capas
- **12 dashboards** ejecutivos en Power BI con RLS
- **Automatización completa** de extracción y consolidación
- **Historización** de datos (mínimo 24 meses)

### Recursos del Proyecto V2.04

| Perfil | Horas Totales | H/Semana | Participación |
|--------|---------------|----------|---------------|
| **Consultor BI** | 935 horas | 26.0h/sem | Todo el proyecto (36 sem) |
| **ABAP Developer** | 270 horas | 10.4h/sem | Fase 0 + Fase 1 (26 sem) |
| **Funcional SAP** | 512 horas | 14.2h/sem | Todo el proyecto (36 sem) |
| **Project Manager** | 163 horas | 4.5h/sem | Todo el proyecto (36 sem) |
| **TOTAL PROYECTO** | **1,880 horas** | **52.2h/sem** | **4 recursos Aunergia** |

**Nota:** ABAP Developer es un recurso **nuevo** en V2.04, no presente en V2.02. Permite reducir duración y riesgo técnico.

### Duración Optimizada V2.04

- **Tiempo total:** 36 semanas (~8.3 meses)
- **Inicio propuesto:** 6 de enero de 2026
- **Finalización estimada:** 13 de septiembre de 2026
- **Distribución por fase:** Fase 0: 6 semanas (328h) · Fase 1: 20 semanas (852h) · Fase 2: 10 semanas (700h) = 36 semanas / 1,880h totales
- **Restricciones:** Consultor BI máximo 30h/semana (promedio 26h/sem en V2.04)

**Ventajas vs V2.02:**
- ✅ Go-Live **6 semanas antes** (13-sep-2026 vs 15-oct-2026)
- ✅ ABAP Developer dedicado para **SLT y Z-transactions**
- ✅ Consultor BI con carga **sostenible** (26h/sem vs 22.9h/sem)
- ✅ **Paralelización efectiva**: ABAP extrae SAP, BI transforma BigQuery
- ✅ **Reducción de riesgo técnico** en Fase 1

### Beneficios Esperados

✅ **Reducción del 70%** en tiempo de extracción y consolidación de datos para todas las áreas
✅ **Dashboards disponibles en 24 horas** tras cierre mensual (vs. 5-7 días actuales)  
✅ **Eliminación de procesos manuales** propensos a errores en áreas críticas (Finanzas, Ventas, Inventario, OPEX)
✅ **Democratización del acceso** a datos mediante 12 dashboards Power BI (promedio ~3 hojas/páginas por dashboard)  
✅ **Plataforma completa** con 18 transacciones SAP automatizadas
✅ **Ahorro estimado:** 3,620 horas/año en procesos manuales
✅ **Go-Live 1 mes antes:** Valor de negocio adelantado (septiembre vs octubre 2026)

### Equipo del Proyecto V2.04

**Equipo Aunergia (4 recursos):**
- **Consultor BI** - Arquitecto de Datos y Desarrollador BigQuery/Power BI (935h)
- **ABAP Developer** - Especialista SAP SLT y Transacciones Custom (270h) **[NUEVO en V2.04]**
- **Funcional SAP** - Analista SAP Power User / Consultoría Funcional (512h)
- **Project Manager** - Coordinación y Seguimiento (163h)

**Equipo Elanco (requerido para el proyecto):**
- **SAP Basis (Elanco)** - Permisos SAP, configuración SLT, soporte infraestructura (bajo demanda, sin costo al proyecto)
- **David Saboya** - Analista IT TechOps CASA (coordinación con TI Global)
- **Representantes de Finanzas** - Validación de reportes y KPIs
- **Representantes de Supply Chain** - Validación de procesos logísticos

---

## ÍNDICE DE DOCUMENTOS V2.04

Esta propuesta está organizada en los siguientes documentos:

### 📄 **Parte 1: Contexto y Antecedentes**
- **00_PORTADA_Y_RESUMEN_EJECUTIVO_V2_04.md** (este documento)
- **01_CONTEXTO_Y_SITUACION_ACTUAL.md** - Análisis de la situación actual y problemática

### 📄 **Parte 2: Alcance y Transacciones**
- **02_ALCANCE_GENERAL_DE_LA_PROPUESTA.md** - Objetivos y alcance del proyecto
- **03_TRANSACCIONES_SAP_INCLUIDAS.md** - Detalle de las 18 transacciones SAP

### 📄 **Parte 3: Descripción de Fases V2.04**
- **04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD_V2_04.md** - Due diligence técnico (328h, 4 recursos)
- **05_FASE_1_CONSTRUCCION_DATA_LAKE_V2_04.md** - Automatización SAP → BigQuery (852h, ABAP 200h)
- **06_FASE_2_MODELADO_Y_DASHBOARDS_V2_04.md** - Power BI y reportería (700h, sin ABAP)
- **07_FASE_3_MODELOS_PREDICTIVOS.md** - Arquitectura de analítica avanzada

### 📄 **Parte 4: Estimaciones y Planificación V2.04**
- **08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS_V2_04.md** - Estimación de 1,880h detallada
- **09_CRONOGRAMA_SEMANAL_V2_04.md** - Planificación de 36 semanas

### 📄 **Parte 5: Requisitos y Cierre V2.04**
- **10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS_V2_04.md** - Prerrequisitos (incluye ABAP Dev)
- **11_RIESGOS_Y_SUPUESTOS_V2_04.md** - Análisis de riesgos (reclutamiento ABAP)
- **12_ENTREGABLES_Y_CONDICIONES_COMERCIALES.md** - Productos y términos contractuales

### 📊 **Documentos de Análisis**
- **RESUMEN_CAMBIOS_V2_04.md** - Comparativa detallada V2.02 vs V2.04
- **CRONOGRAMA_DETALLADO_TAREAS_V2_04.csv** - 25 tareas con horas por recurso

---

## COMPARATIVA DE VERSIONES

### V2.02 (Original) vs V2.04 (Optimizada)

| Métrica | V2.02 | V2.04 | Diferencia |
|---------|-------|-------|------------|
| **Duración Total** | 42 semanas | 36 semanas | -6 sem (-14%) |
| **Esfuerzo Total** | 1,590h | 1,880h | +290h (+18%) |
| **Consultor BI** | 961h (22.9h/sem) | 935h (26.0h/sem) | -26h (-3%) |
| **ABAP Developer** | 0h | 270h (10.4h/sem) | +270h (NUEVO) |
| **Funcional SAP** | 484h | 512h | +28h (+6%) |
| **Project Manager** | 145h | 163h | +18h (+12%) |
| **Recursos Aunergia** | 3 | 4 | +1 |
| **Go-Live** | ~15-oct-2026 | 13-sep-2026 | **-1 mes** |

**Recomendación:** V2.04 ofrece mejor balance costo-beneficio con Go-Live adelantado, menor riesgo técnico y carga de trabajo sostenible.

---

## INFORMACIÓN DE CONTACTO

### Aunergia

**Coordinación de Proyecto:**  
Project Manager  
*Información de contacto será proporcionada por Aunergia*

**Consultoría SAP:**  
Funcional SAP  
*Información de contacto será proporcionada por Aunergia*

**Especialista ABAP/SLT:**  
ABAP Developer (a reclutar)  
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

1. **Revisión de la propuesta V2.04** por stakeholders de Elanco (Semana 1)
2. **Comparativa V2.02 vs V2.04** y decisión sobre inversión adicional (+290h)
3. **Reunión de presentación** y aclaración de dudas (Semana 1-2)
4. **Decisión Go/No-Go** y aprobación de alcance (Semana 2-3)
5. **Inicio de reclutamiento ABAP Developer** (lead time 2-3 semanas)
6. **Firma de contrato** y definición de kick-off (Semana 3-4)
7. **Inicio de Fase 0** (6 de enero de 2026)

---

**Aunergia**  
*Optimización de Procesos de Negocio y Consultoría TI*  
Fundada en 2017 por ex ejecutivos de Big Four  

Clientes en: México, Centroamérica, Brasil, Chile, Perú, Uruguay, Colombia, España

---

*Documento generado: 10 de Noviembre 2025*  
*Versión 2.04 - Con ABAP Developer - Cronograma Moderado*

