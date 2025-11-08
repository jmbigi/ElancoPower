#!/usr/bin/env python3
"""Validate consistency of SAP table scope across repository documents.

Checks performed:
1. Core, conditional, excluded, optional tables align with CSV mapping and YAML config.
2. Detects tables in CSV not in config (unexpected) and config tables absent from CSV (gaps).
3. Ensures obsolete tables (BSEG, COEP, FAGLFLEXA) are not marked incluir / candidato_incluir.
4. Summarizes counts vs expected thresholds.
5. Suggests potential enrichers (recommended_additional_candidates) still not referenced.

Usage: python scripts/validate_table_scope.py
"""
from __future__ import annotations
import csv
import json
import sys
from pathlib import Path
import yaml  # type: ignore

REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "docs" / "internos" / "mapeo_transacciones_tablas_detallado.csv"
YAML_PATH = REPO_ROOT / "config" / "table_scope_expected.yaml"

def load_yaml():
    with YAML_PATH.open() as f:
        return yaml.safe_load(f)

def load_csv():
    rows = []
    with CSV_PATH.open() as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    return rows

def classify_from_csv(rows):
    core = set()
    candidate = set()
    excluded = set()
    for row in rows:
        table = row["tabla"].strip().upper()
        estado = row["estado_inclusion"].strip().lower()
        if estado == "incluir":
            core.add(table)
        elif estado == "candidato_incluir":
            candidate.add(table)
        elif estado == "excluir":
            excluded.add(table)
    return core, candidate, excluded

def main():
    if not CSV_PATH.exists():
        print(f"ERROR: CSV mapping not found at {CSV_PATH}", file=sys.stderr)
        return 2
    if not YAML_PATH.exists():
        print(f"ERROR: YAML config not found at {YAML_PATH}", file=sys.stderr)
        return 2

    cfg = load_yaml()
    rows = load_csv()
    core_csv, candidate_csv, excluded_csv = classify_from_csv(rows)

    core_cfg = set(cfg["core_tables"])
    cond_cfg = set(cfg["conditional_tables"])
    excl_cfg = set(cfg["excluded_tables"])
    optional_cfg = set(cfg.get("optional_tables", []))

    # Differences
    missing_core_in_csv = sorted(core_cfg - core_csv)
    extra_core_in_csv = sorted(core_csv - core_cfg)
    missing_cond_in_csv = sorted(cond_cfg - candidate_csv)
    extra_cond_in_csv = sorted(candidate_csv - cond_cfg)
    wrong_excluded = sorted((excl_cfg & (core_csv | candidate_csv)))
    unexpected_tables = sorted((core_csv | candidate_csv | excluded_csv) - (core_cfg | cond_cfg | excl_cfg | optional_cfg))

    # Counts
    core_count = len(core_csv)
    cond_count = len(candidate_csv)
    excl_count = len(excluded_csv)
    total_mvp = core_count + cond_count  # potential upper bound if cond all included

    expected_core = cfg["rules"]["expected_core_count"]
    min_core = cfg["rules"]["min_core_tables"]
    max_core = cfg["rules"]["max_core_tables"]
    max_total = cfg["rules"]["max_total_tables"]

    status = []
    def ok(flag):
        return "OK" if flag else "WARN"

    status.append({"metric":"core_count","value":core_count,"expected":expected_core,"status":ok(core_count==expected_core)})
    status.append({"metric":"core_within_bounds","value":core_count,"expected_range":f"[{min_core},{max_core}]","status":ok(min_core <= core_count <= max_core)})
    status.append({"metric":"total_mvp_upper","value":total_mvp,"max_allowed":max_total,"status":ok(total_mvp <= max_total)})

    report = {
        "summary":{
            "core_csv_count":core_count,
            "conditional_csv_count":cond_count,
            "excluded_csv_count":excl_count,
            "potential_total_mvp": total_mvp,
        },
        "differences":{
            "missing_core_in_csv":missing_core_in_csv,
            "extra_core_in_csv":extra_core_in_csv,
            "missing_conditional_in_csv":missing_cond_in_csv,
            "extra_conditional_in_csv":extra_cond_in_csv,
            "excluded_marked_incorrectly":wrong_excluded,
            "unexpected_tables_detected":unexpected_tables,
        },
        "status_checks": status,
        "recommendations":{
            "activate_optional_if": cfg["rules"]["include_optional_if"],
            "consider_future_candidates": cfg.get("recommended_additional_candidates", {}),
        },
        "metadata": cfg.get("metadata", {})
    }

    # Human readable section
    human_lines = []
    human_lines.append("== TABLE SCOPE VALIDATION REPORT ==")
    human_lines.append(f"Core tables (CSV): {core_count} (expected {expected_core})")
    human_lines.append(f"Conditional tables (CSV): {cond_count}")
    human_lines.append(f"Excluded tables (CSV): {excl_count}")
    human_lines.append(f"Potential total (core+conditional): {total_mvp}")
    if missing_core_in_csv:
        human_lines.append(f"MISSING core (in config, absent in CSV): {', '.join(missing_core_in_csv)}")
    if extra_core_in_csv:
        human_lines.append(f"EXTRA core (in CSV only): {', '.join(extra_core_in_csv)}")
    if missing_cond_in_csv:
        human_lines.append(f"MISSING conditional (in config, absent in CSV): {', '.join(missing_cond_in_csv)}")
    if extra_cond_in_csv:
        human_lines.append(f"EXTRA conditional (in CSV only): {', '.join(extra_cond_in_csv)}")
    if wrong_excluded:
        human_lines.append(f"ERROR: Excluded tables wrongly marked incluir/candidato: {', '.join(wrong_excluded)}")
    if unexpected_tables:
        human_lines.append(f"UNEXPECTED tables (not in config lists): {', '.join(unexpected_tables)}")
    human_lines.append("Status checks:")
    for s in status:
        human_lines.append(f" - {s['metric']}: {s['value']} -> {s['status']}")

    print("\n".join(human_lines))
    print("\nJSON_REPORT_START")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("JSON_REPORT_END")

    # Exit code: 0 if no critical errors
    critical = bool(wrong_excluded)
    return 1 if critical else 0

if __name__ == "__main__":
    sys.exit(main())
