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

### (Histórico) Referencias a "Solución SLT Completa"

Las referencias a una carpeta `docs/propuesta_final/solucion_slt_completa/` y su documentación específica fueron removidas porque **esa carpeta no existe en el repositorio actual**. El contenido relevante sobre replicación mediante **SAP SLT** fue absorbido en las secciones técnicas de la propuesta final (ver `05_FASE_1_CONSTRUCCION_DATA_LAKE.md` y `ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md`).

Si en el futuro se desea reinstaurar una documentación separada para una "Solución SLT Completa", deberá crearse primero la carpeta y luego incorporar un índice propio. Mientras tanto el **SSOT** permanece en `docs/propuesta_final/`.

> Nota: Presupuesto histórico asociado (USD 122,595) marcado como referencia histórica; no altera cifras canónicas del proyecto integral (1,590h).

---

### 📦 Documentos para Entregar a Elanco

**Carpeta:** `docs/entregables/`

| Documento | Descripción | Páginas |
|-----------|-------------|---------|
| **PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md** | Presupuesto oficial (USD 8,850) | 29 |
| **RESUMEN_EJECUTIVO_PARA_LUCIA.md** | Versión resumida para Lucía | 8 |

### 📊 Documentos Internos de Trabajo (solo referencia, no alteran cifras canónicas)

Nota sobre `docs/internos/`: Se eliminaron referencias a documentos internos específicos porque esa carpeta no contiene archivos en este repo. Cuando haga falta, se podrán reintroducir como documentación de trabajo no canónica. El SSOT sigue siendo `docs/propuesta_final/` y `docs/entregables/`.

### 📚 Archivos Históricos (removidos)

Los archivos históricos previamente referenciados (`presupuesto_actualizado.md`, `confirmacion_necesaria.txt`) ya no están presentes en el repositorio. Se eliminan referencias para mantener consistencia. Si se requiere recuperarlos, crear la carpeta `docs/historicos/` y restaurar su contenido.

---

## 💰 PRESUPUESTOS DISPONIBLES

| Presupuesto | Ubicación | Monto / Horas | Para quién | Estado |
|-------------|-----------|---------------|------------|--------|
| **Solución SLT Completa (Histórico)** | (carpeta no presente) | **USD 122,595** | Cliente/Ejecutivos | 📚 Histórico |
| **Propuesta Integral Data Lake** | `docs/propuesta_final/` | **1,590 horas** | Equipo Aunergia/Elanco | ✅ **CANÓNICO** |
| **Personal JM Bigi (Inicial)** | `docs/entregables/PRESUPUESTO_REAL_...` | **354 horas** | Lucía/Linda/Elanco | 📚 Histórico |
| **Resumen Ejecutivo (Inicial)** | `docs/entregables/RESUMEN_EJECUTIVO_...` | 354 horas (resumen) | Lucía (formato corto) | 📚 Histórico |
| Propuesta Aunergia (Antigua) | (archivo removido) | USD 48,000 | Referencia histórica | 📚 Fuera del repo |

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
Automatizar la extracción de datos desde **SAP S/4HANA** y centralizarlos en **Google BigQuery** para habilitar analítica corporativa con **Microsoft Power BI**.

### Fases del Proyecto (cronograma unificado 42 semanas):
1. **Fase 0 (6 sem):** Revisión de alcance, factibilidad y piloto (Due Diligence + Go/No-Go)
2. **Fase 1 (22 sem):** Construcción del Data Lake y automatización SAP → BigQuery (18 transacciones)
3. **Fase 2 (14 sem):** Modelo dimensional y 12 dashboards en Power BI (incluye UAT y capacitación)
4. **Fase 3 (conceptual):** Modelos predictivos (arquitectura y roadmap, sin implementación)

### Esfuerzo Personal Juan Manuel Bigi (Estimación Inicial - Desactualizada):

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
| **ERP** | SAP S/4HANA (roles MM, SD, FI, CO) | ✅ Confirmado |
| **Data Lake** | Google BigQuery (dataset casa_bi: dev / qa / prod) | ✅ Confirmado |
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
Estado de permisos: consolidado en `docs/propuesta_final/10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md`.

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
| **Consultor BI** | Desarrollador BigQuery/Power BI | Independiente | [pending] |
| **Funcional SAP** | Analista SAP / Power User | Aunergia | lucia.rodriguez@aunergia.com.ar |
| **Project Manager** | Coordinadora Proyecto | Aunergia | linda.lopez@aunergia.com.ar |
| **David Saboya** | Analista IT TechOps CASA | Elanco | david.saboya@network.elancoah.com |
| **Carolina Rondón** | [Rol TBD] | Elanco | carolina.rondon@elancoah.com |
| **Juan Sebastián Ravelo** | [Rol TBD] | Elanco | juan_sebastian.ravelo@elancoah.com |

---

## 📅 CRONOGRAMA PROPUESTO (alineado a `docs/propuesta_final/09_CRONOGRAMA_SEMANAL.md`)

| Hito | Fecha estimada | Responsable | Estado |
|------|----------------|-------------|--------|
| Aprobación propuesta consolidada | Nov-2025 | Project Manager | ✅ Actualizado |
| Kick-off Fase 0 (Semana 0) | 6-ene-2026 | Funcional SAP + Consultor BI | 🗓️ Programado |
| Go/No-Go (Fin Fase 0, Semana 6) | 17-feb-2026 | Equipo completo | 🗓️ Programado |
| Fin Fase 1 (Semana 28) | 19-jul-2026 | Equipo técnico | 🗓️ Estimado |
| Fin Fase 2 / Go-Live dashboards (Semana 42) | 14-oct-2026 | Equipo completo | 🗓️ Estimado |
| Soporte post go-live (30 días) | Oct-Nov 2026 | Consultor BI + Funcional SAP | 🗓️ Planificado |

**Duración total:** 42 semanas (~10 meses).
**Restricción:** Consultor BI trabaja máximo 6h/día (30h/semana) – contemplado en las 1,590h.

## 🔄 Consistencia de Datos (resumen rápido – fuentes únicas y prevalentes)

| Dimensión | Valor actual | Fuente canónica | Observaciones |
|-----------|--------------|-----------------|---------------|
| Transacciones SAP | 18 | `docs/propuesta_final/03_TRANSACCIONES_SAP_INCLUIDAS.md` | Unificado (Prioridad 1/2 + restantes) |
| Dashboards Power BI | 12 | `docs/propuesta_final/06_FASE_2_MODELADO_Y_DASHBOARDS.md` | Consistente tras correcciones 8-nov |
| Horas totales | 1,590 | `docs/propuesta_final/08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md` + `docs/propuesta_final/CRONOGRAMA_DETALLADO_TAREAS.csv` | JMB 961 / Lucía 484 / Linda 145 (bloques históricos marcados) |
| Duración | 42 semanas | `docs/propuesta_final/09_CRONOGRAMA_SEMANAL.md` | Sustituye duraciones previas |
| Tablas SAP estimadas | 25 | `docs/propuesta_final/ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md` | Número optimizado por Universal Journal (S/4HANA). Sustituye rangos previos (~70-90). |
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

### 🌟 Para **Ejecutivos y Project Managers**:
1. **Inicio Rápido:** `RESUMEN_PROPUESTA_FINAL.txt` (Resumen de 5 minutos).
2. **Propuesta Canónica:** `docs/propuesta_final/` (Navegar los documentos 00-12 para ver el detalle completo del proyecto, esfuerzo de 1,590h y cronograma de 42 semanas).
3. **Entregables:** `docs/propuesta_final/12_ENTREGABLES_Y_CONDICIONES_COMERCIALES.md` (Lista de los 20 entregables formales).

### ⚙️ Para el **Equipo Técnico (Desarrollo, SAP, Datos)**:
1. **Contexto y Problemas:** `docs/propuesta_final/01_CONTEXTO_Y_SITUACION_ACTUAL.md`.
2. **Alcance Técnico:** `docs/propuesta_final/03_TRANSACCIONES_SAP_INCLUIDAS.md` (18 transacciones) y `docs/propuesta_final/ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md` (25 tablas).
3. **Fases y Tareas:** `docs/propuesta_final/04_FASE_0...`, `05_FASE_1...`, `06_FASE_2...` para el detalle de cada etapa.
4. **Requisitos y Riesgos:** `docs/propuesta_final/10_REQUISITOS...` y `11_RIESGOS...`.

### 📚 Para **Referencias Históricas**:
1. **Presupuestos Iniciales:** `docs/entregables/` contiene los presupuestos iniciales (ej. 354h). Estos documentos son **históricos** y no reflejan el alcance final.
2. **Fuentes Originales:** `inputs/` contiene los correos y archivos originales que dieron inicio al proyecto. No deben ser modificados.

---

## 🔍 REFERENCIAS RÁPIDAS

### Referencias Eliminadas (Solución SLT Completa)

La tabla anterior de documentos específicos SLT fue removida; la solución se documenta ahora de forma integrada. Ver:
- Arquitectura y conectores: `05_FASE_1_CONSTRUCCION_DATA_LAKE.md`
- Replicación tablas vs transacciones: `ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md`

### 💰 Presupuestos:
| Documento | Ubicación | Monto |
| 22 Transacciones SAP | `inputs/Attach_2_Correo_1_Transacciones SAP.csv` |
| Transacciones (normalizado) | `inputs/Attach_2_Correo_1_Transacciones SAP.normalized.csv` |
| Plataformas confirmadas | `inputs/Que_se_va_a_usar.txt` |
| Issues reportados | `inputs/correo_1_de_lucia.md` |
| Checklist permisos | `docs/propuesta_final/10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS.md` |
| Backlog priorizado | `docs/propuesta_final/04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD.md` |

### 📝 Contexto:
| Documento | Ubicación |
|-----------|-----------|
| Audio transcrito (04:39) | `inputs/conversaciones_con_lucia.md` |
| Power User Persona | `inputs/Attach_1_Correo_1_Texto_de_Imagen.md` |
| Participantes | `inputs/quienes_somos.txt` |
| Índice de la Propuesta Final | `docs/propuesta_final/README.md` |

---

## 📞 CONTACTO

**Para consultas sobre presupuesto:**
- Funcional SAP: lucia.rodriguez@aunergia.com.ar
- Project Manager: linda.lopez@aunergia.com.ar

**Para consultas técnicas:**
- Consultor BI: [email pendiente]
- David Saboya (Elanco TI): david.saboya@network.elancoah.com

---

## 📌 NOTAS FINALES

- ✅ **inputs/**: Contiene fuentes primarias verificables (NO modificar)
- ✅ **docs/entregables/**: Documentos listos para enviar a cliente
   (Se removieron referencias a `docs/internos/` inexistentes en este repo; usar propuesta_final y entregables como fuentes vigentes.)
- ✅ **docs/historicos/**: Archivos de referencia histórica

Para más detalles, navegar `docs/propuesta_final/` y sus secciones 00–12.

---

**Última actualización:** 7 de noviembre de 2025  
**Versión:** 4.0 - Incluye Solución SLT Completa  
**Estructura:** inputs/ (fuentes) + docs/ (entregables, propuesta_final, internos, históricos)

**Novedades Noviembre 2025:**
   (Se eliminó referencia a carpeta inexistente `solucion_slt_completa/`)
- ⭐ 50+ scripts funcionales listos para implementación
- ⭐ Documentación auditada y aprobada (98/100 puntos)
- ⭐ Presupuesto completo: $122,595 año 1, 10 semanas

````
