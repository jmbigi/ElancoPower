# Elanco Power – Documentación del Proyecto

**Actualizado:** 10 de octubre de 2025  
**Proyecto:** Automatización SAP → BigQuery → Power BI  
**Cliente:** Elanco Animal Health  
**Consultoría:** Aunergia

---

## � ESTRUCTURA DEL REPOSITORIO

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
    │   └── RESUMEN_EJECUTIVO_PARA_LUCIA.md
    ├── internos/                (documentos de trabajo)
    │   ├── ANALISIS_DIFERENCIAS_PRESUPUESTOS.md
    │   ├── AUDITORIA_FINAL_CONSOLIDACION.md
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

### 📦 Documentos para Entregar a Elanco

**Carpeta:** `docs/entregables/`

| Documento | Descripción | Páginas |
|-----------|-------------|---------|
| **PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md** | Presupuesto oficial (USD 8,850) | 29 |
| **RESUMEN_EJECUTIVO_PARA_LUCIA.md** | Versión resumida para Lucía | 8 |

### 📊 Documentos Internos de Trabajo

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

## � PRESUPUESTOS DISPONIBLES

| Presupuesto | Ubicación | Monto | Para quién |
|-------------|-----------|-------|------------|
| **Personal JM Bigi** | `docs/entregables/PRESUPUESTO_REAL_...` | **USD 8,850** | Lucía/Linda/Elanco |
| **Resumen Ejecutivo** | `docs/entregables/RESUMEN_EJECUTIVO_...` | USD 8,850 | Lucía (formato corto) |
| Propuesta Aunergia | `docs/historicos/presupuesto_actualizado.md` | USD 48,000 | Referencia histórica |

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

### Fases del Proyecto:
1. **Fase 0 (3-4 sem):** Due Diligence y habilitación de permisos
2. **Fase 1 (6-8 sem):** Automatización SAP → BigQuery (8 transacciones)
3. **Fase 2 (4-5 sem):** Modelado Power BI y dashboards (4-6 dashboards)
4. **Fase 3 (futuro):** Analítica predictiva (opcional)

### Presupuesto Personal Juan Manuel Bigi:

| Concepto | Horas | Costo |
|----------|-------|-------|
| Elaboración presupuesto | 10h | USD 250 |
| Fase 0 - Due Diligence | 40h | USD 1,000 |
| Fase 1 - Automatización | 156h | USD 3,900 |
| Fase 2 - Power BI | 148h | USD 3,700 |
| **TOTAL** | **354h** | **USD 8,850** |

**Tarifa:** USD 25/hora  
**Duración:** 13-17 semanas (~4 meses)  
**Inicio propuesto:** 14-oct-2025

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
| **Juan Manuel Bigi (Manolo)** | Desarrollador BigQuery/Power BI | Independiente | [pending] |
| **Lucía Rodríguez** | Analista SAP / Power User | Aunergia | lucia.rodriguez@aunergia.com.ar |
| **Linda López** | Coordinadora Proyecto | Aunergia | linda.lopez@aunergia.com.ar |
| **David Saboya** | Analista IT TechOps CASA | Elanco | david.saboya@network.elancoah.com |
| **Carolina Rondón** | [Rol TBD] | Elanco | carolina.rondon@elancoah.com |
| **Juan Sebastián Ravelo** | [Rol TBD] | Elanco | juan_sebastian.ravelo@elancoah.com |

---

## 📅 CRONOGRAMA PROPUESTO

| Hito | Fecha | Responsable | Estado |
|------|-------|-------------|--------|
| Aprobación presupuesto | 14-oct-2025 | Linda López | ⏳ Pendiente |
| Kick-off Fase 0 | 16-oct-2025 | Lucía + Manolo | 🗓️ Programado |
| Revisión tickets SAP/BigQuery | 18-oct-2025 | Lucía | ⏳ Pendiente |
| Go/No-Go Fase 1 | 07-nov-2025 | Equipo completo | 🗓️ Programado |
| Fin Fase 0 | 10-nov-2025 | - | 🗓️ Estimado |
| Fin Fase 1 | 05-ene-2026 | - | 🗓️ Estimado |
| Fin Fase 2 | 09-feb-2026 | - | 🗓️ Estimado |

**Duración total:** ~4 meses (13-17 semanas)

---

## 🚨 DEPENDENCIAS CRÍTICAS

**Antes de iniciar Fase 1:**
1. ✅ Permisos SAP completos para power user (Ticket SAP-48219)
2. ✅ Tablas críticas disponibles en BigQuery (Tickets BQ-7713, BQ-7721)
3. ✅ Accesos BigQuery Data Editor activos
4. ✅ Backlog de transacciones priorizado y firmado

---

## 📖 GUÍA DE USO POR ROL

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
- Juan Manuel Bigi (Manolo): [email pendiente]
- David Saboya (Elanco TI): david.saboya@network.elancoah.com

---

## 📌 NOTAS FINALES

- ✅ **inputs/**: Contiene fuentes primarias verificables (NO modificar)
- ✅ **docs/entregables/**: Documentos listos para enviar a cliente
- ✅ **docs/internos/**: Documentos de trabajo y análisis
- ✅ **docs/historicos/**: Archivos de referencia histórica

**Para más detalles:** Ver `docs/internos/INDICE_COMPLETO.md`

---

**Última actualización:** 10 de octubre de 2025  
**Versión:** 3.0 - Repositorio reorganizado y estructurado  
**Estructura:** inputs/ (fuentes) + docs/ (entregables, internos, históricos)
