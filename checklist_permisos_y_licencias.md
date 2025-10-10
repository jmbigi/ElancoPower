# Checklist de Permisos, Licencias y Habilidades Requeridas

Actualizado el **10-oct-2025** tras la revisión conjunta con Finanzas, Operaciones y TI Global. Estados posibles: ✅ Completado · ▶️ En curso · ⏳ Pendiente · 🗓️ Programado.

## 1. SAP

| # | Requisito | Responsable | Fecha objetivo | Estado | Comentarios |
|---|------------|-------------|----------------|--------|-------------|
| 1 | Usuario **Power User** con accesos MM/SD/FI/CO | Lucía Rodríguez | 14-oct-2025 | ▶️ En curso | Ticket SAP-48219 escalado a TI Global; requiere aprobación Carolina Rondón. |
| 2 | Roles para ejecutar transacciones prioritarias (`ME2L`, `VA05`, `KSB1`, `FAGLL03`, etc.) | Juan Sebastián Ravelo | 17-oct-2025 | ⏳ Pendiente | Listado de roles definido; falta firma de Linda López para activar. |
| 3 | Permiso para exportar datos masivos (ALV/Batch Input) | Linda López | 18-oct-2025 | ⏳ Pendiente | Se tramita como extensión del ticket SAP-48219. |
| 4 | Aprobación TI Global para exponer tablas estándar y Z en conectores externos | David Saboyá | 21-oct-2025 | ▶️ En curso | Ticket BQ-7713 abierto; depende de checklist de seguridad. |

> Supuesto: Aunergia ya cuenta con un acuerdo de confidencialidad vigente con Elanco; no se requiere gestión adicional.

## 2. BigQuery / Google Cloud Platform

| # | Requisito | Responsable | Fecha objetivo | Estado | Comentarios |
|---|------------|-------------|----------------|--------|-------------|
| 1 | Cuenta corporativa Elanco con licenciamiento activo | Lucía Rodríguez | 09-oct-2025 | ✅ Completado | Se validó acceso en GCP Console (Project CASA-BI). |
| 2 | Permisos BigQuery Studio (`Data Viewer`, `Job User`, `Data Editor`) | Juan Manuel Bigi | 16-oct-2025 | ▶️ En curso | Se asignaron viewers; falta `Data Editor` para datasets productivos. |
| 3 | Habilitación **ERP Enterprise Data Product** | David Saboyá | 23-oct-2025 | ⏳ Pendiente | Requiere checklist de seguridad firmado; depende del ítem SAP-4. |
| 4 | Tablas faltantes publicadas (ZLEL008, CE1*, CE4*, FAGLFLEXA) | TI Global (Atlanta) | 24-oct-2025 | ⏳ Pendiente | Tickets BQ-7713 y BQ-7721 en revisión; actualizar backlog al completarse. |
| 5 | Seguimiento de consumo y costos de cómputo | Carolina Rondón | 30-oct-2025 | 🗓️ Programado | Se configurará dashboard de costos en Fase 0 Semana 4. |
| 6 | Revisión de acceso a **Gemini AI Cloud Companion** | Linda López | 31-oct-2025 | 🗓️ Programado | Mantener como opcional; evaluar impacto presupuestario Q1 2026. |

## 3. Power BI

| # | Requisito | Responsable | Fecha objetivo | Estado | Comentarios |
|---|------------|-------------|----------------|--------|-------------|
| 1 | Licencias **Power BI Pro** para equipo núcleo (8 licencias) | Finanzas – Compras | 08-oct-2025 | ✅ Completado | Orden de compra PR-55219 cerrada. |
| 2 | Definir necesidad de **Power BI Premium** | Juan Manuel Bigi | 20-oct-2025 | ▶️ En curso | Análisis de capacidad en curso; decisión en comité del 21-oct. |
| 3 | Accesos a workspaces corporativos + gateway BigQuery | TI Local | 17-oct-2025 | ▶️ En curso | Gateway parece instalado; faltan grupos de seguridad. |
| 4 | Configuración de `Row-Level Security` | Equipo BI (Juan Manuel + Finanzas) | 27-oct-2025 | 🗓️ Programado | Se implementará al cierre de Fase 1. |

## 4. Herramientas Complementarias

| # | Requisito | Responsable | Fecha objetivo | Estado | Comentarios |
|---|------------|-------------|----------------|--------|-------------|
| 1 | Driver **ODBC Simba** homologado | TechOps | 18-oct-2025 | ▶️ En curso | Instalador en evaluación de seguridad; depende de TI Global. |
| 2 | Acceso a repositorio de código (Git/DevOps) | Juan Manuel Bigi | 15-oct-2025 | ▶️ En curso | Solicitud DEV-14432 para habilitar Azure DevOps repo `elanco-power`. |
| 3 | Herramientas de documentación (Confluence/SharePoint) | Linda López | 13-oct-2025 | ✅ Completado | Espacio "Elanco Power" publicado en Confluence LATAM. |

## 5. Habilidades del Equipo (Power User Expectations)

- ✅ Dominio de SQL avanzado (Lucía + Juan Manuel certificaron en 2024; se adjuntan diplomas en Confluence).
- ▶️ Sensibilización en políticas de datos sensibles (workshop legal CASA agendado para 22-oct-2025).
- 🗓️ Capacitación en control de costos BigQuery (sesión con FinOps programada 29-oct-2025).
- ✅ Experiencia previa en SAP/Business Objects (documentada en CV internos).
- ▶️ Reforzar narrativa ejecutiva y documentación corporativa (taller interno 24-oct-2025, responsable Linda López).

## 6. Acciones de Seguimiento Integradas

| Acción | Responsable | Fecha objetivo | Estado | Comentarios |
|--------|-------------|----------------|--------|-------------|
| Actualizar `transacciones_sap_backlog.md` con estatus de permisos al cierre de cada semana | Juan Manuel Bigi | Todos los viernes | ▶️ En curso | Se incorporará columna de “fecha último update” (pendiente semana 41). |
| Coordinar sesión de habilitación con TI Global (SAP + BigQuery) | Lucía Rodríguez | 16-oct-2025 | ▶️ En curso | Agenda enviada; esperando confirmación de horario. |
| Revisar vigencia de licencias y renovaciones trimestralmente | Finanzas | 15-ene-2026 | 🗓️ Programado | Registrar recordatorio en ServiceNow. |
| Mantener inventario actualizado de usuarios con acceso privilegiado | Seguridad TI | 31-oct-2025 | ▶️ En curso | Formato definido; falta completar datos iniciales. |
