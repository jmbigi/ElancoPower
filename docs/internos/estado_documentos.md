# Estado de Documentos y Fuentes Canónicas

Este archivo consolida el **estado** (vigente / histórico / auxiliar) de los principales documentos del repositorio para facilitar revisiones de consistencia sin alterar los archivos originales en `inputs/`.

## 1. Principios

- No se modifica nada dentro de `inputs/` (fuentes históricas recibidas de Elanco)
- Cada documento "vigente" debe declarar explícitamente si reemplaza una versión previa
- El alcance funcional (18 transacciones) y el rango de tablas (~76-85) tienen UNA sola fuente canónica

## 2. Fuentes Canónicas Actualizadas

| Dominio | Documento | Rol | Comentario |
|---------|-----------|-----|------------|
| Alcance Transacciones | `docs/propuesta_final/03_TRANSACCIONES_SAP_INCLUIDAS.md` | Vigente (Canónico) | Define las 18 transacciones finales; explica normalización 22→18 |
| Tablas Estimadas | `docs/propuesta_final/ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md` | Vigente (Canónico) | Rango consolidado ~76-85 tablas |
| Esfuerzo & Costos | `docs/propuesta_final/08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md` | Vigente (Canónico) | Total 1,590h consistente |
| Cronograma Global | `docs/propuesta_final/09_CRONOGRAMA_SEMANAL.md` | Vigente (Canónico) | 42 semanas totales |
| Fase 1 (Detalle Data Lake) | `docs/propuesta_final/05_FASE_1_CONSTRUCCION_DATA_LAKE.md` | Vigente | Incluye aclaración semanas internas vs globales |
| Riesgos & Supuestos | `docs/propuesta_final/11_RIESGOS_Y_SUPUESTOS.md` | Vigente | Go/No-Go ≥12 transacciones disponibles |

## 3. Documentos Históricos (Referencia, No Editar)

| Documento | Ubicación | Motivo Histórico |
|-----------|-----------|------------------|
| CSV original transacciones | `inputs/Attach_2_Correo_1_Transacciones SAP.csv` | Fuente inicial con duplicados y formato inconsistente |
| CSV normalizado inicial | `inputs/Attach_2_Correo_1_Transacciones SAP.normalized.csv` | Paso intermedio antes de depuración final |
| Presupuesto fuentes primarias | `docs/entregables/PRESUPUESTO_REAL_BASADO_EN_FUENTES_PRIMARIAS.md` | Contexto histórico de estimaciones previas |

## 4. Reglas de Evolución

1. Cualquier cambio de alcance (nueva transacción) debe:
   - Ser trazado en `CORRECCIONES_APLICADAS_08NOV2025.md` (o archivo sucesor de changelog)
   - Ajustar simultáneamente: 03 (transacciones), Anexo Técnico (tablas), 08 (esfuerzos) si impacta horas
2. El rango de tablas solo puede cambiar tras validación Fase 0 o incidencia formal (ticket documentado)
3. Si se mantiene divergencia deliberada (ej. archivo histórico con datos obsoletos) debe anotarse aquí

## 5. Resumen Ejecutivo de Consistencia (Estado Actual)

| Aspecto | Valor Canónico | Consistencia |
|---------|----------------|--------------|
| Transacciones | 18 | OK |
| Tablas Estimadas | ~76-85 | OK (unificado) |
| Dashboards | 12 | OK |
| Esfuerzo Total | 1,590h | OK |
| Duración | 42 semanas | OK |
| Go/No-Go | ≥12 transacciones con tablas disponibles | OK |

## 6. Próximas Mejores Prácticas (Opcional)

- Automatizar validación de consistencia (script que detecte números divergentes)
- Incorporar versión semántica (v1.0 → v1.1) en encabezados al introducir cambios aprobados
- Añadir diagrama resumen (Mermaid) de dependencias documento → dominio

---
Última actualización: 8-nov-2025
Responsable: (asignar)
