# Resumen Ejecutivo para Stakeholders – Elanco Power

> Actualizado al 10-oct-2025. Todos los montos expresados en USD. El cronograma queda condicionado al cierre del checklist de permisos y a la carga de datos septiembre-octubre.

> Nota: el único presupuesto vigente es `presupuesto_actualizado.md`. Cualquier otro archivo de presupuesto en la carpeta es histórico y se mantiene solo como referencia.

## Objetivo del Proyecto
Automatizar la extracción de datos desde SAP y centralizarlos en BigQuery para habilitar analítica corporativa con Power BI. A largo plazo, montar capacidades predictivas que permitan simular escenarios de negocio.

## Puntos Clave
- **Dolores actuales:** descargas manuales en SAP, falta de permisos BigQuery, tablas críticas ausentes, procesos duplicados con Business Objects.
- **Solución propuesta:** tres fases (Habilitación → Automatización → Analítica BI) con contingencia para migrar a Azure Data Lake si BigQuery presentara limitaciones.
- **Recursos clave actualizados:** consultoría ABAP externa limitada a 40 h (USD 3.400) y absorbida dentro del presupuesto total validado de USD 48.000.
- **Equipo clave:** Aunergia (PMO y gobernanza), Juan Manuel Bigi (BigQuery/Power BI), Lucía Rodríguez (SAP/permiso), Power User interno de Elanco.

## Inversión y Timeline
- **Fase 0 – Due Diligence & Permisos (5 semanas):** USD 11.520, 120 horas (incluye cierre checklist SAP/BigQuery y verificación del acuerdo de confidencialidad vigente con Aunergia).
- **Fase 1 – Automatización SAP → BigQuery (7 semanas):** USD 20.260, 206 horas (con 40 h de consultoría ABAP especializada incluida).
- **Fase 2 – Modelado Power BI & Cierre (4 semanas):** USD 16.220, 168 horas (redistribución interna tras reducción de consultores externos).
- **Total (Fase 0-2):** USD 48.000, 494 horas.
- **Fase 3 (Opcional – Analítica Predictiva):** USD 35.000 – 50.000 (estimado), 8-10 semanas.

> **Dependencias críticas para sostener el timeline:** (a) completar checklist de permisos antes del 16-oct-2025, (b) confirmar disponibilidad de las transacciones septiembre-octubre en SAP/BigQuery, (c) mantener el límite de consultoría externa según acuerdo 10-oct-2025.

## Hitos Relevantes
1. **Kick-off y validación de alcance (Semana 1).**
2. **Permisos y tickets BigQuery aprobados (Semana 4).**
3. **Blueprint y backlog priorizado firmado (Semana 5).**
4. **Pipelines críticos productivos (Semana 10).** *Condicionado a la liberación de tablas Z y CO-PA (tickets BQ-7713/BQ-7721).* 
5. **Dashboards ejecutivos y UAT completado (Semana 14).** *Depende de disponibilidad de Power BI workspaces y RLS.*
6. **Go-Live y plan de soporte (Semana 16).** *Requiere evidencia de datos septiembre-octubre y checklist firmado.*

## Riesgos Principales y Mitigación
| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Permisos SAP incompletos | Alta | Alto | Sponsor ejecutivo, checklist de permisos, seguimiento semanal.
| Tablas no expuestas en BigQuery | Media | Alto | Tickets tempranos, fallback a RFC/Azure, coordinación con TI Global.
| Cambios de alcance | Media | Medio | Backlog priorizado, governance semanal, control de versiones.
| Calidad de datos | Media | Alto | QA cruzado SAP vs BigQuery, pruebas UAT con negocio.
| Adopción de power users | Media | Medio | Capacitación en BigQuery Studio, guía de autosuficiencia, métricas de uso.

## Próximos Pasos Inmediatos
1. Aprobar presupuesto de Fase 0 y dejar constancia del acuerdo de confidencialidad vigente entre Aunergia y Elanco (due 14-oct-2025, responsable Linda López).
2. Confirmar power user interno y agenda de workshops (due 16-oct-2025, responsables Lucía Rodríguez & Finanzas).
3. Iniciar checklist de permisos y revisión de licencias (tracker actualizado en `checklist_permisos_y_licencias.md`).
4. Programar sesión de descubrimiento con TI Global (BigQuery / Gemini / ODBC) y validar cargas septiembre-octubre en SAP (due 18-oct-2025).

## Entregables Vinculados
- `presupuesto_actualizado.md`
- `transacciones_sap_backlog.md`
- `checklist_permisos_y_licencias.md`

> Este resumen está pensado para presentaciones ejecutivas (Linda López, David Saboya, Finanzas y Supply) y puede convertirse rápidamente en un deck corporativo.
