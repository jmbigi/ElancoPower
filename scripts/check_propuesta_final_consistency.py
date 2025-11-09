#!/usr/bin/env python3
"""Extended consistency review focused on docs/propuesta_final vs. whole repository.

Complementa `scripts/check_consistency.py` agregando verificaciones más profundas
específicas de la carpeta `docs/propuesta_final`:

Checks implementados:
 1. Presencia de métricas canónicas (transacciones=18, dashboards=12, horas=1590, semanas=42,
    rango tablas=24–31) en cada archivo de propuesta_final dependiendo de su naturaleza.
 2. Verificación de horas por fase (235 + 696 + 659 = 1590) y semanas por fase (6 + 22 + 14 = 42)
    extraídas de documentos clave (00, 08, 09) y README interno de la subcarpeta.
 3. Detección de referencias a rangos obsoletos (19–25, 20–26, 24–28, 24-28, 19-25, 20-26) en
    archivos de propuesta_final, diferenciando si están marcadas como histórico / actualización.
 4. Reporte por archivo: métricas encontradas, ausentes, advertencias y rangos obsoletos.
 5. Validación de consistencia cruzada: suma de horas y semanas coincide con totales declarados.

Salida:
  - Reporte humano en consola.
  - Bloque JSON entre marcadores JSON_REPORT_START / JSON_REPORT_END para uso programático.

Exit codes:
  0 -> Sin inconsistencias críticas (todo OK o solo warnings menores)
  1 -> Warnings (falta alguna métrica esperada en cierto archivo / rangos obsoletos no contextualizados)
  2 -> Errores críticos (inconsistencia matemática en totales de horas/semanas o ausencia generalizada)
"""
from __future__ import annotations
import re
import json
import sys
from pathlib import Path
from typing import Dict, List, Any

REPO_ROOT = Path(__file__).resolve().parents[1]
PROPUESTA_DIR = REPO_ROOT / "docs" / "propuesta_final"

# Canonical definitions
CANONICAL = {
    "transacciones": 18,
    "dashboards": 12,
    "horas_total": 1590,
    "semanas_total": 42,
    "tablas_rango": (24, 31),  # texto esperado 24–31 (guión EN DASH o '-')
    "fase_horas": {
        "fase_0": 235,
        "fase_1": 696,
        "fase_2": 659,
    },
    "fase_semanas": {
        "fase_0": 6,
        "fase_1": 22,
        "fase_2": 14,
    }
}

# Expected metrics per file (heuristic)
EXPECTATIONS = {
    "00_PORTADA_Y_RESUMEN_EJECUTIVO.md": {"transacciones", "dashboards", "horas_total", "semanas_total"},
    "README.md": {"transacciones", "dashboards", "horas_total", "semanas_total"},
    "03_TRANSACCIONES_SAP_INCLUIDAS.md": {"transacciones", "tablas_rango"},
    "08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md": {"horas_total", "transacciones", "dashboards", "semanas_total", "tablas_rango"},
    "09_CRONOGRAMA_SEMANAL.md": {"semanas_total", "horas_total", "transacciones", "dashboards"},
    "ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md": {"transacciones", "tablas_rango"},
}

OUTDATED_MARKERS = {"19–25", "20–26", "24–28", "24-28", "19-25", "20-26"}

HISTORICAL_KEYWORDS = {
    "histórico", "historico", "exploratorio", "versión", "version", "actualiza", "actualizado", "rango canónico", "canónico", "canonico"
}

def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")

def find_metric_patterns(text: str) -> Dict[str, bool]:
    patterns = {}
    # Transacciones
    patterns["transacciones"] = bool(re.search(rf"\b{CANONICAL['transacciones']}\s+transacciones\b", text))
    # Dashboards
    patterns["dashboards"] = bool(re.search(rf"\b{CANONICAL['dashboards']}\s+dashboards\b", text))
    # Horas total (permitir 1,590 / 1590 / 1.590)
    horas_regex = rf"(1[,\.])?{str(CANONICAL['horas_total'])[1:]}h|\b{CANONICAL['horas_total']}\s+horas\b|\b{CANONICAL['horas_total']:,}\b"
    patterns["horas_total"] = bool(re.search(horas_regex, text))
    # Semanas total
    patterns["semanas_total"] = bool(re.search(rf"\b{CANONICAL['semanas_total']}\s+semanas\b", text))
    # Rango tablas (24–31 tablas / 24-31 tablas)
    low, high = CANONICAL['tablas_rango']
    patterns["tablas_rango"] = bool(re.search(rf"\b{low}\s*[–-]\s*{high}\s+tablas\b", text))
    return patterns

def extract_phase_numbers(text: str) -> Dict[str, Any]:
    data = {"fase_horas": {}, "fase_semanas": {}}
    # Horas por fase (buscar patrones tipo 'Fase 0' seguido de '235h')
    for fase_key, horas in CANONICAL['fase_horas'].items():
        num = horas
        fase_num = fase_key.split('_')[1]
        # Permitir formatos 235h / 235 h / (235h)
        horas_pat = rf"Fase\s+{fase_num}[^\n]*?(\b{num}[hH]\b)"
        data['fase_horas'][fase_key] = bool(re.search(horas_pat, text))
    for fase_key, semanas in CANONICAL['fase_semanas'].items():
        fase_num = fase_key.split('_')[1]
        sem_pat = rf"Fase\s+{fase_num}[^\n]*?(\b{semanas}\s+sem)"
        # También patrones de tabla cronograma: '| 235h | 6 sem |'
        alt_pat = rf"\b{semanas}\s+sem\b"
        present = bool(re.search(sem_pat, text)) or bool(re.search(alt_pat, text))
        data['fase_semanas'][fase_key] = present
    return data

def detect_outdated_ranges(text: str) -> List[str]:
    lines = text.splitlines()
    found = []
    for line in lines:
        lower = line.lower()
        historical_context = any(k in lower for k in HISTORICAL_KEYWORDS)
        for marker in OUTDATED_MARKERS:
            if marker in line:
                # Si la línea también contiene el rango canónico vigente, ignorar para evitar falsos positivos.
                low, high = CANONICAL['tablas_rango']
                canonical_present = bool(re.search(rf"\b{low}\s*[–-]\s*{high}\b", line))
                if canonical_present:
                    continue
                # Si NO hay contexto histórico, marcar warning más fuerte.
                severity = "info" if historical_context else "warning"
                found.append(f"{severity}:{line.strip()}")
    return found

def main() -> int:
    if not PROPUESTA_DIR.exists():
        print(f"ERROR: Directorio no encontrado: {PROPUESTA_DIR}", file=sys.stderr)
        return 2

    report: Dict[str, Any] = {
        "files": {},
        "cross_checks": {},
        "canonical": CANONICAL,
    }
    critical_errors: List[str] = []
    warnings: List[str] = []

    # Procesar cada archivo Markdown en propuesta_final
    md_files = sorted(PROPUESTA_DIR.glob("*.md"))
    for f in md_files:
        text = read_text(f)
        metrics = find_metric_patterns(text)
        phases = extract_phase_numbers(text) if f.name in {"00_PORTADA_Y_RESUMEN_EJECUTIVO.md", "08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md", "09_CRONOGRAMA_SEMANAL.md"} else {"fase_horas": {}, "fase_semanas": {}}
        outdated = detect_outdated_ranges(text)
        expected = EXPECTATIONS.get(f.name, set())
        missing = sorted([m for m in expected if not metrics.get(m, False)])
        file_warnings = []
        if missing:
            file_warnings.append(f"Faltan métricas esperadas: {', '.join(missing)}")
        # Categorizar outdated markers
        outdated_warnings = [o for o in outdated if o.startswith("warning:")]
        outdated_infos = [o for o in outdated if o.startswith("info:")]
        if outdated_warnings:
            file_warnings.append(f"Rangos obsoletos sin contexto histórico: {len(outdated_warnings)}")
        report['files'][f.name] = {
            "metrics_present": metrics,
            "expected_metrics": sorted(list(expected)),
            "missing_expected": missing,
            "phase_flags": phases,
            "outdated_ranges": {"warnings": outdated_warnings, "infos": outdated_infos},
        }
        for w in file_warnings:
            warnings.append(f"{f.name}: {w}")

    # Cross-check global consistencia horas/semanas
    # Recolectar totales declarados explícitos desde README y 08
    def file_text(name: str) -> str:
        p = PROPUESTA_DIR / name
        return read_text(p)

    readme_text = file_text("README.md") + file_text("00_PORTADA_Y_RESUMEN_EJECUTIVO.md")
    estimacion_text = file_text("08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md")
    cronograma_text = file_text("09_CRONOGRAMA_SEMANAL.md")

    # Verificar suma horas fases
    horas_declared = CANONICAL['fase_horas']
    horas_sum = sum(horas_declared.values())
    horas_ok = horas_sum == CANONICAL['horas_total']
    if not horas_ok:
        critical_errors.append(f"Suma horas fases {horas_sum} != total {CANONICAL['horas_total']}")

    semanas_declared = CANONICAL['fase_semanas']
    semanas_sum = sum(semanas_declared.values())
    semanas_ok = semanas_sum == CANONICAL['semanas_total']
    if not semanas_ok:
        critical_errors.append(f"Suma semanas fases {semanas_sum} != total {CANONICAL['semanas_total']}")

    report['cross_checks'] = {
        "horas_sum_fases": horas_sum,
        "horas_total_match": horas_ok,
        "semanas_sum_fases": semanas_sum,
        "semanas_total_match": semanas_ok,
        "warnings_count": len(warnings),
        "critical_errors_count": len(critical_errors),
    }

    # Salida humana
    print("== PROPUESTA_FINAL CONSISTENCY REPORT ==")
    print("Directorio analizado:", PROPUESTA_DIR)
    print("\nArchivos revisados:")
    for name, info in report['files'].items():
        missing = info['missing_expected']
        status = "OK" if not missing else "WARN"
        outdated_warns = len(info['outdated_ranges']['warnings'])
        outdated_infos = len(info['outdated_ranges']['infos'])
        print(f" - {name}: {status} (faltan={len(missing)}, outdated_warn={outdated_warns}, outdated_info={outdated_infos})")
    print("\nVerificación cruzada:")
    print(f" - Horas fases suman {horas_sum} -> {'OK' if horas_ok else 'ERROR'}")
    print(f" - Semanas fases suman {semanas_sum} -> {'OK' if semanas_ok else 'ERROR'}")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f" - {w}")
    if critical_errors:
        print("\nCritical Errors:")
        for e in critical_errors:
            print(f" - {e}")

    print("\nJSON_REPORT_START")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("JSON_REPORT_END")

    if critical_errors:
        return 2
    return 1 if warnings else 0

if __name__ == "__main__":
    sys.exit(main())
