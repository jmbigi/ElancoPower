# PROPUESTA EJECUTIVA ACTUALIZADA – ELANCO POWER

---

## 1. Resumen Ejecutivo
Elanco necesita automatizar la extracción de datos desde SAP, centralizar la información en un repositorio corporativo y potenciar la analítica con Power BI y capacidades predictivas futuras. Esta propuesta actualizada sintetiza la conversación con Lucía Rodríguez, el correo corporativo recibido y el inventario de transacciones SAP priorizadas. El enfoque prioriza una **Fase 0 de habilitación y permisos**, seguida por la **automatización SAP → BigQuery**, la **modelización para Power BI** y un **módulo opcional predictivo**.

La inversión estimada para las primeras tres fases (Fase 0 a Fase 2) es de **USD 46.800**, con un esfuerzo de **516 horas** distribuidas entre gobernanza, extracción SAP, arquitectura de datos y BI. Se asume BigQuery como Data Lake objetivo dado el uso corporativo global; se habilita un plan de contingencia si se confirman limitaciones que obliguen a migrar a Azure Data Lake.

---

## 2. Supuestos y Alcance

- **Plataforma objetivo**: Google BigQuery (Data Lake corporativo autorizado). Alternativas (Azure, Snowflake) se evaluarán en Fase 0 si BigQuery resulta insuficiente.
- **Origen de datos**: Transacciones SAP listadas en `Transacciones SAP.csv` y nuevas fuentes que se definan (ej. Business Objects).
- **Herramientas de visualización**: Power BI corporativo, con modelos tabulares, KPIs financieros y de supply.
- **Usuarios clave**: Finanzas, Supply Chain, TechOps (CASA). Se requerirá la participación de TI Global para permisos.
- **Seguridad y compliance**: Coordinación con políticas globales Elanco, acuerdos de confidencialidad y tickets de permisos.
- **Entregables**: Pipelines automatizados SAP → BigQuery, modelos semánticos, dashboards Power BI certificados, documentación operativa, plan de soporte.

---

## 3. Fases del Proyecto

### Fase 0 (5 semanas) – Due Diligence, Permisos y Blueprint
**Objetivo**: Habilitar cuentas, permisos y definir la arquitectura final.

| Rol | Horas | Tarifa USD/h | Subtotal |
| --- | --- | --- | --- |
| PM / Gobernanza (Aunergia) | 40 | 110 | 4.400 |
| Arquitecto Datos | 32 | 140 | 4.480 |
| Especialista SAP / Lucía | 28 | 60 | 1.680 |
| QA / Compliance | 12 | 80 | 960 |
| **Total Fase 0** | **112** | | **11.520** |

**Actividades clave**:
- Validar alcance con Finanzas y Supply; refinar prioridades del inventario de transacciones.
- Gestionar permisos SAP (power user) y tickets para exponer tablas faltantes en BigQuery.
- Evaluar limitaciones de BigQuery y definir contingencia (Azure Data Lake) con TI Global.
- Diseñar blueprint SAP → BigQuery → Power BI (modelo conceptual y fluxo de datos).
- Definir métricas clave (ventas, opex, inventario) y criterios de calidad.

**Entregables**:
- Arquitectura aprobada y plan de permisos.
- Matriz de riesgos y gobernanza.
- Backlog priorizado de transacciones (`ME2L`, `MM60`, `VA05`, `KSB1`, `KE24`, etc.).

---

### Fase 1 (7 semanas) – Automatización SAP → BigQuery
**Objetivo**: Construir las extracciones y pipelines validados.

| Rol | Horas | Tarifa USD/h | Subtotal |
| --- | --- | --- | --- |
| Arquitecto Datos | 64 | 140 | 8.960 |
| Desarrollador ETL / SAP (Lucía + soporte ABAP) | 90 | 70 | 6.300 |
| PM / Gobernanza | 28 | 110 | 3.080 |
| QA Datos | 24 | 80 | 1.920 |
| **Total Fase 1** | **206** | | **20.260** |

**Actividades clave**:
- Construir pipelines para transacciones críticas (prioridad 1) con historización.
- Implementar mecanismos de control y trazabilidad (auditoría). 
- Gestionar tickets de BigQuery para tablas faltantes y validar permisos productivos.
- Documentar diccionarios de datos y reglas de transformación.

**Entregables**:
- Pipelines productivos SAP → BigQuery para transacciones prioritarias (ME2L, ZLEL008, KSB1, FAGLL03, etc.).
- Data Lake estructurado con particionamiento y políticas de acceso.
- Evidencias de QA: comparativas SAP vs BigQuery, definiciones de error tolerable.

---

### Fase 2 (4 semanas) – Modelado Power BI, Capacitación y Cierre
**Objetivo**: Consumir la data desde Power BI, generar dashboards y capacitar usuarios.

| Rol | Horas | Tarifa USD/h | Subtotal |
| --- | --- | --- | --- |
| Desarrollador Power BI | 60 | 95 | 5.700 |
| Arquitecto Datos | 18 | 140 | 2.520 |
| Analista de Negocio | 40 | 85 | 3.400 |
| PM / Gobernanza | 20 | 110 | 2.200 |
| QA / UAT | 30 | 80 | 2.400 |
| **Total Fase 2** | **168** | | **16.220** |

**Actividades clave**:
- Modelos tabulares y dataset certificado para Finanzas y Supply.
- Dashboards ejecutivos y operativos (ventas, inventario, opex, órdenes abiertas).
- Pruebas funcionales con usuarios clave; checklist de datos críticos.
- Manuales operativos y plan de soporte; talleres con usuarios finales.

**Entregables**:
- Dashboards en producción y dataset gobernado.
- Plan de operación, soporte y mantenimiento.
- Reporte de lecciones aprendidas y roadmap futuro.

---

### Fase 3 (Opcional) – Analítica Predictiva (8-10 semanas)
- Forecast de ventas multivariado (precios, costos, inflación por país).
- Simulación de escenarios y alertas automáticas.
- Integración con modelos de Machine Learning (Vertex AI o Azure ML según plataforma). 
Se cotizará aparte en el futuro, durante Fase 2 (estimado USD 35.000 – 50.000).

---

## 4. Tabla Resumen Financiera

| Concepto | Horas | USD |
| --- | --- | --- |
| Fase 0 – Due Diligence | 112 | 11.520 |
| Fase 1 – Automatización | 206 | 20.260 |
| Fase 2 – BI & Cierre | 168 | 16.220 |
| **Total Proyecto (Fase 0-2)** | **516** | **46.800** |

*Los valores incluyen 15% de contingencia y overhead para coordinación corporativa.*

---

## 5. Matriz de Riesgos Actualizada

| Riesgo | Probabilidad | Impacto | Mitigación |
| --- | --- | --- | --- |
| Permisos SAP insuficientes | Alta | Alto | Fase 0 dedicada a permisos, sponsor ejecutivo, plan de escalamiento TI Global |
| Tablas no expuestas en BigQuery | Media | Alto | Tickets simultáneos, fallback a extracciones vía RFC o Azure |
| Cambios de alcance | Media | Medio | Gobernanza semanal, backlog priorizado, control de versiones |
| Calidad de datos | Media | Alto | QA cruzada SAP vs BigQuery, reglas de validación definidas con negocio |
| Dependencia de expertos locales | Baja | Medio | Documentación exhaustiva, capacitación, rotación de personal |

---

## 6. Próximos Pasos
1. **Aprobación formal del presupuesto Fase 0 (USD 11.520)** y firma de acuerdo de confidencialidad.
2. **Kick-off con stakeholders** (Finanzas, Supply, TI Global, TechOps) para validar backlog y plan de permisos.
3. **Ejecución de Fase 0** y entrega de blueprint, matriz de riesgos y plan de permisos.
4. **Go/No-Go** para Fase 1 en base a resultados de Fase 0.

---

## 7. Criterios de Éxito y ROI Esperado
- Reducción del 70% del tiempo de consolidación de reportes mensuales.
- Dashboard financiero disponible en máximo 24 h tras cierre de mes.
- Disponibilidad del 100% de las transacciones prioritarias en el Data Lake.
- Usuarios de Finanzas certificados en Power BI y procesos de soporte en marcha.
- Recuperación de inversión estimada en 12-15 meses mediante ahorro operativo y reducción de errores.

---

## 8. Consideraciones Finales
- Tarifas pueden ajustarse si Elanco provee recursos internos adicionales (ej. especialistas ABAP).
- La propuesta asume dedicación part-time del equipo de negocio para validaciones semanales.
- Cualquier adopción de nueva plataforma (Azure) implicará revisión de costos y licencias.
- Reportes adicionales o rollout a más países se presupuestará como proyecto aparte.

> **Conclusión**: El plan propone un camino seguro y escalable para que Elanco automatice la extracción desde SAP, centralice la información en BigQuery y despliegue analítica con Power BI, atendiendo las necesidades identificadas por Lucía y los issues corporativos. La inversión incluye el blindaje necesario para navegar la gobernanza global de la compañía.

---

## 9. Notas personales – Juan Manuel Bigi

> Responsabilidad actual: elaborar este presupuesto y documentación, en conjunto con Lucía Rodríguez, para que Aunergia lo presente formalmente a Elanco.

### Presupuesto propio por elaboración de propuesta
- Desarrollo del presente presupuesto y plan detallado (Fase 0 preliminar): **40 horas** × **USD 25/h** = **USD 1.000** (a facturar a Aunergia).

### Participación estimada por fase (facturación personal a USD 25/h)

> Rol previsto: Programador y Analista en BigQuery (modelado, performance, QA) y Programador/Analista Power BI (modelos tabulares, DAX, traspaso de conocimiento).

| Fase | Horas personales | Monto a facturar |
| --- | --- | --- |
| Fase 0 – Due Diligence | 40 | USD 1.000 |
| Fase 1 – Automatización | 110 | USD 2.750 |
| Fase 2 – BI & Cierre | 90 | USD 2.250 |
| Fase 3 – Analítica Predictiva (opcional) | 120 | USD 3.000 |

> Estas horas representan el esfuerzo directo que aportaría Juan Manuel Bigi dentro del equipo extendido. Cualquier ajuste a la distribución de tareas podrá recalibrarse junto con Aunergia en función de la disponibilidad interna y del alcance final.

### Horas estimadas de Lucía Rodríguez – Analista SAP (facturación Aunergia)

| Fase | Horas | Tarifa considerada | Monto |
| --- | --- | --- | --- |
| Fase 0 – Due Diligence | 28 | USD 60/h | USD 1.680 |
| Fase 1 – Automatización | 90 | USD 70/h | USD 6.300 |
| Fase 2 – BI & Cierre | 20 | USD 70/h | USD 1.400 |
| Fase 3 – Analítica Predictiva (opcional) | 30 | USD 70/h | USD 2.100 |

### ABAPers y otros profesionales Aunergia (si se requieren)
- Recursos ABAP senior para desarrollos específicos en SAP (estimación inicial: 40 h a USD 85/h = USD 3.400).
- Especialista en seguridad/compliance corporativa (20 h a USD 90/h = USD 1.800) para auditorías puntuales.
- Analista de datos adicional para soporte de QA (30 h a USD 60/h = USD 1.800).
- Estas horas se activarán únicamente si, durante Fase 0, se confirma la necesidad técnica o de cumplimiento.
