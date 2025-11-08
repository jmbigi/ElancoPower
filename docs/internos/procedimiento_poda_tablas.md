# Procedimiento de Poda de Tablas (S/4HANA → BigQuery)

Fecha: 8-nov-2025
Estado: En progreso
Responsables: Consultor BI (líder), Funcional SAP, TI Global

## Objetivo
Reducir el número de tablas a replicar manteniendo cobertura funcional y KPIs comprometidos, minimizando costo y complejidad.

## Definiciones
- core: imprescindible para KPIs y modelos de Fase 2
- derivada: aporta valor de UX o performance; reemplazable por vistas o joins
- condicional: solo si se requiere el caso de uso (ej. textos STXL)
- obsoleta: sustituida por ACDOCA u otra tabla consolidante

## Pasos
1) Consolidación FI/CO en ACDOCA/ACDOCA_T
   - Excluir BSEG, FAGLFLEXA, COEP
   - Validar joins con BKPF y llaves (RLDNR, BUKRS, GJAHR, BELNR, DOCLN)
2) SD/MM mínimos
   - VA05: VBAK, VBAP, VBUK, VBUP (+ MARA/MAKT)
   - Compras/Movimientos: EKKO, EKPO, MKPF, MSEG (+ MBEW, MARD)
3) Maestros
   - BP: BUT000; clientes/proveedores KNA1/LFA1 si faltan atributos
   - Materiales: MARA + (MAKT opcional)
4) Precios
   - KONV/KONP como derivadas; incluir solo si casos de pricing lo exigen
5) Textos
   - STXL como condicional (declustering)
6) Custom Z
   - Identificar tablas Z* subyacentes (ZLEL008, ZVEL015)
   - Validar impacto en core

## Matriz de Decisión (por tabla)
- ¿Aporta campo requerido por KPI de los 12 dashboards?
- ¿Existe sustituto en ACDOCA/ACDOCA_T?
- ¿Se usa solo para etiquetas (UX)?
- ¿Impacta performance/costo de forma significativa?

## Entregables
- mapeo_transacciones_tablas_detallado.csv (actualizado)
- Informe de poda con conteos: core / derivadas / condicionales / obsoletas
- Pull request de actualización del Anexo Técnico (sección "Justificación de reducción")

## Nota de Consistencia
Hasta completar validación, el rango canónico vigente se mantiene en ~76–85. Cualquier cifra 35–65 se considera estimación exploratoria.
