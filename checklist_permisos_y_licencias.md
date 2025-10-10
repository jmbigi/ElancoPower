# Checklist de Permisos, Licencias y Habilidades Requeridas

Esta lista consolida la información del correo corporativo, el documento **"ERP Enterprise Data Product – Power User Persona"** y las conversaciones con Lucía.

## 1. SAP
- [ ] Usuario **Power User** con acceso a módulos MM, SD, FI y CO.
- [ ] Roles para ejecutar transacciones prioritarias (`ME2L`, `VA05`, `KSB1`, `FAGLL03`, etc.).
- [ ] Permiso para exportar datos masivos (ALV/Batch Input).
- [ ] Aprobación de TI Global para exponer tablas estándar y Z en conectores externos.
- [ ] NDA firmado para intercambio de información confidencial.

## 2. BigQuery / Google Cloud Platform
- [ ] Cuenta corporativa Elanco con licenciamiento activo.
- [ ] Acceso a **BigQuery Studio** con permisos de `Data Viewer`, `BigQuery Job User` y `BigQuery Data Editor` sobre el dataset de CASA.
- [ ] Habilitación del **ERP Enterprise Data Product** (tablas con diccionarios SAP enriquecidos).
- [ ] Validación de disponibilidad de tablas faltantes; levantar tickets para su publicación.
- [ ] Seguimiento del consumo y costos de cómputo (sensibilidad según políticas corporativas).
- [ ] Revisión periódica de acceso a **Gemini AI Cloud Companion** (gratuito al día de hoy, pero sujeto a cambios).

## 3. Power BI
- [ ] Licencia **Power BI Pro** mínima para todos los miembros del equipo de proyecto.
- [ ] Confirmar si se requiere **Power BI Premium** por capacidad para publicación corporativa.
- [ ] Accesos a workspaces corporativos, gateways y fuentes de datos BigQuery.
- [ ] Configuración de `Row-Level Security` acorde a políticas regionales (Finanzas, Supply, Ventas).

## 4. Herramientas Complementarias
- [ ] Driver **ODBC Simba** para conexión desde herramientas legacy (Alteryx, Excel, Tableau).
- [ ] Acceso a repositorio de código (Git / DevOps) definido por TI Global.
- [ ] Herramientas de documentación colaborativa (Confluence, SharePoint).

## 5. Habilidades del Equipo (Power User Expectations)
- [ ] Dominio de SQL para construir y optimizar consultas complejas sobre datos SAP.
- [ ] Comprensión de procesos SAP y experiencia previa en extracción / Business Objects.
- [ ] Conocimiento de políticas de datos sensibles (PII, datos "rojos").
- [ ] Capacidad de comunicar y documentar soluciones en lenguaje corporativo.
- [ ] Sensibilidad al rendimiento de BigQuery y control de costos.
- [ ] Experiencia en herramientas de BI (Power BI, Alteryx, etc.).

## 6. Acciones de Seguimiento
- [ ] Registrar en el backlog los permisos solicitados y fechas de aprobación.
- [ ] Coordinar con TI Global una sesión de habilitación de plataforma.
- [ ] Verificar vigencia de licencias y renovaciones.
- [ ] Mantener inventario actualizado de usuarios con acceso privilegiado.
