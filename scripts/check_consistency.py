#!/usr/bin/env python3
"""Cross-document consistency checker for canonical project metrics.

Validates the presence and consistency of canonical numeric scope values across
markdown documents. Designed to be lightweight and read-only (no file writes).

Canonical values (current):
    - Transacciones SAP: 18
    - Rango tablas SAP: 24–31 (core=24, condicionales potenciales=7)
    - Dashboards Power BI: 12
    - Esfuerzo total (horas): 1,590
    - Duración (semanas): 42

Checks:
 1. Each canonical doc must mention its metric at least once.
 2. Detect outdated ranges (19–25, 20–26, 19-25, 20-26) outside historical log sections.
 3. Summarize warnings for manual review.

Usage:
  python scripts/check_consistency.py

Exit codes:
  0 -> No critical inconsistencies found
  1 -> Warnings present (needs review, but not blocking)
  2 -> Errors (missing canonical metrics in required docs)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Canonical definitions
CANONICAL = {
    "transacciones": 18,
    "tablas_rango": (24, 31),  # inclusive (ampliado para CO-PA + textos)
    "dashboards": 12,
    "horas_total": 1590,
    "semanas": 42,
}

# Docs expected to carry each metric explicitly
EXPECTED_DOCS = {
    "transacciones": [
        "docs/propuesta_final/03_TRANSACCIONES_SAP_INCLUIDAS.md",
        "README.md",
    ],
    "tablas_rango": [
        "docs/propuesta_final/ANEXO_TECNICO_TRANSACCIONES_VS_TABLAS.md",
        "docs/entregables/ALCANCE_TABLAS_E_INDICES.md",
        "docs/internos/estado_documentos.md",
    ],
    "dashboards": [
        "docs/propuesta_final/06_FASE_2_MODELADO_Y_DASHBOARDS.md",
        "README.md",
    ],
    "horas_total": [
        "docs/propuesta_final/08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS.md",
        "docs/internos/estado_documentos.md",
    ],
    "semanas": [
        "docs/propuesta_final/09_CRONOGRAMA_SEMANAL.md",
        "README.md",
    ],
}

HISTORICAL_MARKERS = {
    "19–25", "20–26", "19-25", "20-26", "24–28", "24-28"
}

def read_text(rel_path: str) -> str:
    p = REPO_ROOT / rel_path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")

def contains_transacciones(text: str) -> bool:
    return bool(re.search(rf"\b{CANONICAL['transacciones']}\s+transacciones\b", text))

def contains_dashboards(text: str) -> bool:
    return bool(re.search(rf"\b{CANONICAL['dashboards']}\s+dashboards\b", text))

def contains_horas(text: str) -> bool:
    return bool(re.search(rf"\b{CANONICAL['horas_total']:,}\b|\b{CANONICAL['horas_total']}\b", text))

def contains_semanas(text: str) -> bool:
    return bool(re.search(rf"\b{CANONICAL['semanas']}\s+semanas\b", text))

def contains_tablas_rango(text: str) -> bool:
    low, high = CANONICAL['tablas_rango']
    # Accept forms 24–28, 24-28, 24–28 tablas, etc.
    return bool(re.search(rf"\b{low}\s*[–-]\s*{high}\s+tablas\b", text))

CHECK_FUNCS = {
    "transacciones": contains_transacciones,
    "tablas_rango": contains_tablas_rango,
    "dashboards": contains_dashboards,
    "horas_total": contains_horas,
    "semanas": contains_semanas,
}

def find_outdated_ranges(text: str) -> list[str]:
    """Detect lines containing outdated range markers.

    Skips lines that are clearly explanatory upgrade notes (e.g. lines containing
    'Actualiza rango', 'Versión', or explicit canonical context), to avoid false positives
    where the old range is being referenced as part of a change log statement.
    """
    warnings = []
    for line in text.splitlines():
        normalized = line.lower()
        if (
            "histórico" in normalized
            or "actualiza rango" in normalized
            or "versión" in normalized
        ):
            continue
        for marker in HISTORICAL_MARKERS:
            if marker in line:
                if contains_tablas_rango(line):  # current canonical also present
                    continue
                warnings.append(line.strip())
    return warnings

def main() -> int:
    errors = []
    warnings = []
    results = {}

    for metric, docs in EXPECTED_DOCS.items():
        check = CHECK_FUNCS[metric]
        metric_ok = True
        missing_in = []
        for doc in docs:
            text = read_text(doc)
            if not text:
                warnings.append(f"Falta archivo esperado: {doc}")
                metric_ok = False
                missing_in.append(doc)
            elif not check(text):
                metric_ok = False
                missing_in.append(doc)
        results[metric] = {
            "ok": metric_ok,
            "missing_in": missing_in,
        }
        if not metric_ok:
            errors.append(f"Metric '{metric}' ausente en: {', '.join(missing_in)}")

    # Scan all markdown files for outdated ranges
    md_files = list(REPO_ROOT.rglob("*.md"))
    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="ignore")
        outdated = find_outdated_ranges(text)
        if outdated:
            for fragment in outdated:
                warnings.append(f"Rango obsoleto en {md.relative_to(REPO_ROOT)}: {fragment}")

    # Prepare report
    print("== CONSISTENCY REPORT ==")
    print("Canonical values:")
    for k, v in CANONICAL.items():
        print(f" - {k}: {v}")
    print("\nMetrics presence:")
    for k, info in results.items():
        status = "OK" if info["ok"] else "MISSING"
        print(f" - {k}: {status}")
        if info["missing_in"]:
            print(f"   missing in: {', '.join(info['missing_in'])}")
    if warnings:
        print("Warnings:")
        for w in warnings:
            print(f" - {w}")

    if errors:
        print("\nErrors detected:")
        for e in errors:
            print(f" - {e}")
        return 2
    return 1 if warnings else 0

if __name__ == "__main__":
    sys.exit(main())
