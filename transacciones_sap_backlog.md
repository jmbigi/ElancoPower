# Backlog Prioritario de Transacciones SAP

Este backlog consolida la información proveniente de `Attach_2_Correo_1_Transacciones SAP.csv` y las conversaciones con Lucía. Se eliminaron duplicados y se agregaron columnas para el estado de permisos y notas de seguimiento.

| Transacción | Descripción de referencia | Prioridad | Área responsable | Estado de permiso BigQuery | Tablas SAP a validar | Notas / Próximas acciones |
|-------------|---------------------------|-----------|------------------|----------------------------|----------------------|---------------------------|
| ME2L | Ordenes de compra (Purchasing Document List) | 1 (propuesto) | Supply Chain | Pendiente | EKPO, EKKO | Confirmar variante corporativa utilizada (ME2L vs ME2L-PO). Validar si existe vista Z con campos adicionales. |
| MM60 | Listado de costos estándar | 1 (propuesto) | Finanzas / Costos | Pendiente | MBEW, MARC | Revisar sensibilidad de datos rojo (costos). Requerir aprobación adicional de finanzas regional. |
| VA05 | Sales Orders / Órdenes abiertas | 1 | Ventas / Supply | Parcial | VBAK, VBAP | Revisar notas duplicadas en CSV. Determinar filtros por país. |
| MB59 | Movimientos de material | 2 | Supply / Logística | No iniciado | MSEG, MKPF | Confirmar si se requiere histórico completo o últimos 24 meses. |
| ZLEL008 | Inventario consolidado (Z-report) | 1 | Supply & Finanzas | Pendiente | Tablas Z personalizadas | Necesita ticket a TI Global para exponer tablas Z en BigQuery. |
| KSB1 | Detalle de órdenes de gasto (CO) | 1 | Finanzas | Pendiente | COEP, COBK | Requiere coordinación con controlling. Verificar si hay restricciones PII. |
| KE24 | Reporte de contribución (CO-PA) | 2 | Finanzas | Pendiente | CE1*, CE4* | Verificar versión PA (Account-based o Costing-based). |
| FB03 | Documentos financieros | 2 | Finanzas | Pendiente | BKPF, BSEG | Confirmar alcance de documentos (ventas vs. compras). |
| ZVEL015 | Condiciones de precio | 2 | Ventas / Pricing | No iniciado | KONV, KONP | Validar confidencialidad de acuerdos comerciales. |
| ME23N | Display Purchase Order | 2 | Supply Chain | No aplica (transacción display) | EKPO, EKKO | Definir si se reemplaza por reportes estándar (ME2N) o se extrae directamente tablas de compras. |
| FAGLL03 | Mayor general | 1 | Finanzas | Pendiente | FAGLFLEXA, BSEG | Requiere line-item posting activado; validar performance. |
| FBL1N | Cuentas por pagar | 2 | Finanzas | Pendiente | BSIK, BSAK, LFA1 | Confirmar segmentación por proveedor. |
| FBL5N | Cuentas por cobrar | 2 | Finanzas | Pendiente | BSID, BSAD, KNA1 | Revisar requerimientos de anonimización para datos de clientes. |
| MB5B | Stock disponible por fecha | 2 | Supply | Pendiente | MARD, MCHB | Evaluar si se cubrirá con ZLEL008 o se mantiene separado. |
| XK03 | Datos de proveedor | 2 | Supply / Compras | Pendiente | LFA1, LFB1 | Confirmar necesidad de extracción completa vs. subset. |
| XD03 | Datos de cliente | 2 | Ventas | Pendiente | KNA1, KNB1 | Validar cumplimiento GDPR / PII. |
| F.08 | Balance de comprobación | 2 | Finanzas | Pendiente | GLT0, FAGLFLEXT | Definir periodicidad requerida (mensual vs. trimestral). |
| F.01 | Estado de situación | 2 | Finanzas | Pendiente | GLT0, T001, T003 | Revisar si se reemplaza con Power BI una vez armado modelo financiero. |

> **Leyenda de estado de permiso BigQuery:**
> - **Pendiente:** No existe confirmación de disponibilidad de tablas en BigQuery; se debe levantar ticket.
> - **Parcial:** Hay extractos previos pero requieren permisos adicionales o revisión de performance.
> - **No iniciado:** No se ha solicitado acceso aún.
> - **No aplica:** La transacción es una vista en SAP que puede reemplazarse por acceso directo a tablas.

### Próximos pasos sugeridos
1. Validar prioridades con Finanzas y Supply (workshop Fase 0).
2. Asignar responsables por transacción para levantar tickets BigQuery y requisiciones SAP.
3. Documentar filtros/variantes requeridas por país.
4. Registrar dependencias con Business Objects u otras fuentes (si aplica).
