# Data Quality & Anomaly Log

This document records the automated validation checks, edge-case observations, null value analyses, and referential integrity audits conducted on the 2026 Global Billionaire Wealth dataset.

---

## 1. Audit Summary & Integrity Verification

| Metric | Individual Dataset | Country Aggregate Dataset | Verification Status |
| :--- | :--- | :--- | :---: |
| **Total Rows** | 3,384 | 80 | Verified |
| **Total Columns** | 25 | 23 | Verified |
| **Cumulative Wealth (USD M)** | $19,639,549.70 | $19,639,549.70 | Exact Match (100.0%) |
| **Referential Integrity (Country Key)** | 80 unique countries | 80 unique countries | 0 Orphaned Records |
| **Duplicate Primary Identifiers** | 0 duplicated `rank` / `forbes_uri` | 0 duplicated `country_wealth_rank` | Verified Unique |

---

## 2. Null Value Distribution & Resolution Notes

### A. Individual Dataset (`billionaire_individual_2026`)

1. **`wealth_gdp_ratio_pct` & `wealth_per_citizen_usd` (4 Nulls)**:
   - **Records Affected**:
     - Elizabeth Holmes (Rank 3381, United States)
     - Gary Wang (Rank 3381, United States)
     - Rene Benko (Rank 3381, Austria)
     - Sam Bankman-Fried (Rank 3381, United States)
   - **Root Cause**: These individuals represent "fallen billionaires" whose net worth plummeted to \$0.00 following corporate bankruptcies or legal judgments. Division by population and GDP resulted in `NaN` or uncalculated fields in the raw pipeline.
   - **Model Handling**: Handled via `COALESCE` / `DIVIDE` in DAX to return `0.00` rather than propagating `BLANK()` in aggregate visual card measures.

2. **`age` and `birth_year` (48 Nulls / 1.42%)**:
   - **Root Cause**: Private individuals whose birth dates are withheld from public disclosure or legal filings.
   - **Model Handling**: Excluded from average age calculations using DAX `AVERAGEX` over non-blank filters; does not impair financial totals.

3. **`state` (1,842 Nulls / 54.43%)**:
   - **Root Cause**: Administrative state / province level geography is only systematically captured for US, Canadian, and Australian entries.
   - **Model Handling**: Used exclusively in drill-through geographic hierarchies for North American subsets; national-level reporting relies on `country` and `iso3`.

4. **`city` (49 Nulls / 1.45%)**:
   - **Root Cause**: Unspecified urban residency for private family offices or island residents.

---

## 3. Referential & Structural Integrity

- **Foreign Key Alignment**:
  - Every individual billionaire maps to an existing entry in `billionaire_country_aggregate_2026[country]`.
  - Relationship type: Many-to-One (`*..1`) with single-direction filtering from Country Aggregate to Individual Table.
- **Sum-Check Verification**:
  - Total individual wealth sum (`SUM(billionaire_individual_2026[net_worth_usd_m])`) precisely equals the sum of national totals (`SUM(billionaire_country_aggregate_2026[total_wealth_usd_m])`).
  - Total billionaire count in individual table (3,384) equals the sum of `billionaire_count` in the country aggregate table (3,384).

---

## 4. Anomaly & Outlier Registry

| Subject / Entity | Observed Value | Anomaly Classification | Explanation & Business Treatment |
| :--- | :--- | :--- | :--- |
| **St. Kitts and Nevis** | Wealth/GDP: 860.68% | Macroeconomic Super-Outlier | Result of citizenship-by-investment residency for crypto founders (e.g., Justin Sun) where billionaire capital is foreign-derived rather than domestic GDP. |
| **Eswatini (Swaziland)**| Wealth/GDP: 362.61% | Macroeconomic Super-Outlier | Nathan Kirsh's global real estate and wholesale fortune attributed to country of birth/citizenship against a small domestic GDP base. |
| **Cyprus** | Wealth/GDP: 148.68% | Tax Sanctuary Concentration | Attributed wealth of maritime and international trading families utilizing Cyprus EU residency. |
| **Hong Kong SAR** | Wealth/GDP: 103.86% | Dense Financial Hub Concentration | 70 billionaires residing in an international financial center possessing \$422.6B wealth against \$406.9B annual GDP. |
| **Amancio Ortega** | 51.9% Country Share | Dominant National Oligarch | A single individual holds over half of the national billionaire wealth pool in Spain. |
