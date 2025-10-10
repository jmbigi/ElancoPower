# Resumen Ejecutivo para Stakeholders – Elanco Power

## Objetivo del Proyecto
Automatizar la extracción de datos desde SAP y centralizarlos en BigQuery para habilitar analítica corporativa con Power BI. A largo plazo, montar capacidades predictivas que permitan simular escenarios de negocio.

## Puntos Clave
- **Dolores actuales:** descargas manuales en SAP, falta de permisos BigQuery, tablas críticas ausentes, procesos duplicados con Business Objects.
- **Solución propuesta:** tres fases (Habilitación → Automatización → Analítica BI) con contingencia para migrar a Azure Data Lake si BigQuery presentara limitaciones.
- **Equipo clave:** Aunergia (PMO y gobernanza), Juan Manuel Bigi (BigQuery/Power BI), Lucía Rodríguez (SAP/permiso), Power User interno de Elanco.

## Inversión y Timeline
- **Fase 0 – Due Diligence & Permisos (5 semanas):** USD 11.520, 120 horas.
- **Fase 1 – Automatización SAP → BigQuery (7 semanas):** USD 20.260, 206 horas.
- **Fase 2 – Modelado Power BI & Cierre (4 semanas):** USD 16.220, 168 horas.
- **Total (Fase 0-2):** USD 46.800, 516 horas.
- **Fase 3 (Opcional – Analítica Predictiva):** USD 35.000 – 50.000 (estimado), 8-10 semanas.

## Hitos Relevantes
1. **Kick-off y validación de alcance (Semana 1).**
2. **Permisos y tickets BigQuery aprobados (Semana 4).**
3. **Blueprint y backlog priorizado firmado (Semana 5).**
4. **Pipelines críticos productivos (Semana 10).**
5. **Dashboards ejecutivos y UAT completado (Semana 14).**
6. **Go-Live y plan de soporte (Semana 16).**

## Riesgos Principales y Mitigación
| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Permisos SAP incompletos | Alta | Alto | Sponsor ejecutivo, checklist de permisos, seguimiento semanal.
| Tablas no expuestas en BigQuery | Media | Alto | Tickets tempranos, fallback a RFC/Azure, coordinación con TI Global.
| Cambios de alcance | Media | Medio | Backlog priorizado, governance semanal, control de versiones.
| Calidad de datos | Media | Alto | QA cruzado SAP vs BigQuery, pruebas UAT con negocio.
| Adopción de power users | Media | Medio | Capacitación en BigQuery Studio, guía de autosuficiencia, métricas de uso.

## Próximos Pasos Inmediatos
1. Aprobar presupuesto de Fase 0 y firmar NDA.
2. Confirmar power user interno y agenda de workshops.
3. Iniciar checklist de permisos y revisión de licencias.
4. Programar sesión de descubrimiento con TI Global (BigQuery / Gemini / ODBC).

## Entregables Vinculados
- `presupuesto_actualizado.md`
- `transacciones_sap_backlog.md`
- `checklist_permisos_y_licencias.md`

> Este resumen está pensado para presentaciones ejecutivas (Linda Lopez, David Saboyá, Finanzas y Supply) y puede convertirse rápidamente en un deck corporativo.
