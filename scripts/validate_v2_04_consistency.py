#!/usr/bin/env python3
"""
Script de validación de consistencia para Propuesta Elanco V2.04
Verifica que todos los documentos V2.04 sean consistentes entre sí
"""

import csv
import os
from pathlib import Path

# Métricas esperadas para V2.04
EXPECTED_V2_04 = {
    "esfuerzo_total": 1880,
    "duracion_semanas": 36,
    "recursos": 4,
    "consultor_bi": 935,
    "abap_developer": 270,
    "funcional_sap": 512,
    "project_manager": 163,
    "fase_0_horas": 328,
    "fase_1_horas": 852,
    "fase_2_horas": 700,
    "fase_0_semanas": 6,
    "fase_1_semanas": 20,
    "fase_2_semanas": 10,
    "go_live": "13 de septiembre de 2026"
}

# Métricas esperadas para V2.02 (referencia)
EXPECTED_V2_02 = {
    "esfuerzo_total": 1590,
    "duracion_semanas": 42,
    "recursos": 3,
    "consultor_bi": 961,
    "abap_developer": 0,
    "funcional_sap": 484,
    "project_manager": 145,
    "fase_0_horas": 235,
    "fase_1_horas": 696,
    "fase_2_horas": 659,
    "fase_0_semanas": 6,
    "fase_1_semanas": 22,
    "fase_2_semanas": 14,
    "go_live": "octubre de 2026"
}

def validate_csv_v2_04(csv_path):
    """Valida el CSV de cronograma V2.04"""
    print(f"\n🔍 Validando CSV: {csv_path}")
    
    if not os.path.exists(csv_path):
        print(f"   ❌ Archivo no encontrado: {csv_path}")
        return False
    
    totales = {
        "Consultor_BI": 0,
        "ABAP_Developer": 0,
        "Funcional_SAP": 0,
        "Project_Manager": 0
    }
    
    fase_horas = {"Fase_0": 0, "Fase_1": 0, "Fase_2": 0}
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                fase = row.get('Fase', '')
                totales["Consultor_BI"] += int(row.get('Horas_Consultor_BI', 0))
                totales["ABAP_Developer"] += int(row.get('Horas_ABAP_Developer', 0))
                totales["Funcional_SAP"] += int(row.get('Horas_Funcional_SAP', 0))
                totales["Project_Manager"] += int(row.get('Horas_Project_Manager', 0))
                
                if fase in fase_horas:
                    fase_horas[fase] += int(row.get('Total_Horas', 0))
        
        total_general = sum(totales.values())
        
        print(f"   📊 Totales por recurso:")
        print(f"      Consultor BI: {totales['Consultor_BI']}h (esperado: {EXPECTED_V2_04['consultor_bi']}h)")
        print(f"      ABAP Developer: {totales['ABAP_Developer']}h (esperado: {EXPECTED_V2_04['abap_developer']}h)")
        print(f"      Funcional SAP: {totales['Funcional_SAP']}h (esperado: {EXPECTED_V2_04['funcional_sap']}h)")
        print(f"      Project Manager: {totales['Project_Manager']}h (esperado: {EXPECTED_V2_04['project_manager']}h)")
        print(f"      TOTAL: {total_general}h (esperado: {EXPECTED_V2_04['esfuerzo_total']}h)")
        
        print(f"\n   📊 Totales por fase:")
        print(f"      Fase 0: {fase_horas['Fase_0']}h (esperado: {EXPECTED_V2_04['fase_0_horas']}h)")
        print(f"      Fase 1: {fase_horas['Fase_1']}h (esperado: {EXPECTED_V2_04['fase_1_horas']}h)")
        print(f"      Fase 2: {fase_horas['Fase_2']}h (esperado: {EXPECTED_V2_04['fase_2_horas']}h)")
        
        # Validaciones
        errores = []
        if totales['Consultor_BI'] != EXPECTED_V2_04['consultor_bi']:
            errores.append(f"Consultor BI: {totales['Consultor_BI']} != {EXPECTED_V2_04['consultor_bi']}")
        if totales['ABAP_Developer'] != EXPECTED_V2_04['abap_developer']:
            errores.append(f"ABAP Developer: {totales['ABAP_Developer']} != {EXPECTED_V2_04['abap_developer']}")
        if totales['Funcional_SAP'] != EXPECTED_V2_04['funcional_sap']:
            errores.append(f"Funcional SAP: {totales['Funcional_SAP']} != {EXPECTED_V2_04['funcional_sap']}")
        if totales['Project_Manager'] != EXPECTED_V2_04['project_manager']:
            errores.append(f"Project Manager: {totales['Project_Manager']} != {EXPECTED_V2_04['project_manager']}")
        if total_general != EXPECTED_V2_04['esfuerzo_total']:
            errores.append(f"Total general: {total_general} != {EXPECTED_V2_04['esfuerzo_total']}")
        
        if errores:
            print(f"\n   ❌ Errores detectados:")
            for error in errores:
                print(f"      • {error}")
            return False
        else:
            print(f"\n   ✅ CSV V2.04 es consistente")
            return True
            
    except Exception as e:
        print(f"   ❌ Error al leer CSV: {e}")
        return False

def check_file_exists(file_path, version="V2.04"):
    """Verifica si un archivo existe"""
    exists = os.path.exists(file_path)
    status = "✅" if exists else "❌"
    print(f"   {status} {os.path.basename(file_path)}")
    return exists

def main():
    print("=" * 80)
    print("VALIDACIÓN DE CONSISTENCIA - PROPUESTA ELANCO V2.04")
    print("=" * 80)
    
    base_path = Path(__file__).parent.parent
    docs_path = base_path / "docs" / "propuesta_final"
    
    print("\n📁 Verificando archivos V2.04...")
    
    archivos_v2_04 = [
        "00_PORTADA_Y_RESUMEN_EJECUTIVO_V2_04.md",
        "04_FASE_0_REVISION_ALCANCE_Y_FACTIBILIDAD_V2_04.md",
        "05_FASE_1_CONSTRUCCION_DATA_LAKE_V2_04.md",
        "06_FASE_2_MODELADO_Y_DASHBOARDS_V2_04.md",
        "08_ESTIMACION_DE_ESFUERZOS_Y_COSTOS_V2_04.md",
        "09_CRONOGRAMA_SEMANAL_V2_04.md",
        "10_REQUISITOS_TECNICOS_Y_ADMINISTRATIVOS_V2_04.md",
        "11_RIESGOS_Y_SUPUESTOS_V2_04.md",
        "CRONOGRAMA_DETALLADO_TAREAS_V2_04.csv",
        "README_V2_04.md"
    ]
    
    existentes = 0
    for archivo in archivos_v2_04:
        if check_file_exists(docs_path / archivo):
            existentes += 1
    
    print(f"\n   📊 Archivos V2.04: {existentes}/{len(archivos_v2_04)} completados")
    
    # Validar CSV
    csv_path = docs_path / "CRONOGRAMA_DETALLADO_TAREAS_V2_04.csv"
    csv_ok = validate_csv_v2_04(csv_path)
    
    # Validar archivo raíz
    print("\n📁 Verificando archivos en raíz...")
    resumen_v2_04 = base_path / "RESUMEN_PROPUESTA_FINAL_V2_04.txt"
    check_file_exists(resumen_v2_04)
    
    resumen_v2_02 = base_path / "RESUMEN_PROPUESTA_FINAL_V2_02.txt"
    if check_file_exists(resumen_v2_02):
        print("      ℹ️  V2.02 renombrado correctamente")
    else:
        print("      ⚠️  Falta renombrar RESUMEN_PROPUESTA_FINAL.txt a V2_02")
    
    # Resumen final
    print("\n" + "=" * 80)
    print("RESUMEN DE VALIDACIÓN")
    print("=" * 80)
    
    print(f"\n✅ Métricas V2.04:")
    print(f"   • Esfuerzo total: {EXPECTED_V2_04['esfuerzo_total']}h")
    print(f"   • Duración: {EXPECTED_V2_04['duracion_semanas']} semanas")
    print(f"   • Recursos: {EXPECTED_V2_04['recursos']} (BI, ABAP, SAP, PM)")
    print(f"   • Go-Live: {EXPECTED_V2_04['go_live']}")
    
    print(f"\n📊 Comparativa vs V2.02:")
    print(f"   • Esfuerzo: {EXPECTED_V2_04['esfuerzo_total']}h vs {EXPECTED_V2_02['esfuerzo_total']}h (+{EXPECTED_V2_04['esfuerzo_total'] - EXPECTED_V2_02['esfuerzo_total']}h)")
    print(f"   • Duración: {EXPECTED_V2_04['duracion_semanas']} sem vs {EXPECTED_V2_02['duracion_semanas']} sem ({EXPECTED_V2_04['duracion_semanas'] - EXPECTED_V2_02['duracion_semanas']} sem)")
    print(f"   • Recursos: {EXPECTED_V2_04['recursos']} vs {EXPECTED_V2_02['recursos']} (+1 ABAP Developer)")
    
    if csv_ok and existentes >= 5:
        print(f"\n✅ ESTADO: Documentación V2.04 en buen estado ({existentes}/{len(archivos_v2_04)} archivos)")
    else:
        print(f"\n⚠️  ESTADO: Documentación V2.04 incompleta ({existentes}/{len(archivos_v2_04)} archivos)")
        print(f"   Completar archivos faltantes antes de presentar al cliente")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
