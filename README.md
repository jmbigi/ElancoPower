# Elanco Power – Documentación del Proyecto

**Actualizado:** 10 de octubre de 2025  
**Proyecto:** Automatización SAP → BigQuery → Power BI  
**Cliente:** Elanco Animal Health  
**Consultoría:** Aunergia

---

## 📋 ESTRUCTURA DEL PROYECTO

### 🔴 PRESUPUESTOS (Documentos principales)

| Documento | Tipo | Monto | Descripción |
|-----------|------|-------|-------------|
| **`PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`** | ✅ NUEVO | **USD 8,850** | Presupuesto personal Juan Manuel Bigi (354h × USD 25/h). Solo trabajo técnico. |
| **`ANALISIS_DIFERENCIAS_PRESUPUESTOS.md`** | ✅ NUEVO | - | Comparativa y justificación entre presupuestos. |
| `presupuesto_actualizado.md` | Referencia | USD 48,000 | Propuesta integral Aunergia (equipo completo, 494h). |

---

## 📁 ARCHIVOS POR CATEGORÍA

### 1️⃣ Fuentes Primarias (Datos reales verificables)

| Archivo | Tipo | Fecha | Contenido |
|---------|------|-------|-----------|
| `conversaciones_con_lucia.md` | Audio transcrito | 09-oct-2025 | Audio WhatsApp Lucía explicando el proyecto (04:39 min) |
| `correo_1_de_lucia.md` | Email | 09-oct-2025 | Correo David Saboya (TI Elanco) con issues reportados |
| `Attach_2_Correo_1_Transacciones SAP.csv` | Datos | 09-oct-2025 | 22 transacciones SAP identificadas (prioridades) |
| `Attach_2_Correo_1_Transacciones SAP.xlsx` | Datos | 09-oct-2025 | Mismo contenido en formato Excel |
| `Attach_1_Correo_1_Texto_de_Imagen.md` | Especificación | - | Power User Persona (documento oficial Elanco) |

### 2️⃣ Configuración y Estado Actual

| Archivo | Descripción |
|---------|-------------|
| `Que_se_va_a_usar.txt` | Plataformas confirmadas por Finanzas/Operaciones (10-oct-2025) |
| `quienes_somos.txt` | Contexto del proyecto (participantes, empresas) |

### 3️⃣ Documentos Históricos / Referencia

| Archivo | Estado |
|---------|--------|
| `presupuesto_actualizado.md` | Propuesta Aunergia completa (USD 48,000) - REFERENCIA |
| `confirmacion_necesaria.txt` | Borrador de confirmación a enviar a Lucía - HISTÓRICO |

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

## 🔧 STACK TECNOLÓGICO CONFIRMADO

| Componente | Herramienta | Estado |
|------------|-------------|--------|
| **ERP** | SAP ECC (roles MM, SD, FI, CO) | ✅ Confirmado |
| **Data Lake** | Google BigQuery (dataset CASA) | ✅ Confirmado |
| **BI** | Microsoft Power BI | ✅ Licencias adquiridas (8 Pro) |
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
ME2L, MM60, MB59, ZVEL015, ME23N, FBL1N, FBL5N, MB5B, xk03, xd03

---

## ⚠️ ISSUES CRÍTICOS IDENTIFICADOS

**Fuente:** Correo David Saboya (TI Elanco), 09-oct-2025

### Issue #1: Permisos SAP insuficientes
> *"El usuario asignado como 'power user' para hacer la integración mediante BigQuery no contaba con todos los permisos para visualizar ciertas transacciones en SAP"*

**Estado:** ▶️ En curso (Ticket SAP-48219 escalado a TI Global)

### Issue #2: Tablas no disponibles en BigQuery
> *"Cada transacción cuenta con diferentes tablas, algunas de ellas no se encuentran en BigQuery por lo que se debe solicitar incluirlas para poder 'llamarlas' en la parte de codificación. Estas solicitudes se hacen por medio de tickets"*

**Estado:** ⏳ Pendiente (Tickets BQ-7713, BQ-7721 por abrir)

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

## 📖 CÓMO USAR ESTA CARPETA

### Si eres Lucía / Linda (Aunergia):
1. Lee **`PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`** para ver el costo de Juan Manuel Bigi
2. Lee **`ANALISIS_DIFERENCIAS_PRESUPUESTOS.md`** para entender diferencias con propuesta completa
3. Decide qué presupuesto presentar a Elanco:
   - USD 8,850 (solo JM Bigi) + vuestros costos
   - USD 48,000 (equipo completo Aunergia)
   - Híbrido (~USD 25,000)

### Si eres stakeholder Elanco:
1. Lee **`conversaciones_con_lucia.md`** para contexto del proyecto
2. Lee **`correo_1_de_lucia.md`** para ver los issues reportados por David Saboya
3. Revisa **`Que_se_va_a_usar.txt`** para confirmar plataformas
4. Lee el presupuesto elegido por Aunergia

### Si eres Juan Manuel Bigi (Manolo):
1. Tu presupuesto está en **`PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`**
2. Las transacciones a implementar están en **`Attach_2_Correo_1_Transacciones SAP.csv`**
3. Los issues técnicos están en **`correo_1_de_lucia.md`**
4. Las especificaciones del Power User están en **`Attach_1_Correo_1_Texto_de_Imagen.md`**

---

## 🔍 FUENTES DE VERDAD

### Datos financieros:
- **Presupuesto JM Bigi:** `PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md` (USD 8,850)
- **Presupuesto Aunergia completo:** `presupuesto_actualizado.md` (USD 48,000)

### Datos técnicos:
- **Transacciones SAP:** `Attach_2_Correo_1_Transacciones SAP.csv` (22 transacciones)
- **Plataformas confirmadas:** `Que_se_va_a_usar.txt` (SAP ECC, BigQuery, Power BI)
- **Issues reportados:** `correo_1_de_lucia.md` (permisos SAP, tablas BigQuery)
 - **Checklist permisos/licencias:** `checklist_permisos_y_licencias.md`
 - **Backlog transacciones SAP:** `transacciones_sap_backlog.md`

### Datos de contexto:
- **Audio explicativo:** `conversaciones_con_lucia.md` (09-oct-2025, 04:39 min)
- **Especificaciones técnicas:** `Attach_1_Correo_1_Texto_de_Imagen.md` (Power User Persona)
- **Participantes:** `quienes_somos.txt`

---

## 📞 CONTACTO

**Para consultas sobre presupuesto:**
- Lucía Rodríguez: lucia.rodriguez@aunergia.com.ar
- Linda López: [email pendiente]

**Para consultas técnicas:**
- Juan Manuel Bigi (Manolo): [email pendiente]
- David Saboya (Elanco TI): david.saboya@network.elancoah.com

---

**Última actualización:** 10 de octubre de 2025  
**Versión:** 2.0 - Presupuestos actualizados con fuentes primarias
