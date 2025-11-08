# 8. ESTIMACIÓN DE ESFUERZOS

## 8.1. Resumen Ejecutivo

### Esfuerzo Total del Proyecto

| Fase | Horas |
|------|-------|
| **Fase 0 - Due Diligence** | 235h |
| **Fase 1 - Data Lake** | **Desarrollo Técnico (Juan Manuel Bigi)** | 961h | 60.4% |
| **Consultoría SAP (Lucía Rodríguez)** | 484h | 30.4% |
| **Project Management (Linda López)** | 145h | 9.1% |
| **TOTAL ESFUERZO** | **1,590h** | **100%** |

**Nota:** Totales según CSV del cronograma detallado de tareas. |
| **Fase 2 - Dashboards Power BI** | 659h |
| **Fase 3 - ML Roadmap** | Descripción conceptual |
| **TOTAL HORAS** | **1,590h** |

### Calendario del Proyecto

| Fase | Horas | Duración | Fecha Inicio | Fecha Fin |
|------|-------|----------|--------------|-----------|
| **Inicio del Proyecto** | - | - | 1-dic-2025 | 1-dic-2025 |
| **Fase 0 (Revisión y Alcance)** | 235h | 6 sem | 1-dic-2025 | 12-ene-2026 |
| **Fase 1 (Data Lake)** | 696h | 22 sem | 13-ene-2026 | 14-jun-2026 |
| **Fase 2 (12 Dashboards)** | 659h | 14 sem | 15-jun-2026 | 20-sep-2026 |
| **Go-Live y Cierre** | - | - | 14-sep-2026 | 20-sep-2026 |
| **TOTAL ESFUERZO** | **1,590h** | **42 sem** | **1-dic-2025** | **20-sep-2026** |

**Restricción JMB:** Máximo 6h/día (30h/semana) por restricciones personales.

### Duración Total

- **Tiempo estimado:** 42 semanas (~10 meses)
- **Inicio:** 1 de diciembre 2025
- **Finalización:** 20 de septiembre 2026
- **Restricción:** Juan Manuel Bigi trabaja máximo 6 horas/día (30h/semana)

### Equipo

| Perfil | Horas Totales |
|--------|---------------|
| **Juan Manuel Bigi** - Arquitecto de Datos / Desarrollador | 961h |
| **Lucía Rodríguez** - Analista SAP Power User | 484h |
| **Linda López** - Project Manager | 145h |
| **TOTAL** | **1,590h** |

**Nota:** No se incluye consultoría ABAP adicional, Lucía cuenta con expertise SAP necesario.

---

## 8.2. Desglose Detallado por Fase

### 8.2.1. Fase 0 - Revisión del Alcance y Factibilidad

| **Duración estimada** | 6 semanas |
| **Fase del proyecto:** | Semanas 0-6  |

#### Desglose de Horas por Actividad (del CSV)

| Actividad | JMB | Lucía | Linda | Total |
|-----------|-----|-------|-------|-------|
| Diseño arquitectura preliminar | 6h | 4h | 0h | 10h |
| Estimación esfuerzos ETL | 8h | 6h | 0h | 14h |
| Kick-off y alineamiento | 3h | 4h | 3h | 10h |
| Inventario técnico completo | 20h | 18h | 3h | 41h |
| Gestión de tickets críticos | 8h | 22h | 5h | 35h |
| Workshops y análisis Z | 20h | 36h | 10h | 66h |
| Diseño y POC | 24h | 12h | 0h | 36h |
| Documentación y Go/No-Go | 6h | 10h | 7h | 23h |
| **TOTAL FASE 0** | **95h** | **112h** | **28h** | **235h** |

#### Distribución de Horas Fase 0

| Recurso | Horas |
|---------|-------|
| Juan Manuel Bigi | 95h |
| Lucía Rodríguez | 112h |
| Linda López (PM) | 28h |
| **TOTAL FASE 0** | **235h** |

---

### 8.2.2. Fase 1 - Construcción de Data Lake

**Duración:** 22 semanas  
**Fase del proyecto:** Semanas 6-28

#### Desglose de Horas por Actividad (del CSV)

| Actividad | JMB | Lucía | Linda | Total |
|-----------|-----|-------|-------|-------|
| Setup infraestructura completa | 60h | 6h | 7h | 73h |
| Pipelines Módulo FI (4 trans) | 60h | 26h | 3h | 89h |
| Pipelines Módulo SD (2 trans) | 38h | 20h | 3h | 61h |
| Pipelines MM Procurement (3 trans) | 44h | 24h | 3h | 71h |
| Pipelines MM Inventory (3 trans) | 42h | 20h | 3h | 65h |
| Pipeline ZLEL008 (custom MRP) | 48h | 26h | 3h | 77h |
| Pipelines CO y FI-AP/AR (4 trans) | 56h | 30h | 6h | 92h |
| Pipelines Master Data y ZVEL015 | 48h | 28h | 6h | 82h |
| Optimización y automatización | 50h | 26h | 10h | 86h |
| **TOTAL FASE 1** | **446h** | **206h** | **44h** | **696h** |

#### Distribución de Horas Fase 1

| Recurso | Horas |
|---------|-------|
| Juan Manuel Bigi | 446h |
| Lucía Rodríguez | 206h |
| Linda López (PM) | 44h |
| **TOTAL FASE 1** | **696h** |

---

### 8.2.3. Fase 2 - Modelado de Datos y 12 Dashboards

**Duración:** 14 semanas  
**Fase del proyecto:** Semanas 28-42

#### Desglose de Horas por Actividad (del CSV)

| Actividad | JMB | Lucía | Linda | Total |
|-----------|-----|-------|-------|-------|
| Modelo dimensional completo | 86h | 22h | 8h | 116h |
| Dashboards Financieros (3) | 64h | 14h | 4h | 82h |
| Dashboards Ventas y Rentabilidad (3) | 68h | 14h | 4h | 86h |
| Dashboards Supply Chain (3) | 62h | 12h | 4h | 78h |
| Dashboards Tesorería y Ejecutivo (3) | 66h | 14h | 7h | 87h |
| Testing y UAT completo | 41h | 55h | 26h | 122h |
| Ajustes finales, documentación, capacitación y Go-Live | 33h | 35h | 20h | 88h |
| **TOTAL FASE 2** | **420h** | **166h** | **73h** | **659h** |

**Nota:** El CSV muestra 626h de las tareas registradas (no incluye todo el detalle de subtareas).

#### Distribución de Horas Fase 2

| Recurso | Horas |
|---------|-------|
| Juan Manuel Bigi | 324h |
| Lucía Rodríguez | 120h |
| Linda López (PM) | 52h |
| **TOTAL FASE 2** | **496h** |

**Nota ajustada:** Según CSV las tareas principales suman 626h (116+82+86+78+87+122+88). La distribución por persona del CSV es: JMB=324h, Lucía=120h, Linda=52h totalizando 496h de las 626h registradas en tareas.

---

### 8.2.4. Fase 3 - Modelos Predictivos (Solo Descripción)

**Duración:** Incluida en Fase 2 (últimas 2 semanas)  
**Esfuerzo:** Descripción conceptual incluida en las horas de Fase 2

#### Actividades

| Actividad | Descripción |
|-----------|-------------|
| Elaboración catálogo casos de uso ML | 8 casos de uso identificados |
| Análisis exploratorio de datos (EDA) | Evaluación de viabilidad |
| Propuesta de arquitectura ML | Diseño conceptual |
| Roadmap de implementación | Plan de implementación futura |
| Recomendaciones | Quick-wins vs. Long-term |

**Esfuerzo:** Incluido en las horas de Fase 2 (documentación conceptual)

---

## 8.3. Consolidado por Recurso

### 8.3.1. Horas Totales por Persona (según CSV)

| Recurso | Fase 0 | Fase 1 | Fase 2 | Fase 3 | Total |
|---------|--------|--------|--------|--------|-------|
| **Juan Manuel Bigi** | 95h | 446h | 420h | (incl) | **961h** |
| **Lucía Rodríguez** | 112h | 206h | 166h | - | **484h** |
| **Linda López (PM)** | 28h | 44h | 73h | - | **145h** |
| **SUBTOTAL EQUIPO** | **235h** | **696h** | **659h** | **0h** | **1,590h** |

**Nota:** Totales según CSV del cronograma. Las 1,590h son el esfuerzo total del equipo distribuido en 42 semanas.

### 8.3.2. Consultoría ABAP Especializada

**No incluida:** Lucía Rodríguez cuenta con expertise SAP funcional y ABAP suficiente para analizar transacciones custom (ZLEL008, ZVEL015). Las 484 horas de Lucía ya contemplan este análisis.

---

## 8.4. Esfuerzo Final Consolidado

### 8.4.1. Distribución de Esfuerzo por Recurso

| Recurso | Horas | % del Total |
|---------|-------|-------------|
| **Desarrollo Técnico (Juan Manuel Bigi)** | 961h | 60.6% |
| **Consultoría SAP (Lucía Rodríguez)** | 484h | 30.7% |
| **Project Management (Linda López)** | 145h | 8.7% |
| **TOTAL ESFUERZO** | **1,590h** | **100%** |

**Nota:** Totales según CSV del cronograma detallado de tareas.

### 8.4.2. Calendario del Proyecto

| Fase | Horas | Duración | Periodo |
|------|-------|----------|---------|
| **Inicio del Proyecto** | - | - | Semana 0 |
| **Fase 0 (Revisión y Alcance)** | 235h | 6 semanas | Semanas 0-6 |
| **Fase 1 (Data Lake)** | 696h | 22 semanas | Semanas 6-28 |
| **Fase 2 (12 Dashboards)** | 659h | 14 semanas | Semanas 28-42 |
| **Cierre y Go-Live** | - | - | Semana 42 |
| **TOTAL ESFUERZO** | **1,590h** | **42 semanas** | **~10 meses** |

---

## 8.5. Comparativa de Alcance

### Evolución del Cronograma

| Concepto | Versión Original | Versión Comprimida | Comentario |
|----------|------------------|-------------------|------------|
| **Transacciones SAP** | 18 | 18 | Alcance completo mantenido |
| **Fase 0** | 9 sem | 6 sem | Comprimido 33% |
| **Fase 1** | 31 sem | 22 sem | Comprimido 29% |
| **Fase 2** | 16 sem | 14 sem | Comprimido 12% |
| **PM Formalizado** | Sí (Linda) | Sí (Linda) | Mantenido |
| **TOTAL** | **56 sem** | **42 sem** | **Reducción 25%** |
| **Horas totales** | **1,590h** | **1,590h** | **Mismas horas** |

**Justificación de la compresión:**
- ✅ Mismas 1,590 horas distribuidas en menos semanas
- ✅ Mayor intensidad de trabajo semanal
- ✅ Restricción JMB respetada: máx 6h/día
- ✅ Paralelización de tareas donde es posible
- ✅ Optimización de dependencias críticas

---

## 8.6. Exclusiones (No Incluido en el Alcance del Proyecto)

### 8.6.1. Costos de Infraestructura y Servicios (Responsabilidad del Cliente)

❌ **Licencias Google Cloud Platform (BigQuery)**
- **Responsable: ELANCO** (infraestructura corporativa a cuenta del cliente)
- Incluye: Storage, processing, streaming inserts

❌ **Licencias Microsoft Power BI Pro**
- 8 licencias ya adquiridas por Elanco
- Orden PR-55219 (08-oct-2025)
- **Responsable: ELANCO** (licencias a cuenta del cliente)

❌ **Ambientes de desarrollo/QA/producción**
- Datasets BigQuery (casa_bi_dev, casa_bi_qa, casa_bi_prod)
- **Responsable: ELANCO** (provisionados por TI Global)

❌ **Conectividad y Networking**
- VPN/Private Service Connect (si requerido)
- Certificados SSL, firewall configuration
- **Responsable: ELANCO** (infraestructura de red a cuenta del cliente)

### 8.6.2. Recursos Internos Elanco

❌ **Tiempo de stakeholders**
- Estimado: 50-60 horas (workshops, validaciones, UAT)
- Sin costo (personal interno)

❌ **Soporte TI Global**
- Tickets de permisos SAP
- Tickets de tablas BigQuery
- Sin costo (soporte corporativo)

### 8.6.3. Alcance Futuro

❌ **Implementación de Modelos Predictivos (Fase 3)**
- Solo se entrega descripción conceptual
- Implementación: Requiere proyecto separado

❌ **Soporte Post Go-Live (>30 días)**
- Incluido: 30 días de soporte (horario hábil, incidentes menores)
- Post 30 días: Contrato de soporte separado

❌ **Mantenimiento Evolutivo**
- Nuevos dashboards, transacciones SAP o KPIs requieren cotización separada

❌ **Rollout a Otras Regiones**
- Alcance limitado a CASA
- Rollout EMEA/APAC/NA: Cotización separada

---

## 8.7. Supuestos del Presupuesto

### 8.7.1. Supuestos Técnicos

✅ BigQuery es la plataforma definitiva (validado en Fase 0)  
✅ 18 transacciones suficientes para MVP  
✅ Datos históricos disponibles (24 meses) en SAP  
✅ Power BI se conecta nativamente a BigQuery  
✅ No se requieren interfaces en tiempo real (batch aceptable)  
✅ Tablas SAP estarán disponibles en BigQuery (post-tickets TI Global)

### 8.7.2. Supuestos de Recursos

✅ Lucía Rodríguez tendrá permisos SAP completos al iniciar Fase 1  
✅ Equipo Finanzas/Supply disponible ~4h/semana para validaciones  
✅ TI Global responde tickets en < 1 semana (críticos)  
✅ 8 licencias Power BI Pro activas  
✅ Acuerdo de confidencialidad Aunergia-Elanco vigente  

### 8.7.3. Supuestos de Tiempo

✅ Disponibilidad part-time equipo: 20-25h/semana  
✅ No hay bloqueos por vacaciones/cierre de año (ajustar si aplica)  
✅ Validaciones con usuarios en máximo 3 días hábiles  

---

## 8.8. Factores de Riesgo en el Proyecto

### Riesgos que Pueden Incrementar Esfuerzos

| Riesgo | Probabilidad | Impacto en Tiempo | Mitigación Incluida |
|--------|--------------|-------------------|---------------------|
| Transacciones Z más complejas de lo estimado | Media | +10-15h | Consultoría ABAP (12h incluidas) |
| Cambios de alcance durante desarrollo | Media | Requiere cotización adicional | Proceso formal de Change Request |
| Tablas BigQuery no disponibles (requiere workaround) | Baja | Incluido en esfuerzo | Plan B en Fase 0 |
| Issues de performance BigQuery | Baja | Incluido en esfuerzo | Optimización en diseño |
| Retrasos en tickets TI Global | Media | Tiempo adicional | Holguras en cronograma (18-20 semanas) |

**Nota:** No se incluyen contingencias adicionales en el esfuerzo. Cualquier cambio de alcance mayor requerirá Change Request y cotización adicional.

---

## 8.9. Beneficios Esperados

### 8.9.1. Ahorro Operativo Proyectado

| Beneficio | Ahorro Anual | Metodología de Cálculo |
|-----------|--------------|------------------------|
| **Reducción horas manuales** | 3,120 horas/año | 3 áreas × 20h/semana × 52 semanas |
| **Mejora en decisiones de negocio** | Cualitativo | Mejor forecasting, reducción de obsolescencia |
| **Optimización uso licencias Power BI** | Cuantificable | Aprovechamiento completo de 8 licencias Pro ya adquiridas |
| **Reducción errores de consolidación** | 500 horas/año | Menor reproceso, mejor calidad de datos |
| **TOTAL AHORRO ANUAL** | **~3,620 horas/año** | Equivalente a ~1.7 FTE liberados para tareas estratégicas |

### 8.9.2. Análisis de Beneficios

| Métrica | Valor |
|---------|-------|
| **Esfuerzo del Proyecto** | 1,590 horas (42 semanas) |
| **Ahorro Operativo Anual** | ~3,620 horas/año |
| **Ratio de Retorno** | **2.3:1** (2.3 horas ahorradas por cada hora invertida) |
| **Tiempo de Recuperación** | **~5 meses de operación** |
| **Beneficio Neto 3 años** | >10,000 horas liberadas para tareas estratégicas |

**Conclusión:** Proyecto rentable con recuperación de esfuerzo dentro del primer año, liberando recurso humano para actividades de mayor valor agregado. La solución completa con 18 transacciones y 12 dashboards proporciona una plataforma robusta y escalable.

---

## 8.10. Condiciones del Proyecto

### 8.10.1. Validez de la Propuesta

- **Validez:** 30 días desde fecha de emisión (5-nov-2025 a 5-dic-2025)
- **Vigencia:** Sujeto a confirmación si inicio es posterior a 15-dic-2025

### 8.10.2. Garantías

- ✅ **Garantía de calidad:** Reconciliación SAP ↔ BigQuery >99%
- ✅ **Garantía de funcionalidad:** Dashboards operativos según especificaciones
- ✅ **Garantía de documentación:** Entrega completa de documentación técnica y funcional
- ✅ **Soporte post go-live:** 30 días incluidos (horario hábil, incidentes menores)

### 8.10.3. Exclusiones de Garantía

❌ Problemas derivados de cambios en infraestructura Elanco  
❌ Issues de performance por volúmenes de datos no estimados  
❌ Cambios en requerimientos post-aprobación de Fase 0  

### 8.10.4. Cambios de Alcance

- Cualquier modificación al alcance definido requiere:
  1. Solicitud formal por escrito
  2. Análisis de impacto (tiempo/esfuerzo)
  3. Aprobación por ambas partes
  4. Adenda al contrato

---

*Siguiente sección: [09_CRONOGRAMA_SEMANAL.md](09_CRONOGRAMA_SEMANAL.md)*
