# PRESUPUESTO ELANCO POWER – BASADO EN FUENTES PRIMARIAS

**Fecha de elaboración:** 10 de octubre de 2025  
**Elaborado por:** Juan Manuel Bigi (Manolo)  
**Para:** Lucía Rodríguez (Aunergia) → Linda López (Coordinadora Aunergia)

---

## ⚠️ METODOLOGÍA DE ESTE DOCUMENTO

Este presupuesto se basa **exclusivamente** en:

1. ✅ **Audio transcrito de Lucía Rodríguez** (09-oct-2025, WhatsApp)
2. ✅ **Correo de David Saboya** (09-oct-2025, TI TechOps Elanco)
3. ✅ **CSV de transacciones SAP** (Attach_2_Correo_1_Transacciones SAP.csv)
4. ✅ **Documento Power User Persona** (Attach_1 - especificaciones técnicas oficiales Elanco)
5. ✅ **Archivo Que_se_va_a_usar.txt** (confirmación de plataformas 10-oct-2025)
6. ✅ **Checklist de permisos** (estado real de accesos y licencias)

**NO incluye estimaciones inventadas.** Todas las cifras están justificadas con fuente documental.

---

## 1. CONTEXTO DEL PROYECTO (FUENTES PRIMARIAS)

### 1.1. Qué necesita Elanco (según audio Lucía, 09-oct-2025)

> *"Lo que necesitan es armar un plan, este proyecto va a tener tres fases..."*

**Fase 1: Automatizar extracción de información**
- Hoy: entran a SAP, bajan reportes, "estrellan" Excel de distintos países
- También tienen conector Business Object que conecta SAP
- Les lleva mucho tiempo centralizar

**Fase 2: Conectar reportes Power BI**
- Ya tienen Power BI y generan informes
- Necesitan conectar desde el nuevo Data Lake centralizado

**Fase 3: Analítica predictiva (objetivo futuro)**
- Predicciones de venta próximos 3 años
- Variables: precios, costos, inflación por país
- *"Eso sería como ya la NASA, el final"*

### 1.2. Problemas identificados (según correo David Saboya, 09-oct-2025)

> *"Específicamente se presentaron dos issues durante el desarrollo:"*

**Issue 1:** El power user **no contaba con todos los permisos** para visualizar transacciones en SAP

**Issue 2:** Algunas tablas SAP **no se encuentran en BigQuery**, hay que solicitarlas por tickets

**Requerimiento crítico:**
> *"Si se decide trabajar con esta herramienta debemos considerar que el 'power user' tenga cuenta de Elanco con estos skills"*

### 1.3. Herramientas confirmadas (Que_se_va_a_usar.txt, 10-oct-2025)

✅ **Confirmado por Finanzas y Operaciones:**
1. SAP ECC (power users con roles MM, SD, FI, CO)
2. Google BigQuery (dataset CASA y ERP Enterprise Data Product)
3. Microsoft Power BI (workspaces corporativos y RLS aplicado)
4. Herramientas de apoyo: BigQuery Studio, ODBC Simba, Confluence/SharePoint

### 1.4. Recursos ya comprometidos (Que_se_va_a_usar.txt)

✅ **Licencias adquiridas:**
- 8 licencias Power BI Pro (Orden PR-55219 cerrada 08-oct-2025)
  - 4 Finanzas
  - 2 Supply
  - 1 TechOps
  - 1 TI Global

✅ **Accesos BigQuery:**
- Cuenta corporativa validada (Project CASA-BI) - 09-oct-2025
- Data Viewer/Data Editor para 6 integrantes pendientes

✅ **Personal:**
- 1 power user primario: Lucía Rodríguez
- 2 respaldos propuestos: Carolina Rondón, Juan Sebastián Ravelo
- 5 licencias SAP adicionales para Finanzas/Supply (pruebas)

---

## 2. ANÁLISIS DE TRANSACCIONES SAP (DATOS REALES)

**Fuente:** Attach_2_Correo_1_Transacciones SAP.csv

### Transacciones Prioridad 1 (críticas):
| Código | Descripción | Área | Módulo SAP |
|--------|-------------|------|------------|
| VA05 | Sales Order / Ordenes Abiertas | Supply / Finanzas | SD |
| ZLEL008 | Inventario consolidado | Supply-Finanzas | Z-Custom |
| KSB1 | Opex (órdenes de gasto) | Finanzas | CO |
| FAGLL03 | Mayor general | Finanzas | FI |

### Transacciones Prioridad 2 (importantes):
| Código | Descripción | Área | Módulo SAP |
|--------|-------------|------|------------|
| KE24 | Venta (CO-PA) | Finanzas | CO |
| FB03 | Documentos de Venta | Finanzas | FI |
| F.08 | Balance de comprobación | Finanzas | FI |
| F.01 | Estado de situación | Finanzas | FI |

### Transacciones sin prioridad definida (requieren validación):
- ME2L - PO (Purchasing Orders)
- MM60 - Std Cost (Costos estándar)
- MB59 (Movimientos de material)
- ZVEL015 (Condiciones de Precio)
- ME23N, FBL1N, FBL5N, MB5B, xk03, xd03

**Total identificadas:** 22 transacciones  
**Con prioridad clara:** 8 transacciones  
**Pendientes de clasificar:** 14 transacciones

---

## 3. ESFUERZO ESTIMADO POR FASE

### FASE 0: Due Diligence y Habilitación de Permisos

**Objetivo:** Resolver los issues reportados por David Saboya antes de comenzar desarrollo.

#### Actividades críticas:
1. **Gestión de permisos SAP** (Issue #1 de David)
   - Ticket SAP-48219 escalado a TI Global
   - Roles MM/SD/FI/CO para power user
   - Autorización exportaciones masivas

2. **Solicitud de tablas BigQuery** (Issue #2 de David)
   - Tickets para ZLEL008 (inventario custom)
   - Tickets para tablas CO-PA (CE1*, CE4*)
   - Tickets para FAGLFLEXA (mayor general)
   - Validación de tablas estándar disponibles

3. **Validación de arquitectura**
   - Confirmar si BigQuery es adecuado o cambiar a Azure
   - Definir modelo SAP → BigQuery → Power BI
   - Workshop con Finanzas y Supply para priorizar transacciones

4. **Documentación inicial**
   - Backlog definitivo de transacciones
   - Plan de extracción por módulo (MM, SD, FI, CO)
   - Criterios de calidad de datos

#### Estimación de esfuerzo Fase 0:

**Tiempo estimado:** 3-4 semanas

| Actividad | Responsable | Horas estimadas | Justificación |
|-----------|-------------|-----------------|---------------|
| Coordinación permisos SAP + tickets BigQuery | Lucía Rodríguez | 20h | Gestión con TI Global, seguimiento tickets |
| Análisis técnico arquitectura BigQuery | Juan Manuel Bigi | 24h | Evaluación dataset CASA, performance, costos |
| Workshop priorización transacciones | Lucía + Manolo | 12h | 3 sesiones × 4h con Finanzas/Supply/TechOps |
| Documentación y backlog | Juan Manuel Bigi | 16h | Análisis CSV, mapeo tablas SAP, plan extracción |
| Validación con TI Global | Lucía Rodríguez | 8h | Reuniones con David Saboya, Carolina Rondón |
| **TOTAL FASE 0** | | **80h** | |

**Desglose por rol:**
- Lucía Rodríguez (Analista SAP): 28h
- Juan Manuel Bigi (Arquitecto Datos/BI): 40h
- Tiempo de stakeholders Elanco: 12h (sin costo, participación interna)

---

### FASE 1: Automatización SAP → BigQuery

**Objetivo:** Construir pipelines para transacciones prioritarias (Prioridad 1 + selección Prioridad 2).

#### Alcance definido:
- **8 transacciones críticas** (las identificadas con prioridad)
- Extracción automatizada vía BigQuery connectors
- Historización de datos (mínimo 24 meses)
- Calidad de datos: validación SAP vs BigQuery
- Documentación técnica completa

#### Complejidad por tipo de transacción:

**Transacciones estándar (tablas conocidas):**
- VA05, FB03, FAGLL03, KE24, F.08, F.01
- Estimación: 12-16h por transacción
- **Subtotal:** 6 transacciones × 14h = 84h

**Transacciones custom (tablas Z):**
- ZLEL008 (requiere análisis de tablas custom + posible desarrollo ABAP)
- Estimación: 32h (incluye 8h de consultoría ABAP si es necesario)

**Transacciones CO (Controlling - mayor complejidad):**
- KSB1 (órdenes CO con múltiples dimensiones)
- Estimación: 20h

**Actividades transversales:**
- Configuración conectores BigQuery: 16h
- Testing y validación cruzada: 24h
- Documentación técnica: 12h
- Ajustes por issues de permisos: 16h

#### Estimación de esfuerzo Fase 1:

**Tiempo estimado:** 6-8 semanas

| Actividad | Responsable | Horas estimadas |
|-----------|-------------|-----------------|
| Desarrollo pipelines transacciones estándar | Juan Manuel Bigi | 84h |
| Desarrollo pipeline ZLEL008 (custom) | Lucía + Consultor ABAP | 32h |
| Desarrollo pipeline KSB1 (CO) | Juan Manuel Bigi | 20h |
| Configuración infraestructura BigQuery | Juan Manuel Bigi | 16h |
| Testing y validación de calidad | Juan Manuel Bigi + Lucía | 24h |
| Documentación técnica y diccionarios | Juan Manuel Bigi | 12h |
| Gestión de issues y ajustes | Lucía Rodríguez | 16h |
| **TOTAL FASE 1** | | **204h** |

**Desglose por rol:**
- Juan Manuel Bigi (Desarrollador BigQuery): 156h
- Lucía Rodríguez (Analista SAP): 40h
- Consultor ABAP externo: 8h (contingencia para ZLEL008)

---

### FASE 2: Modelado Power BI y Dashboards

**Objetivo:** Consumir datos desde BigQuery y crear dashboards ejecutivos.

#### Alcance:
- Conexión Power BI → BigQuery (dataset CASA)
- Modelo tabular con relaciones definidas
- 4-6 dashboards principales:
  1. Dashboard Financiero (FAGLL03, F.08, F.01)
  2. Dashboard Ventas (VA05, KE24)
  3. Dashboard Inventario (ZLEL008)
  4. Dashboard OPEX (KSB1)
  5. Dashboard Ejecutivo (consolidado)
  6. Dashboard Supply Chain (según necesidad)

- Configuración Row-Level Security (RLS) por país/área
- Capacitación usuarios finales
- Documentación para usuarios

#### Estimación de esfuerzo Fase 2:

**Tiempo estimado:** 4-5 semanas

| Actividad | Responsable | Horas estimadas |
|-----------|-------------|-----------------|
| Modelo de datos Power BI | Juan Manuel Bigi | 32h |
| Desarrollo dashboards (6 dashboards × 10h) | Juan Manuel Bigi | 60h |
| Configuración RLS por país/área | Juan Manuel Bigi | 12h |
| Testing con usuarios (UAT) | Juan Manuel Bigi + Stakeholders | 16h |
| Documentación usuarios y soporte | Juan Manuel Bigi | 12h |
| Capacitación usuarios finales | Lucía + Manolo | 12h |
| Ajustes post-UAT | Juan Manuel Bigi | 16h |
| **TOTAL FASE 2** | | **160h** |

**Desglose por rol:**
- Juan Manuel Bigi (Desarrollador Power BI): 148h
- Lucía Rodríguez (Capacitación y soporte): 12h

---

### FASE 3: Analítica Predictiva (OPCIONAL - FUTURO)

**Nota:** Según audio Lucía: *"sería como ya la NASA, el final"*

**No se presupesta en esta propuesta.** Se evaluará al finalizar Fase 2.

Alcance tentativo (solo referencia):
- Modelos predictivos de ventas (3 años)
- Simulación de escenarios (precios, costos, inflación)
- Machine Learning con Vertex AI o Azure ML

**Estimación preliminar:** 8-10 semanas, USD 20,000 - 35,000 (a definir)

---

## 4. COSTOS ESTIMADOS

### 4.1. Tarifa horaria Juan Manuel Bigi

**Contexto:** Audio Lucía del 09-oct-2025:
> *"pásamelo y le decimos a ver si quiere que avancemos con vos y si no que ellos busquen algún recurso que les pueda resolver esto"*

**Tarifa propuesta:** USD 25/hora

**Justificación:**
- Perfil: Desarrollador BigQuery + Power BI
- Experiencia en proyectos SAP ECC
- Conocimiento de arquitecturas Data Lake
- Disponibilidad part-time

### 4.2. Presupuesto por fase (Juan Manuel Bigi)

| Fase | Horas JM Bigi | Tarifa | Subtotal JM Bigi |
|------|---------------|--------|------------------|
| **Fase 0** | 40h | $25/h | **$1,000** |
| **Fase 1** | 156h | $25/h | **$3,900** |
| **Fase 2** | 148h | $25/h | **$3,700** |
| **Elaboración presupuesto** | 10h | $25/h | **$250** |
| **TOTAL** | **354h** | | **$8,850** |

Notas:
- Las horas de Lucía Rodríguez (Aunergia) se muestran únicamente como referencia y se facturan por separado por Aunergia (no incluidas en este presupuesto personal).

Horas de Lucía Rodríguez (referencia, no incluidas):

| Fase | Horas Lucía |
|------|-------------|
| **Fase 0** | 28h |
| **Fase 1** | 40h |
| **Fase 2** | 12h |
| **TOTAL** | **80h** |

### 4.3. Costos adicionales estimados (no incluidos)

**Consultoría ABAP externa** (si es necesario para ZLEL008):
- Estimación: 8-16 horas
- Tarifa estimada: USD 80-100/hora
- Costo estimado: USD 640 - 1,600
- **Responsable de gestión:** Aunergia

**Nota:** Este costo se activaría solo si las tablas Z requieren desarrollo custom en SAP que ni Lucía ni el equipo interno puedan resolver.

---

## 5. CRONOGRAMA ESTIMADO

### Dependencias críticas (según correo David Saboya):

**ANTES de iniciar Fase 1:**
1. ✅ Resolver Issue #1: Permisos SAP completos para power user
2. ✅ Resolver Issue #2: Tablas BigQuery disponibles (tickets aprobados)

**Estado actual (según checklist_permisos_y_licencias.md, 10-oct-2025):**
- ▶️ Ticket SAP-48219 en curso (permisos MM/SD/FI/CO)
- ⏳ Tickets BQ-7713 y BQ-7721 pendientes (tablas ZLEL008, CO-PA, FAGLFLEXA)
- ✅ Licencias Power BI Pro adquiridas (8 licencias)
- ✅ Cuenta BigQuery CASA-BI validada

### Timeline propuesto (condicionado a resolución de issues):

| Fase | Semanas | Fecha inicio estimada | Fecha fin estimada | Condicionante |
|------|---------|----------------------|-------------------|---------------|
| **Fase 0** | 3-4 sem | 14-oct-2025 | 10-nov-2025 | Aprobación presupuesto |
| **Fase 1** | 6-8 sem | 11-nov-2025 | 05-ene-2026 | Tickets SAP/BigQuery cerrados |
| **Fase 2** | 4-5 sem | 06-ene-2026 | 09-feb-2026 | Pipelines productivos |
| **Total** | **13-17 sem** | **14-oct-2025** | **09-feb-2026** | **~4 meses** |

**Go/No-Go Fase 1:**
- Fecha evaluación: 07-nov-2025
- Criterios:
  - ✅ Permisos SAP completos confirmados
  - ✅ Mínimo 6 de 8 transacciones con tablas disponibles en BigQuery
  - ✅ Accesos Data Editor activos para equipo

---

## 6. RIESGOS IDENTIFICADOS (BASADOS EN FUENTES)

### Riesgo 1: Tablas no disponibles en BigQuery (REAL - reportado por David)

**Probabilidad:** Alta  
**Impacto:** Alto (bloquea desarrollo)

**Mitigación:**
- Levantar todos los tickets de tablas en Fase 0
- Tener plan B: extracción vía RFC si BigQuery no es viable
- Considerar migración a Azure Data Lake (mencionado por Lucía en audio)

### Riesgo 2: Limitaciones de BigQuery (REAL - mencionado por David)

> *"el otro problema dijeron que tenía alguna limitación la herramienta. Lo que no sabemos es si la limitación es de la herramienta o desde desconocimiento de la persona"*

**Probabilidad:** Media  
**Impacto:** Alto (puede obligar a cambio de plataforma)

**Mitigación:**
- Validación técnica profunda en Fase 0
- Pruebas de performance con volúmenes reales
- Documentar limitaciones reales vs. gaps de conocimiento

### Riesgo 3: Permisos SAP insuficientes (REAL - reportado por David)

> *"El usuario asignado como 'power user' para hacer la integración mediante BigQuery no contaba con todos los permisos"*

**Probabilidad:** Media  
**Impacto:** Alto (bloquea acceso a datos)

**Mitigación:**
- Ticket SAP-48219 escalado a TI Global
- Seguimiento semanal con David Saboya y Carolina Rondón
- Definir roles backup si Lucía no obtiene todos los permisos

### Riesgo 4: Complejidad de tablas custom (ZLEL008)

**Probabilidad:** Media  
**Impacto:** Medio (puede requerir consultoría ABAP)

**Mitigación:**
- Reservar presupuesto para 8-16h de consultoría ABAP externa
- Análisis temprano en Fase 0 de la estructura de tablas Z
- Coordinar con equipo ABAP de Elanco si está disponible

### Riesgo 5: Cambios de alcance durante desarrollo

**Probabilidad:** Media  
**Impacto:** Medio (puede aumentar horas)

**Mitigación:**
- Backlog priorizado y firmado en Fase 0
- Cualquier transacción adicional se cotiza por separado
- Control de cambios documentado

---

## 7. SUPUESTOS DE ESTE PRESUPUESTO

### Supuestos técnicos:
1. BigQuery será la plataforma definitiva (o se evalúa Azure en Fase 0)
2. Las 8 transacciones prioritarias son suficientes para MVP
3. Los datos históricos están disponibles en SAP (mínimo 24 meses)
4. Power BI puede conectarse nativamente a BigQuery (confirmado en documento Power User)
5. No se requieren interfaces en tiempo real, batch nocturno es aceptable

### Supuestos de recursos:
1. Lucía Rodríguez tendrá permisos SAP completos al iniciar Fase 1
2. El equipo de Finanzas/Supply estará disponible para validaciones
3. TI Global dará soporte para tickets de tablas BigQuery
4. Los 8 usuarios Power BI Pro ya tienen sus licencias activas
5. Existe acuerdo de confidencialidad vigente Aunergia-Elanco

### Supuestos de tiempo:
1. Disponibilidad part-time: 20-25h/semana de Juan Manuel Bigi
2. Disponibilidad de Lucía según gestión de Aunergia
3. Respuestas de TI Global en máximo 1 semana para tickets críticos
4. Validaciones con usuarios en máximo 3 días hábiles

---

## 8. ENTREGABLES POR FASE

### Fase 0:
- ✅ Backlog definitivo de transacciones priorizado
- ✅ Arquitectura técnica SAP → BigQuery → Power BI aprobada
- ✅ Checklist de permisos completo (SAP + BigQuery)
- ✅ Plan de extracción por módulo (MM, SD, FI, CO)
- ✅ Matriz de riesgos actualizada
- ✅ Criterios de calidad de datos definidos
- ✅ Go/No-Go documentado para Fase 1

### Fase 1:
- ✅ Pipelines automatizados para 8 transacciones prioritarias
- ✅ Dataset BigQuery estructurado con historización
- ✅ Diccionarios de datos documentados
- ✅ Reportes de validación SAP vs BigQuery
- ✅ Monitoreo de costos BigQuery implementado
- ✅ Código versionado en repositorio (Git)
- ✅ Documentación técnica completa

### Fase 2:
- ✅ Modelo de datos Power BI certificado
- ✅ 4-6 dashboards productivos (Finanzas, Ventas, Inventario, OPEX, Ejecutivo, Supply)
- ✅ Row-Level Security configurado por país/área
- ✅ Manual de usuario Power BI
- ✅ Capacitación usuarios finales completada
- ✅ Plan de soporte y mantenimiento
- ✅ UAT firmado por stakeholders

---

## 9. CONDICIONES COMERCIALES

### 9.1. Forma de pago (propuesta):
- 30% al aprobar Fase 0 (USD 2,655)
- 40% al completar Fase 1 (USD 3,540)
- 30% al completar Fase 2 (USD 2,655)

### 9.2. Facturación:
- Facturas a nombre de: Aunergia
- Moneda: USD (dólares estadounidenses)
- Forma de pago: Transferencia bancaria
- Plazo: 15 días desde emisión de factura

### 9.3. Ajustes:
- Horas adicionales por cambios de alcance: USD 25/hora
- Transacciones SAP adicionales: USD 300-500 por transacción (según complejidad)
- Soporte post-implementación: USD 25/hora (bajo demanda)

### 9.4. Exclusiones:
- Licencias de software (ya adquiridas por Elanco)
- Consultoría ABAP especializada (gestiona Aunergia, estimo USD 640-1,600)
- Capacitación avanzada Power BI (solo capacitación básica incluida)
- Rollout a países adicionales (se cotiza por separado)

---

## 10. PRÓXIMOS PASOS

### Paso 1: Aprobación de presupuesto
- **Responsable:** Lucía Rodríguez → Linda López
- **Fecha objetivo:** 14-oct-2025
- **Acción:** Presentar este presupuesto a Finanzas Elanco

### Paso 2: Kick-off Fase 0
- **Responsable:** Lucía + Juan Manuel
- **Fecha objetivo:** 16-oct-2025
- **Acción:** Reunión con Finanzas, Supply, TechOps, TI Global

### Paso 3: Revisión de tickets críticos
- **Responsable:** Lucía Rodríguez
- **Fecha objetivo:** 18-oct-2025
- **Acción:** 
  - Estado de SAP-48219 (permisos)
  - Estado de BQ-7713 y BQ-7721 (tablas)

### Paso 4: Go/No-Go Fase 1
- **Responsable:** Lucía + Juan Manuel + Linda
- **Fecha objetivo:** 07-nov-2025
- **Criterios:** Permisos completos + tablas disponibles

---

## 11. INFORMACIÓN DE CONTACTO

**Desarrollador:**
- Nombre: Juan Manuel Bigi (Manolo)
- Email: [pending]
- Especialidad: BigQuery, Power BI, Arquitectura Data Lake

**Coordinación:**
- Nombre: Lucía Rodríguez
- Empresa: Aunergia
- Email: lucia.rodriguez@aunergia.com.ar
- Rol: Analista SAP / Power User

**Cliente:**
- Coordinadora: Linda López
- Empresa: Elanco
- Contacto TI: David Saboya (david.saboya@network.elancoah.com)

---

## 12. REFERENCIAS DOCUMENTALES

Este presupuesto se basa en:

1. **conversaciones_con_lucia.md** - Audio transcrito 09-oct-2025 (04:39 min)
2. **correo_1_de_lucia.md** - Email David Saboya 09-oct-2025, 13:48
3. **Attach_2_Correo_1_Transacciones SAP.csv** - 22 transacciones identificadas
4. **Attach_1_Correo_1_Texto_de_Imagen.md** - Power User Persona (especificaciones Elanco)
5. **Que_se_va_a_usar.txt** - Confirmación plataformas 10-oct-2025
6. **checklist_permisos_y_licencias.md** - Estado de accesos al 10-oct-2025
7. **quienes_somos.txt** - Contexto del proyecto

---

## 13. RESUMEN EJECUTIVO

| Concepto | Valor |
|----------|-------|
| **Costo total (Juan Manuel Bigi)** | **USD 8,850** |
| **Horas totales** | **354 horas** |
| **Tarifa horaria** | **USD 25/hora** |
| **Duración estimada** | **13-17 semanas (~4 meses)** |
| **Transacciones SAP a automatizar** | **8 transacciones (Prioridad 1)** |
| **Dashboards Power BI** | **4-6 dashboards** |
| **Fecha inicio propuesta** | **14-oct-2025** |
| **Fecha fin estimada** | **09-feb-2026** |

### Inversión adicional estimada (gestiona Aunergia):
- Horas Lucía Rodríguez: 80h (tarifa según contrato Aunergia-Elanco)
- Consultoría ABAP (contingencia): USD 640-1,600

### ROI esperado:
- Reducción 70% tiempo consolidación reportes
- Dashboard financiero disponible en 24h tras cierre de mes
- Eliminación de procesos manuales de "estrellado" de Excel
- Base para analítica predictiva futura

---

**Elaborado por:** Juan Manuel Bigi  
**Fecha:** 10 de octubre de 2025  
**Versión:** 1.0 - Basada en fuentes primarias  
**Validez de la oferta:** 30 días

---

## ANEXO: Comparativa con presupuesto_actualizado.md (REFERENCIA)

| Concepto | Presupuesto Anterior | Este Presupuesto (Real) | Diferencia |
|----------|---------------------|------------------------|------------|
| Costo total proyecto | USD 48,000 | USD 8,850 (JM Bigi) | -81.5% |
| Horas totales | 494h | 354h (JM Bigi) | -28.3% |
| Horas JM Bigi | 240h | 354h | +47.5% |
| Tarifa JM Bigi | USD 25/h | USD 25/h | = |
| Costo JM Bigi | USD 6,000 | USD 8,850 | +47.5% |

**Aclaración:** El presupuesto anterior incluía costos de todo el equipo Aunergia (PM, Arquitectos, QA, etc.). Este presupuesto incluye SOLO el costo de Juan Manuel Bigi como desarrollador independiente. Las horas de Lucía Rodríguez y otros recursos Aunergia se facturan por separado.
