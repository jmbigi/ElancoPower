# 8. ESTIMACIÓN DE ESFUERZOS

## 8.1. Resumen Ejecutivo

### Esfuerzo Total del Proyecto

| Fase | Horas |
|------|-------|
| **Fase 0 - Due Diligence** | 116h |
| **Fase 1 - Data Lake** | 267h |
| **Fas### Calendario del Proyecto

| Fase | Horas | Duración | Fecha Inicio | Fecha Fin |
|------|-------|----------|--------------|-----------|
| **Inicio del Proyecto** | - | - | 1-dic-2025 | 1-dic-2025 |
| **Fase 0 (Revisión y Alcance)** | 116h | 5 sem | 1-dic-2025 | 12-ene-2026 |
| **Pausa Vacacional** 🎄 | - | 1 sem | 23-dic-2025 | 29-dic-2025 |
| **Fase 1 (Data Lake)** | 267h | 10 sem | 13-ene-2026 | 23-mar-2026 |
| **Fase 2 (12 Dashboards)** | 294h | 8 sem | 24-mar-2026 | 18-may-2026 |
| **Go-Live y Cierre** | - | - | 12-may-2026 | 18-may-2026 |
| **TOTAL ESFUERZO** | **677h** | **24 sem** | **1-dic-2025** | **18-may-2026** |

**Nota:** La duración de 24 semanas incluye 1 semana de pausa vacacional (23-29 diciembre 2025).  
**Restricción JMB:** Máximo 6h/día (30h/semana), Fase 2 ajustada de 7 a 8 semanas.ashboards Power BI** | 294h |
| **Fase 3 - ML Roadmap** | Descripción conceptual |
| **TOTAL HORAS** | **677h** |

### Duración Total

- **Tiempo estimado:** 24 semanas (~6 meses, incluyendo 1 semana vacacional)
- **Inicio:** Mes 1, Semana 1
- **Finalización:** Mes 6, Semana 23
- **Nota:** Incluye 1 semana de pausa vacacional durante festividades de fin de año
- **Restricción:** Juan Manuel Bigi trabaja máximo 6 horas/día (30h/semana)

### Equipo

| Perfil | Horas Totales |
|--------|---------------|
| **Juan Manuel Bigi** - Arquitecto de Datos / Desarrollador | 478h |
| **Lucía Rodríguez** - Analista SAP Power User | 145h |
| **Linda López** - Project Manager | 42h |
| **Consultor ABAP Especializado** | 12h |
| **TOTAL** | **677h** |

---

## 8.2. Desglose Detallado por Fase

### 8.2.1. Fase 0 - Revisión del Alcance y Factibilidad

| **Duración estimada** | 5 semanas (incluyendo 1 sem vacacional) |
| **Fase del proyecto:** | Mes 1, Semanas 1-5  |
| **Pausa vacacional:** | Durante Semana 4 (festividades de fin de año) |

#### Desglose de Horas por Actividad

| Actividad | Lucía R. | Juan M. B. | Stakeholders | Total |
|-----------|----------|------------|--------------|-------|
| Gestión de permisos SAP y tickets BigQuery | 20h | - | - | 20h |
| Análisis técnico arquitectura BigQuery | - | 24h | - | 24h |
| Workshop priorización transacciones | 4h | 8h | 12h | 24h |
| Análisis transacciones custom (Z) | 4h | 4h | - | 8h |
| Definición requisitos técnicos iniciales | - | 16h | - | 16h |
| Elaboración plan de riesgos | 4h | 4h | - | 8h |
| Reunión Go/No-Go | 2h | 2h | 4h | 8h |
| **SUBTOTAL FASE 0** | **34h** | **58h** | **16h** | **108h** |

#### Distribución de Horas Fase 0

| Recurso | Horas |
|---------|-------|
| Lucía Rodríguez | 48h |
| Juan Manuel Bigi | 58h |
| Linda López (PM) | 10h |
| Stakeholders Elanco | 16h (sin costo) |
| **TOTAL FASE 0** | **116h** |

---

### 8.2.2. Fase 1 - Construcción de Data Lake

**Duración:** 10 semanas  
**Fase del proyecto:** Mes 2-3, Semanas 6-15

#### Desglose de Horas por Módulo SAP

| Módulo | Transacciones | Horas Desarrollo | Horas Validación | Total |
|--------|---------------|------------------|------------------|-------|
| **Setup Infraestructura** | - | 16h | - | 16h |
| **Módulo FI** | FAGLL03, FB03, F.08, F.01 | 36h | 4h | 40h |
| **Módulo SD** | VA05 | 14h | 2h | 16h |
| **Módulo MM** | ZLEL008, ME2L, MB5B | 42h | 6h | 48h |
| **Módulo CO** | KSB1, KE24 | 24h | 4h | 28h |
| **Testing integral** | Todas | - | 16h | 16h |
| **Documentación** | Todas | 12h | - | 12h |
| **Gestión y ajustes** | Todas | 16h | - | 16h |
| **SUBTOTAL** | **18 trans** | **160h** | **32h** | **192h** |

#### Distribución por Recurso

| Recurso | Actividades | Horas |
|---------|-------------|-------|
| **Juan Manuel Bigi** | Desarrollo pipelines, infraestructura, documentación | 156h |
| **Lucía Rodríguez** | Validación funcional, análisis Z-tables, coordinación | 40h |
| **Consultor ABAP** | Análisis ZLEL008 (contingencia) | 8h |

#### Distribución de Horas Fase 1

| Recurso | Horas |
|---------|-------|
| Juan Manuel Bigi | 180h |
| Lucía Rodríguez | 60h |
| Linda López (PM) | 15h |
| Consultor ABAP | 12h |
| **TOTAL FASE 1** | **267h** |

---

### 8.2.3. Fase 2 - Modelado de Datos y 12 Dashboards

**Duración:** 8 semanas  
**Fase del proyecto:** Mes 4-6, Semanas 16-23  
**Nota:** Extendida de 7 a 8 semanas para cumplir restricción de JMB (máx 6h/día = 30h/sem)

#### Desglose de Horas por Actividad

| Actividad | Horas JMB | Horas LR | Horas Stakeholders | Total |
|-----------|-----------|----------|--------------------|-------|
| Diseño modelo dimensional | 32h | - | 4h | 36h |
| Desarrollo capa semántica BigQuery | 20h | - | - | 20h |
| Desarrollo Dashboard 1: Financiero General | 10h | - | 2h | 12h |
| Desarrollo Dashboard 2: Ventas (Sales) | 10h | - | 2h | 12h |
| Desarrollo Dashboard 3: Inventario | 10h | - | 2h | 12h |
| Desarrollo Dashboard 4: OPEX | 10h | - | 2h | 12h |
| Desarrollo Dashboard 5: Ejecutivo | 10h | - | 2h | 12h |
| Desarrollo Dashboard 6: Supply Chain | 10h | - | 2h | 12h |
| Desarrollo Dashboard 7: Compras (Procurement) | 10h | - | 2h | 12h |
| Desarrollo Dashboard 8: Rentabilidad por Producto | 10h | - | 2h | 12h |
| Desarrollo Dashboard 9: Cuentas por Pagar | 10h | - | 2h | 12h |
| Desarrollo Dashboard 10: Cuentas por Cobrar | 10h | - | 2h | 12h |
| Desarrollo Dashboard 11: Controlling (CO) | 10h | - | 2h | 12h |
| Desarrollo Dashboard 12: Estadístico Regional | 10h | - | 2h | 12h |
| Configuración RLS (12 dashboards) | 18h | - | - | 18h |
| Testing con usuarios (UAT) | 12h | 6h | 12h | 30h |
| Documentación | 8h | 6h | - | 14h |
| Capacitación usuarios | 8h | 8h | 16h | 32h |
| Ajustes post-UAT | 20h | - | - | 20h |
| **SUBTOTAL FASE 2** | **218h** | **20h** | **54h** | **292h** |

#### Distribución de Horas Fase 2

| Recurso | Horas |
|---------|-------|
| Juan Manuel Bigi | 240h |
| Lucía Rodríguez | 37h |
| Linda López (PM) | 17h |
| Stakeholders Elanco | 54h (sin costo) |
| **TOTAL FASE 2** | **294h** |

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

### 8.3.1. Horas Totales por Persona

| Recurso | Fase 0 | Fase 1 | Fase 2 | Fase 3 | Total |
|---------|--------|--------|--------|--------|-------|
| **Juan Manuel Bigi** | 58h | 180h | 240h | (incl) | **478h** |
| **Lucía Rodríguez** | 48h | 60h | 37h | - | **145h** |
| **Linda López (PM)** | 10h | 15h | 17h | - | **42h** |
| **Consultor ABAP** | - | 12h | - | - | **12h** |
| **SUBTOTAL EQUIPO** | **116h** | **267h** | **294h** | **0h** | **677h** |

### 8.3.2. Consultoría ABAP Especializada

| Concepto | Horas | Justificación |
|----------|-------|---------------|
| Análisis transacciones custom (ZLEL008, ZVEL015) | 12h | Complejidad Z-tables y lógica de negocio custom |

**Nota:** No se incluyen contingencias adicionales. Cualquier cambio de alcance mayor requerirá cotización adicional.

---

## 8.4. Esfuerzo Final Consolidado

### 8.4.1. Distribución de Esfuerzo por Recurso

| Recurso | Horas | % del Total |
|---------|-------|-------------|
| **Desarrollo Técnico (Juan Manuel Bigi)** | 478h | 70.6% |
| **Consultoría SAP (Lucía Rodríguez)** | 145h | 21.4% |
| **Project Management (Linda López)** | 42h | 6.2% |
| **Consultoría ABAP Especializada** | 12h | 1.8% |
| **TOTAL ESFUERZO** | **677h** | **100%** |

### 8.4.2. Calendario del Proyecto

| Fase | Horas | Duración | Periodo |
|------|-------|----------|---------|
| **Inicio del Proyecto** | - | - | Mes 1, Semana 1 |
| **Fase 0 (Revisión y Alcance)** | 116h | 5 semanas | Mes 1, Semanas 1-5 |
| **Fase 1 (Data Lake)** | 267h | 10 semanas | Mes 2-3, Semanas 6-15 |
| **Fase 2 (12 Dashboards)** | 294h | 8 semanas | Mes 4-6, Semanas 16-23 |
| **Cierre y Go-Live** | - | - | Mes 6, Semana 23 |
| **TOTAL ESFUERZO** | **677h** | **24 semanas** | **~6 meses** |

---

## 8.5. Comparativa de Alcance

### Alcance Inicial (Oct 2025) vs. Alcance Final (Nov 2025)

| Concepto | Oct 2025 | Nov 2025 | Dic 2025 (Final) | Comentario |
|----------|----------|----------|------------------|------------|
| **Transacciones SAP** | 8 | 18 | 18 | Alcance completo MM/SD/FI/CO |
| **Fase 0** | 2-3 sem | 4-5 sem | 5 sem | Más tiempo para validaciones |
| **Fase 1** | 6-8 sem | 8-10 sem | 10 sem | Incluye transacciones custom ABAP |
| **Fase 2** | 4-5 sem | 6-7 sem | 8 sem | Ajustado por restricción 6h/día JMB |
| **PM Formalizado** | No | Sí (Linda) | Sí (Linda) | Project Management explícito |
| **TOTAL** | **12-16 sem** | **18-20 sem** | **24 sem** | Restricción JMB: máx 6h/día |

**Justificación de la expansión:**
- ✅ Alcance expandido: 18 transacciones (vs. 8 iniciales)
- ✅ PM formalizado (Linda López)
- ✅ Tiempos más holgados para calidad
- ✅ Consultoría ABAP especializada contemplada
- ✅ Revisión exhaustiva de alcance y factibilidad (Fase 0)

---

## 8.6. Exclusiones (No Incluido en el Alcance del Proyecto)

### 8.6.1. Costos de Infraestructura y Servicios (Responsabilidad del Cliente)

❌ **Licencias Google Cloud Platform (BigQuery)**
- Costo estimado: USD $300-$500/mes
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
| **Esfuerzo del Proyecto** | 677 horas (21-23 semanas, incl. 1 sem vacacional) |
| **Ahorro Operativo Anual** | ~3,620 horas/año |
| **Ratio de Retorno** | **5.3:1** (5.3 horas ahorradas por cada hora invertida) |
| **Tiempo de Recuperación** | **~2 meses de operación** |
| **Beneficio Neto 3 años** | >10,000 horas liberadas para tareas estratégicas |

**Conclusión:** Proyecto altamente rentable con recuperación de esfuerzo en corto plazo, liberando recurso humano para actividades de mayor valor agregado.

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
