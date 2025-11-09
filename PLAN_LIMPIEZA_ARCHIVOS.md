# Plan de Limpieza de Archivos - 9 de Noviembre 2025

## 📋 OBJETIVO
Eliminar archivos redundantes, reportes históricos, auditorías intermedias y duplicados para mantener solo la documentación canónica y necesaria del proyecto.

---

## 🗑️ ARCHIVOS A ELIMINAR

### Categoría 1: Reportes de Consistencia Históricos (OBSOLETOS)

#### ❌ ELIMINAR: `CONSISTENCY_REPORT_2025-11-08.md` (5.1 KB)
**Justificación:**
- Reporte de validación del 8 de noviembre
- Versión temprana, SUPERADA por versión v2 y FINAL
- Información duplicada en reportes posteriores
- **Reemplazo:** `CONSISTENCY_REPORT_2025-11-09_FINAL.md` contiene toda la información

#### ❌ ELIMINAR: `CONSISTENCY_REPORT_2025-11-08_v2.md` (3.5 KB)
**Justificación:**
- Segunda versión del reporte del 8 de noviembre
- SUPERADA por el reporte final del 9 de noviembre
- Contiene advertencias menores sobre rangos obsoletos que fueron documentadas en el reporte final
- **Reemplazo:** `CONSISTENCY_REPORT_2025-11-09_FINAL.md` incluye análisis más completo

#### ❌ ELIMINAR: `CONSISTENCY_REPORT_2025-11-09.md` (2.6 KB)
**Justificación:**
- Versión preliminar del reporte del 9 de noviembre
- SUPERADA por la versión FINAL del mismo día
- Menos completa que la versión final
- **Reemplazo:** `CONSISTENCY_REPORT_2025-11-09_FINAL.md` (16 KB) es la versión completa y definitiva

**Impacto:** BAJO - Son reportes de auditoría interna temporales
**Riesgo:** NINGUNO - La versión FINAL conserva toda la información relevante

---

### Categoría 2: Documentos Históricos de Correcciones (ARCHIVO ÚNICO SUFICIENTE)

#### ⚠️ CONSERVAR: `CORRECCIONES_APLICADAS_08NOV2025.md` (18 KB)
**Justificación para CONSERVAR:**
- Documenta el historial completo de correcciones aplicadas
- Referencia importante para trazabilidad
- NO es redundante - es el único registro de cambios
- Útil para entender la evolución del proyecto
- **Acción:** Mantener pero mover a carpeta de históricos

---

### Categoría 3: Documentos Resumen Redundantes (DUPLICADOS)

#### ❌ ELIMINAR: `Presupuesto.txt` (2.9 KB)
**Justificación:**
- Documento resumen muy genérico y desactualizado
- Menciona "44 tablas" (dato obsoleto, ahora 24-31)
- Menciona "35-90 tablas" (rango obsoleto)
- NO está alineado con métricas canónicas actuales (18 transacciones, 24-31 tablas, 1590h, 42 sem)
- **Reemplazo:** `docs/propuesta_final/00_PORTADA_Y_RESUMEN_EJECUTIVO.md` y `README.md` contienen información actualizada y completa

#### ⚠️ CONSERVAR (con condición): `RESUMEN_PROPUESTA_FINAL.txt` (14 KB)
**Justificación para CONSERVAR:**
- Resumen ejecutivo en formato texto plano (útil para copiar/pegar en emails)
- **PERO** necesita actualización para alinearse con métricas actuales
- Menciona correctamente: 18 transacciones, 12 dashboards, 1590h, 42 semanas
- Es el ÚNICO resumen en formato .txt (diferente propósito que el .md)
- **Acción:** CONSERVAR pero verificar que esté 100% alineado con métricas canónicas

---

### Categoría 4: Archivos en Carpeta "ignorar/" (NO REVISAR POR NOMBRE)

#### ✅ CONSERVAR carpeta `ignorar/`
**Justificación:**
- La carpeta se llama "ignorar" por algo
- Contiene documentos históricos que el usuario decidió mantener separados
- No interfieren con la documentación principal
- **Acción:** No tocar esta carpeta

---

## 📊 RESUMEN DE ELIMINACIONES

| Archivo | Tamaño | Categoría | Acción |
|---------|--------|-----------|--------|
| `CONSISTENCY_REPORT_2025-11-08.md` | 5.1 KB | Reporte histórico | ❌ ELIMINAR |
| `CONSISTENCY_REPORT_2025-11-08_v2.md` | 3.5 KB | Reporte histórico | ❌ ELIMINAR |
| `CONSISTENCY_REPORT_2025-11-09.md` | 2.6 KB | Reporte histórico | ❌ ELIMINAR |
| `Presupuesto.txt` | 2.9 KB | Documento obsoleto | ❌ ELIMINAR |
| `CORRECCIONES_APLICADAS_08NOV2025.md` | 18 KB | Historial cambios | ✅ MOVER a docs/internos/ |
| `RESUMEN_PROPUESTA_FINAL.txt` | 14 KB | Resumen ejecutivo | ✅ CONSERVAR |
| `CONSISTENCY_REPORT_2025-11-09_FINAL.md` | 16 KB | Reporte canónico | ✅ CONSERVAR |

**Total a eliminar:** 4 archivos (14.1 KB)
**Total a mover:** 1 archivo (18 KB) → docs/internos/
**Total a conservar en raíz:** 2 archivos (30 KB)

---

## 🎯 DOCUMENTOS CANÓNICOS QUE SE CONSERVAN

### En Raíz del Proyecto:
1. ✅ `README.md` - Índice principal del proyecto
2. ✅ `CONSISTENCY_REPORT_2025-11-09_FINAL.md` - Reporte de consistencia definitivo
3. ✅ `RESUMEN_PROPUESTA_FINAL.txt` - Resumen ejecutivo en texto plano

### En docs/propuesta_final/:
- Todos los 16 documentos .md (00-12 + anexos + README)
- `CRONOGRAMA_DETALLADO_TAREAS.csv` y `.xlsx`

### En docs/entregables/:
- Todos los documentos (alcances y listas)

### En docs/internos/:
- `estado_documentos.md`
- `mapeo_transacciones_tablas_detallado.csv`
- `mapeo_transacciones_tablas.txt`
- `procedimiento_poda_tablas.md`
- **+ NUEVO:** `CORRECCIONES_APLICADAS_08NOV2025.md` (movido desde raíz)

### En config/:
- `table_scope_expected.yaml`

### En scripts/:
- Los 3 scripts de validación

---

## 🔄 ACCIONES RECOMENDADAS

### Paso 1: Eliminar Reportes Históricos
```bash
rm CONSISTENCY_REPORT_2025-11-08.md
rm CONSISTENCY_REPORT_2025-11-08_v2.md
rm CONSISTENCY_REPORT_2025-11-09.md
```

### Paso 2: Eliminar Documento Obsoleto
```bash
rm Presupuesto.txt
```

### Paso 3: Mover Historial de Correcciones
```bash
mv CORRECCIONES_APLICADAS_08NOV2025.md docs/internos/
```

### Paso 4: Actualizar README.md (si es necesario)
Actualizar referencias en el README principal para reflejar la nueva ubicación del archivo de correcciones.

---

## ✅ BENEFICIOS DE LA LIMPIEZA

1. **Claridad:** Solo documentos relevantes en la raíz
2. **Mantenibilidad:** Menos archivos que mantener sincronizados
3. **Profesionalismo:** Proyecto limpio para presentar al cliente
4. **Trazabilidad:** Historial de cambios preservado en docs/internos/
5. **Performance:** Scripts de búsqueda más rápidos con menos archivos

---

## ⚠️ PRECAUCIONES

1. ✅ **Backup realizado:** Git mantiene historial completo
2. ✅ **No se elimina información única:** Todo está preservado en versión FINAL
3. ✅ **Trazabilidad mantenida:** Historial de correcciones movido a internos/
4. ✅ **Documentación canónica intacta:** docs/propuesta_final/ sin cambios

---

## 📝 VERIFICACIÓN POST-LIMPIEZA

Después de la limpieza, verificar:
- [ ] Raíz del proyecto solo contiene 3 archivos .md/.txt principales
- [ ] docs/internos/ contiene el historial de correcciones
- [ ] Todos los scripts de validación siguen funcionando
- [ ] README.md está actualizado con ubicaciones correctas
- [ ] No hay referencias rotas en documentos

---

**Responsable:** Asistente IA - GitHub Copilot  
**Fecha Plan:** 9 de noviembre de 2025  
**Estado:** LISTO PARA EJECUTAR  
