#!/usr/bin/env python3
"""
Data Integrity & PBIP Model Validator
Global Billionaire Wealth to GDP (2026)
"""

import os
import sys
import json
import pandas as pd

def run_validations():
    print("=" * 60)
    print("🚀 Running Global Billionaire Wealth 2026 Validation Suite")
    print("=" * 60)

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ind_csv = os.path.join(base_dir, "data", "raw", "billionaire_individual_2026.csv")
    agg_csv = os.path.join(base_dir, "data", "raw", "billionaire_country_aggregate_2026.csv")
    pbip_file = os.path.join(base_dir, "powerbi", "Global_Billionaire_Wealth_2026.pbip")
    report_json = os.path.join(base_dir, "powerbi", "Global_Billionaire_Wealth_2026.Report", "definition", "report.json")
    model_tmdl = os.path.join(base_dir, "powerbi", "Global_Billionaire_Wealth_2026.SemanticModel", "definition", "model.tmdl")

    errors = []
    checks = []

    # 1. File existence checks
    critical_files = [ind_csv, agg_csv, pbip_file, report_json, model_tmdl]
    for filepath in critical_files:
        rel_path = os.path.relpath(filepath, base_dir)
        if os.path.exists(filepath):
            checks.append((f"File Exists: `{rel_path}`", "PASS", f"{os.path.getsize(filepath):,} bytes"))
        else:
            errors.append(f"Missing critical file: {rel_path}")
            checks.append((f"File Exists: `{rel_path}`", "FAIL", "File Not Found"))

    if errors:
        print("\n❌ File checks failed:")
        for e in errors:
            print(f"  - {e}")
        return False, checks

    # 2. Data load and schema checks
    try:
        df_ind = pd.read_csv(ind_csv)
        df_agg = pd.read_csv(agg_csv)
        checks.append(("Load Datasets", "PASS", f"Individual: {len(df_ind)} rows | Aggregate: {len(df_agg)} rows"))
    except Exception as e:
        errors.append(f"Failed to read CSV files: {e}")
        return False, checks

    # 3. Expected columns verification
    expected_ind_cols = [
        "rank", "person_name", "gender", "age", "country", "iso3", 
        "net_worth_usd_m", "primary_industry", "self_made"
    ]
    expected_agg_cols = [
        "country_wealth_rank", "country", "iso3", "billionaire_count", 
        "total_wealth_usd_m", "country_wealth_gdp_pct", "wealth_concentration_tier"
    ]

    missing_ind = [c for c in expected_ind_cols if c not in df_ind.columns]
    missing_agg = [c for c in expected_agg_cols if c not in df_agg.columns]

    if missing_ind:
        errors.append(f"Missing columns in individual CSV: {missing_ind}")
        checks.append(("Individual Table Schema", "FAIL", f"Missing: {missing_ind}"))
    else:
        checks.append(("Individual Table Schema", "PASS", f"All {len(df_ind.columns)} columns intact"))

    if missing_agg:
        errors.append(f"Missing columns in country aggregate CSV: {missing_agg}")
        checks.append(("Country Aggregate Schema", "FAIL", f"Missing: {missing_agg}"))
    else:
        checks.append(("Country Aggregate Schema", "PASS", f"All {len(df_agg.columns)} columns intact"))

    # 4. Referential integrity (Countries)
    ind_countries = set(df_ind["country"].unique())
    agg_countries = set(df_agg["country"].unique())
    orphans = ind_countries - agg_countries

    if orphans:
        errors.append(f"Found orphaned countries in individual dataset: {orphans}")
        checks.append(("Referential Integrity (Country Key)", "FAIL", f"Orphaned: {orphans}"))
    else:
        checks.append(("Referential Integrity (Country Key)", "PASS", f"100% match across {len(agg_countries)} sovereign entities"))

    # 5. Financial Balance Sheet Reconciliation
    ind_total = df_ind["net_worth_usd_m"].sum()
    agg_total = df_agg["total_wealth_usd_m"].sum()
    delta = abs(ind_total - agg_total)

    if delta > 1.0:
        errors.append(f"Wealth sum mismatch: Individual = ${ind_total:,.2f}M vs Aggregate = ${agg_total:,.2f}M (Delta: ${delta:,.2f}M)")
        checks.append(("Financial Balance Reconciliation", "FAIL", f"Delta: ${delta:,.2f}M"))
    else:
        checks.append(("Financial Balance Reconciliation", "PASS", f"Exact Match (${ind_total:,.2f}M / $19.64T USD)"))

    # 6. JSON validity check
    try:
        with open(report_json, "r", encoding="utf-8") as f:
            json.load(f)
        checks.append(("Power BI Report JSON Syntax", "PASS", "Valid JSON syntax"))
    except Exception as e:
        errors.append(f"Invalid JSON in {report_json}: {e}")
        checks.append(("Power BI Report JSON Syntax", "FAIL", str(e)))

    # Output Console Summary
    print("\n--- Validation Results Summary ---")
    for name, status, detail in checks:
        icon = "✅" if status == "PASS" else "❌"
        print(f"{icon} {name:<40} [{status}] {detail}")

    # Output to GitHub Step Summary if running in GitHub Actions
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write("## 🔍 Global Billionaire Wealth 2026 - Data Integrity Report\n\n")
            f.write(f"**Overall Status**: {'✅ PASSED' if not errors else '❌ FAILED'}\n\n")
            f.write("| Verification Check | Status | Details |\n")
            f.write("| :--- | :---: | :--- |\n")
            for name, status, detail in checks:
                badge = "🟢 PASS" if status == "PASS" else "🔴 FAIL"
                f.write(f"| {name} | {badge} | {detail} |\n")
            f.write("\n")
            f.write(f"- **Total Billionaires Tracked**: {len(df_ind):,}\n")
            f.write(f"- **Total Sovereign Jurisdictions**: {len(df_agg)}\n")
            f.write(f"- **Reconciled Global Wealth**: ${ind_total:,.2f} Million USD (~${ind_total/1e6:.2f} Trillion)\n")

    if errors:
        print(f"\n❌ Validation Suite finished with {len(errors)} error(s).")
        return False, checks

    print("\n✨ All tests passed successfully!")
    return True, checks

if __name__ == "__main__":
    success, _ = run_validations()
    sys.exit(0 if success else 1)
