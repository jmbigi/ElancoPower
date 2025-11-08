# RESUMEN EJECUTIVO - PRESUPUESTO ELANCO POWER

**Para:** Funcional SAP (Aunergia)  
**De:** Consultor BI  
**Fecha:** 10 de octubre de 2025  
**Asunto:** Presupuesto personal para proyecto Elanco Power

---

## 🎯 RESPUESTA A TU CONSULTA

En tu audio del 09-oct-2025 me pediste:

> *"pásamelo y le decimos a ver si quiere que avancemos con vos y si no que ellos busquen algún recurso que les pueda resolver esto"*

Aquí está mi presupuesto personal para el trabajo técnico que puedo aportar.

---

## 💰 ESFUERZO CONSULTOR BI

### Resumen:
- **Horas totales:** 354 horas
- **Duración:** 13-17 semanas (~4 meses)
- **Disponibilidad:** Part-time (20-25h/semana)

### Desglose por fase:

| Fase | Duración | Horas |
|------|----------|-------|
| **Elaboración presupuesto** | - | 10h |
| **Fase 0 - Due Diligence** | 3-4 semanas | 40h |
| **Fase 1 - Automatización** | 6-8 semanas | 156h |
| **Fase 2 - Power BI** | 4-5 semanas | 148h |
| **TOTAL** | **~4 meses** | **354h** |

---

## 📋 QUÉ INCLUYE MI TRABAJO

### ✅ FASE 0: Due Diligence (40h)
- Análisis técnico de arquitectura BigQuery
- Workshop con Finanzas/Supply para priorizar transacciones
- Documentación de backlog técnico
- Validación de viabilidad técnica
- Plan de extracción por módulo SAP

### ✅ FASE 1: Automatización SAP → BigQuery (156h)
- Desarrollo de **8 pipelines** para transacciones prioritarias:
  - VA05, ZLEL008, KSB1, FAGLL03 (Prioridad 1)
  - KE24, FB03, F.08, F.01 (Prioridad 2 si da el tiempo)
- Configuración infraestructura BigQuery
- Historización de datos (24 meses)
- Testing y validación de calidad
- Documentación técnica completa

### ✅ FASE 2: Power BI (148h)
- Modelo de datos Power BI (conexión BigQuery)
- Desarrollo de **12 dashboards:**
  1. Dashboard Financiero General
  2. Dashboard Ventas
  3. Dashboard Inventario
  4. Dashboard OPEX
  5. Dashboard Supply Chain
  6. Dashboard Compras
  7. Dashboard Rentabilidad
  8. Dashboard Cuentas por Pagar
  9. Dashboard Cuentas por Cobrar
  10. Dashboard Controlling
  11. Dashboard Ejecutivo
  12. Dashboard Regional Estadístico
- Configuración Row-Level Security (RLS) por país
- Testing con usuarios (UAT)
- Documentación para usuarios
- Ajustes post-UAT

---

## ❌ QUÉ NO INCLUYE (lo gestiona Aunergia o Elanco)

- Project Management y gobernanza
- Horas del Funcional SAP (las factura Aunergia)
- QA formal / Compliance corporativo
- Consultoría ABAP externa (si es necesario)
- Análisis de negocio profundo
- Capacitación avanzada (solo capacitación básica incluida)

---

## 🧩 QUÉ PROBLEMAS RESUELVO

Según el correo de **David Saboya** (09-oct-2025), Elanco tiene estos issues:

### ✅ Issue #1: Permisos SAP insuficientes
**Mi aporte:** No gestiono permisos (eso es del Funcional SAP), pero diseño la arquitectura para trabajar con los permisos que se obtengan.

### ✅ Issue #2: Tablas no disponibles en BigQuery
**Mi aporte:** Identifico qué tablas faltan, preparo los tickets técnicos y diseño el workaround mientras se aprueban.

### ✅ Issue #3: Posibles limitaciones BigQuery
**Mi aporte:** Valido técnicamente si es limitación real o falta de conocimiento. Si BigQuery no funciona, propongo migración a Azure.

---

## 🛠️ MI PERFIL TÉCNICO

**Experiencia:**
- ✅ Desarrollo en BigQuery (SQL avanzado, optimización de queries)
- ✅ Power BI (modelos tabulares, DAX, visualizaciones)
- ✅ Integración SAP → Data Lakes
- ✅ Arquitecturas de datos (diseño ETL/ELT)
- ✅ Row-Level Security y gobernanza de datos

**Herramientas confirmadas para este proyecto:**
- Google BigQuery + BigQuery Studio
- Microsoft Power BI
- ODBC Simba (para conectores)
- Git (versionado de código)

---

## 🗓️ CRONOGRAMA PROPUESTO

| Fecha | Hito |
|-------|------|
| **14-oct-2025** | Aprobación de presupuesto |
| **16-oct-2025** | Kick-off Fase 0 |
| **07-nov-2025** | Go/No-Go Fase 1 (solo si permisos ok) |
| **10-nov-2025** | Fin Fase 0 |
| **05-ene-2026** | Fin Fase 1 |
| **09-feb-2026** | Fin Fase 2 |

**Total: ~4 meses** (condicionado a resolución de issues de permisos)

---

## ⚠️ CONDICIONES Y SUPUESTOS

### Para que pueda arrancar necesito:
1. ✅ Que el Funcional SAP tenga permisos SAP completos (Ticket SAP-48219)
2. ✅ Que las tablas críticas estén en BigQuery o tengamos plan B
3. ✅ Acceso a dataset casa_bi en BigQuery (ya confirmado)
4. ✅ Backlog priorizado (lo hacemos en Fase 0)

### Forma de pago propuesta:
- 30% al aprobar Fase 0
- 40% al completar Fase 1
- 30% al completar Fase 2

### Facturo a:
- Aunergia (ustedes me pagan, ustedes facturan a Elanco)
- O directamente a Elanco (si ustedes prefieren)

---

## 📊 COMPARATIVA (para tu información)

Tu presupuesto completo de Aunergia incluye equipo completo con todas las horas y roles necesarios.

Mi presupuesto es solo para el trabajo técnico de desarrollo (354 horas).

### ¿Por qué la diferencia?
- El presupuesto completo incluye PM, Arquitectos Senior, QA, Analistas, tu tiempo, overhead
- Mi presupuesto es solo mi trabajo de desarrollo técnico
- Los dos son correctos, depende de qué modelo quieran usar

### Opciones para ustedes:
1. **Propuesta completa Aunergia:** Equipo completo (llave en mano)
2. **Solo yo + ustedes coordinan:** Mis 354h + sus costos internos
3. **Híbrido:** Consultor BI + Funcional SAP + PM mínimo + QA

---

## 📄 DOCUMENTOS ENTREGADOS

He creado 3 documentos en la carpeta del proyecto:

1. **`PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md`**
   - Mi presupuesto completo (29 páginas)
   - Incluye justificación de cada hora
   - Basado solo en fuentes verificables

2. **`ANALISIS_DIFERENCIAS_PRESUPUESTOS.md`**
   - Comparativa con presupuesto de USD 48,000
   - Explica por qué la diferencia
   - Recomendaciones según contexto

3. **`README.md`**
   - Índice de toda la carpeta
   - Cómo navegar los documentos
   - Resumen del proyecto

---

## 🤝 PRÓXIMOS PASOS

### Si quieren avanzar conmigo:
1. **Hoy (10-oct):** Revisen mi presupuesto
2. **11-oct:** Me confirman si avanzan
3. **14-oct:** Aprobación formal con Elanco
4. **16-oct:** Kick-off Fase 0

### Si prefieren buscar otro recurso:
- No hay problema, los documentos quedan para referencia
- Cobro solo las 10h de elaboración del presupuesto

---

## 💬 MIS DUDAS / CONSULTAS

1. **¿Quién gestiona el PM del proyecto?**
   - ¿Lo hace Linda/Aunergia o esperan que yo lo haga?
   - Mi presupuesto asume que ustedes coordinan

2. **¿Las horas de consultoría ABAP las gestiona Aunergia?**
   - Estimé 8-16h para ZLEL008
   - ¿Ustedes lo contratan o lo incluyo en mi presupuesto?

3. **¿Facturación directa o a través de Aunergia?**
   - ¿Prefieren que facture a Aunergia y ustedes a Elanco?
   - ¿O directamente a Elanco?

4. **¿Disponibilidad del Funcional SAP en cada fase?**
   - Estimé 28h Fase 0, 40h Fase 1, 12h Fase 2
   - ¿Es realista con su agenda?

---

## 📞 CONTACTO

**Consultor BI**
- Email: [pending - confirmar]
- Disponibilidad: Part-time 20-25h/semana
- Inicio disponible: 14-oct-2025

---

## ✅ CONCLUSIÓN

**Mi esfuerzo: 354 horas de desarrollo técnico.**

Incluye:
- ✅ 18 transacciones SAP → BigQuery
- ✅ 12 dashboards Power BI
- ✅ Documentación completa
- ✅ Testing y validación
- ✅ Soporte durante implementación

No incluye:
- ❌ PM y gobernanza (ustedes)
- ❌ Horas del Funcional SAP (ustedes)
- ❌ QA formal externo (ustedes o Elanco)
- ❌ Consultoría ABAP (estimar aparte)

**¿Avanzamos?** Espero tu confirmación.

Saludos,  
**Consultor BI**

---

**Fecha:** 10 de octubre de 2025  
**Validez:** 30 días  
**Documentos adjuntos:** Ver carpeta ElancoPower/
