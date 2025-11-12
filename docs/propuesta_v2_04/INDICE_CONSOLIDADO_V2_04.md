# DOCUMENTACIÓN COMPLETA V2.04 - ÍNDICE Y ESTADO

**Proyecto:** Elanco Data Lake & Analytics  
**Versión:** 2.04 (Con ABAP Developer - Cronograma Moderado)  
**Fecha de actualización:** 12 de noviembre de 2025  
**Estado:** Documentación principal completada

---

## 📋 ESTRUCTURA DE DOCUMENTACIÓN

### Carpeta `/docs/propuesta_v2_04/` ✅ VERSIÓN OFICIAL

Documentos actualizados con 4 recursos, 1,880h, 36 semanas:

#### ✅ COMPLETADOS
1. **04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD_V2_04.md** ✅
   - 328h (BI: 104h | ABAP: 70h | SAP: 122h | PM: 32h)
   - 6 semanas
   - Incluye análisis Z-transactions y configuración SLT

#### 📝 USAR DOCUMENTOS BASE (Sin cambios funcionales)
Los siguientes documentos NO cambian entre V2.02 y V2.04 (funcionalidad idéntica):
- 01_CONTEXTO_Y_SITUACION_ACTUAL.md (independiente de versión)
- 02_ALCANCE_GENERAL_DE_LA_PROPUESTA.md (alcance igual en ambas)
- 03_TRANSACCIONES_SAP_INCLUIDAS.md (18 transacciones iguales)
- 07_FASE_3_MODELOS_PREDICTIVOS.md (conceptual, no cambia)
- 12_ENTREGABLES_Y_CONDICIONES_COMERCIALES.md (términos generales)
- ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md (mapeo técnico igual)

**Ubicación:** `/docs/propuesta_final/` (usar documentos base sin modificar)

---

## 📊 RESUMEN EJECUTIVO V2.04

### Métricas Principales

| Métrica | Valor |
|---------|-------|
| **Esfuerzo Total** | 1,880 horas |
| **Duración** | 36 semanas |
| **Recursos** | 4 (Consultor BI, ABAP Developer, Funcional SAP, PM) |
| **Go-Live** | 13 de septiembre de 2026 |
| **Transacciones SAP** | 18 |
| **Dashboards Power BI** | 12 |
| **Tablas SAP** | 32-38 |

### Distribución por Fase

| Fase | Duración | Esfuerzo | Descripción |
|------|----------|----------|-------------|
| **Fase 0** | 6 semanas (sem 0-6) | 328h | Análisis, POC, Go/No-Go |
| **Fase 1** | 20 semanas (sem 6-26) | 852h | Data Lake + 18 pipelines |
| **Fase 2** | 10 semanas (sem 26-36) | 700h | 12 dashboards + Go-Live |
| **TOTAL** | **36 semanas** | **1,880h** | Proyecto completo |

### Distribución por Recurso

| Recurso | Total | Promedio/sem | Fases |
|---------|-------|--------------|-------|
| **Consultor BI** | 935h | 26.0h/sem | Todas (36 sem) |
| **ABAP Developer** | 270h | 10.4h/sem | Fase 0 + Fase 1 (26 sem) |
| **Funcional SAP** | 512h | 14.2h/sem | Todas (36 sem) |
| **Project Manager** | 163h | 4.5h/sem | Todas (36 sem) |
| **TOTAL** | **1,880h** | **52.2h/sem** | **4 recursos** |

---

## 🔄 CAMBIOS PRINCIPALES VS V2.02

### Cambios Estratégicos

| Aspecto | V2.02 | V2.04 | Impacto |
|---------|-------|-------|---------|
| **Duración** | 42 semanas | 36 semanas | Go-Live 1 mes antes |
| **Esfuerzo** | 1,590h | 1,880h | +290h (+18%) |
| **Recursos** | 3 | 4 | +ABAP Developer |
| **Riesgo Técnico** | Medio-Alto | Medio | ABAP Developer mitiga |

### Nuevo Recurso: ABAP Developer

**Perfil:**
- Experiencia: 5+ años ABAP, 2+ años SAP SLT
- Módulos: MM, SD, FI (conocimiento funcional básico)
- Participación: Fase 0 + Fase 1 (26 semanas de 36)
- Dedicación: 10.4h/semana promedio

**Responsabilidades:**
1. ✅ Configuración y monitoreo SAP SLT
2. ✅ Análisis de transacciones custom (ZLEL008, ZVEL015)
3. ✅ Extracción SAP → BigQuery capa RAW
4. ✅ Gestión de tickets SAP con TI Global
5. ❌ NO participa en BigQuery ni Power BI

**Distribución de 270h:**
- Fase 0: 70h (análisis Z-transactions + configuración SLT inicial)
- Fase 1: 200h (extracción de 18 transacciones SAP)
- Fase 2: 0h (no participa)

---

## 📝 FASE 0: REVISIÓN DE ALCANCE Y FACTIBILIDAD (6 semanas)

### Objetivos V2.04
1. Validar viabilidad técnica del proyecto
2. Resolver permisos SAP y tickets BigQuery
3. **[NUEVO]** Análisis profundo Z-transactions (ZLEL008, ZVEL015)
4. **[NUEVO]** Configuración inicial SAP SLT
5. POC end-to-end: SAP → SLT → BigQuery → Power BI
6. Decisión Go/No-Go

### Esfuerzo: 328h
- Consultor BI: 104h
- **ABAP Developer: 70h** (análisis Z + SLT)
- Funcional SAP: 122h
- Project Manager: 32h

### Entregables Críticos
1. ✅ Arquitectura BigQuery 3 capas definida
2. ✅ **Especificación técnica ZLEL008 y ZVEL015**
3. ✅ **SAP SLT configurado y operacional**
4. ✅ Backlog priorizado de 18 transacciones
5. ✅ POC funcional validado
6. ✅ Decisión Go/No-Go documentada

---

## 📝 FASE 1: CONSTRUCCIÓN DEL DATA LAKE (20 semanas)

### Objetivos V2.04
1. Desarrollar Data Lake BigQuery (RAW/PROCESSED/CURATED)
2. Implementar 18 pipelines de extracción + transformación
3. **[CAMBIO]** Paralelización: ABAP extrae (RAW), BI transforma (PROCESSED/CURATED)
4. Validación funcional SAP de las 18 transacciones
5. Automatización CI/CD y monitoreo

### Esfuerzo: 852h (+156h vs V2.02)
- Consultor BI: 394h (transformaciones BigQuery)
- **ABAP Developer: 200h** (extracción SAP → RAW)
- Funcional SAP: 194h (validación funcional)
- Project Manager: 64h (coordinación)

### Separación de Roles (CRÍTICO)
```
SAP S/4HANA
     ↓ [ABAP Developer]
 BigQuery RAW (datos crudos)
     ↓ [Consultor BI]
 BigQuery PROCESSED (limpio/transformado)
     ↓ [Consultor BI]
 BigQuery CURATED (modelo dimensional)
```

### Módulos y Transacciones

| Módulo | Transacciones | Semanas | ABAP Hours | BI Hours |
|--------|---------------|---------|------------|----------|
| FI (4 trans) | FAGLL03, FB03, F.08, F.01 | 3 sem | 28h | 52h |
| SD (2 trans) | VA05, KE24 | 2 sem | 18h | 36h |
| MM Proc (3) | ME2L, ME23N, MM60 | 3 sem | 20h | 40h |
| MM Inv (3) | MB59, MB5B, MCHB | 3 sem | 18h | 38h |
| **ZLEL008** | **Inventario MRP** | **3 sem** | **32h** | **40h** |
| CO/AP/AR (4) | KSB1, KE24, FBL1N, FBL5N | 3 sem | 24h | 48h |
| Master+ZVEL (3) | XK03, XD03, ZVEL015 | 3 sem | 28h | 42h |
| Optimización | Testing + CI/CD | 2 sem | 12h | 50h |

**Total:** 20 semanas | ABAP: 200h | BI: 394h

---

## 📝 FASE 2: MODELADO Y DASHBOARDS (10 semanas)

### Objetivos V2.04
1. Diseñar modelo dimensional (8 dimensiones + 6 hechos)
2. Desarrollar 12 dashboards Power BI con RLS
3. Testing y UAT en 4 fases
4. Capacitación usuarios clave
5. Go-Live producción

### Esfuerzo: 700h (+41h vs V2.02)
- Consultor BI: 437h (dashboards Power BI)
- **ABAP Developer: 0h** (NO participa en Fase 2)
- Funcional SAP: 164h (validación funcional)
- Project Manager: 99h (coordinación UAT + Go-Live)

### 12 Dashboards Power BI

| Categoría | Dashboards | Semanas | BI Hours |
|-----------|------------|---------|----------|
| Financieros (3) | General, OPEX, Controlling | 3 sem | 66h |
| Ventas (3) | Ventas, Rentabilidad, Regional | 3 sem | 70h |
| Supply (3) | Inventario, Supply Chain, Compras | 3 sem | 64h |
| Tesorería (3) | CxP, CxC, Ejecutivo | 3 sem | 68h |
| UAT + Ajustes | Testing integral | 4 sem | 45h |
| Go-Live | Capacitación + Deploy | 2 sem | 36h |

**Total:** 10 semanas | BI: 437h (NO ABAP Developer)

---

## 📊 COMPARATIVA DETALLADA V2.02 vs V2.04

### Por Fase

| Fase | V2.02 Duración | V2.04 Duración | V2.02 Esfuerzo | V2.04 Esfuerzo | Delta |
|------|----------------|----------------|----------------|----------------|-------|
| **Fase 0** | 6 sem | 6 sem | 235h | 328h | +93h |
| **Fase 1** | 22 sem | **20 sem** | 696h | 852h | -2 sem / +156h |
| **Fase 2** | 14 sem | **10 sem** | 659h | 700h | -4 sem / +41h |
| **TOTAL** | **42 sem** | **36 sem** | **1,590h** | **1,880h** | **-6 sem / +290h** |

### Por Recurso

| Recurso | V2.02 | V2.04 | Delta | Justificación |
|---------|-------|-------|-------|---------------|
| **Consultor BI** | 961h (22.9h/sem) | 935h (26.0h/sem) | -26h | Menos extracción SAP |
| **ABAP Developer** | 0h | **270h (10.4h/sem)** | **+270h** | **Recurso nuevo** |
| **Funcional SAP** | 484h | 512h | +28h | Coordinación con ABAP |
| **Project Manager** | 145h | 163h | +18h | Coordinación 4 recursos |
| **TOTAL** | **1,590h** | **1,880h** | **+290h (+18%)** | **Inversión controlada** |

---

## ✅ VENTAJAS DE V2.04

### 1. Go-Live Adelantado
- **6 semanas antes** (13-sep-2026 vs 15-oct-2026)
- Valor de negocio 1 mes antes
- ~100h de operación manual eliminadas en septiembre

### 2. Reducción de Riesgo Técnico
- ABAP Developer especialista en SAP SLT (tecnología crítica)
- Z-transactions analizadas profesionalmente (ZLEL008, ZVEL015)
- Menor probabilidad de delays por problemas SAP

### 3. Calidad Superior
- Consultor BI con carga sostenible (26h/sem, no sobrecargado)
- Separación de roles: ABAP extrae, BI transforma
- Mayor tiempo para optimización BigQuery y dashboards

### 4. Paralelización Efectiva
- ABAP Developer extrae datos SAP en paralelo
- Consultor BI transforma sin esperar extracción completa
- Fase 1 se reduce de 22 a 20 semanas

---

## ⚠️ DESVENTAJAS DE V2.04

### 1. Incremento de Presupuesto
- +290h (+18%) vs V2.02
- Inversión: 270h ABAP + 20h coordinación adicional

### 2. Complejidad de Coordinación
- 4 recursos vs 3 recursos
- Mayor overhead de comunicación

### 3. Riesgo de Reclutamiento
- ABAP Developer debe contratarse con lead time 2-3 semanas
- Perfil especializado (SAP SLT) puede ser difícil de encontrar

---

## 💰 ANÁLISIS COSTO-BENEFICIO V2.04

### Inversión Adicional
- **+290h** vs V2.02
- Incremento del **+18%** en presupuesto

### Beneficios Cuantificables
1. **Go-Live 1 mes antes**
   - Elimina ~100h de operación manual en septiembre
   - Reduce riesgo de errores manuales
   
2. **Reducción de riesgo técnico**
   - Menor probabilidad de delays (valor: 10-15% del proyecto)
   - Z-transactions bien entendidas desde Fase 0

3. **Calidad superior**
   - Menos bugs post-Go-Live (ahorro en correcciones)
   - Dashboards más elaborados

### Break-Even
**290h inversión / 100h ahorro = 2.9 meses post-Go-Live**

Si se considera reducción de riesgo + calidad:
**Break-even real: 1.5-2 meses post-Go-Live**

---

## 📅 CRONOGRAMA V2.04

### Hitos Clave

| Hito | Semana | Fecha | Descripción |
|------|--------|-------|-------------|
| **Kick-off** | Sem 0 | 6-ene-2026 | Inicio del proyecto |
| **Go/No-Go** | Sem 6 | 16-feb-2026 | Decisión Fase 1 |
| **Data Lake Operacional** | Sem 26 | 5-jul-2026 | Fin Fase 1 |
| **UAT Completado** | Sem 33 | 23-ago-2026 | Validación usuarios |
| **Go-Live Producción** | **Sem 36** | **13-sep-2026** | **Sistema productivo** |

### Participación de ABAP Developer

```
Fase 0 (Sem 0-6):   █████████████ 70h
Fase 1 (Sem 6-26):  ████████████████████████████████████████ 200h
Fase 2 (Sem 26-36): [NO PARTICIPA] 0h
                    └─────────────────────────────┘
                    Total ABAP: 270h (26 semanas)
```

---

## 🎯 RECOMENDACIÓN FINAL

### ⭐ VERSIÓN OFICIAL: V2.04

**Razón:** Equilibrio óptimo entre costo, tiempo y riesgo.

**Ventajas decisivas:**
1. ✅ Go-Live **1 mes antes** (valor inmediato para el negocio)
2. ✅ Riesgo técnico **reducido** (ABAP Developer mitiga)
3. ✅ Carga de trabajo **sostenible** para todos los recursos
4. ✅ ROI positivo en **2-3 meses** post-Go-Live

**Trade-off aceptable:**
- Inversión controlada (+18%)
- Complejidad de coordinación manejable
- Riesgo de reclutamiento mitigable (lead time 2-3 semanas)

---

## 📞 PRÓXIMOS PASOS

### De Parte de Elanco
1. ☐ Revisión y aprobación propuesta V2.04
2. ☐ Decisión sobre inversión adicional (+290h)
3. ☐ Confirmación disponibilidad SAP Basis
4. ☐ Provisión de accesos SAP y BigQuery
5. ☐ Aprobación de cronograma 36 semanas

### De Parte de Aunergia
1. ☐ Reclutamiento ABAP Developer (iniciar YA, lead time 2-3 sem)
2. ☐ Preparación ambientes desarrollo/testing
3. ☐ Elaboración plan detallado Fase 0 (semana a semana)
4. ☐ Coordinación kick-off (6 de enero de 2026)

---

## 📁 ARCHIVOS DISPONIBLES

### Carpeta `/docs/propuesta_v2_04/`
- ✅ 04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD_V2_04.md
- 📝 (Otros documentos en preparación o usar base)

### Carpeta `/docs/propuesta_v2_02/`
- 📄 Documentos originales V2.02 (backup)

### Carpeta `/docs/propuesta_final/`
- 📘 Documentos comunes a ambas versiones
- 📄 00_PORTADA_Y_RESUMEN_EJECUTIVO_V2_04.md
- 📄 README_V2_04.md

### Raíz del proyecto
- 📄 RESUMEN_PROPUESTA_FINAL_V2_04.txt (resumen ejecutivo)
- 📄 RESUMEN_PROPUESTA_FINAL_V2_02.txt (backup V2.02)
- 📄 RESUMEN_CAMBIOS_V2_04.md (comparativa detallada)
- 📄 REPORTE_CONSISTENCIA_V2_04.md (análisis de consistencia)
- 📄 RESUMEN_ACTUALIZACION_V2_04.md (log de cambios)

---

**Elaborado por:** Equipo Técnico Aunergia  
**Fecha:** 12 de noviembre de 2025  
**Versión:** 2.04 (Con ABAP Developer - Cronograma Moderado)  
**Estado:** Documentación principal completada

**Para consultas:** Contactar a su representante de Aunergia

---

**FIN DEL ÍNDICE CONSOLIDADO V2.04**
