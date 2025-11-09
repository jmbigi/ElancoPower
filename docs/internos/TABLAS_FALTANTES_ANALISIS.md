# Análisis de Tablas Faltantes por Transacción SAP

**Fecha:** 9 de noviembre de 2025  
**Estado:** Documento de análisis técnico para Fase 0

---

## Resumen Ejecutivo

### Estado Actual del Mapeo

- ✅ **30 tablas únicas** ya identificadas en el mapeo
- ✅ **Todas las tablas CORE** están cubiertas (0 faltantes)
- ⚠️ **22 tablas IMPORTANTES** no están documentadas
- 📊 **Rango actual documentado (previo):** 24–31 tablas (histórico)
- ✅ **Nuevo rango canónico:** 32–38 tablas (32 núcleo extendido + hasta 6 condicionales iniciales)
- 📊 **Rango potencial con IMPORTANTES:** 52 tablas

### Criterio de Evaluación

**Buenas noticias:** Todas las tablas **CORE** (absolutamente necesarias) ya están identificadas.

**Área de mejora:** Hay 22 tablas **IMPORTANTES** que complementan la funcionalidad pero que actualmente no están en el mapeo.

---

## 1. Tablas Faltantes por Categoría Funcional

### 1.1. Textos y Descripciones (5 tablas)

Estas tablas contienen descripciones legibles para usuarios:

| Tabla | Descripción | Transacciones Afectadas | Criticidad |
|-------|-------------|------------------------|------------|
| **SKAT** | Textos plan cuentas (GL) | FAGLL03, FB03, F.08, F.01 | Alta |
| **CSKT** | Textos centros de costo | KSB1 | Media |
| **CSKB** | Datos adicionales CC | KSB1 | Media |
| **CEPC** | Maestro centros beneficio | FAGLL03, F.08, F.01 | Media |
| **CEPCT** | Textos centros beneficio | FAGLL03 | Baja |

**Impacto sin ellas:** Los reportes mostrarían códigos técnicos (ej. "600100") en lugar de descripciones ("Gastos de Personal").

**Recomendación:** Incluir al menos **SKAT** (crítico para FI), considerar **CSKT** para CO.

---

### 1.2. Datos Maestros Extendidos de Clientes/Proveedores (6 tablas)

Datos de clientes y proveedores más allá de lo básico:

| Tabla | Descripción | Transacciones Afectadas | Criticidad |
|-------|-------------|------------------------|------------|
| **KNB1** | Cliente por sociedad (datos contables) | VA05, XD03, FBL5N | Alta |
| **KNVV** | Cliente por área ventas | VA05, XD03 | Alta |
| **LFB1** | Proveedor por sociedad (datos contables) | XK03, FBL1N | Alta |
| **LFM1** | Proveedor por organización compras | XK03 | Media |
| **ADRC** | Direcciones (clientes/proveedores) | XD03, XK03 | Media |
| **TKA01** | Áreas de controlling | KSB1 | Media |

**Impacto sin ellas:** 
- No se podrían filtrar por condiciones de pago, grupos de cuentas
- Faltarían datos específicos de área de ventas (canal, sector)
- No habría información de direcciones de entrega/facturación

**Recomendación:** Incluir **KNB1**, **KNVV**, **LFB1** si se requiere análisis detallado de clientes/proveedores.

---

### 1.3. Compras - Programaciones y Solicitudes (3 tablas)

Para análisis detallado de compras:

| Tabla | Descripción | Transacciones Afectadas | Criticidad |
|-------|-------------|------------------------|------------|
| **EKET** | Programación entregas OC | ME2L, ME23N | Alta |
| **EKES** | Confirmaciones proveedor | ME23N | Media |
| **EBAN** | Solicitudes de compra | ME2L | Media |

**Impacto sin ellas:**
- No se pueden analizar fechas de entrega programadas vs. confirmadas
- Falta trazabilidad desde solicitud → pedido

**Recomendación:** Incluir **EKET** si se requieren KPIs de cumplimiento de entregas de proveedores.

---

### 1.4. Costos Estándar y Material Ledger (3 tablas)

Para análisis detallado de costos MM60:

| Tabla | Descripción | Transacciones Afectadas | Criticidad |
|-------|-------------|------------------------|------------|
| **CKMLCR** | Componentes costo (ML actual) | MM60 | Alta |
| **CKMLHD** | Cabecera ML | MM60 | Media |
| **CKMLPP** | Periodo ML | MM60 | Media |

**Impacto sin ellas:**
- No se puede desglosar el costo estándar en componentes (material, MOD, CIF, etc.)
- Solo se vería costo total desde MBEW

**Recomendación:** Incluir si se requiere análisis de **composición de costos** (ej. variación material vs. MOD).

---

### 1.5. Pricing y Condiciones (2 tablas)

Para análisis detallado de precios:

| Tabla | Descripción | Transacciones Afectadas | Criticidad |
|-------|-------------|------------------------|------------|
| **KONP** | Registros de condición (pricing) | KE24, ZVEL015 | Media |
| **A005** | Tipos de condición por cliente/material | ZVEL015 | Media |

**Impacto sin ellas:**
- KONV (ya incluida) da el resultado final
- Estas dan el detalle histórico y configuración de pricing

**Recomendación:** **KONP** ya está en lista condicional. A005 solo si se necesita análisis profundo de estrategia pricing.

---

### 1.6. Organizaciones y Centros (3 tablas)

Tablas de configuración/maestros de localización:

| Tabla | Descripción | Transacciones Afectadas | Criticidad |
|-------|-------------|------------------------|------------|
| **T001W** | Centros (plantas) | VA05, ZLEL008, MB59 | Alta |
| **T001L** | Almacenes | ZLEL008, MB59 | Media |
| **T156** | Clases de movimiento | MB59 | Media |

**Impacto sin ellas:**
- Sin T001W: no hay nombres de centros, solo códigos
- Sin T001L: no hay nombres de almacenes
- Sin T156: no hay descripciones de movimientos (101=entrada, 261=consumo, etc.)

**Recomendación:** Incluir **T001W** (crítico para multi-planta) y **T156** (descripciones de movimientos).

---

## 2. Priorización Recomendada

### 🔴 CRÍTICAS - Incluir en Fase 1 (8 tablas)

Estas 8 tablas son las más importantes de las 22 faltantes:

1. **SKAT** - Textos de cuentas GL (FI)
2. **KNB1** - Clientes por sociedad (SD/FI)
3. **KNVV** - Clientes por área ventas (SD)
4. **LFB1** - Proveedores por sociedad (MM/FI)
5. **T001W** - Centros/plantas
6. **EKET** - Programación entregas OC
7. **CKMLCR** - Componentes de costo (si MM60 es prioridad)
8. **CSKT** - Textos centros de costo (CO)

**Nuevo total con críticas:** 30 + 8 = **38 tablas**

---

### 🟡 IMPORTANTES - Evaluar en Fase 0 (7 tablas)

Dependen de casos de uso específicos:

9. **KONP** - Detalle de condiciones pricing (ya está como condicional)
10. **LFM1** - Proveedores por org. compras
11. **ADRC** - Direcciones
12. **T001L** - Almacenes
13. **T156** - Clases de movimiento
14. **EKES** - Confirmaciones proveedor
15. **EBAN** - Solicitudes de compra

**Total con importantes:** 38 + 7 = **45 tablas**

---

### 🟢 OPCIONALES - Diferir a fases posteriores (7 tablas)

Menor impacto o casos muy específicos:

16. **CEPC** - Maestro centros beneficio
17. **CEPCT** - Textos centros beneficio
18. **CSKB** - Datos adicionales CC
19. **CKMLHD** - Cabecera Material Ledger
20. **CKMLPP** - Periodo Material Ledger
21. **A005** - Condiciones cliente/material
22. **TKA01** - Áreas controlling

---

## 3. Análisis por Transacción

### Transacciones SIN tablas faltantes importantes ✅

Estas ya tienen cobertura completa de tablas importantes:

- **FBL1N** - Partidas proveedores
- **FBL5N** - Partidas clientes
- **KE24** - CO-PA (si es account-based)
- **MB5B** - Stock por material

---

### Transacciones con 1 tabla importante faltante ⚠️

| Transacción | Tabla Faltante | Acción Recomendada |
|-------------|----------------|-------------------|
| **F.08** | SKAT | ✅ Incluir |
| **F.01** | SKAT | ✅ Incluir |
| **MB59** | T156 | ✅ Incluir |

---

### Transacciones con 2 tablas importantes faltantes ⚠️

| Transacción | Tablas Faltantes | Acción Recomendada |
|-------------|------------------|-------------------|
| **ME2L** | EBAN, EKET | ✅ Incluir EKET |
| **ME23N** | EKET, EKES | ✅ Incluir EKET |
| **ZLEL008** | T001W, T001L | ✅ Incluir T001W |
| **ZVEL015** | KONP, A005 | ⏳ KONP ya condicional |

---

### Transacciones con 3+ tablas importantes faltantes ⚠️⚠️

| Transacción | Tablas Faltantes | Acción Recomendada |
|-------------|------------------|-------------------|
| **FAGLL03** | SKAT, CEPC, CEPCT | ✅ Incluir SKAT |
| **KSB1** | CSKT, CSKB, TKA01 | ✅ Incluir CSKT |
| **VA05** | KNB1, KNVV, T001W | ✅ Incluir las 3 |
| **MM60** | CKMLCR, CKMLHD, CKMLPP | 🔍 Evaluar si se requiere desglose |
| **XD03** | KNB1, KNVV, ADRC | ✅ Incluir KNB1, KNVV |
| **XK03** | LFB1, LFM1, ADRC | ✅ Incluir LFB1 |

---

## 4. Impacto en el Rango de Tablas

### Escenario 1: Núcleo Extendido ✅
- **32 tablas** (24 técnicas + 8 semánticas críticas)
- Cobertura: Básica (todas las CORE cubiertas)
- Riesgo: Reportes con códigos técnicos, falta de dimensiones clave

### Escenario 2: Núcleo + Condicionales Parciales 🎯 RECOMENDADO
- **32–38 tablas** (activando 0–6 condicionales según KPI)
- Cobertura: Completa para dashboards funcionales
- Riesgo: Bajo, se cubren los principales casos de uso

### Escenario 3: Núcleo + Todas las Condicionales
- **39 tablas** (32 núcleo + 7 condicionales)
- Cobertura: Extendida con casos de uso avanzados
- Riesgo: Muy bajo, máxima flexibilidad analítica

### Escenario 4: Cobertura Extendida Post-MVP
- **>39 tablas** (activando opcionales + enriquecedores futuros)
- Cobertura: Exhaustiva
- Riesgo: Mínimo, pero puede ser over-engineering

---

## 5. Recomendación Final

### Para Fase 0 (Workshop Semana 2)

**Acción 1:** Validar con el negocio la necesidad de las **8 tablas CRÍTICAS**:

```
✅ SKAT   - ¿Los reportes FI necesitan nombres de cuentas o solo códigos?
✅ KNB1   - ¿Se analizará por condiciones de pago, grupos contables?
✅ KNVV   - ¿Se requiere filtrar por canal, sector, oficina ventas?
✅ LFB1   - ¿Se analizará AP por condiciones de pago?
✅ T001W  - ¿Sistema multi-planta requiere nombres de centros?
✅ EKET   - ¿KPIs de cumplimiento entregas proveedores?
✅ CKMLCR - ¿Análisis de componentes de costo (MM60)?
✅ CSKT   - ¿Reportes CO necesitan nombres de centros costo?
```

**Acción 2:** Actualizar el rango canónico definitivo:
- De: **24–31 tablas (histórico)**
- A: **32–38 tablas (vigente)**

**Acción 3:** Validar disponibilidad en BigQuery con TI Global para las 8 críticas.

---

## 6. Checklist de Validación Fase 0

Para cada transacción priorizada:

- [ ] Confirmar tablas CORE disponibles en BigQuery
- [ ] Evaluar necesidad de tablas IMPORTANTES faltantes
- [ ] Documentar decisión (incluir/excluir) con justificación
- [ ] Estimar volumen de datos para tablas nuevas
- [ ] Definir estrategia de particionamiento/clustering
- [ ] Actualizar mapeo detallado CSV
- [ ] Actualizar documentos de alcance

---

## 7. Tablas que NO Faltan (Ya Cubiertas)

Para contexto, estas tablas importantes ya están en el mapeo:

✅ ACDOCA, ACDOCA_T (Universal Journal - corazón de FI/CO)  
✅ VBAK, VBAP, VBUK, VBUP (SD completo)  
✅ EKKO, EKPO (MM compras básico)  
✅ MKPF, MSEG (movimientos materiales)  
✅ MARA, MAKT (maestro materiales con textos)  
✅ KNA1, LFA1, BUT000 (maestros cliente/proveedor básicos)  
✅ MBEW, MARC, MARD (valoración, material x planta, stock)  
✅ AUFK, CSKS, CSKA (órdenes CO, centros costo, elementos costo)  
✅ SKA1, BKPF, T001 (plan cuentas, docs FI, sociedades)  

---

## Anexo: Resumen Visual

```
┌─────────────────────────────────────────────────────────────┐
│  COBERTURA ACTUAL DE TABLAS SAP                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✅ CORE (todas cubiertas)           0 faltantes            │
│  ⚠️  IMPORTANTES (cubiertas parcial)  22 faltantes          │
│  ℹ️  OPCIONALES (no evaluadas)       ~40+ faltantes        │
│                                                             │
│  ESTADO ACTUAL:   [████████░░] 30 tablas                    │
│  CON CRÍTICAS:    [███████████] 38 tablas ⭐ RECOMENDADO    │
│  CON IMPORTANTES: [████████████] 45 tablas                  │
│  COBERTURA TOTAL: [█████████████] 52 tablas                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

**Elaborado por:** Análisis técnico basado en conocimiento estándar SAP S/4HANA  
**Para:** Fase 0 - Workshop de Priorización  
**Próximo paso:** Validar con negocio y TI Global durante Semana 2 de Fase 0

