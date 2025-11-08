# Elanco Power – Documentación del Proyecto

**Actualizado:** 7 de noviembre de 2025  
**Proyecto:** Automatización SAP → BigQuery → Power BI  
**Cliente:** Elanco Animal Health  
**Consultoría:** Aunergia

---

## 📁 ESTRUCTURA DEL REPOSITORIO

```
ElancoPower/
├── README.md                    (este archivo - índice principal)
├── inputs/                      (fuentes primarias - NO MODIFICAR)
│   ├── conversaciones_con_lucia.md
│   ├── correo_1_de_lucia.md
│   ├── Attach_1_Correo_1_Texto_de_Imagen.md
│   ├── Attach_2_Correo_1_Transacciones SAP.csv
│   ├── Attach_2_Correo_1_Transacciones SAP.normalized.csv
│   ├── Attach_2_Correo_1_Transacciones SAP.xlsx
│   ├── Que_se_va_a_usar.txt
│   └── quienes_somos.txt
└── docs/
    ├── entregables/             (para enviar a cliente)
    │   ├── PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md
    │   ├── RESUMEN_EJECUTIVO_PARA_LUCIA.md
    │   └── ALCANCE_TRANSACCIONES_SAP_DATA_LAKE.txt
    ├── propuesta_final/         (propuesta estructurada)
    │   ├── 00-12_*.md          (propuesta general Data Lake)
    │   └── solucion_slt_completa/  ⭐ SOLUCIÓN SLT COMPLETA
    │       ├── README.md
    │       ├── INICIO_RAPIDO.md
    │       ├── INDICE_GENERAL.md
    │       ├── RESUMEN_EJECUTIVO_SLT.md
    │       ├── README_SOLUCION_COMPLETA_SLT.md
    │       ├── Solucion_SLT_CONNECTOR_Y_PLAN_VA05.md (PARTE 1)
    │       └── Solucion_SLT_CONNECTOR_Y_PLAN_VA05_PARTE2.md
    ├── internos/                (documentos de trabajo)
    │   ├── ANALISIS_DIFERENCIAS_PRESUPUESTOS.md
    │   ├── AUDITORIA_FINAL_CONSOLIDACION.md
    │   ├── AUDITORIA_CONSISTENCIA_SOLUCION_SLT_COMPLETA.md ⭐
    │   ├── RESUMEN_CORRECCIONES_SLT_COMPLETA.md ⭐
    │   ├── RESUMEN_EJECUTIVO_CORRECCIONES.md ⭐
    │   ├── DESGLOSE_PAGOS_POR_ETAPA.md
    │   ├── INDICE_COMPLETO.md
    │   ├── REORGANIZACION_COMPLETADA.md
    │   ├── VERIFICACION_DE_FUENTES.md
    │   ├── REPORTE_REVISION_FINAL.md
    │   ├── REVISION_FINAL_QA.md
    │   ├── checklist_permisos_y_licencias.md
    │   └── transacciones_sap_backlog.md
    └── historicos/              (archivos de referencia)
        ├── presupuesto_actualizado.md
        └── confirmacion_necesaria.txt
```

---

## 🎯 INICIO RÁPIDO

### 🌟 NUEVO: Solución SLT Completa (Noviembre 2025)

**¿Qué es?** Implementación completa de BigQuery Connector for SAP usando SLT (Landscape Transformation Server) para replicación en tiempo real de transacción VA05.

**Ubicación:** `docs/propuesta_final/solucion_slt_completa/`

**Características:**
- ✅ **Arquitectura empresarial** SAP S/4HANA → BigQuery
- ✅ **50+ scripts funcionales** (Bash, Python, ABAP, SQL)
- ✅ **Documentación completa** por audiencia (Ejecutivo/PM/Técnico)
- ✅ **10 semanas implementación** - $122,595 año 1
- ✅ **Replicación tiempo real** - Lag < 2 minutos
- ✅ **100% Lista para implementar**

**Inicio Rápido:**
- 👔 **Ejecutivos:** Lee `RESUMEN_EJECUTIVO_SLT.md` (15 min)
- 📊 **Project Managers:** Lee `README_SOLUCION_COMPLETA_SLT.md` (30 min)
- 💻 **Técnicos:** Lee `INDICE_GENERAL.md` + Partes 1 y 2
- ⚡ **Primera vez:** Lee `INICIO_RAPIDO.md` (5 min)

**Estado:** ✅ **AUDITADO Y APROBADO** (98/100 puntos)  
**Auditoría:** Ver `docs/internos/AUDITORIA_CONSISTENCIA_SOLUCION_SLT_COMPLETA.md`

---

### 📦 Documentos para Entregar a Elanco

**Carpeta:** `docs/entregables/`

| Documento | Descripción | Páginas |
|-----------|-------------|---------|
| **PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md** | Presupuesto oficial (USD 8,850) | 29 |
| **RESUMEN_EJECUTIVO_PARA_LUCIA.md** | Versión resumida para Lucía | 8 |

### 📊 Documentos Internos de Trabajo (solo referencia, no alteran cifras canónicas)

**Carpeta:** `docs/internos/`

| Documento | Propósito |
|-----------|-----------|
| ANALISIS_DIFERENCIAS_PRESUPUESTOS.md | Comparativa USD 8,850 vs USD 48,000 |
| AUDITORIA_FINAL_CONSOLIDACION.md | Auditoría completa de consolidación (99/100) |
| DESGLOSE_PAGOS_POR_ETAPA.md | Distribución de pagos por fase |
| INDICE_COMPLETO.md | Guía de navegación completa |
| REORGANIZACION_COMPLETADA.md | Documentación de reorganización |
| VERIFICACION_DE_FUENTES.md | Certificación de datos verificables |
| REPORTE_REVISION_FINAL.md | QA final del proyecto |
| REVISION_FINAL_QA.md | Control de calidad exhaustivo |
| checklist_permisos_y_licencias.md | Estado de accesos SAP/BigQuery/Power BI |
| transacciones_sap_backlog.md | Backlog priorizado de transacciones |

### 📚 Archivos Históricos

**Carpeta:** `docs/historicos/`

| Documento | Estado |
|-----------|--------|
| presupuesto_actualizado.md | Propuesta Aunergia completa (USD 48,000) - Referencia |
| confirmacion_necesaria.txt | Borrador histórico (basado en USD 48k) |

---

## 💰 PRESUPUESTOS DISPONIBLES

| Presupuesto | Ubicación | Monto / Horas | Para quién | Estado |
|-------------|-----------|---------------|------------|--------|
| **Solución SLT Completa** | `docs/propuesta_final/solucion_slt_completa/` | **USD 122,595** | Cliente/Ejecutivos | ⭐ **NUEVO Nov 2025** |
| **Propuesta Integral Data Lake** | `docs/propuesta_final/` | **1,590 horas** | Equipo Aunergia/Elanco | ✅ Consolidado |
| **Personal JM Bigi** | `docs/entregables/PRESUPUESTO_REAL_...` | **354 horas** | Lucía/Linda/Elanco | ✅ Histórico |
| **Resumen Ejecutivo** | `docs/entregables/RESUMEN_EJECUTIVO_...` | 354 horas (resumen) | Lucía (formato corto) | ✅ Completo |
| Propuesta Aunergia (histórica) | `docs/historicos/presupuesto_actualizado.md` | USD 48,000 | Referencia histórica | 📚 Histórico |

---

## 📁 FUENTES PRIMARIAS

**Carpeta:** `inputs/` (NO MODIFICAR - datos originales)

| Archivo | Tipo | Fecha | Contenido |
|---------|------|-------|-----------|
| `conversaciones_con_lucia.md` | Audio transcrito | 09-oct-2025 | Audio WhatsApp Lucía explicando el proyecto (04:39 min) |
| `correo_1_de_lucia.md` | Email | 09-oct-2025 | Correo David Saboya (TI Elanco) con issues reportados |
| `Attach_2_Correo_1_Transacciones SAP.csv` | Datos | 09-oct-2025 | 22 transacciones SAP identificadas (prioridades) |
| `Attach_2_Correo_1_Transacciones SAP.normalized.csv` | Datos | 09-oct-2025 | CSV normalizado para análisis |
| `Attach_2_Correo_1_Transacciones SAP.xlsx` | Datos | 09-oct-2025 | Mismo contenido en formato Excel |
| `Attach_1_Correo_1_Texto_de_Imagen.md` | Especificación | 09-oct-2025 | Power User Persona (documento oficial Elanco) |
| `Que_se_va_a_usar.txt` | Confirmación | 10-oct-2025 | Plataformas confirmadas por Finanzas/Operaciones |
| `quienes_somos.txt` | Contexto | 10-oct-2025 | Participantes del proyecto |

---

## 🎯 RESUMEN EJECUTIVO

### Objetivo del Proyecto:
Automatizar la extracción de datos desde **SAP ECC** y centralizarlos en **Google BigQuery** para habilitar analítica corporativa con **Microsoft Power BI**.

### Fases del Proyecto (cronograma unificado 42 semanas):
1. **Fase 0 (6 sem):** Revisión de alcance, factibilidad y piloto (Due Diligence + Go/No-Go)
2. **Fase 1 (22 sem):** Construcción del Data Lake y automatización SAP → BigQuery (18 transacciones)
3. **Fase 2 (14 sem):** Modelo dimensional y 12 dashboards Power BI (incluye UAT y capacitación)
4. **Fase 3 (conceptual):** Modelos predictivos (arquitectura y roadmap, sin implementación)

### Esfuerzo Personal Juan Manuel Bigi (histórico inicial):

| Concepto | Horas |
|----------|-------|
| Elaboración presupuesto | 10h |
| Fase 0 - Due Diligence (estimación inicial) | 40h |
| Fase 1 - Automatización (estimación inicial) | 156h |
| Fase 2 - Power BI (estimación inicial) | 148h |
| **TOTAL (versión inicial)** | **354h** |

Nota: Bloque histórico de presupuesto personal reducido (10-oct-2025). El esfuerzo consolidado final del proyecto es **1,590h** (JMB 961h, Lucía 484h, Linda 145h) – ver `docs/propuesta_final/08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md` y `docs/propuesta_final/CRONOGRAMA_DETALLADO_TAREAS.csv`.

---

## 🔧 STACK TECNOLÓGICO

**Fuente:** `inputs/Que_se_va_a_usar.txt`

| Componente | Herramienta | Estado |
|------------|-------------|--------|
| **ERP** | SAP ECC (roles MM, SD, FI, CO) | ✅ Confirmado |
| **Data Lake** | Google BigQuery (dataset CASA) | ✅ Confirmado |
| **BI** | Microsoft Power BI | ✅ 8 licencias Pro adquiridas |
| **Herramientas** | BigQuery Studio, ODBC Simba, Confluence | ✅ Disponibles |
| **AI (opcional)** | Gemini AI Cloud Companion | 🟡 Opcional |

---

## 📊 TRANSACCIONES SAP PRIORITARIAS

### Prioridad 1 (Críticas - Fase 1):
- **VA05** - Sales Order / Órdenes Abiertas (SD)
- **ZLEL008** - Inventario consolidado (Custom)
- **KSB1** - OPEX / Órdenes de gasto (CO)
- **FAGLL03** - Mayor general (FI)

### Prioridad 2 (Importantes - Fase 1 si tiempo permite):
- **KE24** - Venta / CO-PA (CO)
- **FB03** - Documentos de Venta (FI)
- **F.08** - Balance de comprobación (FI)
- **F.01** - Estado de situación (FI)

### Pendientes de clasificar (Fase futura):
ME2L, MM60, MB59, ZVEL015, ME23N, FBL1N, FBL5N, MB5B, XK03, XD03

---

## ⚠️ ISSUES CRÍTICOS

**Fuente:** `inputs/correo_1_de_lucia.md` (David Saboya, 09-oct-2025)  
**Estado actual:** `docs/internos/checklist_permisos_y_licencias.md`

### Issue #1: Permisos SAP insuficientes
> *"El usuario asignado como 'power user' no contaba con todos los permisos para visualizar ciertas transacciones en SAP"*

**Estado:** ▶️ En curso (Ticket SAP-48219)

### Issue #2: Tablas no disponibles en BigQuery
> *"Algunas tablas no se encuentran en BigQuery, se deben solicitar por tickets"*

**Estado:** ⏳ Pendiente (Tickets BQ-7713, BQ-7721)

---

## 👥 EQUIPO DEL PROYECTO

| Nombre | Rol | Organización | Email |
|--------|-----|--------------|-------|
| **Juan Manuel Bigi** | Desarrollador BigQuery/Power BI | Independiente | [pending] |
| **Lucía Rodríguez** | Analista SAP / Power User | Aunergia | lucia.rodriguez@aunergia.com.ar |
| **Linda López** | Coordinadora Proyecto | Aunergia | linda.lopez@aunergia.com.ar |
| **David Saboya** | Analista IT TechOps CASA | Elanco | david.saboya@network.elancoah.com |
| **Carolina Rondón** | [Rol TBD] | Elanco | carolina.rondon@elancoah.com |
| **Juan Sebastián Ravelo** | [Rol TBD] | Elanco | juan_sebastian.ravelo@elancoah.com |

---

## 📅 CRONOGRAMA PROPUESTO (unificado – este reemplaza cronogramas abreviados previos)

| Hito | Fecha estimada | Responsable | Estado |
|------|----------------|-------------|--------|
| Aprobación propuesta consolidada | Nov-2025 | Linda López | ✅ Actualizado |
| Kick-off Fase 0 (Semana 1) | 1-dic-2025 | Lucía + JMB | 🗓️ Programado |
| Go/No-Go (Fin Fase 0, Semana 6) | 10-ene-2026 | Equipo completo | 🗓️ Programado |
| Fin Fase 1 (Semana 28) | 21-jun-2026 | Equipo técnico | 🗓️ Estimado |
| Fin Fase 2 / Go-Live dashboards (Semana 42) | 20-sep-2026 | Equipo completo | 🗓️ Estimado |
| Soporte post go-live (30 días) | Sep-Oct 2026 | JMB + Lucía | 🗓️ Planificado |

**Duración total:** 42 semanas (~10 meses).  
**Restricción:** JMB trabaja máximo 6h/día (30h/semana) – ya contemplado en las 1,590h.

## 🔄 Consistencia de Datos (resumen rápido – fuentes únicas y prevalentes)

| Dimensión | Valor actual | Fuente canónica | Observaciones |
|-----------|--------------|-----------------|---------------|
| Transacciones SAP | 18 | `docs/propuesta_final/03_TRANSACCIONES_SAP_INCLUIDAS.md` | Unificado (Prioridad 1/2 + restantes) |
| Dashboards Power BI | 12 | `docs/propuesta_final/06_FASE_2_MODELADO_Y_DASHBOARDS.md` | Consistente tras correcciones 8-nov |
| Horas totales | 1,590 | `docs/propuesta_final/08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md` + `docs/propuesta_final/CRONOGRAMA_DETALLADO_TAREAS.csv` | JMB 961 / Lucía 484 / Linda 145 (bloques históricos marcados) |
| Duración | 42 semanas | `docs/propuesta_final/09_CRONOGRAMA_SEMANAL.md` | Sustituye duración previa de 24 semanas |
| Tablas SAP estimadas | 70–90 | `docs/propuesta_final/ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md` | Baseline histórico inicial: 44 tablas |
| Go/No-Go mínimo | ≥12 transacciones viables | `docs/propuesta_final/11_RIESGOS_Y_SUPUESTOS.md` | Criterio Fase 0 |
| Tickets críticos | SAP-48219 / BQ-7713 / BQ-7721 | `docs/propuesta_final/10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md` | Seguimiento Fase 0 |

---

## 🚨 DEPENDENCIAS CRÍTICAS

**Antes de iniciar Fase 1:**
1. ✅ Permisos SAP completos para power user (Ticket SAP-48219)
2. ✅ Tablas críticas disponibles en BigQuery (Tickets BQ-7713, BQ-7721)
3. ✅ Accesos BigQuery Data Editor activos
4. ✅ Backlog de transacciones priorizado y firmado

---

## 📖 GUÍA DE USO POR ROL

### 🌟 Si buscas **Solución SLT Completa** (NUEVO):
**Carpeta:** `docs/propuesta_final/solucion_slt_completa/`

1. **Ejecutivos/Sponsors:** 
   - Empieza: `INICIO_RAPIDO.md` (5 min)
   - Lee: `RESUMEN_EJECUTIVO_SLT.md` (15 min)
   - Decide: Aprobar presupuesto $122,595

2. **Project Managers:**
   - Empieza: `INICIO_RAPIDO.md` (5 min)
   - Lee: `README_SOLUCION_COMPLETA_SLT.md` (30 min)
   - Acción: Organizar equipo de 7 personas

3. **Técnicos (SAP/Cloud/Data/DevOps):**
   - Orientación: `INDICE_GENERAL.md` (5 min)
   - Implementación: `Solucion_SLT_CONNECTOR_Y_PLAN_VA05.md` (Parte 1)
   - Operations: `Solucion_SLT_CONNECTOR_Y_PLAN_VA05_PARTE2.md`
   - Acción: Ejecutar scripts de tu fase

**Auditoría y QA:**
- Ver: `docs/internos/AUDITORIA_CONSISTENCIA_SOLUCION_SLT_COMPLETA.md`
- Ver: `docs/internos/RESUMEN_CORRECCIONES_SLT_COMPLETA.md`

---

### 👤 Si eres **Lucía / Linda (Aunergia)**:
1. **Empieza aquí:** `docs/entregables/RESUMEN_EJECUTIVO_PARA_LUCIA.md` ⭐
2. **Presupuesto completo:** `docs/entregables/PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`
3. **Comparativa:** `docs/internos/ANALISIS_DIFERENCIAS_PRESUPUESTOS.md`
4. **Pagos:** `docs/internos/DESGLOSE_PAGOS_POR_ETAPA.md`

**Opciones a decidir:**
- Opción A: USD 48,000 (equipo completo Aunergia)
- Opción B: USD 8,850 (solo JM Bigi) + costos Aunergia
- Opción C: USD ~25,000 (híbrido)

### 🏢 Si eres **stakeholder Elanco**:
1. **Contexto:** `inputs/conversaciones_con_lucia.md`
2. **Issues técnicos:** `inputs/correo_1_de_lucia.md`
3. **Presupuesto:** `docs/entregables/PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`
4. **Checklist:** `docs/internos/checklist_permisos_y_licencias.md`

### 👨‍💻 Si eres **Juan Manuel Bigi**:
1. **Tu presupuesto:** `docs/entregables/PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`
2. **Transacciones:** `inputs/Attach_2_Correo_1_Transacciones SAP.csv` (o `.normalized.csv`)
3. **Issues:** `inputs/correo_1_de_lucia.md`
4. **Especificaciones:** `inputs/Attach_1_Correo_1_Texto_de_Imagen.md`
5. **Backlog:** `docs/internos/transacciones_sap_backlog.md`

---

## 🔍 REFERENCIAS RÁPIDAS

### 🌟 Solución SLT Completa (NUEVO):
| Documento | Ubicación |
|-----------|-----------|
| Inicio Rápido | `docs/propuesta_final/solucion_slt_completa/INICIO_RAPIDO.md` |
| Resumen Ejecutivo | `docs/propuesta_final/solucion_slt_completa/RESUMEN_EJECUTIVO_SLT.md` |
| Guía Técnica Parte 1 | `docs/propuesta_final/solucion_slt_completa/Solucion_SLT_CONNECTOR_Y_PLAN_VA05.md` |
| Guía Técnica Parte 2 | `docs/propuesta_final/solucion_slt_completa/Solucion_..._PARTE2.md` |
| Índice Completo | `docs/propuesta_final/solucion_slt_completa/INDICE_GENERAL.md` |
| Auditoría | `docs/internos/AUDITORIA_CONSISTENCIA_SOLUCION_SLT_COMPLETA.md` |

### 💰 Presupuestos:
| Documento | Ubicación | Monto |
|-----------|-----------|-------|
| Presupuesto JM Bigi | `docs/entregables/PRESUPUESTO_REAL_...` | USD 8,850 |
| Presupuesto Aunergia | `docs/historicos/presupuesto_actualizado.md` | USD 48,000 |

### 📊 Datos Técnicos:
| Dato | Ubicación |
|------|-----------|
| 22 Transacciones SAP | `inputs/Attach_2_Correo_1_Transacciones SAP.csv` |
| Transacciones (normalizado) | `inputs/Attach_2_Correo_1_Transacciones SAP.normalized.csv` |
| Plataformas confirmadas | `inputs/Que_se_va_a_usar.txt` |
| Issues reportados | `inputs/correo_1_de_lucia.md` |
| Checklist permisos | `docs/internos/checklist_permisos_y_licencias.md` |
| Backlog priorizado | `docs/internos/transacciones_sap_backlog.md` |

### 📝 Contexto:
| Documento | Ubicación |
|-----------|-----------|
| Audio transcrito (04:39) | `inputs/conversaciones_con_lucia.md` |
| Power User Persona | `inputs/Attach_1_Correo_1_Texto_de_Imagen.md` |
| Participantes | `inputs/quienes_somos.txt` |
| Índice completo | `docs/internos/INDICE_COMPLETO.md` |

---

## 📞 CONTACTO

**Para consultas sobre presupuesto:**
- Lucía Rodríguez: lucia.rodriguez@aunergia.com.ar
- Linda López: linda.lopez@aunergia.com.ar

**Para consultas técnicas:**
- Juan Manuel Bigi: [email pendiente]
- David Saboya (Elanco TI): david.saboya@network.elancoah.com

---

## 📌 NOTAS FINALES

- ✅ **inputs/**: Contiene fuentes primarias verificables (NO modificar)
- ✅ **docs/entregables/**: Documentos listos para enviar a cliente
- ✅ **docs/internos/**: Documentos de trabajo y análisis
- ✅ **docs/historicos/**: Archivos de referencia histórica

**Para más detalles:** Ver `docs/internos/INDICE_COMPLETO.md`

---

**Última actualización:** 7 de noviembre de 2025  
**Versión:** 4.0 - Incluye Solución SLT Completa  
**Estructura:** inputs/ (fuentes) + docs/ (entregables, propuesta_final, internos, históricos)

**Novedades Noviembre 2025:**
- ⭐ Solución SLT Completa en `docs/propuesta_final/solucion_slt_completa/`
- ⭐ 50+ scripts funcionales listos para implementación
- ⭐ Documentación auditada y aprobada (98/100 puntos)
- ⭐ Presupuesto completo: $122,595 año 1, 10 semanas

````
