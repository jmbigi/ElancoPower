# ANÁLISIS DE DIFERENCIAS ENTRE PRESUPUESTOS

**Fecha:** 10 de octubre de 2025  
**Analista:** Juan Manuel Bigi

---

## PROPÓSITO DE ESTE DOCUMENTO

Explicar las diferencias entre:
- **Presupuesto Anterior:** `presupuesto_actualizado.md` (USD 48,000)
- **Presupuesto Nuevo:** `PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md` (USD 8,850)

---

## DIFERENCIAS PRINCIPALES

### 1. ENFOQUE Y ALCANCE

| Aspecto | Presupuesto Anterior | Presupuesto Nuevo |
|---------|---------------------|-------------------|
| **Perspectiva** | Propuesta completa de Aunergia (equipo completo) | Cotización personal Juan Manuel Bigi |
| **Roles incluidos** | PM, Arquitecto, QA, Desarrolladores, Analistas | Solo Desarrollador (JM Bigi) |
| **Estructura** | Consultoría integral con gobernanza | Recurso técnico puntual |
| **Tipo de documento** | Propuesta corporativa formal | Presupuesto freelance |

### 2. DESGLOSE DE COSTOS

#### Presupuesto Anterior (USD 48,000):
```
Fase 0: USD 11,520 (120h)
├── PM/Gobernanza: 40h × $110 = $4,400
├── Arquitecto Datos: 32h × $140 = $4,480
├── Especialista SAP (Lucía): 28h × $60 = $1,680
└── QA/Compliance: 12h × $80 = $960

Fase 1: USD 20,260 (206h)
├── Arquitecto Datos: 64h × $140 = $8,960
├── Desarrollador ETL/SAP: 90h × $70 = $6,300
├── PM/Gobernanza: 28h × $110 = $3,080
└── QA Datos: 24h × $80 = $1,920

Fase 2: USD 16,220 (168h)
├── Desarrollador Power BI: 60h × $95 = $5,700
├── Arquitecto Datos: 18h × $140 = $2,520
├── Analista Negocio: 40h × $85 = $3,400
├── PM/Gobernanza: 20h × $110 = $2,200
└── QA/UAT: 30h × $80 = $2,400

TOTAL: 494h, USD 48,000
```

#### Presupuesto Nuevo (USD 8,850):
```
Elaboración presupuesto: 10h × $25 = $250
Fase 0: 40h × $25 = $1,000
Fase 1: 156h × $25 = $3,900
Fase 2: 148h × $25 = $3,700

TOTAL: 354h, USD 8,850
```

### 3. ROLES NO INCLUIDOS EN PRESUPUESTO NUEVO

Los siguientes roles del presupuesto anterior NO están en el nuevo presupuesto porque los asume Aunergia o Elanco:

| Rol | Horas (anterior) | Costo (anterior) | Responsable ahora |
|-----|------------------|------------------|-------------------|
| PM/Gobernanza | 88h | USD 9,680 | Aunergia (Linda López) |
| Arquitecto Datos (Senior) | 114h | USD 15,960 | Aunergia o interno Elanco |
| QA/Compliance | 66h | USD 5,280 | Aunergia |
| Analista Negocio | 40h | USD 3,400 | Interno Elanco |
| Especialista SAP (Lucía) | 80h | USD 5,520 | Aunergia (factura directa) |
| **TOTAL ROLES NO INCLUIDOS** | **388h** | **USD 39,840** | **Otros** |

---

## JUSTIFICACIÓN DEL PRESUPUESTO NUEVO

### ¿Por qué USD 8,850 en vez de USD 48,000?

**El presupuesto nuevo responde a la pregunta real de Lucía en el audio:**

> *"pásamelo y le decimos a ver si quiere que avancemos con vos y si no que ellos busquen algún recurso que les pueda resolver esto"*

**Interpretación:**
- Lucía quiere saber **cuánto cuesta Juan Manuel Bigi específicamente**
- No quiere una propuesta completa de Aunergia
- Quiere tener la opción de "avanzar con vos" o buscar otro recurso

### ¿Qué incluye el presupuesto de USD 8,850?

✅ **Trabajo técnico directo de Juan Manuel Bigi:**
1. Análisis técnico de arquitectura BigQuery
2. Desarrollo de 8 pipelines SAP → BigQuery
3. Configuración de infraestructura Data Lake
4. Desarrollo de 4-6 dashboards Power BI
5. Configuración de Row-Level Security
6. Testing y validación
7. Documentación técnica
8. Soporte durante implementación

❌ **NO incluye (debe gestionar Aunergia o Elanco):**
- Project Management
- Arquitectura empresarial (solo técnica)
- QA formal/Compliance
- Análisis de negocio profundo
- Horas de Lucía Rodríguez
- Consultoría ABAP externa

---

## ANÁLISIS DE HORAS POR FASE

### FASE 0: Due Diligence

| Actividad | Presup. Anterior | Presup. Nuevo | Diferencia | Explicación |
|-----------|------------------|---------------|------------|-------------|
| Coordinación permisos | 40h (varios roles) | 20h (Lucía) | -20h | Lucía gestiona, JM Bigi no participa en burocracia |
| Análisis técnico | 32h (Arquitecto) | 24h (JM Bigi) | -8h | Foco solo en BigQuery/Power BI, no arquitectura empresarial |
| Workshops | 28h (varios) | 12h (JM Bigi) | -16h | Solo participación técnica, no facilitación |
| Documentación | 12h (PM) | 16h (JM Bigi) | +4h | JM Bigi hace su propia documentación técnica |
| Validación TI | 8h (Lucía) | 8h (Lucía) | 0h | Lucía lo hace, no JM Bigi |
| **TOTAL FASE 0** | **120h** | **80h** | **-40h** | **-33%** |

**Horas JM Bigi en Fase 0:** 40h (50% del total)  
**Horas otros (Lucía, stakeholders):** 40h (gestionan Aunergia/Elanco)

### FASE 1: Automatización

| Actividad | Presup. Anterior | Presup. Nuevo | Diferencia | Explicación |
|-----------|------------------|---------------|------------|-------------|
| Desarrollo pipelines | 90h (Lucía+ABAP) | 156h (JM Bigi) | +66h | JM Bigi hace TODO el desarrollo técnico |
| Arquitectura datos | 64h (Arquitecto) | 16h (JM Bigi) | -48h | Solo configuración, no diseño empresarial |
| PM/Coordinación | 28h (PM) | 0h | -28h | No incluido (gestiona Aunergia) |
| QA | 24h (QA) | 24h (JM+Lucía) | 0h | Incluido en horas desarrollo |
| Ajustes/Issues | 0h | 16h (Lucía) | +16h | Realista según issues reportados |
| **TOTAL FASE 1** | **206h** | **204h** | **-2h** | **-1%** |

**Horas JM Bigi en Fase 1:** 156h (76% del total)  
**Horas Lucía:** 40h (gestiona Aunergia)  
**Horas ABAP externo:** 8h (contingencia, gestiona Aunergia)

### FASE 2: Power BI

| Actividad | Presup. Anterior | Presup. Nuevo | Diferencia | Explicación |
|-----------|------------------|---------------|------------|-------------|
| Desarrollo Power BI | 60h (Dev BI) | 148h (JM Bigi) | +88h | JM Bigi hace modelo + dashboards + RLS + ajustes |
| Arquitectura datos | 18h (Arquitecto) | 0h | -18h | Ya definido en Fase 1 |
| Analista Negocio | 40h (Analista) | 0h | -40h | Stakeholders de Elanco lo hacen |
| PM/Coordinación | 20h (PM) | 0h | -20h | No incluido (gestiona Aunergia) |
| QA/UAT | 30h (QA) | 16h (JM Bigi) | -14h | Incluido en horas desarrollo |
| **TOTAL FASE 2** | **168h** | **160h** | **-8h** | **-5%** |

**Horas JM Bigi en Fase 2:** 148h (93% del total)  
**Horas Lucía:** 12h (capacitación, gestiona Aunergia)

---

## COMPARATIVA DE TARIFAS

### Tarifas presupuesto anterior:
- PM/Gobernanza: USD 110/h
- Arquitecto Datos: USD 140/h
- Desarrollador Power BI: USD 95/h
- Analista Negocio: USD 85/h
- Consultor ABAP: USD 85/h
- QA: USD 80/h
- Desarrollador ETL: USD 70/h
- Especialista SAP (Lucía): USD 60/h

**Promedio ponderado:** USD 97/h

### Tarifa presupuesto nuevo:
- Juan Manuel Bigi: USD 25/h

**Diferencia:** -74% vs. promedio anterior

---

## VENTAJAS Y DESVENTAJAS DE CADA ENFOQUE

### PRESUPUESTO ANTERIOR (USD 48,000)

#### ✅ Ventajas:
1. **Propuesta completa "llave en mano"**
2. **Incluye gobernanza y PM profesional**
3. **QA y compliance formales**
4. **Múltiples especialistas**
5. **Menor riesgo para Elanco (Aunergia se responsabiliza de todo)**
6. **Incluye contingencias y overhead**

#### ❌ Desventajas:
1. **Costo 5.4x mayor**
2. **Estructura más pesada**
3. **Posible sobre-ingeniería para un MVP**
4. **Más coordinación y burocracia**

### PRESUPUESTO NUEVO (USD 8,850)

#### ✅ Ventajas:
1. **Costo 81% menor**
2. **Enfoque lean y ágil**
3. **Ejecución directa sin intermediarios**
4. **Flexibilidad para ajustes**
5. **Perfil técnico específico (BigQuery + Power BI)**
6. **Ideal para MVP y validación rápida**

#### ❌ Desventajas:
1. **Requiere que Aunergia gestione PM y coordinación**
2. **No incluye QA formal externo**
3. **Menor cobertura de riesgos**
4. **Depende de disponibilidad de un solo recurso**
5. **Requiere mayor involucramiento de Elanco**

---

## RECOMENDACIÓN

### Opción 1: Presupuesto Completo (USD 48,000)
**Cuándo elegirlo:**
- Elanco quiere una solución "llave en mano"
- No tienen capacidad interna de PM
- Requieren QA y compliance formales
- Prefieren minimizar riesgos
- Presupuesto aprobado sin restricciones

### Opción 2: Presupuesto JM Bigi (USD 8,850)
**Cuándo elegirlo:**
- Presupuesto ajustado
- Aunergia puede gestionar PM y coordinación
- Quieren validar un MVP rápido
- Tienen capacidad interna de QA
- Buscan flexibilidad y agilidad

### Opción 3: Híbrido (USD ~25,000-30,000)
**Propuesta:**
- JM Bigi: USD 8,850 (desarrollo técnico)
- Lucía Rodríguez: 80h × USD 60/h = USD 4,800 (SAP + coordinación)
- PM Aunergia: 40h × USD 110/h = USD 4,400 (gobernanza mínima)
- QA: 30h × USD 80/h = USD 2,400 (validación formal)
- ABAP: USD 1,600 (contingencia)
- Overhead 10%: USD 2,205

**TOTAL HÍBRIDO: USD 24,255**

---

## VALIDACIÓN DE REALISMO

### ¿Es realista que JM Bigi haga 156h de desarrollo en Fase 1?

**Análisis:**
- 6-8 semanas = 42-56 días
- 156h ÷ 50 días = 3.1h/día promedio
- Part-time 20h/semana = **razonable ✅**

**Desglose Fase 1 (156h JM Bigi):**
- Transacciones estándar: 84h (6 trans × 14h)
- Transacción custom ZLEL008: 24h (sin ABAP)
- Transacción CO KSB1: 20h
- Configuración BigQuery: 16h
- Testing: 12h (con Lucía adicionales 12h)
- Documentación: 12h
- **TOTAL: 156h** ✅

### ¿Es realista que JM Bigi haga 148h de Power BI en Fase 2?

**Análisis:**
- 4-5 semanas = 28-35 días
- 148h ÷ 32 días = 4.6h/día promedio
- Part-time 20h/semana = **razonable ✅**

**Desglose Fase 2 (148h JM Bigi):**
- Modelo datos: 32h
- Desarrollo 6 dashboards: 60h
- RLS configuración: 12h
- Testing UAT: 16h
- Documentación: 12h
- Ajustes post-UAT: 16h
- **TOTAL: 148h** ✅

---

## CONCLUSIÓN

**Ambos presupuestos son válidos, pero responden a preguntas diferentes:**

1. **Presupuesto Anterior (USD 48,000):**
   - Pregunta: *"¿Cuánto cuesta que Aunergia haga todo el proyecto?"*
   - Respuesta: USD 48,000 con equipo completo

2. **Presupuesto Nuevo (USD 8,850):**
   - Pregunta: *"¿Cuánto cobras vos (JMB) por el trabajo técnico?"*
   - Respuesta: USD 8,850 por 354h de desarrollo puro

**La elección depende de:**
- Presupuesto disponible
- Capacidad interna de Elanco/Aunergia
- Nivel de riesgo aceptable
- Velocidad requerida
- Complejidad de governance

---

**Elaborado por:** Juan Manuel Bigi  
**Fecha:** 10 de octubre de 2025  
**Documento complementario a:** PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md
